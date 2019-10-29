# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QStatusBar
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
        self.img_qlabel.setGeometry(QRect(40, 20, 351, 551))
        self.img_qlabel.setObjectName("img_qlabel")
        self.img_qlabel.setAlignment(Qt.AlignCenter)
        
        self.text_qlabel = QLabel(self.centralwidget)
        self.text_qlabel.setFont(QFont("Roman times",12,QFont.Bold))
        self.text_qlabel.setGeometry(QRect(450, 20, 331, 241))
        self.text_qlabel.setStyleSheet("color: rgb(121, 121, 121)")
        self.text_qlabel.setObjectName("text_qlabel")
        
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
        
        self.pathButton = QPushButton(self.centralwidget)
        self.pathButton.setGeometry(QRect(450, 315, 331, 75))
        self.pathButton.setObjectName("pathButton")
        self.pathButton.setIcon(QIcon(QPixmap(resource_path('folder.png'))))
        self.pathButton.setIconSize(QSize(40, 40))   
        self.pathButton.setFont(QFont("Roman times",10,QFont.Bold))
        
        self.prevButton = QPushButton(self.centralwidget)
        self.prevButton.setGeometry(QRect(450, 410, 331, 75))
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
        self.img_qlabel.setText(_translate("MainWindow", ""))
        self.text_qlabel.setText(_translate("MainWindow", "Please select a folder"))
        self.clipButton.setText(_translate("MainWindow", "Clip to BBox"))
        self.MergeButton.setText(_translate("MainWindow", "Merge to Json"))
        self.pathButton.setText(_translate("MainWindow", "Open Dir"))
        self.prevButton.setText(_translate("MainWindow", "Previous"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
