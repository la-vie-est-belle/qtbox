# PyQt
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QPushButton
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QPushButton = createWidgetMenuBase(QPushButton)
PATH_TO_IMG = str(Path(__file__).parent.parent.parent / "res/images/search.png").replace("\\", "/")

class QtBoxStyleButton7(QPushButton):
    def __init__(self):
        super(QtBoxStyleButton7, self).__init__(str(Path(__file__)))
        self.setText("BUTTON ")
        self.setFixedSize(150, 40)
        self.setIconSize(QSize(25, 25))
        self.setIcon(QIcon(PATH_TO_IMG))
        self.setLayoutDirection(Qt.RightToLeft)
        self.setStyleSheet("""
        QPushButton {
            background-color: #292929;
            border-radius: 5px;
            font-size: 20px;
            font-weight: bold;
            color: white;
            border: 1px solid white;
        }

        QPushButton:pressed {
            background-color: black;
        }
        """)
# PyQt

# PySide
# from PySide2.QtGui import QIcon
# from PySide2.QtCore import QSize, Qt
# from PySide2.QtWidgets import QPushButton


# class QtBoxStyleButton7(QPushButton):
#     def __init__(self):
#         super(QtBoxStyleButton7, self).__init__()
#         self.setText("BUTTON ")
#         self.setFixedSize(150, 40)
#         self.setIconSize(QSize(25, 25))
#         self.setIcon(QIcon(PATH_TO_IMG))
#         self.setLayoutDirection(Qt.RightToLeft)
#         self.setStyleSheet("""
#         QPushButton {
#             background-color: #292929;
#             border-radius: 5px;
#             font-size: 20px;
#             font-weight: bold;
#             color: white;
#             border: 1px solid white;
#         }

#         QPushButton:pressed {
#             background-color: black;
#         }
#         """)
# PySide