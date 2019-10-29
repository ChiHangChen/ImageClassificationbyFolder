# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal, QEvent
import sys
from glob import glob
from numpy import array as nparray
from PIL.Image import open as imopen
from win32gui import GetWindowText, GetForegroundWindow
from MainWindow import Ui_MainWindow, resource_path
from qimage2ndarray import array2qimage
from shutil import move
from os import makedirs, chdir, getcwd
from os import path as ospath

keymap = {}
for key, value in vars(Qt).items():
    if isinstance(value, Qt.Key):
        temp = key.partition('_')[2]
        if len(temp)==1:
            keymap[value] = temp 
            

desired_window = "Quick Classification"

class mainProgram(QMainWindow, Ui_MainWindow):
    keyPressed = pyqtSignal(QEvent)
    def __init__(self, parent=None):
        super(mainProgram, self).__init__(parent)
        self.setupUi(self)
        self.saveButton.clicked.connect(self.save)
        self.prevButton.clicked.connect(self.prev_image)
        self.pathButton.clicked.connect(self.select_path)
        self.keyPressed.connect(self.on_key)
        self.path_click=False
        
    def read_img(self, path):
        if not ospath.exists(path):
            QMessageBox.information(self, "Warning", f"No image found : {path}")
            sys.exit(app.exec_())
        else:
            return nparray(imopen(path))      


    def save(self):
        if not self.path_click:
            QMessageBox.information(self, "Warning", "Please select folder first!")
        elif len(self.new_class)==0:
            QMessageBox.information(self, "Warning", "No images need to be saved!")
        else:
            for im, c in zip(self.done_img_list, self.new_class):
                output_path = ospath.dirname(getcwd())+"/"+c
                if not ospath.exists(output_path):
                    makedirs(output_path)
                move(im, output_path+"/"+ospath.basename(im))
            
            self.image_list = glob('*.jpg')
            self.imgnumber = 0
            self.new_class = []
            self.done_img_list = []
            if self.to_the_end:
                QMessageBox.information(self, "Warning", "Job Done!")
                sys.exit(app.exec_())
            else:
                bbox = self.read_img(self.image_list[self.imgnumber])
                self.update_image(bbox)            
                QMessageBox.information(self, "Warning", "Image saved!")
            
    # Done
    def select_path(self):
        path = QFileDialog.getExistingDirectory()
        self.to_the_end = False
        if len(path) == 0:
            QMessageBox.information(self,"Warning", "Please select a valid path!")
        else:
            chdir(path)
            self.image_list = glob('*.jpg')
            if len(self.image_list)==0:
                QMessageBox.information(self,"Warning", "No jpg images found!")
            else:
                self.imgnumber = 0
                self.new_class = []
                self.done_img_list = []
                self.path_click = True
                bbox = self.read_img(self.image_list[self.imgnumber])
                self.update_image(bbox)
        
    def update_image(self, bbox):
        qImg = array2qimage(bbox)
        pixmap = QPixmap(qImg)
        if not pixmap.isNull():
            pixmap = pixmap.scaled(225, 450, Qt.KeepAspectRatio)
            self.img_qlabel.setPixmap(pixmap)
            try : 
                split_imgName = self.image_list[self.imgnumber].split("-")
                text = ""
                text += f"Dataset name : {split_imgName[0]}"
                text += f"\nImage name : {split_imgName[1]}.jpg"
                text += f"\nBBox id : {split_imgName[2].replace('.jpg','')}"
            except:
                text = "Filename : "+self.image_list[self.imgnumber]
            text += "\n\n"+f"Current progress : {self.imgnumber+1}/{len(self.image_list)}"
            text += f"\n{self.imgnumber} images haven't been saved"
            self.text_qlabel.setText(text)
            
    def keyPressEvent(self, event):
        super(mainProgram, self).keyPressEvent(event)
        self.keyPressed.emit(event) 
            
    def on_key(self, event):
        current_window = GetWindowText(GetForegroundWindow())
        if current_window==desired_window:
            if event.key() in keymap:
                self.new_class.append(keymap[event.key()])
                self.done_img_list.append(self.image_list[self.imgnumber])
                
                self.imgnumber += 1
                
                # If to the end, save and close program
                if self.imgnumber==len(self.image_list):
                    self.to_the_end = True
                    self.save()
                else:
                    bbox = self.read_img(self.image_list[self.imgnumber])
                    self.update_image(bbox)
            else:
                QMessageBox.information(self,"Warning", "Can not press special keys!")
                
    def prev_image(self):
        if self.imgnumber==0:
            QMessageBox.information(self,"Warning", "No previous image!")
        else:
            self.imgnumber -= 1
            self.new_class = self.new_class[:-1]
            self.done_img_list = self.done_img_list[:-1]
            
            bbox = self.read_img(self.image_list[self.imgnumber])
            self.update_image(bbox)
        
        
if __name__ == '__main__':  
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(resource_path('main.ico')))
    main = mainProgram()
    main.show()
    sys.exit(app.exec_())
    
 


