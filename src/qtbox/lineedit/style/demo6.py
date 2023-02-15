# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QLineEdit = createWidgetMenuBase(QLineEdit)

class QtBoxStyleLineEdit6(QLineEdit):
    def __init__(self):
        super(QtBoxStyleLineEdit6, self).__init__(str(Path(__file__)))
        self.setMaxLength(1)
        self.setFixedSize(50, 50)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""
        QLineEdit {
            font-size: 25px;
            border: 2px solid black;
        }
        """)
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QLineEdit


# class QtBoxStyleLineEdit6(QLineEdit):
#     def __init__(self):
#         super(QtBoxStyleLineEdit6, self).__init__()
#         self.setMaxLength(1)
#         self.setFixedSize(50, 50)
#         self.setAlignment(Qt.AlignCenter)
#         self.setStyleSheet("""
#         QLineEdit {
#             font-size: 25px;
#             border: 2px solid black;
#         }
#         """)
# PySide