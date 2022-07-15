import platform
import os
import shutil
import requests
import py7zr

print("**IT'S AN FFMPEG INSTALLER WHICH WILL APPARENTLY INSTALL FFMPEG AUTOMATICALLY.**")
print("**IT'S A REPLACEMENT OF MY BABYMODE IN OTHER PROGRAMS.**")
pf = platform.system()
desktop = os.path.expanduser("~/Desktop")
if pf == 'Windows':
    sth = requests.get('https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z')
    with open('ffmpeg-git-full.7z', 'w') as f:
        f.write(sth.content)
    with py7zr.SevenZipFile('ffmpeg-git-full.7z', mode='r') as z:
        z.extractall(path='tmp')
    shutil.copy('', desktop+"/ffmpeg安装目录")
    
elif pf == 'Darwin':
    print("**PLEASE BE SURE BREW IS INSTALLED.**")
    try:
        os.system("brew install ffmpeg")
        print("DONE!!!")
        input("**PRESS ENTER TO EXIT!**")
    except:
        print("**SEEMS LIKE STH'S WRONG?**")
        print("**WOW, YOU SHOULD CHECK YOUR BREW, IF YOU HAVEN'T INSTALL BREW, INSTALL ONE in (https://brew.sh/).**")
        input("**PRESS ENTER TO EXIT!**")