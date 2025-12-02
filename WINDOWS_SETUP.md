# 🪟 Windows Setup Guide

Run torrents directly on your Windows machine using a simple Python script!

## ⚠️ Important Note

**libtorrent** has compatibility issues with Windows. Here are your options:

---

## 🎯 **Option 1: Use Google Colab** (Recommended for Windows)

**Easiest solution** - No installation needed!

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ushanmalinda/torrent-to-google-drive/blob/main/Torrent_to_Google_Drive.ipynb)

Just click and run - works perfectly on Windows!

---

## 🎯 **Option 2: Use WSL (Windows Subsystem for Linux)**

Run the Ubuntu version inside Windows!

### Step 1: Install WSL

```powershell
# Open PowerShell as Administrator and run:
wsl --install
```

Or manually:
1. Open PowerShell as Administrator
2. Run: `wsl --install -d Ubuntu`
3. Restart your computer
4. Open "Ubuntu" from Start menu
5. Create username and password

### Step 2: Install Dependencies in WSL

```bash
# Inside Ubuntu terminal:
sudo apt update
sudo apt install python3-libtorrent git

# Verify installation
python3 -c "import libtorrent; print('✅ libtorrent installed!')"
```

### Step 3: Download and Use

```bash
# Clone the repo
git clone https://github.com/Ushanmalinda/torrent-to-google-drive.git
cd torrent-to-google-drive

# Run downloads
python3 torrent_downloader.py --torrent file.torrent --output ~/Downloads

# Access files from Windows at:
# \\wsl$\Ubuntu\home\YOUR_USERNAME\Downloads
```

### Access WSL Files from Windows

1. Open File Explorer
2. In address bar type: `\\wsl$\Ubuntu\home\YOUR_USERNAME\`
3. Your downloads will be in the `Downloads` folder

---

## 🎯 **Option 3: Use Docker** (Advanced)

Run in a container with everything pre-installed.

### Step 1: Install Docker Desktop

Download from: https://www.docker.com/products/docker-desktop/

### Step 2: Create Dockerfile

Save this as `Dockerfile` in your project folder:

```dockerfile
FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-libtorrent \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY torrent_downloader.py .

ENTRYPOINT ["python3", "torrent_downloader.py"]
```

### Step 3: Build and Run

```powershell
# Build the image
docker build -t torrent-downloader .

# Run with torrent file
docker run -v ${PWD}:/downloads torrent-downloader --torrent /downloads/file.torrent --output /downloads

# Run with magnet link
docker run -v ${PWD}:/downloads torrent-downloader --magnet "magnet:?xt=..." --output /downloads
```

Files will be saved in your current directory!

---

## 🎯 **Option 4: Alternative Torrent Client** (Traditional)

If you just want to download torrents on Windows, use a regular client:

### Free Torrent Clients:
1. **qBittorrent** (Recommended) - https://www.qbittorrent.org/
2. **Transmission** - https://transmissionbt.com/
3. **Deluge** - https://deluge-torrent.org/

These are easier to use on Windows and don't require Python.

---

## 🎯 **Option 5: Use Portable Python Build** (Experimental)

Try installing Python with pre-compiled libtorrent:

### Step 1: Install Python 3.10

Download Python 3.10 (not 3.11+) from: https://www.python.org/downloads/

⚠️ **Important:** Check "Add Python to PATH" during installation

### Step 2: Try Installing libtorrent

```powershell
# Open PowerShell or Command Prompt
pip install libtorrent

# Test if it works
python -c "import libtorrent; print('Success!')"
```

If this works (rare on Windows), you can use the script:

```powershell
# Clone repo
git clone https://github.com/Ushanmalinda/torrent-to-google-drive.git
cd torrent-to-google-drive

# Run
python torrent_downloader.py --torrent file.torrent --output C:\Downloads
```

⚠️ **This often fails on Windows** due to missing C++ dependencies

---

## 📊 Comparison: Which Option for Windows?

| Option | Difficulty | Best For |
|--------|-----------|----------|
| **Google Colab** | ⭐ Easy | Everyone, works 100% |
| **WSL** | ⭐⭐ Medium | Want Linux tools on Windows |
| **Docker** | ⭐⭐⭐ Advanced | Developers, clean environment |
| **Regular Client** | ⭐ Easy | Just want to download torrents |
| **Native Python** | ⭐⭐⭐⭐ Hard | Usually doesn't work |

---

## 🎯 **Recommended Workflow for Windows Users**

### For Quick Downloads:
→ Use **Google Colab** (click badge in README)

### For Frequent Use:
→ Install **WSL** and use Ubuntu version

### For Simple Use:
→ Install **qBittorrent** desktop app

---

## 💡 WSL Quick Reference

### Common Commands:

```powershell
# Start WSL from Windows
wsl

# Run command in WSL from PowerShell
wsl python3 torrent_downloader.py --torrent file.torrent

# Copy file from Windows to WSL
# In PowerShell:
wsl cp /mnt/c/Users/YourName/Downloads/file.torrent ~/

# Copy from WSL to Windows
wsl cp ~/Downloads/result.iso /mnt/c/Users/YourName/Downloads/
```

### Access Windows drives from WSL:
- `C:\` is at `/mnt/c/`
- `D:\` is at `/mnt/d/`

### Example: Download to Windows Downloads folder

```bash
# In WSL
python3 torrent_downloader.py --torrent file.torrent --output /mnt/c/Users/YourName/Downloads
```

---

## 🔧 Troubleshooting WSL

### WSL not installed?

```powershell
# Enable WSL (PowerShell as Admin)
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

# Restart computer

# Install Ubuntu
wsl --install -d Ubuntu
```

### Can't find WSL files?

Open File Explorer and go to: `\\wsl$\`

### WSL is slow?

Make sure you're using WSL 2:
```powershell
wsl --set-default-version 2
```

---

## 🎬 Video Tutorial (Concept)

**Using WSL for Torrents:**
1. Install WSL → Open Ubuntu terminal
2. Install libtorrent → Run script
3. Access files from Windows Explorer
4. Done!

---

## ❓ FAQ

**Q: Can I run the Python script natively on Windows?**  
A: It's very difficult. libtorrent has C++ dependencies that are hard to compile on Windows. WSL is much easier.

**Q: Is WSL safe?**  
A: Yes! It's an official Microsoft feature. It's just Linux running inside Windows.

**Q: Will WSL slow down my computer?**  
A: No, it's lightweight and only uses resources when you're using it.

**Q: Can I use both Colab and WSL?**  
A: Yes! Use Colab when you're away from your PC, and WSL when you're at home.

**Q: Do I need Ubuntu knowledge?**  
A: No! Just follow the commands above. It's very similar to Command Prompt.

---

## 🚀 Quick Start: Best Path for Windows

```powershell
# 1. Install WSL (one-time setup)
wsl --install

# 2. Restart computer

# 3. Open Ubuntu from Start menu

# 4. Inside Ubuntu terminal:
sudo apt update
sudo apt install python3-libtorrent git
git clone https://github.com/Ushanmalinda/torrent-to-google-drive.git
cd torrent-to-google-drive

# 5. Download torrents!
python3 torrent_downloader.py --torrent /mnt/c/Users/YourName/Downloads/file.torrent --output /mnt/c/Users/YourName/Downloads
```

---

## 📚 Additional Resources

- [WSL Documentation](https://docs.microsoft.com/en-us/windows/wsl/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [qBittorrent Download](https://www.qbittorrent.org/download.php)
- [Python Downloads](https://www.python.org/downloads/)

---

## 🤝 Need Help?

- 🐛 [Report Issues](https://github.com/Ushanmalinda/torrent-to-google-drive/issues)
- 💬 [Ask Questions](https://github.com/Ushanmalinda/torrent-to-google-drive/discussions)

---

**TL;DR for Windows Users:**

- **Easiest**: Use Google Colab (just click and run)
- **Best for regular use**: Install WSL + Ubuntu version
- **Alternative**: Use qBittorrent desktop app

All options work great on Windows! 🚀
