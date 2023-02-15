# PyQt
from PyQt5.QtWidgets import QProgressBar
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QProgressBar = createWidgetMenuBase(QProgressBar)

class QtBoxStyleProgressBar3(QProgressBar):
    def __init__(self):
        super(QtBoxStyleProgressBar3, self).__init__(str(Path(__file__)))
        self.setRange(0, 100)
        self.setValue(80)
        self.setStyleSheet("""
        QProgressBar {
            border: 2px solid white;
            background-color: black;
            padding-left: 2px;
            padding-right: 2px;
            text-align: center;
        }

        QProgressBar::chunk {
            background-color: white;
            margin-top: 2px;
            margin-bottom: 2px;
        }
        """)
# PyQt

# PySide
# from PySide2.QtWidgets import QProgressBar


# class QtBoxStyleProgressBar3(QProgressBar):
#     def __init__(self):
#         super(QtBoxStyleProgressBar3, self).__init__()
#         self.setRange(0, 100)
#         self.setValue(80)
#         self.setStyleSheet("""
#         QProgressBar {
#             border: 2px solid white;
#             background-color: black;
#             padding-left: 2px;
#             padding-right: 2px;
#             text-align: center;
#         }

#         QProgressBar::chunk {
#             background-color: white;
#             margin-top: 2px;
#             margin-bottom: 2px;
#         }
#         """)
# PySide