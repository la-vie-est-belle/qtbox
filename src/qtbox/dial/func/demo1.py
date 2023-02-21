# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QFont, QFontMetricsF
from PyQt5.QtWidgets import QDial
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QDial = createWidgetMenuBase(QDial)

class QtBoxFuncDial1(QDial):
    def __init__(self):
        super(QtBoxFuncDial1, self).__init__(str(Path(__file__)))
        self.setRange(0, 100)
        self.setWrapping(True)
        self.setNotchTarget(10)
        self.setNotchesVisible(True)

    def paintEvent(self, event):
        super(QtBoxFuncDial1, self).paintEvent(event)
        painter = QPainter(self)
        painter.setPen(Qt.SolidLine)

        font = QFont()
        font.setPixelSize(18)
        painter.setFont(font)
        font_metrics = QFontMetricsF(font)
        text_width = font_metrics.width(str(self.value()))
        painter.drawText(int(self.width()/2-text_width/2), int(self.height()/2), str(self.value()))
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtGui import QPainter, QFont, QFontMetricsF
# from PySide2.QtWidgets import QDial


# class QtBoxFuncDial1(QDial):
#     def __init__(self):
#         super(QtBoxFuncDial1, self).__init__(str(Path(__file__)))
#         self.setRange(0, 100)
#         self.setWrapping(True)
#         self.setNotchTarget(10)
#         self.setNotchesVisible(True)

#     def paintEvent(self, event):
#         super(QtBoxFuncDial1, self).paintEvent(event)
#         painter = QPainter(self)
#         painter.setPen(Qt.SolidLine)

#         font = QFont()
#         font.setPixelSize(18)
#         painter.setFont(font)
#         font_metrics = QFontMetricsF(font)
#         text_width = font_metrics.width(str(self.value()))
#         painter.drawText(int(self.width()/2-text_width/2), int(self.height()/2), str(self.value()))
# PySide