# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QComboBox, QCompleter
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QComboBox = createWidgetMenuBase(QComboBox)

class QtBoxFuncComboBox2(QComboBox):
    def __init__(self):
        super(QtBoxFuncComboBox2, self).__init__(str(Path(__file__)))
        self.setEditable(True)
        self.addItems(['1', '2', '3', '4', '5', '6'])
        comp = QCompleter(["1a", "1b", "1c"])
        comp.setFilterMode(Qt.MatchContains)
        self.setCompleter(comp)
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QComboBox, QCompleter


# class QtBoxFuncComboBox2(QComboBox):
#     def __init__(self):
#         super(QtBoxFuncComboBox2, self).__init__()
#         self.setEditable(True)
#         self.addItems(['1', '2', '3', '4', '5', '6'])
#         comp = QCompleter(["1a", "1b", "1c"])
#         comp.setFilterMode(Qt.MatchContains)
#         self.setCompleter(comp)
# PySide