# PyQt
from PyQt5.QtWidgets import QProgressBar
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QProgressBar = createWidgetMenuBase(QProgressBar)

class QtBoxStyleProgressBar1(QProgressBar):
    def __init__(self):
        super(QtBoxStyleProgressBar1, self).__init__(str(Path(__file__)))
        self.setFormat("loading...")
        self.setRange(0, 100)
        self.setValue(80)
        self.setStyleSheet("""
        QProgressBar {
            border: 2px solid lightgray;
            border-radius: 5px;
            text-align: center;
            color: white;
        }
        
        QProgressBar::chunk {
            background-color: #cd96cd;
            border-radius: 4px;
        }
        """)
# PyQt

# PySide
# from PySide2.QtWidgets import QProgressBar


# class QtBoxStyleProgressBar1(QProgressBar):
#     def __init__(self):
#         super(QtBoxStyleProgressBar1, self).__init__()
#         self.setFormat("loading...")
#         self.setRange(0, 100)
#         self.setValue(80)
#         self.setStyleSheet("""
#         QProgressBar {
#             border: 2px solid lightgray;
#             border-radius: 5px;
#             text-align: center;
#             color: white;
#         }

#         QProgressBar::chunk {
#             background-color: #cd96cd;
#             border-radius: 4px;
#         }
#         """)
# PySide