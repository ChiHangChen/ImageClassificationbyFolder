# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QStatusBar, QScrollArea, QDialog,QProgressBar
from PyQt5.QtCore import QRect, Qt, QSize, QMetaObject, QCoreApplication
from PyQt5.QtGui import QFont, QIcon, QPixmap
import sys
from os.path import join, abspath

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return join(sys._MEIPASS, relative_path)
    return join(abspath("."), relative_path)
     
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.img_qlabel = QLabel(self.centralwidget)
        self.img_qlabel.setFont(QFont("Roman times",15,QFont.Bold))
        self.img_qlabel.setGeometry(QRect(20, 20, 405, 551))
        self.img_qlabel.setStyleSheet("QLabel{color: gray;border: 1px solid gray}")
        self.img_qlabel.setAlignment(Qt.AlignLeading|Qt.AlignCenter|Qt.AlignCenter)
        self.img_qlabel.setObjectName("img_qlabel")
        
        self.text_qlabel = QLabel(self.centralwidget)
        self.text_qlabel.setFont(QFont("Roman times",12,QFont.Bold))
        self.text_qlabel.setGeometry(QRect(0, 0, 800, 190))
        self.text_qlabel.setStyleSheet("background: white; color: rgb(121, 121, 121)")
        self.text_qlabel.setObjectName("text_qlabel")
        self.text_qlabel.setTextInteractionFlags(Qt.TextSelectableByMouse)
        
        self.scroll = QScrollArea(self.centralwidget)
        self.scroll.setGeometry(QRect(440, 20, 350, 190))
        self.scroll.setWidget(self.text_qlabel)

        self.clipButton = QPushButton(self.centralwidget)
        self.clipButton.setGeometry(QRect(450, 220, 160, 75))
        self.clipButton.setObjectName("clipButton")
        self.clipButton.setIcon(QIcon(QPixmap(resource_path('scissors.png'))))
        self.clipButton.setIconSize(QSize(40, 40))
        self.clipButton.setFont(QFont("Roman times",10,QFont.Bold))
        
        self.MergeButton = QPushButton(self.centralwidget)
        self.MergeButton.setGeometry(QRect(621, 220, 160, 75))
        self.MergeButton.setObjectName("MergeButton")
        self.MergeButton.setIcon(QIcon(QPixmap(resource_path('paste.png'))))
        self.MergeButton.setIconSize(QSize(40, 40))
        self.MergeButton.setFont(QFont("Roman times",10,QFont.Bold))
        
        self.bbox_label = QLabel(self.centralwidget)
        self.bbox_label.setFont(QFont("Roman times",10))
        self.bbox_label.setGeometry(QRect(450, 310, 331, 2))
        self.bbox_label.setStyleSheet("QLabel{color: red;border: 1px solid gray}")
        self.bbox_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.bbox_label.setOpenExternalLinks(False)
        self.bbox_label.setObjectName("bbox_label")
        # -----------------------------------------------------------------------
        self.pathButton = QPushButton(self.centralwidget)
        self.pathButton.setGeometry(QRect(450, 325, 331, 75))
        self.pathButton.setObjectName("pathButton")
        self.pathButton.setIcon(QIcon(QPixmap(resource_path('folder.png'))))
        self.pathButton.setIconSize(QSize(40, 40))   
        self.pathButton.setFont(QFont("Roman times",10,QFont.Bold))
        
        self.prevButton = QPushButton(self.centralwidget)
        self.prevButton.setGeometry(QRect(450, 415, 331, 75))
        self.prevButton.setObjectName("prevButton")
        self.prevButton.setIcon(QIcon(QPixmap(resource_path('back.png'))))
        self.prevButton.setIconSize(QSize(40, 40))   
        self.prevButton.setFont(QFont("Roman times",10,QFont.Bold))
        
        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QRect(450, 505, 331, 75))
        self.saveButton.setObjectName("saveButton")
        self.saveButton.setIcon(QIcon(QPixmap(resource_path('download.png'))))
        self.saveButton.setIconSize(QSize(40, 40))   
        self.saveButton.setFont(QFont("Roman times",10,QFont.Bold))
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quick Classification"))
        self.img_qlabel.setText(_translate("MainWindow", "Image Display"))
        self.text_qlabel.setText(_translate("MainWindow", "Please select a folder"))
        self.clipButton.setText(_translate("MainWindow", "Clip to BBox"))
        self.MergeButton.setText(_translate("MainWindow", "Merge to Json"))
        self.pathButton.setText(_translate("MainWindow", "Open Dir"))
        self.prevButton.setText(_translate("MainWindow", "Previous"))
        self.saveButton.setText(_translate("MainWindow", "Save"))

class progressWindow(QDialog):
    def __init__(self,bar_len,title):
        super().__init__()
        self.bar_len = bar_len
        self.initUI()
        self.setWindowTitle(title)
        
    def initUI(self):
        self.progress = QProgressBar(self)
        self.progress.setGeometry(0, 0, 300, 25)
        self.progress.setMaximum(self.bar_len)
        self.show()
        
    def set_progress_value(self,value):
        self.progress.setValue(value)
        
        
        