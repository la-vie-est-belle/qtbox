# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLineEdit, QPushButton
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QLineEdit = createWidgetMenuBase(QLineEdit)
PATH_TO_IMG = str(Path(__file__).parent.parent.parent / "res/images/search.png").replace("\\", "/")

class QtBoxStyleLineEdit1(QLineEdit):
    def __init__(self):
        super(QtBoxStyleLineEdit1, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 30)
        self.setPlaceholderText("search")

        self.search_btn = QPushButton(self)
        self.search_btn.setIcon(QIcon(PATH_TO_IMG))
        self.search_btn.setCursor(Qt.PointingHandCursor)
        self.search_btn.setFixedSize(self.height(), self.height())
        self.search_btn.move(self.width()-self.search_btn.width(), 0)

        self.setStyleSheet("""
        QPushButton {
            border: none;
        }

        QLineEdit {
            background-color: #232324;
            border: 1px solid gray;
            border-radius: 3px;
            padding-left: 2px;
            padding-right: 25px;
            color: #f0f0f0;
        }
        """)
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtGui import QIcon
# from PySide2.QtWidgets import QLineEdit, QPushButton


# class QtBoxStyleLineEdit1(QLineEdit):
#     def __init__(self):
#         super(QtBoxStyleLineEdit1, self).__init__()
#         self.setFixedSize(150, 30)
#         self.setPlaceholderText("search")

#         self.search_btn = QPushButton(self)
#         self.search_btn.setIcon(QIcon(PATH_TO_IMG))
#         self.search_btn.setCursor(Qt.PointingHandCursor)
#         self.search_btn.setFixedSize(self.height(), self.height())
#         self.search_btn.move(self.width()-self.search_btn.width(), 0)

#         self.setStyleSheet("""
#         QPushButton {
#             border: none;
#         }

#         QLineEdit {
#             background-color: #232324;
#             border: 1px solid gray;
#             border-radius: 3px;
#             padding-left: 2px;
#             padding-right: 25px;
#             color: #f0f0f0;
#         }
#         """)
# PySide