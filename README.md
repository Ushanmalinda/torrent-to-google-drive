# 🌩️ Torrent to Google Drive Converter

**Download torrents directly to your Google Drive using Google Colab's free cloud servers!**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ushanmalinda/torrent-to-google-drive/blob/main/Torrent_to_Google_Drive.ipynb)

## ✨ Features

- ✅ **100% Free** - No installation, no cost, no sign-ups needed
- ✅ **Fast Downloads** - Leverage Google's high-speed infrastructure
- ✅ **Direct to Drive** - Files automatically saved to your Google Drive
- ✅ **Zero Local Storage** - Everything happens in the cloud
- ✅ **Multiple Formats** - Supports both .torrent files and magnet links
- ✅ **Live Progress Tracking** - Real-time download monitoring with progress bars
- ✅ **Instant Access** - Get clickable links to your files immediately after download
- ✅ **Easy to Use** - Simple notebook interface, no technical knowledge required

## 🚀 How to Use

### Step 1: Open in Google Colab
Click the "Open in Colab" badge above or [click here](https://colab.research.google.com/github/Ushanmalinda/torrent-to-google-drive/blob/main/Torrent_to_Google_Drive.ipynb)

### Step 2: Run the Cells
Execute each cell in order by clicking the ▶️ play button or pressing `Shift + Enter`:

1. **Cell 1** - Install dependencies (~30 seconds)
2. **Cell 2** - Initialize torrent engine
3. **Cell 3** - Connect your Google Drive (will ask for permission)
4. **Cell 4** - Upload your .torrent file(s) OR
5. **Cell 5** - Paste a magnet link
6. **Cell 6** - Watch live download progress
7. **Cell 7** - Get direct links to access your files

### Step 3: Access Your Files
Click the generated Google Drive links to open your downloaded files instantly!

## 📋 Requirements

- A Google account (for Google Colab and Google Drive)
- Internet connection
- A valid torrent file or magnet link

**That's it!** No installation, no software, no configuration needed.

## ⚠️ Important Notes

### Python Version
If Cell 1 shows an error:
1. Go to `Runtime` → `Change runtime type`
2. Select `Python 3.10` from the dropdown
3. Click `Save`
4. Run Cell 1 again

### Session Limits
- **Free Colab sessions last ~12 hours**
- Keep your browser tab open while downloading
- Downloads will stop if you close the tab or lose connection

### Storage
- Files use **your Google Drive storage quota**
- Check your available space before downloading large files
- Free Google accounts get 15GB of storage

### Legal Usage
**⚠️ Important**: Only download content you have legal rights to access. This includes:
- Open-source software
- Public domain content
- Linux distributions
- Content you own or have permission to download

**Do NOT use this tool for piracy or illegal downloads.**

## 🎯 Example Use Cases

### ✅ Legal Uses:
- Download Linux distributions (Ubuntu, Debian, Fedora, etc.)
- Get open-source software packages
- Archive public domain movies and books
- Download Creative Commons content
- Backup your own files distributed via torrent
- Academic datasets and research materials

### ❌ Illegal Uses (DO NOT):
- Pirated movies, TV shows, or music
- Copyrighted software without permission
- Any content that violates copyright laws

## 💡 Pro Tips

1. **Download Multiple Torrents**: Upload several .torrent files in Cell 4 before running Cell 6 to download them all in parallel
2. **Keep Tab Open**: Don't close the browser tab while downloading
3. **Check Progress**: Cell 6 shows real-time speed, peers, and completion percentage
4. **Quick Access**: Use the links in Cell 7 to open files without searching through your Drive
5. **Organize Files**: Downloaded files are automatically organized in a `Torrents` folder in your Drive

## 🔧 Troubleshooting

### "Module libtorrent not found"
**Solution**: Change runtime to Python 3.10:
- `Runtime` → `Change runtime type` → `Python 3.10` → `Save`

### "Session disconnected"
**Solution**: Your session timed out. Re-run all cells from the beginning.

### "Out of memory" error
**Solution**: The file might be too large. Try downloading smaller torrents or restart the runtime.

### Downloads are slow
**Possible reasons**:
- Few seeders available for the torrent
- Time of day (peak usage hours)
- Torrent health/popularity

### Can't find my files
**Solution**: Run Cell 7 to get direct links, or check your Google Drive in the `Torrents` folder.

## 📊 Performance

**Typical download speeds**:
- Well-seeded torrents: 5-20 MB/s
- Moderately seeded: 1-5 MB/s
- Poorly seeded: <1 MB/s

**Speed depends on**:
- Number of seeders
- Torrent health
- Google's current network conditions
- Time of day

## 🤝 Contributing

Contributions are welcome! If you have suggestions or improvements:

1. Fork this repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit (`git commit -am 'Add new feature'`)
5. Push (`git push origin feature/improvement`)
6. Create a Pull Request

## ⭐ Support This Project

If you find this tool useful:
- ⭐ Star this repository
- 🔄 Share it with others
- 🐛 Report bugs or issues
- 💡 Suggest new features

## 📝 License

This project is provided as-is for educational and legal use only. 

**Disclaimer**: The creators of this tool are not responsible for how users choose to use it. Users are solely responsible for ensuring their use complies with all applicable laws and regulations.

## 🔗 Related Projects

- [Google Colab](https://colab.research.google.com/)
- [libtorrent](https://www.libtorrent.org/)
- [Google Drive API](https://developers.google.com/drive)

## 📧 Contact

Have questions or suggestions? 
- Open an [Issue](https://github.com/Ushanmalinda/torrent-to-google-drive/issues)
- Start a [Discussion](https://github.com/Ushanmalinda/torrent-to-google-drive/discussions)

---

**Made with ❤️ for the open-source community**

**Remember**: Use this tool responsibly and legally!
