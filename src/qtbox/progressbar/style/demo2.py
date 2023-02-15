# PyQt
from PyQt5.QtWidgets import QProgressBar
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QProgressBar = createWidgetMenuBase(QProgressBar)

class QtBoxStyleProgressBar2(QProgressBar):
    def __init__(self):
        super(QtBoxStyleProgressBar2, self).__init__(str(Path(__file__)))
        self.setTextVisible(False)
        self.setRange(0, 100)
        self.setValue(80)
        self.setStyleSheet("""
        QProgressBar {
            border: 2px solid #888783;
            border-radius: 5px;
        }

        QProgressBar::chunk {
            background-color: #74d65f;
            border-radius: 2px;
            width: 9px;
            margin: 0.5px;
        }
        """)
# PyQt

# PySide
# from PySide2.QtWidgets import QProgressBar


# class QtBoxStyleProgressBar2(QProgressBar):
#     def __init__(self):
#         super(QtBoxStyleProgressBar2, self).__init__()
#         self.setTextVisible(False)
#         self.setRange(0, 100)
#         self.setValue(80)
#         self.setStyleSheet("""
#         QProgressBar {
#             border: 2px solid #888783;
#             border-radius: 5px;
#         }

#         QProgressBar::chunk {
#             background-color: #74d65f;
#             border-radius: 2px;
#             width: 9px;
#             margin: 0.5px;
#         }
#         """)
# PySide