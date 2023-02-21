# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QFont, QFontMetricsF
from PyQt5.QtWidgets import QSlider
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QSlider = createWidgetMenuBase(QSlider)

class QtBoxFuncSlider1(QSlider):
    def __init__(self):
        super(QtBoxFuncSlider1, self).__init__(str(Path(__file__)))
        self.setMinimum(0)
        self.setMaximum(100)
        self.setOrientation(Qt.Horizontal)
        self.is_number_shown = False

    def mousePressEvent(self, event):
        super(QtBoxFuncSlider1, self).mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self.is_number_shown = True
            self.update()

    def mouseReleaseEvent(self, event):
        super(QtBoxFuncSlider1, self).mouseReleaseEvent(event)
        if event.button() == Qt.LeftButton:
            self.is_number_shown = False
            self.update()

    def paintEvent(self, event):
        super(QtBoxFuncSlider1, self).paintEvent(event)

        if not self.is_number_shown:
            return

        painter = QPainter(self)
        painter.setBrush(QColor(220, 220, 220, 120))

        font = QFont()
        font.setPixelSize(13)
        painter.setFont(font)
        font_metrics = QFontMetricsF(font)
        text_width = font_metrics.width(str(self.value()))
        text_height = font_metrics.height()

        x = (self.value() - self.minimum()) / (self.maximum() - self.minimum()) * (self.width() - text_width)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(x, 0, text_width, text_height*1.3, 3, 3)
        painter.setPen(Qt.SolidLine)
        painter.drawText(int(x), int(text_height), str(self.value()))
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtGui import QPainter, QColor, QFont, QFontMetricsF
# from PySide2.QtWidgets import QSlider


# class QtBoxFuncSlider1(QSlider):
#     def __init__(self):
#         super(QtBoxFuncSlider1, self).__init__(str(Path(__file__)))
#         self.setMinimum(0)
#         self.setMaximum(100)
#         self.setOrientation(Qt.Horizontal)
#         self.is_number_shown = False

#     def mousePressEvent(self, event):
#         super(QtBoxFuncSlider1, self).mousePressEvent(event)
#         if event.button() == Qt.LeftButton:
#             self.is_number_shown = True
#             self.update()

#     def mouseReleaseEvent(self, event):
#         super(QtBoxFuncSlider1, self).mouseReleaseEvent(event)
#         if event.button() == Qt.LeftButton:
#             self.is_number_shown = False
#             self.update()

#     def paintEvent(self, event):
#         super(QtBoxFuncSlider1, self).paintEvent(event)

#         if not self.is_number_shown:
#             return

#         painter = QPainter(self)
#         painter.setBrush(QColor(200, 200, 200, 120))

#         font = QFont()
#         font.setPixelSize(15)
#         painter.setFont(font)
#         font_metrics = QFontMetricsF(font)
#         text_width = font_metrics.width(str(self.value()))
#         text_height = font_metrics.height()

#         x = (self.value() - self.minimum()) / (self.maximum() - self.minimum()) * (self.width() - text_width)
#         painter.setPen(Qt.NoPen)
#         painter.drawRoundedRect(x, 0, text_width, text_height, 2, 2)
#         painter.setPen(Qt.SolidLine)
#         painter.drawText(int(x), int(text_height), str(self.value()))
# PySide