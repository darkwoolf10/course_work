#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys, random
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QWidget, QDesktopWidget, 
    QGridLayout, QVBoxLayout, QPushButton, QInputDialog, QLabel, QHBoxLayout,
    QToolTip, QMessageBox, QLineEdit, QTextEdit,QFrame, QLCDNumber, QSlider)
from PyQt5.QtGui import QIcon, QFont, QColor

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QHBoxLayout(self)
        button = QHBoxLayout(self)
        self.arr = []
    
        self.resize(800, 440)
        self.center()
        self.setWindowTitle('Merge sort')
        self.setWindowIcon(QIcon('web.png'))    

        # rand button
        self.randButton = QPushButton('Rand', self)
        self.randButton.clicked.connect(self.randArray)
        button.addWidget(self.randButton)
        self.randButton.move(0, 0)
        self.randButton.setStyleSheet("""
            color: #fff;
            text-decoration: none;
            background: rgb(212,75,56);
            } 
            QPushButton:hover { background: rgb(232,95,76); }
            QPushButton:active { background: rgb(152,15,0); }
            """)

        self.sort = QPushButton('Sort array', self)
        self.sort.clicked.connect(self.sortArray)
        button.addWidget(self.sort)
        self.sort.move(11, 60)
        self.sort.setStyleSheet("""
            color: #fff;
            text-decoration: none;
            background: rgb(212,75,56);
            } 
            QPushButton:hover { background: rgb(232,95,76); }
            QPushButton:active { background: rgb(152,15,0); }
            """)

        self.clear = QPushButton('Clear', self)
        self.clear.clicked.connect(self.clearWindow)
        button.addWidget(self.clear)
        self.clear.move(11, 100)
        self.clear.setStyleSheet("""
            color: #fff;
            text-decoration: none;
            background: rgb(212,75,56);
            } 
            QPushButton:hover { background: rgb(232,95,76); }
            QPushButton:active { background: rgb(152,15,0); }
            """)

        self.btn = QPushButton('Enter array', self)
        self.btn.clicked.connect(self.getnum)
        layout.addWidget(self.btn)
        self.btn.setStyleSheet("""
            color: #fff;
            text-decoration: none;
            background: rgb(212,75,56);
            padding: .7em 1.5em;
            } 
            QPushButton:hover { background: rgb(232,95,76); }
            QPushButton:active { background: rgb(152,15,0); }
            """)
        self.randButton.move(11, 140)

        # Array input field
        self.lbl = QLabel('<b>Enter array:</b>', self)
        layout.addWidget(self.lbl)

        # output sorting
        self.output = QTextEdit(self)
        layout.addWidget(self.output)  
        
        self.output.setStyleSheet("color:blue")
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
            self.output.append("<font color=red>Splitting: </font>" + str(alist))
            mid = len(alist)//2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]

            self.mergeSort(lefthalf)
            self.mergeSort(righthalf)

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
                alist[k]=lefthalf[i]
                i=i+1
                k=k+1

            while j<len(righthalf):
                alist[k]=righthalf[j]
                j=j+1
                k=k+1
            self.output.append("<font color=green>Merging: </>"+ str(alist))              

    # Enter array
    def getnum(self):
        num, ok = QInputDialog.getInt(self, 'integer input dualog',
            'Enter element:')      
        if ok:
            self.arr.append(num)
            self.output.setText(str(self.arr))

    # Enter number in array
    def randArray(self, length):
        i = 0
        length, ok = QInputDialog.getInt(self, 'integer input dualog',
            'question element:') 
        if ok:
            while( i < length):
                self.arr.append(random.randint(0, 99))
                i+=1
            if length > 1:

                self.output.setText("<b>Your array: </b>" + str(self.arr))
                self.mergeSort( self.arr )
                self.output.append("\n<b>Result: </b>" + str(self.arr))
            else:
                self.output.append("<b>Your array: </b>" + str(self.arr))
    
    # Displaying sorting results
    def sortArray(self):
        self.mergeSort(self.arr)
        self.output.append("\n<b>Result: </b>" + str(self.arr))

    # Screen cleaning function    
    def clearWindow(self):
        self.output.clear() 
        self.arr = []
    

if __name__ == '__main__':
    app = QApplication(sys.argv)    
    ex = Example()
    sys.exit(app.exec_())