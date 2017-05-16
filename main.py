#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
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
        '''
            кнопка с подсказкой 
        '''
        #QToolTip.setFont(QFont('SansSerif', 10))

        #self.setToolTip('This is a <b>QWidget</b> widget')

        #btn = QPushButton('Button', self)
        #btn.setToolTip('This is a <b>QWidget</b> widget')
        #btn.resize(btn.sizeHint())
        #btn.move(50, 50)
        '''
            кнопка выхода
        '''
        #qbtn = QPushButton('Quit', self)
        #qbtn.clicked.connect(QCoreApplication.instance().quit)
        #qbtn.resize(qbtn.sizeHint())
        #qbtn.move(50, 50)
    
        self.resize(800, 440)
        self.center()
        self.setWindowTitle('merge sort')
        self.setWindowIcon(QIcon('web.png'))    

        self.btn = QPushButton('Enter array', self)
        self.btn.clicked.connect(self.gettext)
        layout.addWidget(self.btn)

        # Array input field
        self.lbl = QLabel('<b>Enter array:</b>', self)
        layout.addWidget(self.lbl)

        # output element
        self.le = QLabel(self)
        layout.addWidget(self.le)  

        self.show()

    # Питає чи ви точно впевнені, що хочете закрити
    def closeEvent(self, event):
         
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()   

    # Робить щоб вікно було по центру
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter( cp )
        self.move(qr.topLeft()) 

    # введення массиву
    def gettext(self):

        text, ok = QInputDialog.getText(self, 'Input Dialog',
            'Enter element:')      
        if ok:
            self.le.setText(str(text))



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())