# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidget, QListWidgetItem
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QListWidget = createWidgetMenuBase(QListWidget)

class QtBoxStyleListWidget2(QListWidget):
    def __init__(self):
        super(QtBoxStyleListWidget2, self).__init__(str(Path(__file__)))
        self.setFixedSize(200, 200)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        for i in range(10):
            item = QListWidgetItem()
            item.setText(str(i))
            self.addItem(item)

        self.setStyleSheet("""
        QListView {
            border: none;
            background-color: #65afdc;
            font-weight: bold;
        }

        QListView::item {
            height: 40px;
            color: white;
            border-bottom: 1px solid #8fcef4;
        }

        QListView::item:hover:!selected{
            background-color: #8fcef4;
            padding-left: 5px;
            padding-bottom: 2px;
        }

        QListView::item:selected{
            background-color: #5da0c7;
        }
        """)
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QListWidget, QListWidgetItem


# class QtBoxStyleListWidget2(QListWidget):
#     def __init__(self):
#         super(QtBoxStyleListWidget2, self).__init__()
#         self.setFixedSize(200, 200)
#         self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
#         self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

#         for i in range(10):
#             item = QListWidgetItem()
#             item.setText(str(i))
#             self.addItem(item)

#         self.setStyleSheet("""
#         QListView {
#             border: none;
#             background-color: #65afdc;
#             font-weight: bold;
#         }

#         QListView::item {
#             height: 40px;
#             color: white;
#             border-bottom: 1px solid #8fcef4;
#         }

#         QListView::item:hover:!selected{
#             background-color: #8fcef4;
#             padding-left: 5px;
#             padding-bottom: 2px;
#         }

#         QListView::item:selected{
#             background-color: #5da0c7;
#         }
#         """)
# PySide