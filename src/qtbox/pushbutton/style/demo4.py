# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPainter, QPen, QColor, QPainterPath, QFont, QFontMetricsF
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QPushButton = createWidgetMenuBase(QPushButton)

class QtBoxStyleButton4(QPushButton):
    def __init__(self):
        super(QtBoxStyleButton4, self).__init__(str(Path(__file__)))
        self.btn_state = "normal"
        self.setFixedSize(90, 90)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.setStyleSheet("""
        QPushButton {
            font-size: 20px;;
            font-weight: bold;
        }
        """)

    def paintEvent(self, event):
        painter = QPainter(self)

        if self.btn_state == "normal":
            painter.setBrush(QColor("#3b3f42"))
            pen = QPen(Qt.SolidLine)
            pen.setColor(Qt.white)
            pen .setWidth(3)
            painter.setPen(pen)

        elif self.btn_state == "hover":
            painter.setBrush(Qt.black)
            pen = QPen(Qt.SolidLine)
            pen.setColor(Qt.white)
            pen.setWidth(3)
            painter.setPen(pen)

        elif self.btn_state == "press":
            painter.setBrush(Qt.white)
            pen = QPen(Qt.SolidLine)
            pen.setColor(Qt.black)
            pen.setWidth(3)
            painter.setPen(pen)

        path = QPainterPath()
        path.moveTo(self.rect().left()+self.rect().width()/2, self.rect().top())
        path.lineTo(self.rect().bottomLeft())
        path.lineTo(self.rect().bottomRight())
        path.lineTo(self.rect().left()+self.rect().width()/2, self.rect().top())
        painter.drawPath(path)

        font = QFont()
        font.setBold(True)
        font.setPixelSize(20)
        painter.setFont(font)
        font_metrics = QFontMetricsF(font)
        text_width = font_metrics.width("BTN")
        painter.drawText(int(self.rect().width()/2-text_width/2), int(self.rect().height()/2+20), "BTN")

    def mousePressEvent(self, event):
        self.btn_state = "press"
        self.update()

    def mouseReleaseEvent(self, event):
        self.btn_state = "hover"
        self.update()

    def enterEvent(self, event):
        self.btn_state = "hover"
        self.update()

    def leaveEvent(self, event):
        self.btn_state = "normal"
        self.update()
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QPushButton
# from PySide2.QtGui import QPainter, QPen, QColor, QPainterPath, QFont, QFontMetricsF


# class QtBoxStyleButton4(QPushButton):
#     def __init__(self):
#         super(QtBoxStyleButton4, self).__init__()
#         self.btn_state = "normal"
#         self.setFixedSize(90, 90)
#         self.setAttribute(Qt.WA_TranslucentBackground)

#         self.setStyleSheet("""
#         QPushButton {
#             font-size: 20px;;
#             font-weight: bold;
#         }
#         """)

#     def paintEvent(self, event):
#         painter = QPainter(self)

#         if self.btn_state == "normal":
#             painter.setBrush(QColor("#3b3f42"))
#             pen = QPen(Qt.SolidLine)
#             pen.setColor(Qt.white)
#             pen .setWidth(3)
#             painter.setPen(pen)

#         elif self.btn_state == "hover":
#             painter.setBrush(Qt.black)
#             pen = QPen(Qt.SolidLine)
#             pen.setColor(Qt.white)
#             pen.setWidth(3)
#             painter.setPen(pen)

#         elif self.btn_state == "press":
#             painter.setBrush(Qt.white)
#             pen = QPen(Qt.SolidLine)
#             pen.setColor(Qt.black)
#             pen.setWidth(3)
#             painter.setPen(pen)

#         path = QPainterPath()
#         path.moveTo(self.rect().left()+self.rect().width()/2, self.rect().top())
#         path.lineTo(self.rect().bottomLeft())
#         path.lineTo(self.rect().bottomRight())
#         path.lineTo(self.rect().left()+self.rect().width()/2, self.rect().top())
#         painter.drawPath(path)

#         font = QFont()
#         font.setBold(True)
#         font.setPixelSize(20)
#         painter.setFont(font)
#         font_metrics = QFontMetricsF(font)
#         text_width = font_metrics.width("BTN")
#         painter.drawText(int(self.rect().width()/2-text_width/2), int(self.rect().height()/2+20), "BTN")

#     def mousePressEvent(self, event):
#         self.btn_state = "press"
#         self.update()

#     def mouseReleaseEvent(self, event):
#         self.btn_state = "hover"
#         self.update()

#     def enterEvent(self, event):
#         self.btn_state = "hover"
#         self.update()

#     def leaveEvent(self, event):
#         self.btn_state = "normal"
#         self.update()
# PySide