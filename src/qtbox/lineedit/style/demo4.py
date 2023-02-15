# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QPushButton
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QLineEdit = createWidgetMenuBase(QLineEdit)

class QtBoxStyleLineEdit4(QLineEdit):
    def __init__(self):
        super(QtBoxStyleLineEdit4, self).__init__(str(Path(__file__)))
        self.setAttribute(Qt.WA_MacShowFocusRect, False)
        self.setPlaceholderText("search")
        self.setFixedSize(180, 30)
        self.setStyleSheet("""
        QLineEdit {
            border: 1px solid lightgray;
            border-radius: 5px;
            padding-left: 5px;
            padding-right: 60px;
        }
        """)

        self.search_btn = QPushButton(self)
        self.search_btn.setText("Search")
        self.search_btn.setFixedSize(60, self.height())
        self.search_btn.setCursor(Qt.PointingHandCursor)
        self.search_btn.move(self.width()-self.search_btn.width(), 0)
        self.search_btn.setStyleSheet("""
        QPushButton {
            background-color: #2a70f4;
            color: white; 
            font-size: 13px;
            border-top-right-radius: 5px;
            border-bottom-right-radius: 5px;
        }

        QPushButton:hover {
            background-color: #2361d0;
        }
        
        QPushButton:pressed {
            background-color: #2058bc;
        }
        """)
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QLineEdit, QPushButton


# class QtBoxStyleLineEdit4(QLineEdit):
#     def __init__(self):
#         super(QtBoxStyleLineEdit4, self).__init__()
#         self.setAttribute(Qt.WA_MacShowFocusRect, False)
#         self.setPlaceholderText("search")
#         self.setFixedSize(180, 30)
#         self.setStyleSheet("""
#         QLineEdit {
#             border: 1px solid lightgray;
#             border-radius: 5px;
#             padding-left: 5px;
#             padding-right: 60px;
#         }
#         """)

#         self.search_btn = QPushButton(self)
#         self.search_btn.setText("Search")
#         self.search_btn.setFixedSize(60, self.height())
#         self.search_btn.setCursor(Qt.PointingHandCursor)
#         self.search_btn.move(self.width()-self.search_btn.width(), 0)
#         self.search_btn.setStyleSheet("""
#         QPushButton {
#             background-color: #2a70f4;
#             color: white;
#             font-size: 13px;
#             border-top-right-radius: 5px;
#             border-bottom-right-radius: 5px;
#         }

#         QPushButton:hover {
#             background-color: #2361d0;
#         }

#         QPushButton:pressed {
#             background-color: #2058bc;
#         }
#         """)
# PySide