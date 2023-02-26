# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QCompleter
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QLineEdit = createWidgetMenuBase(QLineEdit)

class QtBoxFuncLineEdit5(QLineEdit):
    def __init__(self):
        super(QtBoxFuncLineEdit5, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 30)
        self.setPlaceholderText("Type P or Q")

        comp = QCompleter(["PyQt", "Qt", "Qt Box", "PySide", "Python"])
        comp.setFilterMode(Qt.MatchContains)
        self.setCompleter(comp)
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QLineEdit, QCompleter


# class QtBoxFuncLineEdit5(QLineEdit):
#     def __init__(self):
#         super(QtBoxFuncLineEdit5, self).__init__()
#         self.setFixedSize(150, 30)
#         self.setPlaceholderText("Type P or Q")

#         comp = QCompleter(["PyQt", "Qt", "Qt Box", "PySide", "Python"])
#         comp.setFilterMode(Qt.MatchContains)
#         self.setCompleter(comp)
# PySide