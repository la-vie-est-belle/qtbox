# PyQt
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import QLabel
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QLabel = createWidgetMenuBase(QLabel)

class QtBoxFuncLabel6(QLabel):
    def __init__(self):
        super(QtBoxFuncLabel6, self).__init__(str(Path(__file__)))
        self.update_text()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_text)
        self.timer.start(1000)

    def update_text(self):
        self.setText(QTime.currentTime().toString())
# PyQt

# PySide
# from PySide2.QtCore import QTimer, QTime
# from PySide2.QtWidgets import QLabel


# class QtBoxFuncLabel6(QLabel):
#     def __init__(self):
#         super(QtBoxFuncLabel6, self).__init__(str(Path(__file__)))
#         self.update_text()

#         self.timer = QTimer()
#         self.timer.timeout.connect(self.update_text)
#         self.timer.start(1000)

#     def update_text(self):
#         self.setText(QTime.currentTime().toString())
# PySide