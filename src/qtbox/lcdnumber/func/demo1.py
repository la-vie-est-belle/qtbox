# PyQt
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import QLCDNumber
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QLCDNumber = createWidgetMenuBase(QLCDNumber)

class QtBoxFuncLCDNumber1(QLCDNumber):
    def __init__(self):
        super(QtBoxFuncLCDNumber1, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 50)
        self.setDigitCount(8)
        self.update_display()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_display)
        self.timer.start(1000)

    def update_display(self):
        self.display(QTime.currentTime().toString())
# PyQt

# PySide
# from PySide2.QtCore import QTimer, QTime
# from PySide2.QtWidgets import QLCDNumber


# class QtBoxFuncLCDNumber1(QLCDNumber):
#     def __init__(self):
#         super(QtBoxFuncLCDNumber1, self).__init__()
#         self.setFixedSize(150, 50)
#         self.setDigitCount(8)
#         self.update_display()

#         self.timer = QTimer()
#         self.timer.timeout.connect(self.update_display)
#         self.timer.start(1000)

#     def update_display(self):
#         self.display(QTime.currentTime().toString())
# PySide