# SubsyncDLSubs
a script to walk on your media directory to sync already downloaded subtitles with subsync. Assuming you have fixed naming schema for both movies and their subtitles, like *.MKV for movie and *.en.srt

<br />

---
## Usage:
```
python sync.py <PATH> <audio_lang> <subtitles_lang>
```

<br />

### Example:
```
python sync.py "Z:\Movies" en ar
```
---


### Packeges:
```
pip install pymediainfo
```
<br />

--- 

## Note: 
- subsync should be installed and **subsync-cmd.exe** have to be added to windows's enviroment variable.
    - to download: https://subsync.online/
- tested on windows.
- some arguments of sybsync are hardcoded in the script, feel free to tweak them as you like.
<br />

--- 
## to-do 
- add multithreading support to process large amount of media faster.
- sync multiple subtitles with diff language to the same movie. (for now only one language per time)
