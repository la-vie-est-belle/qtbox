# PyQt
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import QRegExp
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QLineEdit = createWidgetMenuBase(QLineEdit)

class QtBoxFuncLineEdit2(QLineEdit):
    def __init__(self):
        super(QtBoxFuncLineEdit2, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 30)
        self.setPlaceholderText("Numbers only")

        reg_exp = QRegExp("[0-9]+")
        self.setValidator(QRegExpValidator(reg_exp))
# PyQt

# PySide
# from PySide2.QtGui import QRegExpValidator
# from PySide2.QtWidgets import QLineEdit
# from PySide2.QtCore import QRegExp


# class QtBoxFuncLineEdit2(QLineEdit):
#     def __init__(self):
#         super(QtBoxFuncLineEdit2, self).__init__()
#         self.setFixedSize(150, 30)
#         self.setPlaceholderText("Numbers only")

#         reg_exp = QRegExp("[0-9]+")
#         self.setValidator(QRegExpValidator(reg_exp))
# PySide