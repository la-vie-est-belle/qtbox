# PyQt
from PyQt5.QtWidgets import QProgressBar
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QProgressBar = createWidgetMenuBase(QProgressBar)

class QtBoxFuncProgressBar2(QProgressBar):
    def __init__(self):
        super(QtBoxFuncProgressBar2, self).__init__(str(Path(__file__)))
        self.setInvertedAppearance(True)
        self.setRange(0, 100)
        self.setValue(80)
# PyQt

# PySide
# from PySide2.QtWidgets import QProgressBar


# class QtBoxFuncProgressBar2(QProgressBar):
#     def __init__(self):
#         super(QtBoxFuncProgressBar2, self).__init__()
#         self.setInvertedAppearance(True)
#         self.setRange(0, 100)
#         self.setValue(80)
# PySide