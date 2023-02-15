# PyQt
from PyQt5.QtWidgets import QLCDNumber
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QLCDNumber = createWidgetMenuBase(QLCDNumber)

class QtBoxStyleLCDNumber1(QLCDNumber):
    def __init__(self):
        super(QtBoxStyleLCDNumber1, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 50)
        self.setDigitCount(6)
        self.display(123456)
        self.setSegmentStyle(QLCDNumber.Flat)
        self.setStyleSheet("""
        QLCDNumber {
            background-color: #98a780;
            border: none;
        }
        """)
# PyQt

# PySide
# from PySide2.QtWidgets import QLCDNumber


# class QtBoxStyleLCDNumber1(QLCDNumber):
#     def __init__(self):
#         super(QtBoxStyleLCDNumber1, self).__init__()
#         self.setFixedSize(150, 50)
#         self.setDigitCount(6)
#         self.display(123456)
#         self.setSegmentStyle(QLCDNumber.Flat)
#         self.setStyleSheet("""
#         QLCDNumber {
#             background-color: #98a780;
#             border: none;
#         }
#         """)
# PySide