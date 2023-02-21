# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidget, QListWidgetItem
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QListWidget = createWidgetMenuBase(QListWidget)

class QtBoxStyleListWidget1(QListWidget):
    def __init__(self):
        super(QtBoxStyleListWidget1, self).__init__(str(Path(__file__)))
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
            background-color: #edeef3;
        }
        
        QListView::item {
            height: 40px;
            margin: 5px 5px 5px 5px;
            background-color: white;
            border-radius: 6px;
        }
        
        QListView::item:hover{
            background-color: whitesmoke;
        }
        
        QListView::item:selected{
            color: black;
            border: 1px solid lightgray;
        }
        """)
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QListWidget, QListWidgetItem


# class QtBoxStyleListWidget1(QListWidget):
#     def __init__(self):
#         super(QtBoxStyleListWidget1, self).__init__(str(Path(__file__)))
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
#             background-color: #edeef3;
#         }

#         QListView::item {
#             height: 40px;
#             margin: 5px 5px 5px 5px;
#             background-color: white;
#             border-radius: 6px;
#         }

#         QListView::item:hover{
#             background-color: whitesmoke;
#         }

#         QListView::item:selected{
#             color: black;
#             border: 1px solid lightgray;
#         }
#         """)
# PySide