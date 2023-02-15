# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QGraphicsDropShadowEffect
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QPushButton = createWidgetMenuBase(QPushButton)

class QtBoxStyleButton9(QPushButton):
    def __init__(self):
        super(QtBoxStyleButton9, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 40)
        self.setText("BUTTON")
        self.add_shadow()

    def add_shadow(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setOffset(3, 3)
        shadow.setColor(Qt.gray)
        self.setGraphicsEffect(shadow)
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QPushButton, QGraphicsDropShadowEffect


# class QtBoxStyleButton9(QPushButton):
#     def __init__(self):
#         super(QtBoxStyleButton9, self).__init__()
#         self.setFixedSize(150, 40)
#         self.setText("BUTTON")
#         self.add_shadow()

#     def add_shadow(self):
#         shadow = QGraphicsDropShadowEffect(self)
#         shadow.setBlurRadius(15)
#         shadow.setOffset(3, 3)
#         shadow.setColor(Qt.gray)
#         self.setGraphicsEffect(shadow)
# PySide