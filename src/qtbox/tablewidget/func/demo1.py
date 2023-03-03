# PyQt
from PyQt5.QtWidgets import QTableWidget, QPushButton
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QTableWidget = createWidgetMenuBase(QTableWidget)

class QtBoxFuncTableWidget1(QTableWidget):
    def __init__(self):
        super(QtBoxFuncTableWidget1, self).__init__(str(Path(__file__)))
        self.setFixedSize(200, 150)
        self.setColumnCount(3)
        self.setRowCount(5)
        self.add_btns()

    def add_btns(self):
        for row in range(self.rowCount()):
            for col in range(self.columnCount()):
                btn = QPushButton()
                btn.setText("button")
                self.setCellWidget(row, col, btn)
# PyQt

# PySide
# from PySide2.QtWidgets import QTableWidget, QPushButton


# class QtBoxFuncTableWidget1(QTableWidget):
#     def __init__(self):
#         super(QtBoxFuncTableWidget1, self).__init__()
#         self.setFixedSize(200, 150)
#         self.setColumnCount(3)
#         self.setRowCount(5)
#         self.add_btns()

#     def add_btns(self):
#         for row in range(self.rowCount()):
#             for col in range(self.columnCount()):
#                 btn = QPushButton()
#                 btn.setText("button")
#                 self.setCellWidget(row, col, btn)
# PySide