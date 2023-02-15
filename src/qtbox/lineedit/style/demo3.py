# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QLabel
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QLineEdit = createWidgetMenuBase(QLineEdit)

class QtBoxStyleLineEdit3(QLineEdit):
    def __init__(self):
        super(QtBoxStyleLineEdit3, self).__init__(str(Path(__file__)))
        self.setAttribute(Qt.WA_MacShowFocusRect, False)
        self.setPlaceholderText("Enter username")
        self.setFixedSize(180, 30)
        self.setStyleSheet("""
        QLineEdit {
            border: 1px solid lightgray;
            border-radius: 5px;
            border-top-left-radius: 10px;
            border-bottom-left-radius: 10px;
            padding-left: 62px;
            padding-right: 5px;
        }
        """)

        self.label = QLabel(self)
        self.label.setText("Qt Box")
        self.label.setFixedSize(60, 30)
        self.label.move(0, 0)
        self.label.setStyleSheet("""
        QLabel {
            background-color: #f8f9fb;
            color: black; 
            font-size: 15px;
            padding-left: 3px;
            border: 1px solid lightgray;
            border-top-left-radius: 10px;
            border-bottom-left-radius: 10px;
        }
        
        QLabel:hover {
            background-color: #ebecf0;
        }
        """)
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QLineEdit, QLabel


# class QtBoxStyleLineEdit3(QLineEdit):
#     def __init__(self):
#         super(QtBoxStyleLineEdit3, self).__init__()
#         self.setAttribute(Qt.WA_MacShowFocusRect, False)
#         self.setPlaceholderText("Enter username")
#         self.setFixedSize(180, 30)
#         self.setStyleSheet("""
#         QLineEdit {
#             border: 1px solid lightgray;
#             border-radius: 5px;
#             border-top-left-radius: 10px;
#             border-bottom-left-radius: 10px;
#             padding-left: 62px;
#             padding-right: 5px;
#         }
#         """)

#         self.label = QLabel(self)
#         self.label.setText("Qt Box")
#         self.label.setFixedSize(60, 30)
#         self.label.move(0, 0)
#         self.label.setStyleSheet("""
#         QLabel {
#             background-color: #f8f9fb;
#             color: black;
#             font-size: 15px;
#             padding-left: 3px;
#             border: 1px solid lightgray;
#             border-top-left-radius: 10px;
#             border-bottom-left-radius: 10px;
#         }

#         QLabel:hover {
#             background-color: #ebecf0;
#         }
#         """)
# PySide