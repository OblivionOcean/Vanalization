import os
import shutil
import requests
import py7zr

desktop = os.path.expanduser("~/Desktop")
sth = requests.get('https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z')
with open('ffmpeg-git-full.7z', 'w') as f:
    f.write(sth.content)
with py7zr.SevenZipFile('ffmpeg-git-full.7z', mode='r') as z:
    z.extractall(path='/tmp')