# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QProgressBar
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QProgressBar = createWidgetMenuBase(QProgressBar)

class QtBoxStyleProgressBar9(QProgressBar):
    def __init__(self):
        super(QtBoxStyleProgressBar9, self).__init__(str(Path(__file__)))
        self.setOrientation(Qt.Vertical)
        self.setTextVisible(False)
        self.setMaximumWidth(10)
        self.setRange(0, 100)
        self.setValue(80)
        self.setStyleSheet("""
        QProgressBar {
            border: 2px solid black;
            background-color: #f8f8f8;
            border-radius: 5px;
            padding-left: 2px;
            padding-right: 2px;
        }

        QProgressBar::chunk {
            background-color: #d33124;
            border-radius: 4px;
            margin-top: 2px;
            margin-bottom: 2px;
        }
        """)
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QProgressBar


# class QtBoxStyleProgressBar9(QProgressBar):
#     def __init__(self):
#         super(QtBoxStyleProgressBar9, self).__init__()
#         self.setOrientation(Qt.Vertical)
#         self.setTextVisible(False)
#         self.setMaximumWidth(10)
#         self.setRange(0, 100)
#         self.setValue(80)
#         self.setStyleSheet("""
#         QProgressBar {
#             border: 2px solid black;
#             background-color: #f8f8f8;
#             border-radius: 5px;
#             padding-left: 2px;
#             padding-right: 2px;
#         }

#         QProgressBar::chunk {
#             background-color: #d33124;
#             border-radius: 4px;
#             margin-top: 2px;
#             margin-bottom: 2px;
#         }
#         """)
# PySide