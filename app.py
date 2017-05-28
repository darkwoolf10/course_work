#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from random import randint

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QApplication, QWidget, QSizePolicy, QRadioButton, QPushButton, QVBoxLayout, QTextEdit, QLabel, QMessageBox
)


class PlotCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.sort_func = None
        FigureCanvasQTAgg.__init__(self, fig)
        self.setParent(parent)
        FigureCanvasQTAgg.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvasQTAgg.updateGeometry(self)
        self.timer = QtCore.QTimer(self)

    def sort_shit(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr) - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    yield arr

    def get_arr(self, arr=None, time=1500, minimum=-50, maximum=50, amount=20):
        if arr:
            self.timer.stop()
            self.timer = QtCore.QTimer(self)
            self.sort_func = self.sort_shit(arr)
            self.axes.cla()
            self.axes.plot(arr, "-ro")
            self.draw()
            self.timer.timeout.connect(self.update_figure)
            self.timer.start(time)
        else:
            self.timer.stop()
            self.timer = QtCore.QTimer(self)
            initial_arr = [randint(minimum, maximum) for _ in range(amount)]
            self.axes.cla()
            self.axes.plot(initial_arr, "-ro")
            self.draw()
            self.sort_func = self.sort_shit(initial_arr)
            self.timer.timeout.connect(self.update_figure)
            self.timer.start(time)

    def stop_sort(self):
        self.timer.stop()
        self.axes.cla()
        self.timer = QtCore.QTimer(self)

    def update_figure(self):
        try:
            arr_inst = next(self.sort_func)
            print(arr_inst)
        except StopIteration:
            self.timer.stop()
            arr_inst = None
            self.sort_func = None
        if arr_inst:
            self.axes.cla()
            self.axes.plot(arr_inst, "-ro")
            self.draw()


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 900, 400)
        self.setWindowTitle("Shit")

        self.current_state = "user"

        self.pc = PlotCanvas(self)
        self.pc.move(400, 0)

        self.start_sort_button = QPushButton("Sorting", self)
        self.start_sort_button.move(70, 360)
        self.start_sort_button.resize(
            self.start_sort_button.frameGeometry().width() + 10, self.start_sort_button.frameGeometry().height()
        )
        self.start_sort_button.clicked.connect(self.start_button)
        self.stop_sort_button = QPushButton("Stop sorting", self)
        self.stop_sort_button.move(190, 360)
        self.stop_sort_button.resize(
            self.stop_sort_button.frameGeometry().width() + 40, self.stop_sort_button.frameGeometry().height()
        )
        self.stop_sort_button.clicked.connect(self.pc.stop_sort)

        self.timer_warning = QLabel("Default - 1.5 s:", self)
        self.timer_warning.move(20, 320)
        self.timer_warning.resize(
            170, self.timer_warning.frameGeometry().height()
        )
        self.timer_field = QTextEdit(self)
        self.timer_field.move(200, 325)
        self.timer_field.resize(50, 20)

        self.field_warning = QLabel("Please enter data with a space", self)
        self.field_warning.move(30, 60)
        self.field_warning.resize(
            340, self.field_warning.frameGeometry().height()
        )
        self.enter_field = QTextEdit(self)
        self.enter_field.move(20, 90)
        self.enter_field.resize(360, 150)

        self.random_warning = QLabel("Values ​​do not need to be entered, according to the standard\nthe minimum value is -50, and a maximum of 50\nand the number of array elements is 20", self)
        self.random_warning.move(20, 90)
        self.random_warning.resize(280, 40)
        self.random_warning.hide()

        self.min_field_warning = QLabel("Минимальное значение:", self)
        self.min_field_warning.move(20, 130)
        self.min_field_warning.resize(
            120, self.min_field_warning.frameGeometry().height()
        )
        self.min_field_warning.hide()
        self.min_field = QTextEdit(self)
        self.min_field.move(150, 135)
        self.min_field.resize(50, 20)
        self.min_field.hide()

        self.max_field_warning = QLabel("Max value:", self)
        self.max_field_warning.move(20, 160)
        self.max_field_warning.resize(
            130, self.max_field_warning.frameGeometry().height()
        )
        self.max_field_warning.hide()
        self.max_field = QTextEdit(self)
        self.max_field.move(160, 165)
        self.max_field.resize(50, 20)
        self.max_field.hide()

        self.num_field_warning = QLabel("Amount of elements:", self)
        self.num_field_warning.move(20, 190)
        self.num_field_warning.resize(
            130, self.num_field_warning.frameGeometry().height()
        )
        self.num_field_warning.hide()
        self.num_field = QTextEdit(self)
        self.num_field.move(160, 195)
        self.num_field.resize(50, 20)
        self.num_field.hide()

        vbox = QVBoxLayout()
        vbox.setAlignment(QtCore.Qt.AlignTop)

        self.user_array_input = QRadioButton("Enter array")
        self.user_array_input.setChecked(True)
        self.user_array_input.toggled.connect(lambda: self.radio_button_state(self.user_array_input))
        vbox.addWidget(self.user_array_input)
        self.random_array = QRadioButton("Generate array")
        self.random_array.toggled.connect(lambda: self.radio_button_state(self.random_array))
        vbox.addWidget(self.random_array)

        self.setLayout(vbox)

        self.show()

    def radio_button_state(self, button):
        if button.text() == "Ввести массив":
            if button.isChecked():
                if not self.current_state == "user":
                    self.current_state = "user"

                    self.random_warning.hide()
                    self.min_field_warning.hide()
                    self.min_field.clear()
                    self.min_field.hide()
                    self.max_field_warning.hide()
                    self.max_field.clear()
                    self.max_field.hide()
                    self.num_field_warning.hide()
                    self.num_field.clear()
                    self.num_field.hide()

                    self.enter_field.show()
                    self.field_warning.show()
        elif button.text() == "Generate array":
            if button.isChecked():
                if not self.current_state == "random":
                    self.current_state = "random"

                    self.enter_field.clear()
                    self.enter_field.hide()
                    self.field_warning.hide()

                    self.random_warning.show()
                    self.min_field_warning.show()
                    self.min_field.show()
                    self.max_field_warning.show()
                    self.max_field.show()
                    self.num_field_warning.show()
                    self.num_field.show()

    def start_button(self):
        sender = self.sender()
        if self.current_state == "user":
            print(sender.text(), "user")
            if not all(map(lambda x: x.isnumeric(), self.enter_field.toPlainText().split())):
                QMessageBox.warning(self, "Warning", "Please enter whole numbers with a space", QMessageBox.Ok)
            else:
                if self.timer_field.toPlainText() == "":
                    self.pc.get_arr([int(i) for i in self.enter_field.toPlainText().split()])
                else:
                    self.pc.get_arr([int(i) for i in self.enter_field.toPlainText().split()],
                                    time=int(float(self.timer_field.toPlainText()*1000)))
        else:
            if all(map(lambda x: x.toPlainText() == "", [self.min_field, self.max_field, self.num_field])):
                if self.timer_field.toPlainText() == "":
                    self.pc.get_arr()
                else:
                    self.pc.get_arr(time=int(float(self.timer_field.toPlainText())*1000))
            else:
                if all(
                        map(
                            lambda x: x.isnumeric() or "-" in x,
                            [self.min_field.toPlainText(), self.max_field.toPlainText(), self.num_field.toPlainText()]
                        )
                ):
                    if self.timer_field.toPlainText() == "":
                        self.pc.get_arr(minimum=int(self.min_field.toPlainText()),
                                        maximum=int(self.max_field.toPlainText()),
                                        amount=int(self.num_field.toPlainText()))
                    else:
                        self.pc.get_arr(minimum=int(self.min_field.toPlainText()),
                                        maximum=int(self.max_field.toPlainText()),
                                        amount=int(self.num_field.toPlainText()),
                                        time=int(float(self.timer_field.toPlainText()) * 1000))
            print(sender.text(), "random")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())