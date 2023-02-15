# PyQt
from PyQt5.QtWidgets import QPushButton
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QPushButton = createWidgetMenuBase(QPushButton)

class QtBoxStyleButton2(QPushButton):
    def __init__(self):
        super(QtBoxStyleButton2, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 50)
        self.setText("BUTTON")
        self.setStyleSheet("""
        QPushButton {
            background-color: qlineargradient(x1:0, y1:0.5, x2:1, y2:0.5, stop:0 #47a7ed, stop: 1 #a967b2);
            color: white;
            font-size: 20px;
            font-weight: bold;
            border-radius: 25px;
        }
        
        QPushButton:hover {
            background-color: qlineargradient(x1:0, y1:0.5, x2:1, y2:0.5, stop:0 #459ee0, stop: 1 #995da1);
        }
        
        QPushButton:pressed {
               background-color: qlineargradient(x1:0, y1:0.5, x2:1, y2:0.5, stop:0 #4093d1, stop: 1 #87538e);
        }
        """)
# PyQt

# PySide
# from PySide2.QtWidgets import QPushButton


# class QtBoxStyleButton2(QPushButton):
#     def __init__(self):
#         super(QtBoxStyleButton2, self).__init__()
#         self.setFixedSize(150, 50)
#         self.setText("BUTTON")
#         self.setStyleSheet("""
#         QPushButton {
#             background-color: qlineargradient(x1:0, y1:0.5, x2:1, y2:0.5, stop:0 #47a7ed, stop: 1 #a967b2);
#             color: white;
#             font-size: 20px;
#             font-weight: bold;
#             border-radius: 25px;
#         }

#         QPushButton:hover {
#             background-color: qlineargradient(x1:0, y1:0.5, x2:1, y2:0.5, stop:0 #459ee0, stop: 1 #995da1);
#         }

#         QPushButton:pressed {
#                background-color: qlineargradient(x1:0, y1:0.5, x2:1, y2:0.5, stop:0 #4093d1, stop: 1 #87538e);
#         }
#         """)
# PySide