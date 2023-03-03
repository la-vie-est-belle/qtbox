# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QTableWidget = createWidgetMenuBase(QTableWidget)

class QtBoxFuncTableWidget2(QTableWidget):
    def __init__(self):
        super(QtBoxFuncTableWidget2, self).__init__(str(Path(__file__)))
        self.setFixedSize(200, 150)
        self.setColumnCount(3)
        self.setRowCount(5)
        self.set_text_and_align_center()

    def set_text_and_align_center(self):
        for row in range(self.rowCount()):
            for col in range(self.columnCount()):
                item = QTableWidgetItem()
                item.setText(f"{row+1}, {col+1}")
                item.setTextAlignment(Qt.AlignCenter)
                self.setItem(row, col, item)
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QTableWidget, QTableWidgetItem


# class QtBoxFuncTableWidget2(QTableWidget):
#     def __init__(self):
#         super(QtBoxFuncTableWidget2, self).__init__(str(Path(__file__)))
#         self.setFixedSize(200, 150)
#         self.setColumnCount(3)
#         self.setRowCount(5)
#         self.set_text_and_align_center()

#     def set_text_and_align_center(self):
#         for row in range(self.rowCount()):
#             for col in range(self.columnCount()):
#                 item = QTableWidgetItem()
#                 item.setText(f"{row+1}, {col+1}")
#                 item.setTextAlignment(Qt.AlignCenter)
#                 self.setItem(row, col, item)
# PySide