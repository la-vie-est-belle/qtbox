# PyQt
from PyQt5.QtWidgets import QPushButton
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QPushButton = createWidgetMenuBase(QPushButton)

class QtBoxStyleButton1(QPushButton):
    def __init__(self):
        super(QtBoxStyleButton1, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 50)
        self.setText("BUTTON")
        self.setStyleSheet("""
        QPushButton {
            background-color: qlineargradient(x1:1, y1:0, x2:1, y2:0.3, stop:0 #8a9195, stop:1 black);
            color: white;
            font-size: 20px;
            font-weight: bold;
            border-radius: 25px;
        }

        QPushButton:hover {
            background-color: qlineargradient(x1:1, y1:0, x2:1, y2:0.3, stop:0 #7d8488, stop:1 black);
        }

        QPushButton:pressed {
            background-color: qlineargradient(x1:1, y1:0, x2:1, y2:0.3, stop:0 #6a7073, stop:1 black);
        }
        """)
# PyQt

# PySide
# from PySide2.QtWidgets import QPushButton


# class QtBoxStyleButton1(QPushButton):
#     def __init__(self):
#         super(QtBoxStyleButton1, self).__init__()
#         self.setFixedSize(150, 50)
#         self.setText("BUTTON")
#         self.setStyleSheet("""
#         QPushButton {
#             background-color: qlineargradient(x1:1, y1:0, x2:1, y2:0.3, stop:0 #8a9195, stop:1 black);
#             color: white;
#             font-size: 20px;
#             font-weight: bold;
#             border-radius: 25px;
#         }

#         QPushButton:hover {
#             background-color: qlineargradient(x1:1, y1:0, x2:1, y2:0.3, stop:0 #7d8488, stop:1 black);
#         }

#         QPushButton:pressed {
#             background-color: qlineargradient(x1:1, y1:0, x2:1, y2:0.3, stop:0 #6a7073, stop:1 black);
#         }
#         """)
# PySide