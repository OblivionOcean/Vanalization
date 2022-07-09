# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(302, 108)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(70, 60, 101, 31))
        font = QFont()
        font.setFamilies([u"YuMincho +36p Kana"])
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.comboBox.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 60, 71, 31))
        font1 = QFont()
        font1.setFamilies([u"Weibei SC"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.label.setFont(font1)
        self.TransNow = QPushButton(self.centralwidget)
        self.TransNow.setObjectName(u"TransNow")
        self.TransNow.setGeometry(QRect(180, 60, 111, 41))
        font2 = QFont()
        font2.setFamilies([u"Weibei SC"])
        font2.setPointSize(24)
        font2.setBold(True)
        self.TransNow.setFont(font2)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 211, 41))
        font3 = QFont()
        font3.setFamilies([u"Weibei SC"])
        font3.setPointSize(24)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        self.label_2.setFont(font3)
        self.ChooseFile = QPushButton(self.centralwidget)
        self.ChooseFile.setObjectName(u"ChooseFile")
        self.ChooseFile.setGeometry(QRect(180, 10, 111, 41))
        self.ChooseFile.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"MP4", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"MP3", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"FLV", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"MOV", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"FLAC", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"OGG", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"WMA", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"AVI", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"WMV", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"WAV", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"M4A", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u5316\u4e3a\uff1a", None))
        self.TransNow.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8f6c\u6362", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Van\u80fd\u8f6c\u6362\u5668", None))
        self.ChooseFile.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
    # retranslateUi

