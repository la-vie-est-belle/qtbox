# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QWidget, QGraphicsBlurEffect
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QWidget = createWidgetMenuBase(QWidget)

class QtBoxStyleWidget2(QWidget):
    def __init__(self):
        super(QtBoxStyleWidget2, self).__init__(str(Path(__file__)))
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedSize(100, 100)
        self.set_background_color()
        self.blur()

    def set_background_color(self):
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(245, 245, 245, 220))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

    def blur(self):
        blur = QGraphicsBlurEffect()
        blur.setBlurRadius(10)
        blur.setBlurHints(QGraphicsBlurEffect.QualityHint)
        self.setGraphicsEffect(blur)
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtGui import QPalette, QColor
# from PySide2.QtWidgets import QWidget, QGraphicsBlurEffect


# class QtBoxStyleWidget2(QWidget):
#     def __init__(self):
#         super(QtBoxStyleWidget2, self).__init__()
#         self.setWindowFlag(Qt.FramelessWindowHint)
#         self.setFixedSize(100, 100)
#         self.set_background_color()
#         self.blur()

#     def set_background_color(self):
#         palette = QPalette()
#         palette.setColor(QPalette.Background, QColor(245, 245, 245, 220))
#         self.setPalette(palette)
#         self.setAutoFillBackground(True)

#     def blur(self):
#         blur = QGraphicsBlurEffect()
#         blur.setBlurRadius(10)
#         blur.setBlurHints(QGraphicsBlurEffect.QualityHint)
#         self.setGraphicsEffect(blur)
# PySide
