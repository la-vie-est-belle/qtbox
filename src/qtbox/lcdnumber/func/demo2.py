# PyQt
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QLCDNumber
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QLCDNumber = createWidgetMenuBase(QLCDNumber)

class QtBoxFuncLCDNumber2(QLCDNumber):
    def __init__(self):
        super(QtBoxFuncLCDNumber2, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 50)
        self.text = "HELLO"
        self.setDigitCount(len(self.text))
        self.display("")

        self.count = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_display)
        self.timer.start(1000)

    def update_display(self):
        self.count += 1
        if self.count > len(self.text):
            self.display(self.text+(self.count-len(self.text))*" ")
        else:
            self.display(self.text[0:self.count])

        if self.count == 2*len(self.text):
            self.count = 0
# PyQt

# PySide
# from PySide2.QtCore import QTimer
# from PySide2.QtWidgets import QLCDNumber


# class QtBoxFuncLCDNumber2(QLCDNumber):
#     def __init__(self):
#         super(QtBoxFuncLCDNumber2, self).__init__()
#         self.setFixedSize(150, 50)
#         self.text = "HELLO"
#         self.setDigitCount(len(self.text))
#         self.display("")

#         self.count = 0
#         self.timer = QTimer()
#         self.timer.timeout.connect(self.update_display)
#         self.timer.start(1000)

#     def update_display(self):
#         self.count += 1
#         if self.count > len(self.text):
#             self.display(self.text+(self.count-len(self.text))*" ")
#         else:
#             self.display(self.text[0:self.count])

#         if self.count == 2*len(self.text):
#             self.count = 0
# PySide