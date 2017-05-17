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

        #self.MargerSort(arr)

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

    # Enter array
    def getnum(self):
        num, ok = QInputDialog.getInt(self, 'integer input dualog',
            'Enter element:')      
        if ok:
            self.arr.append(num)
            self.output.setText(str(self.arr))

    def randArray(self, length):
        i = 0
        length, ok = QInputDialog.getInt(self, 'integer input dualog',
            'question element:') 
        if ok:
            while( i < length):
                self.arr.append(random.randint(0, 99))
                i+=1
            self.output.setText(str(self.arr))

    def MergerSort(arr):       
        def MergerGroup(arr, left, m, right):
            if left >= right: return None
            if m < left or right < m: return None
            t = left
            for j in xrange(m+1, right+1):#подгруппа 2
                for i in xrange(t, j):#цикл подгруппы 1
                    if arr[j] < arr[i]:
                        r = arr[j]
                        #итерационно переставляем элементы, чтобы упорядочить
                        for k in xrange(j, i, -1):
                            arr[k] = arr[k - 1]
                        arr[i] = r
                        t = i#проджолжение вставки в группе 1
                        break#к следующему узлу из подгруппы 2                   
        if len(num) < 2: return None
        k=1
        while k<len(num):
            g=0
            while g<len(num):#группы
                z = g + k + k - 1#последний эл-т группы
                r = z if z < len(num) else len(num) - 1#последняя группа
                MergerGroup(num, g, g + k - 1, r)#слияние
                g+=2*k
            k*=2




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())