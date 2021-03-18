# -*-coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QFont, QTextCursor, QFontDatabase
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication, QWidget, QMessageBox, QPushButton, QToolTip, \
    QSizePolicy, QScrollArea, QFileDialog, QInputDialog
import subprocess
from datetime import date, time, datetime, timedelta
import sys
import os
import speech_recognition as sr


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(863, 618)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.load_btn = QtWidgets.QPushButton(self.centralwidget)
        self.load_btn.setGeometry(QtCore.QRect(20, 550, 151, 41))
        self.load_btn.setObjectName("pushButton")
        self.load_btn.clicked.connect(self.load_audio_file)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 831, 491))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setFont(QFont("Calibri", 14))
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(700, 550, 151, 41))
        self.exit_btn.setObjectName("pushButton_3")
        self.exit_btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setGeometry(QtCore.QRect(360, 550, 151, 41))
        self.clear_btn.setObjectName("pushButton_4")
        self.clear_btn.clicked.connect(self.clear_text_browser_window)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Программа для транскрибации"))
        self.load_btn.setText(_translate("MainWindow", "Загрузить аудио файл"))
        self.exit_btn.setText(_translate("MainWindow", "Выход"))
        self.clear_btn.setText(_translate("MainWindow", "Очистить"))

    def center(self):
        frameGm = MainWindow.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        MainWindow.move(frameGm.topLeft())

    def clear_text_browser_window(self):
        """
        Очищает окно текстового браузера
        :return:
        """
        self.textBrowser.clear()

    def load_audio_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(MainWindow, "Загрузить файл",
                                                   "", "All Files (*);;Key Files (*.wav)",
                                                   options=options)
        try:
            recognizer = sr.Recognizer()
            with sr.AudioFile(file_name) as source:
                audio = recognizer.record(source)
                self.textBrowser.setText(recognizer.recognize_google(audio, language="ru-RU"))


        except AttributeError:
            pass

        except FileNotFoundError:
            pass

        except Exception:
            QtWidgets.QMessageBox.critical(MainWindow, 'Ошибка',
                                           'Произошла ошибка во время загрузки файла',
                                           QMessageBox.Ok)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
