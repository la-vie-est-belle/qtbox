# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QCheckBox
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QCheckBox = createWidgetMenuBase(QCheckBox)

class QtBoxFuncCheckBox2(QCheckBox):
    def __init__(self):
        super(QtBoxFuncCheckBox2, self).__init__(str(Path(__file__)))
        self.setText("Text on the left")
        self.setLayoutDirection(Qt.RightToLeft)
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QCheckBox


# class QtBoxFuncCheckBox2(QCheckBox):
#     def __init__(self):
#         super(QtBoxFuncCheckBox2, self).__init__()
#         self.setText("Text on the left")
#         self.setLayoutDirection(Qt.RightToLeft)
# PySide