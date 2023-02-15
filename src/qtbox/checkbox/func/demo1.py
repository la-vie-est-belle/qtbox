# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QCheckBox
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QCheckBox = createWidgetMenuBase(QCheckBox)

class QtBoxFuncCheckBox1(QCheckBox):
    def __init__(self):
        super(QtBoxFuncCheckBox1, self).__init__(str(Path(__file__)))
        self.setTristate(True)
        self.setText("UnChecked")
        self.stateChanged.connect(self.update_text)

    def update_text(self):
        if self.checkState() == Qt.Unchecked:
            self.setText("UnChecked")
        elif self.checkState() == Qt.PartiallyChecked:
            self.setText("PartiallyChecked")
        elif self.checkState() == Qt.Checked:
            self.setText("Checked")
# PyQt

# PySide
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QCheckBox


# class QtBoxFuncCheckBox1(QCheckBox):
#     def __init__(self):
#         super(QtBoxFuncCheckBox1, self).__init__()
#         self.setTristate(True)
#         self.setText("UnChecked")
#         self.stateChanged.connect(self.update_text)

#     def update_text(self):
#         if self.checkState() == Qt.Unchecked:
#             self.setText("UnChecked")
#         elif self.checkState() == Qt.PartiallyChecked:
#             self.setText("PartiallyChecked")
#         elif self.checkState() == Qt.Checked:
#             self.setText("Checked")
# PySide
