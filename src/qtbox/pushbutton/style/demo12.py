# PyQt
from PyQt5.QtCore import pyqtProperty, QPropertyAnimation
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QColor
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QPushButton = createWidgetMenuBase(QPushButton)

class QtBoxStyleButton12(QPushButton):
    def __init__(self):
        super(QtBoxStyleButton12, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 40)
        self.setText("BUTTON")
        self._color = QColor()

        self.color_anim = QPropertyAnimation(self, b"color")
        self.color_anim.setDuration(6000)
        self.color_anim.setStartValue(QColor(0, 0, 0))
        self.color_anim.setEndValue(QColor(255, 255, 255))
        self.color_anim.start()

    @pyqtProperty(QColor)
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
        red = value.red()
        green = value.green()
        blue = value.blue()
        self.setStyleSheet(f"background-color: rgb({red}, {green}, {blue})")
# PyQt

# PySide
# from PySide2.QtCore import Property, QPropertyAnimation
# from PySide2.QtWidgets import QPushButton
# from PySide2.QtGui import QColor


# class QtBoxStyleButton12(QPushButton):
#     def __init__(self):
#         super(QtBoxStyleButton12, self).__init__()
#         self.setFixedSize(150, 40)
#         self.setText("BUTTON")
#         self._color = QColor()

#         self.color_anim = QPropertyAnimation(self, b"color")
#         self.color_anim.setDuration(6000)
#         self.color_anim.setStartValue(QColor(0, 0, 0))
#         self.color_anim.setEndValue(QColor(255, 255, 255))
#         self.color_anim.start()

#     @Property(QColor)
#     def color(self):
#         return self._color

#     @color.setter
#     def color(self, value):
#         self._color = value
#         red = value.red()
#         green = value.green()
#         blue = value.blue()
#         self.setStyleSheet(f"background-color: rgb({red}, {green}, {blue})")
# PySide
