# PyQt
from PyQt5.QtWidgets import QLabel
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QLabel = createWidgetMenuBase(QLabel)

class QtBoxFuncLabel1(QLabel):
    def __init__(self):
        super(QtBoxFuncLabel1, self).__init__(str(Path(__file__)))
        self.setText("<a href='https://github.com/la-vie-est-belle/qtbox' style='text-decoration:none'>Qt Box link</a>")
        self.setOpenExternalLinks(True)
# PyQt

# PySide
# from PySide2.QtWidgets import QLabel


# class QtBoxFuncLabel1(QLabel):
#     def __init__(self):
#         super(QtBoxFuncLabel1, self).__init__()
#         self.setText("<a href='https://github.com/la-vie-est-belle/qtbox' style='text-decoration:none'>Qt Box link</a>")
#         self.setOpenExternalLinks(True)
# PySide