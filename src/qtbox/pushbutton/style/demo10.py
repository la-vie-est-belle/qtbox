# PyQt
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPainter, QPen, QColor, QLinearGradient, QFont, QFontMetricsF
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QPushButton = createWidgetMenuBase(QPushButton)

class QtBoxStyleButton10(QPushButton):
    def __init__(self):
        super(QtBoxStyleButton10, self).__init__(str(Path(__file__)))
        self.btn_rect = None
        self.btn_state = "off"
        self.setFixedSize(90, 90)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        if self.btn_state == "on":
            offset = 40
            font_size = 15
        else:
            offset = 30
            font_size = 20

        painter.setPen(Qt.NoPen)
        base_linear_gradient = QLinearGradient(self.rect().topLeft(), self.rect().bottomRight())
        base_linear_gradient.setColorAt(0, QColor("#757575"))
        base_linear_gradient.setColorAt(1, QColor("#616161"))
        painter.setBrush(base_linear_gradient)
        painter.drawEllipse(self.rect())

        self.btn_rect = QRectF(self.rect().left()+offset/2, self.rect().top()+offset/2, self.rect().width()-offset, self.rect().height()-offset)
        btn_linear_gradient = QLinearGradient(self.btn_rect.topLeft(), self.btn_rect.bottomRight())
        btn_linear_gradient.setColorAt(0, QColor("#f17075"))
        btn_linear_gradient.setColorAt(1, QColor("#df5459"))
        painter.setBrush(btn_linear_gradient)
        painter.drawEllipse(self.btn_rect)

        pen = QPen(Qt.SolidLine)
        pen.setColor(Qt.white)
        painter.setPen(pen)

        font = QFont()
        font.setBold(True)
        font.setPixelSize(font_size)
        painter.setFont(font)
        font_metrics = QFontMetricsF(font)
        text_width = font_metrics.width("BTN")
        painter.drawText(int(self.rect().width()/2-text_width/2), int(self.rect().height()/2+5), "BTN")

    def mousePressEvent(self, event):
        if event.button() != Qt.LeftButton or not self.btn_rect.contains(event.pos()):
            return

        self.btn_state = "on"
        self.update()

    def mouseReleaseEvent(self, event):
        self.btn_state = "off"
        self.update()
# PyQt

# PySide
# from PySide2.QtCore import Qt, QRectF
# from PySide2.QtWidgets import QPushButton
# from PySide2.QtGui import QPainter, QPen, QColor, QLinearGradient, QFont, QFontMetricsF


# class QtBoxStyleButton10(QPushButton):
#     def __init__(self):
#         super(QtBoxStyleButton10, self).__init__()
#         self.btn_rect = None
#         self.btn_state = "off"
#         self.setFixedSize(90, 90)

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.Antialiasing)

#         if self.btn_state == "on":
#             offset = 40
#             font_size = 15
#         else:
#             offset = 30
#             font_size = 20

#         painter.setPen(Qt.NoPen)
#         base_linear_gradient = QLinearGradient(self.rect().topLeft(), self.rect().bottomRight())
#         base_linear_gradient.setColorAt(0, QColor("#757575"))
#         base_linear_gradient.setColorAt(1, QColor("#616161"))
#         painter.setBrush(base_linear_gradient)
#         painter.drawEllipse(self.rect())

#         self.btn_rect = QRectF(self.rect().left()+offset/2, self.rect().top()+offset/2, self.rect().width()-offset, self.rect().height()-offset)
#         btn_linear_gradient = QLinearGradient(self.btn_rect.topLeft(), self.btn_rect.bottomRight())
#         btn_linear_gradient.setColorAt(0, QColor("#f17075"))
#         btn_linear_gradient.setColorAt(1, QColor("#df5459"))
#         painter.setBrush(btn_linear_gradient)
#         painter.drawEllipse(self.btn_rect)

#         pen = QPen(Qt.SolidLine)
#         pen.setColor(Qt.white)
#         painter.setPen(pen)

#         font = QFont()
#         font.setBold(True)
#         font.setPixelSize(font_size)
#         painter.setFont(font)
#         font_metrics = QFontMetricsF(font)
#         text_width = font_metrics.width("BTN")
#         painter.drawText(int(self.rect().width()/2-text_width/2), int(self.rect().height()/2+5), "BTN")

#     def mousePressEvent(self, event):
#         if event.button() != Qt.LeftButton or not self.btn_rect.contains(event.pos()):
#             return

#         self.btn_state = "on"
#         self.update()

#     def mouseReleaseEvent(self, event):
#         self.btn_state = "off"
#         self.update()
# PySide