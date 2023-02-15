# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QMessageBox
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QLineEdit = createWidgetMenuBase(QLineEdit)

class QtBoxFuncLineEdit1(QLineEdit):
    def __init__(self):
        super(QtBoxFuncLineEdit1, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 30)
        self.setPlaceholderText("press Enter or Return")

    def keyPressEvent(self, event):
        super(QtBoxFuncLineEdit1, self).keyPressEvent(event)
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            QMessageBox.information(self, "Qt Box", "Key Enter or Return pressed")
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QLineEdit, QMessageBox


# class QtBoxFuncLineEdit1(QLineEdit):
#     def __init__(self):
#         super(QtBoxFuncLineEdit1, self).__init__()
#         self.setFixedSize(150, 30)
#         self.setPlaceholderText("press Enter or Return")

#     def keyPressEvent(self, event):
#         super(QtBoxFuncLineEdit1, self).keyPressEvent(event)
#         if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
#             QMessageBox.information(self, "Qt Box", "Key Enter or Return pressed")
# PySide