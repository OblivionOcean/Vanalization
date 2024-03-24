import platform
import os
import requests
import py7zr
import shutil

pm = platform.machine()

def linuxInstall():
    name = f"ffmpeg-{pm}.tar.xz"
    if pm.capitalize() in ("AMD64","ARM64","I686","ARMHF","ARMEL"):
        con = requests.get(f"https://johnvansickle.com/ffmpeg/builds/ffmpeg-git-{pm}-static.tar.xz").content
        with open(name, "wb") as f:
            f.write(con)
            os.system(f"tar xvJf {name}")
            print("We have downloaded the suitable version of FFMpeg for you in the same folder. Please check it out")
        for root, dirs, files in os.walk("."):
            if "ffmpeg" in dirs:
                os.chdir(dirs)
        with open(".ffmpeg_profile" ,"wt") as x:
            x.write(f"export PATH={os.path.abspath('.')}:$PATH")
    else:
        print("Unable to Install FFMpeg for You.")
        raise SystemError
        

print("**It's a USELESS FFMpeg installer.**")

pf = platform.system()

if pf == 'Darwin':
    print("System: Darwin")
    try:
        print("Please wait")
        os.system("brew install ffmpeg")
        print("Successfully installed FFMpeg to your Mac.")
    except:
        print("Something's WRONG?")
        print("Wow, you should check your brew, if you haven't install brew, install one in (https://brew.sh/).")

elif pf == 'Linux':
    try:
        print("System: Linux")
        linuxInstall()
    except:
        print("A problem occured when running this program. Please try to install ffmpeg manually.")

elif pf == 'Windows':
    print("Please RUN AS AN ADMIN.")
    try:
        spath = os.path.expandvars("%windir%\\System32")
        cont = requests.get("https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.7z")
        with open('ffmpeg-essencials.7z', "wb") as f:
            f.write(cont)
        with py7zr.SevenZipFile('ffmpeg-essentials.7z', mode='r') as z:
            z.extractall()
        for root, dirs, files in os.walk("."):
                if "ffmpeg" in dirs:
                    os.chdir(dirs)
        os.chdir("bin")
        shutil.copy("ffmpeg.exe",spath+"\\ffmpeg.exe")
        shutil.copy("ffplay.exe",spath+"\\ffplay.exe")
        shutil.copy("ffprobe.exe",spath+"\\ffprobe.exe")
        print("Successfully installed FFMpeg to your PC.")
    except:
        print("A problem occured when running this program. Please try to install ffmpeg manually.")

input("**Press [Enter] to EXIT!**")