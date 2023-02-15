# PyQt
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QLabel
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QLabel = createWidgetMenuBase(QLabel)

class QtBoxStyleLabel4(QLabel):
    def __init__(self):
        super(QtBoxStyleLabel4, self).__init__(str(Path(__file__)))
        self.setText("Change text color")
        self.color_list = ["rgb(255, 0, 0)", "rgb(255, 165, 0)", "rgb(255, 255, 0)",
                           "rgb(0, 255, 0)", "rgb(0, 127, 255)", "rgb(0, 0, 255)",
                           "rgb(139, 0, 255)"]

        self.count = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.change_color)
        self.timer.start(100)

    def change_color(self):
        color = self.color_list[self.count]
        self.setStyleSheet(f"""
        color: {color}
        """)

        self.count += 1
        if self.count >= len(self.color_list):
            self.count = 0
# PyQt

# PySide
# from PySide2.QtCore import QTimer
# from PySide2.QtWidgets import QLabel


# class QtBoxStyleLabel4(QLabel):
#     def __init__(self):
#         super(QtBoxStyleLabel4, self).__init__()
#         self.setText("Change text color")
#         self.color_list = ["rgb(255, 0, 0)", "rgb(255, 165, 0)", "rgb(255, 255, 0)",
#                            "rgb(0, 255, 0)", "rgb(0, 127, 255)", "rgb(0, 0, 255)",
#                            "rgb(139, 0, 255)"]

#         self.count = 0
#         self.timer = QTimer()
#         self.timer.timeout.connect(self.change_color)
#         self.timer.start(100)

#     def change_color(self):
#         color = self.color_list[self.count]
#         self.setStyleSheet(f"""
#         color: {color}
#         """)

#         self.count += 1
#         if self.count >= len(self.color_list):
#             self.count = 0
# PySide