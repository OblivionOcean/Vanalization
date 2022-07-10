import sys
import pathlib
from pydub import AudioSegment
from gui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PySide6 import QtCore
import cv2

QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
MUSIC = ["MP3", "FLAC", "WAV", "OGG", "WMA", "M4A"]
VIDEO = ["MP4", "FLV", "MOV", "WMV", "AVI"]
loadtext = """食用说明: 
1. 文件的保存位置一般为原文件位置。
2. 部分格式之间的互换未经过完整测试。
3. 支持视频转视频，视频转音频，音频转音频。
4. 请勿作死尝试将音频转成视频。
5. 未在Windows/Linux上经过测试，理论上支持这两个平台。
6. 有bug可反馈至作者博客: https://chuishen.cf/。
7. 请通过源代码安装的用户自行安装ffmpeg。地址: https://ffmpeg.org/。
8. 支持导出的文件格式有: MP3, FLAC, WAV, OGG, WMA, M4A, MP4, FLV, MOV, WMV, AVI等，支持导入的文件格式更加多样，且未来将支持更多导出格式。"""

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.TransNow.clicked.connect(self.tran)
        self.ui.ChooseFile.clicked.connect(self.choicebox)
        self.filename = None
        self.func = None
        QMessageBox.information(self, "食用说明", loadtext, QMessageBox.Ok)

    def fext(self, f):
        file_extension = pathlib.Path(f).suffix
        EXT = file_extension.strip('.')
        return EXT
    
    def to_video(self, filepath, input_type, output_type):
        try:
            cap = cv2.VideoCapture(filepath)
            frame_cnt = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            weight = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            fps = int(cap.get(cv2.CAP_PROP_FPS))
            size = (weight, height)
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter(filepath+"."+output_type, fourcc, fps, size)
            for n in range(frame_cnt):
                _, frame = cap.read()
                out.write(frame)
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
            cap.release()
            out.release()
            return 1
        except:
            return 0
    
    def to_audio(self, filepath, input_type, output_type):
        try:
            song = AudioSegment.from_file(filepath)
            print(song)
            filename = filepath.split(".")[-2]
            song.export(f"{filename}.{output_type}", format=f"{output_type}")
            return 1
        except Exception as e:
            return 0
    
    def choicebox(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "选择音乐、视频", ".", "*")
        self.file = filePath

    def tran(self):
        text = self.ui.comboBox.currentText()
        suffix = self.fext(self.file).upper()
        if text in MUSIC:
            self.func = self.to_audio
        elif text in VIDEO:
            self.func = self.to_video
        if self.func(self.file, suffix, text) == 0:
            QMessageBox.information(self, "出错啦!", "出错啦!请检查配置与输入有无错误。", QMessageBox.Ok)
        else:
            QMessageBox.information(self, "成功!", "成功!", QMessageBox.Ok)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())