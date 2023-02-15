# PyQt
from PyQt5.QtGui import QRegExpValidator, QValidator
from PyQt5.QtWidgets import QLineEdit, QMessageBox
from PyQt5.QtCore import QRegExp, Qt
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QLineEdit = createWidgetMenuBase(QLineEdit)

class QtBoxFuncLineEdit3(QLineEdit):
    def __init__(self):
        super(QtBoxFuncLineEdit3, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 30)
        self.setPlaceholderText("example@email.com")

        reg_exp = QRegExp("[a-zA-Z0-9-_]+@([a-z0-9A-Z]+(-[a-z0-9A-Z]+)?\\.)+[a-z]{2,}$")
        self.setValidator(QRegExpValidator(reg_exp))

    def validate_email(self):
        if self.validator().validate(self.text(), 0)[0] == QValidator.Acceptable:
            QMessageBox.information(self, "Qt Box", "Correct email format")
        else:
            QMessageBox.information(self, "Qt Box", "Wrong email format")

    def keyPressEvent(self, event):
        super(QtBoxFuncLineEdit3, self).keyPressEvent(event)
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.validate_email()
# PyQt

# PySide
# from PySide2.QtGui import QRegExpValidator, QValidator
# from PySide2.QtWidgets import QLineEdit, QMessageBox
# from PySide2.QtCore import QRegExp, Qt


# class QtBoxFuncLineEdit3(QLineEdit):
#     def __init__(self):
#         super(QtBoxFuncLineEdit3, self).__init__()
#         self.setFixedSize(150, 30)
#         self.setPlaceholderText("example@email.com")

#         reg_exp = QRegExp("[a-zA-Z0-9-_]+@([a-z0-9A-Z]+(-[a-z0-9A-Z]+)?\\.)+[a-z]{2,}$")
#         self.setValidator(QRegExpValidator(reg_exp))

#     def validate_email(self):
#         if self.validator().validate(self.text(), 0)[0] == QValidator.Acceptable:
#             QMessageBox.information(self, "Qt Box", "Correct email format")
#         else:
#             QMessageBox.information(self, "Qt Box", "Wrong email format")

#     def keyPressEvent(self, event):
#         super(QtBoxFuncLineEdit3, self).keyPressEvent(event)
#         if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
#             self.validate_email()
# PySide