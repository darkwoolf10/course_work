#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys, random
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QWidget, QDesktopWidget, 
    QGridLayout, QVBoxLayout, QPushButton, QInputDialog, QLabel, QHBoxLayout,
    QToolTip, QMessageBox, QLineEdit, QTextEdit,QFrame, QLCDNumber, QSlider,)
from PyQt5.QtGui import QIcon, QFont, QColor

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QHBoxLayout(self)

        self.arr = []
    
        self.resize(800, 440)
        self.center()
        self.setWindowTitle('merge sort')
        self.setWindowIcon(QIcon('web.png'))    

        self.btn = QPushButton('Enter array', self)
        self.btn.clicked.connect(self.getnum)
        layout.addWidget(self.btn)

        # rand button
        self.randButton = QPushButton('rand', self)
        self.randButton.clicked.connect(self.randArray)
        layout.addWidget(self.randButton)

        # Array input field
        self.lbl = QLabel('<b>Enter array:</b>', self)
        layout.addWidget(self.lbl)

        self.output = QTextEdit(self)
        self.output.setPlaceholderText("[1,2,3,4,5,6..]") 
        layout.addWidget(self.output)  

        self.mergeSort( self.arr )

        self.show()

    #  Asked whether you really sure you want to close
    def closeEvent(self, event):
         
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()   

    # Makes the window was centered
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter( cp )
        self.move(qr.topLeft()) 

    # function marge sort

    def mergeSort(self, alist):
        if len(alist)>1:
            mid = len(alist)//2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]

            mergeSort(lefthalf)
            mergeSort(righthalf)

            i=0
            j=0
            k=0
            while i<len(lefthalf) and j<len(righthalf):
                if lefthalf[i]<righthalf[j]:
                    alist[k]=lefthalf[i]
                    i=i+1
                else:
                    alist[k]=righthalf[j]
                    j=j+1
                k=k+1

            while i<len(lefthalf):
                aist[k]=lefthalf[i]
                i=i+1
                k=k+1

            while j<len(righthalf):
                alist[k]=righthalf[j]
                j=j+1
                k=k+1
            self.output.setText(str("\n" + self.alist))     
            

    # Enter array
    def getnum(self):
        num, ok = QInputDialog.getInt(self, 'integer input dualog',
            'Enter element:')      
        if ok:
            self.arr.append(num)
            self.output.setText(str(self.arr))
            self.mergeSort(self.arr)

    # Enter number in array
    def randArray(self, length):
        i = 0
        length, ok = QInputDialog.getInt(self, 'integer input dualog',
            'question element:') 
        if ok:
            while( i < length):
                self.arr.append(random.randint(0, 99))
                i+=1
            self.output.setText(str(self.arr))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())