# PyQt
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QPushButton
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QListWidget = createWidgetMenuBase(QListWidget)

class QtBoxFuncListWidget1(QListWidget):
    def __init__(self):
        super(QtBoxFuncListWidget1, self).__init__(str(Path(__file__)))
        self.setFixedSize(100, 200)
        self.add_btns()

    def add_btns(self):
        for _ in range(5):
            item = QListWidgetItem()
            item.setSizeHint(QSize(80, 30))
            self.addItem(item)

            btn = QPushButton()
            btn.setText("button")
            self.setItemWidget(item, btn)
# PyQt

# PySide
# from PySide2.QtCore import QSize
# from PySide2.QtWidgets import QListWidget, QListWidgetItem, QPushButton


# class QtBoxFuncListWidget1(QListWidget):
#     def __init__(self):
#         super(QtBoxFuncListWidget1, self).__init__()
#         self.setFixedSize(80, 200)
#         self.add_btns()

#     def add_btns(self):
#         for _ in range(5):
#             item = QListWidgetItem()
#             item.setSizeHint(QSize(100, 30))
#             self.addItem(item)

#             btn = QPushButton()
#             btn.setText("button")
#             self.setItemWidget(item, btn)
# PySide