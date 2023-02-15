# PyQt
from PyQt5.QtWidgets import QLabel, QGraphicsBlurEffect
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QLabel = createWidgetMenuBase(QLabel)

class QtBoxStyleLabel3(QLabel):
    def __init__(self):
        super(QtBoxStyleLabel3, self).__init__(str(Path(__file__)))
        self.setText("Blur")
        self.blur()

    def blur(self):
        blur = QGraphicsBlurEffect(self)
        blur.setBlurRadius(6)
        blur.setBlurHints(QGraphicsBlurEffect.QualityHint)
        self.setGraphicsEffect(blur)
# PyQt

# PySide
# from PySide2.QtWidgets import QLabel, QGraphicsBlurEffect


# class QtBoxStyleLabel3(QLabel):
#     def __init__(self):
#         super(QtBoxStyleLabel3, self).__init__()
#         self.setText("Blur")
#         self.blur()

#     def blur(self):
#         blur = QGraphicsBlurEffect(self)
#         blur.setBlurRadius(6)
#         blur.setBlurHints(QGraphicsBlurEffect.QualityHint)
#         self.setGraphicsEffect(blur)
# PySide