# PyQt
from PyQt5.QtWidgets import QProgressBar
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QProgressBar = createWidgetMenuBase(QProgressBar)

class QtBoxFuncProgressBar1(QProgressBar):
    def __init__(self):
        super(QtBoxFuncProgressBar1, self).__init__(str(Path(__file__)))
        self.setRange(0, 0)
# PyQt

# PySide
# from PySide2.QtWidgets import QProgressBar


# class QtBoxFuncProgressBar1(QProgressBar):
#     def __init__(self):
#         super(QtBoxFuncProgressBar1, self).__init__()
#         self.setRange(0, 0)
# PySide