# PyQt
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPainter, QPen, QColor, QFont
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QPushButton = createWidgetMenuBase(QPushButton)

class QtBoxStyleButton11(QPushButton):
    def __init__(self):
        super(QtBoxStyleButton11, self).__init__(str(Path(__file__)))
        self.btn_state = "off"
        self.setFixedSize(90, 90)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        if self.btn_state == "on":
            font_size = 15
            shadow_color = "#b0b0b0"
            white_part_color = "#eeeeee"
        else:
            font_size = 16
            shadow_color = "#d0d0d0"
            white_part_color = "#fcfcfc"

        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(shadow_color))
        btn_shadow_part_rect = self.rect()
        painter.drawRoundedRect(btn_shadow_part_rect, 5, 5)

        offset = 20
        btn_white_part_rect = QRectF(self.rect().left()+offset/2, self.rect().top()+offset/4, self.rect().width()-offset, self.rect().height()-offset)
        painter.setBrush(QColor(white_part_color))
        painter.drawRoundedRect(btn_white_part_rect, 5, 5)

        pen = QPen(Qt.SolidLine)
        pen.setColor(Qt.black)
        painter.setPen(pen)

        font = QFont()
        font.setBold(True)
        font.setPixelSize(font_size)
        painter.setFont(font)
        painter.drawText(int(btn_white_part_rect.x()+2), int(btn_white_part_rect.y()+font_size), "BTN")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setFixedSize(86, 86)
            self.btn_state = "on"
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setFixedSize(90, 90)
            self.btn_state = "off"
            self.update()
# PyQt

# PySide
# from PySide2.QtCore import Qt, QRectF
# from PySide2.QtWidgets import QPushButton
# from PySide2.QtGui import QPainter, QPen, QColor, QFont


# class QtBoxStyleButton11(QPushButton):
#     def __init__(self):
#         super(QtBoxStyleButton11, self).__init__()
#         self.btn_state = "off"
#         self.setFixedSize(90, 90)

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.Antialiasing)

#         if self.btn_state == "on":
#             font_size = 15
#             shadow_color = "#b0b0b0"
#             white_part_color = "#eeeeee"
#         else:
#             font_size = 16
#             shadow_color = "#d0d0d0"
#             white_part_color = "#fcfcfc"

#         painter.setPen(Qt.NoPen)
#         painter.setBrush(QColor(shadow_color))
#         btn_shadow_part_rect = self.rect()
#         painter.drawRoundedRect(btn_shadow_part_rect, 5, 5)

#         offset = 20
#         btn_white_part_rect = QRectF(self.rect().left()+offset/2, self.rect().top()+offset/4, self.rect().width()-offset, self.rect().height()-offset)
#         painter.setBrush(QColor(white_part_color))
#         painter.drawRoundedRect(btn_white_part_rect, 5, 5)

#         pen = QPen(Qt.SolidLine)
#         pen.setColor(Qt.black)
#         painter.setPen(pen)

#         font = QFont()
#         font.setBold(True)
#         font.setPixelSize(font_size)
#         painter.setFont(font)
#         painter.drawText(int(btn_white_part_rect.x()+2), int(btn_white_part_rect.y()+font_size), "BTN")

#     def mousePressEvent(self, event):
#         if event.button() == Qt.LeftButton:
#             self.setFixedSize(86, 86)
#             self.btn_state = "on"
#             self.update()

#     def mouseReleaseEvent(self, event):
#         if event.button() == Qt.LeftButton:
#             self.setFixedSize(90, 90)
#             self.btn_state = "off"
#             self.update()
# PySide