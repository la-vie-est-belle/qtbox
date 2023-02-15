# PyQt
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QLabel
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QLabel = createWidgetMenuBase(QLabel)

class QtBoxFuncLabel3(QLabel):
    def __init__(self):
        super(QtBoxFuncLabel3, self).__init__(str(Path(__file__)))
        self.text = ""
        self.count = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_text)
        self.type_text("Typewriter effect")

    def type_text(self, text):
        self.text = text
        self.count = 0
        self.timer.stop()
        self.timer.start(500)

    def update_text(self):
        self.count += 1
        self.setText(self.text[0:self.count])

        if self.count >= len(self.text):
            self.count = 0
            self.timer.stop()
# PyQt

# PySide
# from PySide2.QtCore import QTimer
# from PySide2.QtWidgets import QLabel


# class QtBoxFuncLabel3(QLabel):
#     def __init__(self):
#         super(QtBoxFuncLabel3, self).__init__()
#         self.text = ""
#         self.count = 0
#         self.timer = QTimer()
#         self.timer.timeout.connect(self.update_text)
#         self.type_text("Typewriter effect")

#     def type_text(self, text):
#         self.text = text
#         self.count = 0
#         self.timer.stop()
#         self.timer.start(500)

#     def update_text(self):
#         self.count += 1
#         self.setText(self.text[0:self.count])
#
#         if self.count >= len(self.text):
#             self.count = 0
#             self.timer.stop()
# PySide