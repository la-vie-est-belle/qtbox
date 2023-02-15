# PyQt
from PyQt5.QtWidgets import QLineEdit, QLabel
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QLineEdit = createWidgetMenuBase(QLineEdit)

class QtBoxStyleLineEdit2(QLineEdit):
    def __init__(self):
        super(QtBoxStyleLineEdit2, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 50)
        self.setStyleSheet("""
        QLineEdit {
            border: 1px solid gray;
            border-radius: 5px;
            padding-top: 14px;
            padding-left: 2px;
            padding-right: 2px;
        }
        """)

        self.label = QLabel(self)
        self.label.setText("Name")
        self.label.move(5, 16)
        self.label.setStyleSheet("""
        QLabel {
            color: gray;
            font-size: 16px;
        }
        """)

    def focusInEvent(self, event):
        super(QtBoxStyleLineEdit2, self).focusInEvent(event)
        self.label.move(5, 5)
        self.label.setStyleSheet("""
        QLabel {
            color: black;
            font-size: 12px;
        }
        """)

    def focusOutEvent(self, event):
        super(QtBoxStyleLineEdit2, self).focusOutEvent(event)
        if self.text():
            return

        self.label.move(5, 16)
        self.label.setStyleSheet("""
        QLabel {
            color: gray;
            font-size: 16px;
        }
        """)
# PyQt

# PySide
# from PySide2.QtWidgets import QLineEdit, QLabel


# class QtBoxStyleLineEdit2(QLineEdit):
#     def __init__(self):
#         super(QtBoxStyleLineEdit2, self).__init__()
#         self.setFixedSize(150, 50)
#         self.setStyleSheet("""
#         QLineEdit {
#             border: 1px solid gray;
#             border-radius: 5px;
#             padding-top: 14px;
#             padding-left: 2px;
#             padding-right: 2px;
#         }
#         """)

#         self.label = QLabel(self)
#         self.label.setText("Name")
#         self.label.move(5, 16)
#         self.label.setStyleSheet("""
#         QLabel {
#             color: gray;
#             font-size: 16px;
#         }
#         """)

#     def focusInEvent(self, event):
#         super(QtBoxStyleLineEdit2, self).focusInEvent(event)
#         self.label.move(5, 5)
#         self.label.setStyleSheet("""
#         QLabel {
#             color: black;
#             font-size: 12px;
#         }
#         """)

#     def focusOutEvent(self, event):
#         super(QtBoxStyleLineEdit2, self).focusOutEvent(event)
#         if self.text():
#             return

#         self.label.move(5, 16)
#         self.label.setStyleSheet("""
#         QLabel {
#             color: gray;
#             font-size: 16px;
#         }
#         """)
# PySide