# PyQt
from PyQt5.QtWidgets import QPushButton
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QPushButton = createWidgetMenuBase(QPushButton)

class QtBoxStyleButton3(QPushButton):
    def __init__(self):
        super(QtBoxStyleButton3, self).__init__(str(Path(__file__)))
        self.setFixedSize(90, 90)
        self.setText("BTN")
        self.setStyleSheet("""
        QPushButton {
            background-color: qlineargradient(x1:1, y1:0, x2:1, y2:1, stop:0 #454b4f, stop: 1 #1d2225);
            color: white;
            border-radius: 45px;
            font-size: 18px;
            font-weight: bold;
            border: 10px solid #f9f9f9;
        }
        
        QPushButton:hover {
            border: 10px solid white;
            background-color: qlineargradient(x1:1, y1:0, x2:1, y2:1, stop:0 #35393c, stop: 1 #101214);
        }
        
        QPushButton:pressed {
            color: black;
            border: 10px solid black;
            background-color: white;
        }
        """)
# PyQt

# PySide
# from PySide2.QtWidgets import QPushButton


# class QtBoxStyleButton3(QPushButton):
#     def __init__(self):
#         super(QtBoxStyleButton3, self).__init__()
#         self.setFixedSize(90, 90)
#         self.setText("BTN")
#         self.setStyleSheet("""
#         QPushButton {
#             background-color: qlineargradient(x1:1, y1:0, x2:1, y2:1, stop:0 #454b4f, stop: 1 #1d2225);
#             color: white;
#             border-radius: 45px;
#             font-size: 18px;
#             font-weight: bold;
#             border: 10px solid #f9f9f9;
#         }

#         QPushButton:hover {
#             border: 10px solid white;
#             background-color: qlineargradient(x1:1, y1:0, x2:1, y2:1, stop:0 #35393c, stop: 1 #101214);
#         }

#         QPushButton:pressed {
#             color: black;
#             border: 10px solid black;
#             background-color: white;
#         }
#         """)
# PySide