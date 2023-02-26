# PyQt
from PyQt5.QtCore import QPointF
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen, QColor
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QWidget = createWidgetMenuBase(QWidget)

class QtBoxFuncWidget2(QWidget):
    def __init__(self):
        super(QtBoxFuncWidget2, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 150)

        self.line_gap = 5
        self.start_x = self.width() / 2
        self.start_y = self.height() / 2

        self.light_pen = QPen(QColor(222, 222, 222))
        self.dark_pen = QPen(QColor(222, 222, 222))
        self.dark_pen.setWidth(2)

    def draw_lines(self, painter):
        painter.setPen(self.dark_pen)

        line_count = 0
        is_row_drawing_stopped = False
        is_col_drawing_stopped = False
        x1, x2 = self.start_x, self.start_x
        y1, y2 = self.start_y, self.start_y
        while True:
            if not is_col_drawing_stopped:
                painter.drawLine(QPointF(x1, 0.0), QPointF(x1, self.height()))
                painter.drawLine(QPointF(x2, 0.0), QPointF(x2, self.height()))

            if not is_row_drawing_stopped:
                painter.drawLine(QPointF(0.0, y1), QPointF(self.width(), y1))
                painter.drawLine(QPointF(0.0, y2), QPointF(self.width(), y2))

            x1 -= self.line_gap
            x2 += self.line_gap
            y1 -= self.line_gap
            y2 += self.line_gap
            if x1 <= 0 or x2 >= self.width():
                is_col_drawing_stopped = True
            if y1 <= 0 or y2 >= self.height():
                is_row_drawing_stopped = True
            if is_row_drawing_stopped and is_col_drawing_stopped:
                break

            line_count += 1
            if line_count % 10 == 0:
                painter.setPen(self.dark_pen)
            else:
                painter.setPen(self.light_pen)

    def paintEvent(self, event):
        super(QtBoxFuncWidget2, self).paintEvent(event)
        painter = QPainter(self)
        self.draw_lines(painter)

    def resizeEvent(self, event):
        super(QtBoxFuncWidget2, self).resizeEvent(event)
        self.start_x = self.width() / 2
        self.start_y = self.height() / 2
        self.update()
# PyQt

# PySide
# from PySide2.QtCore import QPointF
# from PySide2.QtWidgets import QWidget
# from PySide2.QtGui import QPainter, QPen, QColor


# class QtBoxFuncWidget2(QWidget):
#     def __init__(self):
#         super(QtBoxFuncWidget2, self).__init__()
#         self.setFixedSize(150, 150)

#         self.line_gap = 5
#         self.start_x = self.width() / 2
#         self.start_y = self.height() / 2

#         self.light_pen = QPen(QColor(222, 222, 222))
#         self.dark_pen = QPen(QColor(222, 222, 222))
#         self.dark_pen.setWidth(2)

#     def draw_lines(self, painter):
#         painter.setPen(self.dark_pen)

#         line_count = 0
#         is_row_drawing_stopped = False
#         is_col_drawing_stopped = False
#         x1, x2 = self.start_x, self.start_x
#         y1, y2 = self.start_y, self.start_y
#         while True:
#             if not is_col_drawing_stopped:
#                 painter.drawLine(QPointF(x1, 0.0), QPointF(x1, self.height()))
#                 painter.drawLine(QPointF(x2, 0.0), QPointF(x2, self.height()))

#             if not is_row_drawing_stopped:
#                 painter.drawLine(QPointF(0.0, y1), QPointF(self.width(), y1))
#                 painter.drawLine(QPointF(0.0, y2), QPointF(self.width(), y2))

#             x1 -= self.line_gap
#             x2 += self.line_gap
#             y1 -= self.line_gap
#             y2 += self.line_gap
#             if x1 <= 0 or x2 >= self.width():
#                 is_col_drawing_stopped = True
#             if y1 <= 0 or y2 >= self.height():
#                 is_row_drawing_stopped = True
#             if is_row_drawing_stopped and is_col_drawing_stopped:
#                 break

#             line_count += 1
#             if line_count % 10 == 0:
#                 painter.setPen(self.dark_pen)
#             else:
#                 painter.setPen(self.light_pen)

#     def paintEvent(self, event):
#         super(QtBoxFuncWidget2, self).paintEvent(event)
#         painter = QPainter(self)
#         self.draw_lines(painter)

#     def resizeEvent(self, event):
#         super(QtBoxFuncWidget2, self).resizeEvent(event)
#         self.start_x = self.width() / 2
#         self.start_y = self.height() / 2
#         self.update()
# PySide