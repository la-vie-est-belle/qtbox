# PyQt
from PyQt5.QtWidgets import QDial
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QDial = createWidgetMenuBase(QDial)

class QtBoxStyleDial1(QDial):
    def __init__(self):
        super(QtBoxStyleDial1, self).__init__(str(Path(__file__)))
        self.setStyleSheet("""
        QDial {
            background-color: gray;
        }
        """)
# PyQt

# PySide
# from PySide2.QtWidgets import QDial


# class QtBoxStyleDial1(QDial):
#     def __init__(self):
#         super(QtBoxStyleDial1, self).__init__(str(Path(__file__)))
#         self.setStyleSheet("""
#         QDial {
#             background-color: gray;
#         }
#         """)
# PySide