# PyQt
from PyQt5.QtWidgets import QSpinBox
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QSpinBox = createWidgetMenuBase(QSpinBox)

class QtBoxFuncSpinBox1(QSpinBox):
    def __init__(self):
        super(QtBoxFuncSpinBox1, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 30)
        self.setPrefix("Sth: ")
        self.setSuffix(" PCS")
# PyQt

# PySide
# from PySide2.QtWidgets import QSpinBox


# class QtBoxFuncSpinBox1(QSpinBox):
#     def __init__(self):
#         super(QtBoxFuncSpinBox1, self).__init__(str(Path(__file__)))
#         self.setFixedSize(150, 30)
#         self.setPrefix("Sth: ")
#         self.setSuffix(" PCS")
# PySide