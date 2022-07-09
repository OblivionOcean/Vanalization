import os
import pathlib
from pydub import AudioSegment

desk = os.path.join(os.path.expanduser("~"),"Desktop")

def fext(f):
    file_extension = pathlib.Path(f.filename).suffix
    EXT = file_extension.strip('.')
    return EXT

def trans_sth_to_sth(filepath, input_type, output_type):
    try:
        song = AudioSegment.from_file(filepath, input_type)
        filename = filepath.split(".")[0]
        if os.getcwd() != desk:
            print(os.getcwd())
            os.chdir('./static/')
        song.export(f"{filename}.{output_type}", format=f"{output_type}")
        return 1
    except:
        return 0