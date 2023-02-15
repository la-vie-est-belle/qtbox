# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLineEdit, QPushButton
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QLineEdit = createWidgetMenuBase(QLineEdit)
PATH_TO_IMG = str(Path(__file__).parent.parent.parent / "res/images/camera.png").replace("\\", "/")

class QtBoxStyleLineEdit7(QLineEdit):
    def __init__(self):
        super(QtBoxStyleLineEdit7, self).__init__(str(Path(__file__)))
        self.setAttribute(Qt.WA_MacShowFocusRect, False)
        self.setPlaceholderText("search")
        self.setFixedSize(185, 30)
        self.setStyleSheet("""
        QLineEdit {
            border: 2px solid red;
            border-radius: 5px;
            padding-left: 5px;
            padding-right: 80px;
        }
        """)

        self.search_btn = QPushButton(self)
        self.search_btn.setText("Search")
        self.search_btn.setFixedSize(55, self.height())
        self.search_btn.setCursor(Qt.PointingHandCursor)
        self.search_btn.move(self.width() - self.search_btn.width(), 0)
        self.search_btn.setStyleSheet("""
        QPushButton {
            background-color: red;
            color: white; 
            font-size: 13px;
            border-top: 2px solid red;
            border-right: 2px solid red;
            border-bottom: 2px solid red;
            border-top-right-radius: 5px;
            border-bottom-right-radius: 5px;
        }

        QPushButton:hover {
            background-color: #f31919;
        }

        QPushButton:pressed {
            background-color: #e21818;
        }
        """)

        self.camera_btn = QPushButton(self)
        self.camera_btn.setIcon(QIcon(PATH_TO_IMG))
        self.camera_btn.setCursor(Qt.PointingHandCursor)
        self.camera_btn.setFixedSize(self.height(), self.height())
        self.camera_btn.move(self.width()-self.search_btn.width()-self.camera_btn.width(), 0)
        self.camera_btn.setStyleSheet("""
        QPushButton {
            border: none;
        }
        """)
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtGui import QIcon
# from PySide2.QtWidgets import QLineEdit, QPushButton


# class QtBoxStyleLineEdit7(QLineEdit):
#     def __init__(self):
#         super(QtBoxStyleLineEdit7, self).__init__()
#         self.setAttribute(Qt.WA_MacShowFocusRect, False)
#         self.setPlaceholderText("search")
#         self.setFixedSize(185, 30)
#         self.setStyleSheet("""
#         QLineEdit {
#             border: 2px solid red;
#             border-radius: 5px;
#             padding-left: 5px;
#             padding-right: 80px;
#         }
#         """)

#         self.search_btn = QPushButton(self)
#         self.search_btn.setText("Search")
#         self.search_btn.setFixedSize(55, self.height())
#         self.search_btn.setCursor(Qt.PointingHandCursor)
#         self.search_btn.move(self.width() - self.search_btn.width(), 0)
#         self.search_btn.setStyleSheet("""
#         QPushButton {
#             background-color: red;
#             color: white;
#             font-size: 13px;
#             border-top: 2px solid red;
#             border-right: 2px solid red;
#             border-bottom: 2px solid red;
#             border-top-right-radius: 5px;
#             border-bottom-right-radius: 5px;
#         }

#         QPushButton:hover {
#             background-color: #f31919;
#         }
#
#         QPushButton:pressed {
#             background-color: #e21818;
#         }
#         """)

#         self.camera_btn = QPushButton(self)
#         self.camera_btn.setIcon(QIcon(PATH_TO_IMG))
#         self.camera_btn.setCursor(Qt.PointingHandCursor)
#         self.camera_btn.setFixedSize(self.height(), self.height())
#         self.camera_btn.move(self.width()-self.search_btn.width()-self.camera_btn.width(), 0)
#         self.camera_btn.setStyleSheet("""
#         QPushButton {
#             border: none;
#         }
#         """)
# PySide