# 🐧 Ubuntu/Linux Setup Guide

Run torrents directly on your Ubuntu machine - faster, no time limits, complete control!

## 🚀 Quick Start

### 1️⃣ Install Dependencies

```bash
# Update package list
sudo apt update

# Install libtorrent (Python bindings)
sudo apt install python3-libtorrent

# Verify installation
python3 -c "import libtorrent; print(f'libtorrent {libtorrent.__version__} installed!')"
```

**Alternative installation** (if apt doesn't work):
```bash
pip3 install libtorrent
```

### 2️⃣ Download the Script

```bash
# Clone the repository
git clone https://github.com/Ushanmalinda/torrent-to-google-drive.git
cd torrent-to-google-drive

# Make script executable
chmod +x torrent_downloader.py
```

### 3️⃣ Run Your First Download

**Download a torrent file:**
```bash
python3 torrent_downloader.py --torrent ubuntu.torrent --output ~/Downloads
```

**Download from magnet link:**
```bash
python3 torrent_downloader.py --magnet "magnet:?xt=urn:btih:..." --output ~/Downloads
```

---

## 📋 Usage Examples

### Basic Usage

```bash
# Download to current directory
python3 torrent_downloader.py --torrent file.torrent

# Download to specific location
python3 torrent_downloader.py --torrent file.torrent --output /home/user/Videos

# Use magnet link
python3 torrent_downloader.py --magnet "magnet:?xt=urn:btih:ABC123..." --output ~/Downloads
```

### Advanced Usage

**Download multiple torrents sequentially:**
```bash
#!/bin/bash
for torrent in *.torrent; do
    python3 torrent_downloader.py --torrent "$torrent" --output ~/Downloads
done
```

**Run in background:**
```bash
nohup python3 torrent_downloader.py --torrent file.torrent --output ~/Downloads > download.log 2>&1 &
```

**Check background process:**
```bash
# View log
tail -f download.log

# Find process
ps aux | grep torrent_downloader

# Kill process
kill <PID>
```

---

## 🎯 Features

### Local Ubuntu Version:
- ✅ **No time limits** - Run as long as needed
- ✅ **Faster** - Uses your own internet connection
- ✅ **Offline** - No cloud dependency
- ✅ **Full control** - Choose any download location
- ✅ **Background running** - Can run 24/7
- ✅ **Live progress** - Real-time speed and ETA
- ✅ **Auto-seeding** - Seeds for 60 seconds after download

### Colab Version (still available):
- ✅ **Free cloud servers** - No local resources used
- ✅ **High-speed downloads** - Google's infrastructure
- ✅ **Google Drive integration** - Auto-upload to Drive
- ✅ **No installation** - Just click and run

---

## 📊 What You'll See

```
📁 Download path: /home/user/Downloads
⚙️  Initializing torrent session...
📦 Loading torrent file: ubuntu.torrent
📝 Name: ubuntu-22.04-desktop-amd64.iso
📊 Size: 3.45 GB
📄 Files: 1

🚀 Starting download...

📦 ubuntu-22.04-desktop-amd64.iso
[████████████████████░░░░░░░░░] 65.3%
⬇️  2450.5 KB/s | ⬆️  120.3 KB/s | 👥 25 peers (15 seeds) | ⏱️  ETA: 8m 45s | 📊 downloading

✅ Download Complete!
======================================================================
📝 Name: ubuntu-22.04-desktop-amd64.iso
📊 Size: 3.45 GB
📁 Location: /home/user/Downloads/ubuntu-22.04-desktop-amd64.iso
======================================================================

⬆️  Seeding for 60 seconds... (Press Ctrl+C to stop)
⬆️  450.2 KB/s | 32s remaining...
```

---

## ⚙️ Configuration

### Change Default Download Path

Edit the script or use `--output`:
```bash
python3 torrent_downloader.py --torrent file.torrent --output /mnt/storage/torrents
```

### Change Port Range

Edit line 49 in `torrent_downloader.py`:
```python
ses.listen_on(6881, 6891)  # Change these port numbers
```

### Skip Seeding

Press `Ctrl+C` during the 60-second seeding period to exit immediately.

---

## 🔧 Troubleshooting

### Error: "ModuleNotFoundError: No module named 'libtorrent'"

**Solution 1** (Recommended):
```bash
sudo apt install python3-libtorrent
```

**Solution 2** (If apt fails):
```bash
pip3 install libtorrent
```

**Solution 3** (Build from source):
```bash
sudo apt install build-essential libboost-all-dev libssl-dev python3-dev
pip3 install libtorrent --no-binary :all:
```

### Error: "Permission denied"

**Make script executable:**
```bash
chmod +x torrent_downloader.py
```

**Or run with python3:**
```bash
python3 torrent_downloader.py --torrent file.torrent
```

### Slow Download Speed

**Check:**
- Number of seeders (use well-seeded torrents)
- Your internet connection
- Firewall settings (open ports 6881-6891)
- ISP throttling (some ISPs limit torrent traffic)

**Improve speed:**
```bash
# Open firewall ports
sudo ufw allow 6881:6891/tcp
sudo ufw allow 6881:6891/udp
```

### Downloads Keep Stopping

**Run in screen/tmux:**
```bash
# Install screen
sudo apt install screen

# Start screen session
screen -S torrent

# Run download
python3 torrent_downloader.py --torrent file.torrent

# Detach: Press Ctrl+A then D
# Reattach: screen -r torrent
```

---

## 🆚 Ubuntu vs Google Colab

| Feature | Ubuntu (Local) | Google Colab (Cloud) |
|---------|----------------|----------------------|
| **Speed** | Your ISP speed | 5-20 MB/s (Google) |
| **Time Limit** | Unlimited | ~12 hours |
| **Storage** | Your disk | Google Drive (15GB free) |
| **Internet** | Uses your bandwidth | Free (Google's) |
| **Setup** | One-time install | No install needed |
| **Accessibility** | Only on your PC | Anywhere with browser |
| **Best For** | Large files, 24/7 | Quick downloads, away from PC |

---

## 💡 Pro Tips

### 1. Create an Alias
```bash
# Add to ~/.bashrc
echo "alias torrent='python3 ~/torrent-to-google-drive/torrent_downloader.py'" >> ~/.bashrc
source ~/.bashrc

# Now you can use:
torrent --torrent file.torrent
```

### 2. Set Default Download Path
```bash
# Add to ~/.bashrc
export TORRENT_PATH="$HOME/Downloads/Torrents"
mkdir -p "$TORRENT_PATH"

# Use in command:
torrent --torrent file.torrent --output "$TORRENT_PATH"
```

### 3. Run as System Service

Create `/etc/systemd/system/torrent@.service`:
```ini
[Unit]
Description=Torrent Download Service
After=network.target

[Service]
Type=simple
User=%i
ExecStart=/usr/bin/python3 /path/to/torrent_downloader.py --torrent %h/torrent.torrent --output %h/Downloads
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

### 4. Monitor Multiple Downloads

Create a bash wrapper:
```bash
#!/bin/bash
# download_all.sh

for torrent in "$1"/*.torrent; do
    echo "Starting: $torrent"
    python3 torrent_downloader.py --torrent "$torrent" --output "$2" &
done
wait
echo "All downloads complete!"
```

---

## 🔐 Security Notes

- ✅ Only download legal content
- ✅ Use VPN if concerned about privacy
- ✅ Check torrent sources before downloading
- ✅ Scan downloaded files with antivirus
- ⚠️ Be aware of copyright laws in your country

---

## 📚 Additional Resources

- [libtorrent Documentation](https://www.libtorrent.org/)
- [BitTorrent Protocol](https://www.bittorrent.org/beps/bep_0003.html)
- [Ubuntu Firewall Guide](https://help.ubuntu.com/community/UFW)

---

## 🤝 Need Help?

- 🐛 [Report Issues](https://github.com/Ushanmalinda/torrent-to-google-drive/issues)
- 💬 [Ask Questions](https://github.com/Ushanmalinda/torrent-to-google-drive/discussions)
- 📖 [Main README](README.md)

---

**Choose what works best for you:**
- **Use Colab** when you're away from your PC or want free cloud downloading
- **Use Ubuntu script** when you need full control, unlimited time, and faster speeds

Both options are available in this repository! 🚀
