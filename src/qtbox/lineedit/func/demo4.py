# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLineEdit, QPushButton
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QLineEdit = createWidgetMenuBase(QLineEdit)
PATH_TO_OPEN_EYE_IMG = str(Path(__file__).parent.parent.parent / "res/images/open_eye.png").replace("\\", "/")
PATH_TO_CLOSED_EYE_IMG = str(Path(__file__).parent.parent.parent / "res/images/closed_eye.png").replace("\\", "/")

class QtBoxFuncLineEdit4(QLineEdit):
    def __init__(self):
        super(QtBoxFuncLineEdit4, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 30)
        self.setEchoMode(QLineEdit.Password)
        self.setPlaceholderText("Enter password")
        self.setStyleSheet("""
        QLineEdit {
            padding-right: 25px;
        }
        """)

        self.eye_btn = QPushButton(self)
        self.eye_btn.setIcon(QIcon(PATH_TO_CLOSED_EYE_IMG))
        self.eye_btn.setFixedSize(self.height(), self.height())
        self.eye_btn.move(self.width()-self.eye_btn.width(), 0)
        self.eye_btn.clicked.connect(self.change_echo_mode)
        self.eye_btn.setCursor(Qt.PointingHandCursor)
        self.eye_btn.setStyleSheet("""
        QPushButton {
            border: none;
        }
        """)

    def change_echo_mode(self):
        if self.echoMode() == QLineEdit.Normal:
            self.setEchoMode(QLineEdit.Password)
            self.eye_btn.setIcon(QIcon(PATH_TO_CLOSED_EYE_IMG))
        else:
            self.setEchoMode(QLineEdit.Normal)
            self.eye_btn.setIcon(QIcon(PATH_TO_OPEN_EYE_IMG))
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtGui import QIcon
# from PySide2.QtWidgets import QLineEdit, QPushButton


# class QtBoxFuncLineEdit4(QLineEdit):
#     def __init__(self):
#         super(QtBoxFuncLineEdit4, self).__init__(str(Path(__file__)))
#         self.setFixedSize(150, 30)
#         self.setEchoMode(QLineEdit.Password)
#         self.setPlaceholderText("Enter password")
#         self.setStyleSheet("""
#         QLineEdit {
#             padding-right: 25px;
#         }
#         """)

#         self.eye_btn = QPushButton(self)
#         self.eye_btn.setIcon(QIcon(PATH_TO_CLOSED_EYE_IMG))
#         self.eye_btn.setFixedSize(self.height(), self.height())
#         self.eye_btn.move(self.width()-self.eye_btn.width(), 0)
#         self.eye_btn.clicked.connect(self.change_echo_mode)
#         self.eye_btn.setCursor(Qt.PointingHandCursor)
#         self.eye_btn.setStyleSheet("""
#         QPushButton {
#             border: none;
#         }
#         """)

#     def change_echo_mode(self):
#         if self.echoMode() == QLineEdit.Normal:
#             self.setEchoMode(QLineEdit.Password)
#             self.eye_btn.setIcon(QIcon(PATH_TO_CLOSED_EYE_IMG))
#         else:
#             self.setEchoMode(QLineEdit.Normal)
#             self.eye_btn.setIcon(QIcon(PATH_TO_OPEN_EYE_IMG))
# PySide