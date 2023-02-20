# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QWidget = createWidgetMenuBase(QWidget)

class QtBoxStyleWidget1(QWidget):
    def __init__(self):
        super(QtBoxStyleWidget1, self).__init__(str(Path(__file__)))
        self.setFixedSize(100, 100)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.lightGray)
        painter.drawRoundedRect(self.rect(), 10, 10)
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtGui import QPainter
# from PySide2.QtWidgets import QWidget


# class QtBoxStyleWidget1(QWidget):
#     def __init__(self):
#         super(QtBoxStyleWidget1, self).__init__()
#         self.setFixedSize(100, 100)
#         self.setWindowFlag(Qt.FramelessWindowHint)
#         self.setAttribute(Qt.WA_TranslucentBackground)

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setPen(Qt.NoPen)
#         painter.setBrush(Qt.lightGray)
#         painter.drawRoundedRect(self.rect(), 10, 10)
# PySide