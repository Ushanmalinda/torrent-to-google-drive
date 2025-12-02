#!/usr/bin/env python3
"""
Torrent Downloader for Ubuntu/Linux
Simple command-line tool to download torrents locally

Usage:
    python3 torrent_downloader.py --torrent file.torrent --output /path/to/downloads
    python3 torrent_downloader.py --magnet "magnet:?xt=..." --output /path/to/downloads
"""

import libtorrent as lt
import time
import sys
import os
import argparse
from pathlib import Path


def format_size(bytes):
    """Convert bytes to human readable format"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024.0
    return f"{bytes:.2f} PB"


def format_time(seconds):
    """Convert seconds to human readable format"""
    if seconds < 60:
        return f"{int(seconds)}s"
    elif seconds < 3600:
        return f"{int(seconds/60)}m {int(seconds%60)}s"
    else:
        hours = int(seconds / 3600)
        minutes = int((seconds % 3600) / 60)
        return f"{hours}h {minutes}m"


def download_torrent(torrent_file=None, magnet_link=None, output_path="./downloads"):
    """Download a torrent file or magnet link"""
    
    # Create output directory
    output_path = Path(output_path).resolve()
    output_path.mkdir(parents=True, exist_ok=True)
    
    print(f"📁 Download path: {output_path}")
    print("⚙️  Initializing torrent session...")
    
    # Create session
    ses = lt.session()
    ses.listen_on(6881, 6891)
    
    # Configure settings
    settings = {
        'user_agent': 'libtorrent/2.0',
        'listen_interfaces': '0.0.0.0:6881',
        'enable_outgoing_utp': True,
        'enable_incoming_utp': True,
        'enable_outgoing_tcp': True,
        'enable_incoming_tcp': True,
    }
    ses.apply_settings(settings)
    
    # Add DHT routers
    ses.add_dht_router("router.utorrent.com", 6881)
    ses.add_dht_router("router.bittorrent.com", 6881)
    ses.add_dht_router("dht.transmissionbt.com", 6881)
    ses.start_dht()
    
    # Add torrent
    params = {
        'save_path': str(output_path),
        'storage_mode': lt.storage_mode_t.storage_mode_sparse,
    }
    
    if torrent_file:
        print(f"📦 Loading torrent file: {torrent_file}")
        info = lt.torrent_info(torrent_file)
        params['ti'] = info
        handle = ses.add_torrent(params)
        print(f"📝 Name: {info.name()}")
        print(f"📊 Size: {format_size(info.total_size())}")
        print(f"📄 Files: {info.num_files()}")
    elif magnet_link:
        print(f"🧲 Loading magnet link...")
        handle = lt.add_magnet_uri(ses, magnet_link, params)
        print("⏳ Fetching metadata...")
    else:
        print("❌ Error: No torrent file or magnet link provided")
        return False
    
    # State strings
    state_str = [
        "queued", "checking", "downloading metadata", "downloading",
        "finished", "seeding", "allocating", "checking fastresume"
    ]
    
    print("\n🚀 Starting download...\n")
    
    # Monitor progress
    while not handle.status().is_seeding:
        s = handle.status()
        
        # Get torrent name (for magnet links)
        name = s.name if s.name else 'Fetching metadata...'
        
        # Calculate stats
        state = state_str[s.state] if s.state < len(state_str) else 'unknown'
        progress = s.progress * 100
        download_rate = s.download_rate / 1024  # KB/s
        upload_rate = s.upload_rate / 1024      # KB/s
        peers = s.num_peers
        seeds = s.num_seeds
        
        # Calculate ETA
        if s.download_rate > 0:
            eta_seconds = (s.total_wanted - s.total_wanted_done) / s.download_rate
            eta = format_time(eta_seconds)
        else:
            eta = "Unknown"
        
        # Progress bar
        bar_length = 40
        filled_length = int(bar_length * progress / 100)
        bar = '█' * filled_length + '░' * (bar_length - filled_length)
        
        # Clear line and print status
        print(f"\r📦 {name[:50]}", end='')
        print(f"\n[{bar}] {progress:.1f}%", end='')
        print(f"\n⬇️  {download_rate:.1f} KB/s | ⬆️  {upload_rate:.1f} KB/s", end='')
        print(f" | 👥 {peers} peers ({seeds} seeds)", end='')
        print(f" | ⏱️  ETA: {eta}", end='')
        print(f" | 📊 {state}        ", end='')
        
        # Move cursor up for next update
        sys.stdout.write('\033[3A')
        sys.stdout.flush()
        
        time.sleep(1)
    
    # Download complete
    s = handle.status()
    print("\n" * 4)  # Clear progress display
    print("="*70)
    print("✅ Download Complete!")
    print("="*70)
    print(f"📝 Name: {s.name}")
    print(f"📊 Size: {format_size(s.total_wanted)}")
    print(f"📁 Location: {output_path / s.name}")
    print("="*70)
    
    # Keep seeding for a bit
    print("\n⬆️  Seeding for 60 seconds... (Press Ctrl+C to stop)")
    try:
        for i in range(60, 0, -1):
            s = handle.status()
            upload_rate = s.upload_rate / 1024
            print(f"\r⬆️  {upload_rate:.1f} KB/s | {i}s remaining...   ", end='')
            sys.stdout.flush()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n⏸️  Seeding stopped")
    
    print("\n✅ Done!")
    return True


def main():
    parser = argparse.ArgumentParser(
        description='Download torrents to your local machine',
        epilog='Example: python3 torrent_downloader.py --torrent ubuntu.torrent --output ~/Downloads'
    )
    
    parser.add_argument('-t', '--torrent', help='Path to .torrent file')
    parser.add_argument('-m', '--magnet', help='Magnet link (wrap in quotes)')
    parser.add_argument('-o', '--output', default='./downloads', help='Output directory (default: ./downloads)')
    
    args = parser.parse_args()
    
    # Validate arguments
    if not args.torrent and not args.magnet:
        parser.error("Please provide either --torrent or --magnet")
    
    if args.torrent and args.magnet:
        parser.error("Please provide only one: --torrent OR --magnet")
    
    if args.torrent and not os.path.exists(args.torrent):
        print(f"❌ Error: Torrent file not found: {args.torrent}")
        sys.exit(1)
    
    # Check if libtorrent is available
    try:
        import libtorrent as lt
        print(f"✅ libtorrent {lt.__version__}")
    except ImportError:
        print("❌ Error: libtorrent not installed")
        print("\nInstall it with:")
        print("  sudo apt install python3-libtorrent")
        print("  OR")
        print("  pip3 install libtorrent")
        sys.exit(1)
    
    # Start download
    try:
        success = download_torrent(
            torrent_file=args.torrent,
            magnet_link=args.magnet,
            output_path=args.output
        )
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⏸️  Download cancelled by user")
        sys.exit(130)
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
