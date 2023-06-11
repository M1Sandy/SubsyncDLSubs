#!/usr/bin/python3

import os
import subprocess
import sys
from pymediainfo import MediaInfo

def isVideo(file):
    try:
        fInfo = MediaInfo.parse(file)
    except:
        return False
    for track in fInfo.tracks:
        if track.track_type == "Video":
            return True
    return False

def SubExist(file):
    if os.path.exists(file):
        return True
    return False

def GetSubFileName(dir, filename):
    for file in dir:
        if isVideo(file):
            continue
        if filename in file and file.endswith("srt"):
            return file
    return filename
    

if __name__ == "__main__":
        if len(sys.argv) != 4:
            print("[-] Usage: sync.py <PATH> <subtitles_lang> <audio_lang> ")
            exit()
        rootdir = sys.argv[1]
        sub_lang = str(sys.argv[2])
        audio_lang = str(sys.argv[3])

        for subdir, dirs, files in os.walk(rootdir):
            for file in files:
                if not file.endswith("srt") and isVideo(os.path.join(subdir,file)):
                    tFileName = os.path.splitext(file)
                    tmp = tFileName[0]
                    relatedSub = GetSubFileName(files, tmp)
                    if relatedSub == tmp:
                        print(f"[-] No sub Found. [{tmp}]")
                    tmp += "." + sub_lang + ".srt"
                    if SubExist(os.path.join(subdir,tmp)):
                        print("[*] Sub Found. Syncing . . .")
                        cmd = ["subsync-cmd.exe",
                                "sync",
                                "--sub-lang",
                                sub_lang,       
                                "--ref-lang",
                                audio_lang,        
                                "--sub",
                                os.path.join(subdir,tmp),
                                "--ref" ,
                                os.path.join(subdir,file), 
                                "--out", os.path.join(subdir,tmp),
                                "--window-size=10000",
                                "--effort=1",
                                "--overwrite"]
                        proc = subprocess.Popen(cmd)
                        proc.wait()
                        print(f"[+] Synced.[{tmp}][{file}]")
                    else:
                        print(f"[-] Sub NOT Found. [{tmp}]")
                        continue

                    # print(f"[{os.path.join(subdir,tmp)}] [Video]")


