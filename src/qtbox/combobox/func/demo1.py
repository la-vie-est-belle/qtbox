# PyQt
from PyQt5.QtWidgets import QComboBox
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QComboBox = createWidgetMenuBase(QComboBox)

class QtBoxFuncComboBox1(QComboBox):
    def __init__(self):
        super(QtBoxFuncComboBox1, self).__init__(str(Path(__file__)))
        self.setEditable(True)
        self.addItems(['1', '2', '3', '4', '5', '6'])
        self.currentTextChanged.connect(self.update_item)

    def update_item(self, txt):
        self.setItemText(self.currentIndex(), txt)
# PyQt

# PySide
# from PySide2.QtWidgets import QComboBox


# class QtBoxFuncComboBox1(QComboBox):
#     def __init__(self):
#         super(QtBoxFuncComboBox1, self).__init__()
#         self.setEditable(True)
#         self.addItems(['1', '2', '3', '4', '5', '6'])
#         self.currentTextChanged.connect(self.update_item)

#     def update_item(self, txt):
#         self.setItemText(self.currentIndex(), txt)
# PySide