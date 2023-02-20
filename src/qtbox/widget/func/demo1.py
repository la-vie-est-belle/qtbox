# PyQt
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QPen, QPalette, QColor
from PyQt5.QtWidgets import QWidget
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QWidget = createWidgetMenuBase(QWidget)

class QtBoxFuncWidget1(QWidget):
    def __init__(self):
        super(QtBoxFuncWidget1, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 150)
        self.rect_list = []
        self.rect_start_point = None
        self.rect_end_point = None
        self.set_background_color()

    def set_background_color(self):
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(100, 100, 100, 255))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.rect_start_point = event.pos()
            self.rect_end_point = event.pos()
            self.update()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.rect_end_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if self.rect_start_point and self.rect_end_point:
            self.rect_list.append((self.rect_start_point, self.rect_end_point))
            self.update()

        self.rect_start_point = None
        self.rect_end_point = None

    def paintEvent(self, event):
        super(QtBoxFuncWidget1, self).paintEvent(event)
        painter = QPainter(self)
        pen = QPen(Qt.SolidLine)
        pen.setColor(Qt.green)
        painter.setPen(pen)

        if self.rect_start_point and self.rect_end_point:
            painter.drawText(self.rect_start_point, f"Rect {len(self.rect_list) + 1}")
            rect = QRect(self.rect_start_point, self.rect_end_point)
            painter.drawRect(rect)

        for i, point_tuple in enumerate(self.rect_list):
            painter.drawText(point_tuple[0], f"Rect {i + 1}")
            rect = QRect(point_tuple[0], point_tuple[1])
            painter.drawRect(rect)
# PyQt

# PySide
# from PySide2.QtCore import Qt, QRect
# from PySide2.QtGui import QPainter, QPen, QPalette, QColor
# from PySide2.QtWidgets import QWidget


# class QtBoxFuncWidget1(QWidget):
#     def __init__(self):
#         super(QtBoxFuncWidget1, self).__init__()
#         self.setFixedSize(150, 150)
#         self.rect_list = []
#         self.rect_start_point = None
#         self.rect_end_point = None
#         self.set_background_color()

#     def set_background_color(self):
#         palette = QPalette()
#         palette.setColor(QPalette.Background, QColor(100, 100, 100, 255))
#         self.setPalette(palette)
#         self.setAutoFillBackground(True)

#     def mousePressEvent(self, event):
#         if event.button() == Qt.LeftButton:
#             self.rect_start_point = event.pos()
#             self.rect_end_point = event.pos()
#             self.update()

#     def mouseMoveEvent(self, event):
#         if event.buttons() == Qt.LeftButton:
#             self.rect_end_point = event.pos()
#             self.update()

#     def mouseReleaseEvent(self, event):
#         if self.rect_start_point and self.rect_end_point:
#             self.rect_list.append((self.rect_start_point, self.rect_end_point))
#             self.update()

#         self.rect_start_point = None
#         self.rect_end_point = None

#     def paintEvent(self, event):
#         super(QtBoxFuncWidget1, self).paintEvent(event)
#         painter = QPainter(self)
#         pen = QPen(Qt.SolidLine)
#         pen.setColor(Qt.green)
#         painter.setPen(pen)

#         if self.rect_start_point and self.rect_end_point:
#             painter.drawText(self.rect_start_point, f"Rect {len(self.rect_list) + 1}")
#             rect = QRect(self.rect_start_point, self.rect_end_point)
#             painter.drawRect(rect)

#         for i, point_tuple in enumerate(self.rect_list):
#             painter.drawText(point_tuple[0], f"Rect {i + 1}")
#             rect = QRect(point_tuple[0], point_tuple[1])
#             painter.drawRect(rect)
# PySide