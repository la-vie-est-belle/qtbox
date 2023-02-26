# PyQt
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPainter, QPen, QColor
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QPushButton = createWidgetMenuBase(QPushButton)

class QtBoxStyleButton8(QPushButton):
    def __init__(self):
        super(QtBoxStyleButton8, self).__init__(str(Path(__file__)))
        self.btn_state = "on"
        self.setFixedSize(80, 40)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        pen = QPen(Qt.NoPen)
        painter.setPen(pen)

        if self.btn_state == "on":
            painter.setBrush(QColor("#60ca5b"))
            rect = QRectF(0, 0, self.width(), self.height())
            painter.drawRoundedRect(rect, self.height()/2, self.height()/2)

            painter.setBrush(Qt.white)
            rect = QRectF(self.width()/2-5, 5, self.width()/2, self.height()-5*2)
            painter.drawRoundedRect(rect, (self.height()-5*2)/2, (self.height()-5*2)/2)

        else:
            painter.setBrush(QColor("#dcdcdc"))
            rect = QRectF(0, 0, self.width(), self.height())
            painter.drawRoundedRect(rect, self.height()/2, self.height()/2)

            painter.setBrush(Qt.white)
            rect = QRectF(5, 5, self.width()/2, self.height()-5*2)
            painter.drawRoundedRect(rect, (self.height()-5*2)/2, (self.height()-5*2)/2)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.btn_state == "on":
                self.btn_state = "off"
            else:
                self.btn_state = "on"
# PyQt

# PySide
# from PySide2.QtCore import Qt, QRectF
# from PySide2.QtWidgets import QPushButton
# from PySide2.QtGui import QPainter, QPen, QColor


# class QtBoxStyleButton8(QPushButton):
#     def __init__(self):
#         super(QtBoxStyleButton8, self).__init__()
#         self.btn_state = "on"
#         self.setFixedSize(80, 40)

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.Antialiasing)
#         pen = QPen(Qt.NoPen)
#         painter.setPen(pen)

#         if self.btn_state == "on":
#             painter.setBrush(QColor("#60ca5b"))
#             rect = QRectF(0, 0, self.width(), self.height())
#             painter.drawRoundedRect(rect, self.height()/2, self.height()/2)

#             painter.setBrush(Qt.white)
#             rect = QRectF(self.width()/2-5, 5, self.width()/2, self.height()-5*2)
#             painter.drawRoundedRect(rect, (self.height()-5*2)/2, (self.height()-5*2)/2)

#         else:
#             painter.setBrush(QColor("#dcdcdc"))
#             rect = QRectF(0, 0, self.width(), self.height())
#             painter.drawRoundedRect(rect, self.height()/2, self.height()/2)

#             painter.setBrush(Qt.white)
#             rect = QRectF(5, 5, self.width()/2, self.height()-5*2)
#             painter.drawRoundedRect(rect, (self.height()-5*2)/2, (self.height()-5*2)/2)

#     def mousePressEvent(self, event):
#         if event.button() == Qt.LeftButton:
#             if self.btn_state == "on":
#                 self.btn_state = "off"
#             else:
#                 self.btn_state = "on"
# PySide