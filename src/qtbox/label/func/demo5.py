# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QLabel = createWidgetMenuBase(QLabel)

class QtBoxFuncLabel5(QLabel):
    def __init__(self):
        super(QtBoxFuncLabel5, self).__init__(str(Path(__file__)))
        text = 'Lay words vertically'.replace(" ", "\n")
        self.setText(text)
        self.setAlignment(Qt.AlignCenter)
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QLabel


# class QtBoxFuncLabel5(QLabel):
#     def __init__(self):
#         super(QtBoxFuncLabel5, self).__init__(str(Path(__file__)))
#         text = 'Lay words vertically'.replace(" ", "\n")
#         self.setText(text)
#         self.setAlignment(Qt.AlignCenter)
# PySide