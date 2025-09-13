# 🎵 Music Player (Python + VLC)

This is a simple **command-line music player** built using **Python** and the **VLC library**.
It allows you to play songs continuously, shuffle them, like/favorite songs, and even select specific songs to play.

---

## 🚀 Features

* ▶️ **Continuous Play** – Plays songs one after another
* 🔀 **Shuffle Play** – Plays songs in random order
* ❤️ **Like Songs** – Save favorite songs while listening
* 🗑️ **Manage Favorites** – View or delete your liked songs
* 🎶 **Choose Your Song** – Select a song by number from the list

---

## 🛠️ Tech Stack

* **Python 3**
* **VLC Python Bindings (`python-vlc`)**

---

## 📂 Project Structure

```
├── music_player.py     # Main Python script
├── songs/              # Folder containing mp3 songs
```

---

## ⚡ How to Run

1. Install **VLC Media Player** on your system
2. Install required Python library:

   ```bash
   pip install python-vlc
   ```
3. Update the song file paths inside `music_player.py` if needed
4. Run the program:

   ```bash
   python music_player.py
   ```

---

## 📌 Usage Instructions

When you start the program, you will see these options:

* `1` → Play songs continuously
* `2` → View liked songs
* `3` → Play your liked songs
* `4` → Select and play a specific song
* `5` → Play songs in shuffled order
* `6` → Exit

While playing:

* Press **Enter** → Go to next song
* Press **l** → Like the current song
* Press **q** → Quit playback
* Press **d** → Delete a liked song

---

## 🎯 Note

* This project is for **learning and practice purposes**
* Make sure you update the correct file paths for your songs


Would you like me to also **add some screenshots/GIF demo steps** to make the README look more attractive for GitHub?
