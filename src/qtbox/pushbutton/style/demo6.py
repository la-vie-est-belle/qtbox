# PyQt
from PyQt5.QtWidgets import QPushButton
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QPushButton = createWidgetMenuBase(QPushButton)

class QtBoxStyleButton6(QPushButton):
    def __init__(self):
        super(QtBoxStyleButton6, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 40)
        self.setText("BUTTON")
        self.setStyleSheet("""
        QPushButton {
            background-color: #57bd6a;
            color: #f9ffff;
            font-size: 20px;
            font-weight: bold;
            border-radius: 5px;
        }

        QPushButton:pressed {
            background-color: #4eaa5f;
        }
        """)
# PyQt

# PySide
# from PySide2.QtWidgets import QPushButton


# class QtBoxStyleButton6(QPushButton):
#     def __init__(self):
#         super(QtBoxStyleButton6, self).__init__()
#         self.setFixedSize(150, 40)
#         self.setText("BUTTON")
#         self.setStyleSheet("""
#         QPushButton {
#             background-color: #57bd6a;
#             color: #f9ffff;
#             font-size: 20px;
#             font-weight: bold;
#             border-radius: 5px;
#         }

#         QPushButton:pressed {
#             background-color: #4eaa5f;
#         }
#         """)
# PySide