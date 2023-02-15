# PyQt
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QPushButton
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QPushButton = createWidgetMenuBase(QPushButton)
PATH_TO_IMG = str(Path(__file__).parent.parent.parent / "res/images/plus.png").replace("\\", "/")

class QtBoxStyleButton5(QPushButton):
    def __init__(self):
        super(QtBoxStyleButton5, self).__init__(str(Path(__file__)))
        self.setFixedSize(90, 90)
        self.setIconSize(QSize(80, 80))
        self.setIcon(QIcon(PATH_TO_IMG))
        self.setStyleSheet("""
        QPushButton {
            background-color: qlineargradient(x1:1, y1:0, x2:0, y2:1, stop:0 #f9ab6a, stop: 1 #f08833);
            border-radius: 45px;
            border: none
        }

        QPushButton:hover {
            background-color: qlineargradient(x1:1, y1:0, x2:0, y2:1, stop:0 #f7a25b, stop: 1 #f19040);
        }

        QPushButton:pressed {
            background-color: qlineargradient(x1:1, y1:0, x2:0, y2:1, stop:0 #e39b5f, stop: 1 #e58637);
        }
        """)
# PyQt

# PySide
# from PySide2.QtGui import QIcon
# from PySide2.QtCore import QSize
# from PySide2.QtWidgets import QPushButton


# class QtBoxStyleButton5(QPushButton):
#     def __init__(self):
#         super(QtBoxStyleButton5, self).__init__()
#         self.setFixedSize(90, 90)
#         self.setIconSize(QSize(80, 80))
#         self.setIcon(QIcon(PATH_TO_IMG))
#         self.setStyleSheet("""
#         QPushButton {
#             background-color: qlineargradient(x1:1, y1:0, x2:0, y2:1, stop:0 #f9ab6a, stop: 1 #f08833);
#             border-radius: 45px;
#             border: none
#         }

#         QPushButton:hover {
#             background-color: qlineargradient(x1:1, y1:0, x2:0, y2:1, stop:0 #f7a25b, stop: 1 #f19040);
#         }

#         QPushButton:pressed {
#             background-color: qlineargradient(x1:1, y1:0, x2:0, y2:1, stop:0 #e39b5f, stop: 1 #e58637);
#         }
#         """)
# PySide