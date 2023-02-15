# PyQt
from time import strftime, gmtime
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QLCDNumber
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QLCDNumber = createWidgetMenuBase(QLCDNumber)

class QtBoxFuncLCDNumber3(QLCDNumber):
    def __init__(self):
        super(QtBoxFuncLCDNumber3, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 50)
        self.setDigitCount(8)

        self.count_down = 3600
        self.update_display()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_display)
        self.timer.start(1000)

    def update_display(self):
        self.count_down -= 1
        self.display(strftime("%H:%M:%S", gmtime(self.count_down)))
        if self.count_down <= 0:
            self.count_down = 3600
# PyQt

# PySide
# from time import strftime, gmtime
# from PySide2.QtCore import QTimer
# from PySide2.QtWidgets import QLCDNumber


# class QtBoxFuncLCDNumber3(QLCDNumber):
#     def __init__(self):
#         super(QtBoxFuncLCDNumber3, self).__init__()
#         self.setFixedSize(150, 50)
#         self.setDigitCount(8)

#         self.count_down = 3600
#         self.update_display()
#         self.timer = QTimer()
#         self.timer.timeout.connect(self.update_display)
#         self.timer.start(1000)

#     def update_display(self):
#         self.count_down -= 1
#         self.display(strftime("%H:%M:%S", gmtime(self.count_down)))
#         if self.count_down <= 0:
#             self.count_down = 3600
# PySide