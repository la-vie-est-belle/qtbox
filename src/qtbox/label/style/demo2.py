# PyQt
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPixmap, QPainter, QBrush
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QLabel = createWidgetMenuBase(QLabel)
PATH_TO_IMG = str(Path(__file__).parent.parent.parent / "res/images/qt.png").replace("\\", "/")

class QtBoxStyleLabel2(QLabel):
    def __init__(self):
        super(QtBoxStyleLabel2, self).__init__(str(Path(__file__)))
        self.setFixedSize(90, 90)
        self.pixmap = QPixmap(PATH_TO_IMG).scaled(self.width(), self.height())

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        brush = QBrush(self.pixmap)
        painter.setBrush(brush)

        points = [
            QPointF(10.0, 80.0),
            QPointF(20.0, 10.0),
            QPointF(80.0, 30.0),
            QPointF(90.0, 70.0)
        ]
        painter.drawConvexPolygon(*points)
# PyQt

# PySide
# from PySide2.QtWidgets import QLabel
# from PySide2.QtCore import Qt, QPointF
# from PySide2.QtGui import QPixmap, QPainter, QBrush


# class QtBoxStyleLabel2(QLabel):
#     def __init__(self):
#         super(QtBoxStyleLabel2, self).__init__()
#         self.setFixedSize(90, 90)
#         self.pixmap = QPixmap(PATH_TO_IMG).scaled(self.width(), self.height())

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setPen(Qt.NoPen)
#         brush = QBrush(self.pixmap)
#         painter.setBrush(brush)

#         points = [
#             QPointF(10.0, 80.0),
#             QPointF(20.0, 10.0),
#             QPointF(80.0, 30.0),
#             QPointF(90.0, 70.0)
#         ]
#         painter.drawConvexPolygon(points)
# PySide