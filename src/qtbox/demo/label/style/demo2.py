# PyQt
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPixmap, QPainter, QBrush
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QLabel = createWidgetMenuBase(QLabel)
PATH_TO_IMG = str(Path(__file__).parent.parent.parent.parent / "res/images/qt.png").replace("\\", "/")

class QtBoxStyleLabel2(QLabel):
    def __init__(self):
        super(QtBoxStyleLabel2, self).__init__(str(Path(__file__)))
        self.setFixedSize(90, 90)
        self.pixmap = QPixmap(PATH_TO_IMG).scaled(self.width(), self.height())

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
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
#         painter.setRenderHint(QPainter.Antialiasing)
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

# C++/Qt
# #ifndef QTBOXSTYLELABEL2_H
# #define QTBOXSTYLELABEL2_H
# #include <QLabel>
# #include <QPixmap>
# #include <QPaintEvent>

# class QtBoxStyleLabel2 : public QLabel
# {
#     Q_OBJECT

# public:
#     QtBoxStyleLabel2(QWidget *parent = nullptr);

# protected:
#     void paintEvent(QPaintEvent *event);

# private:
#     QPixmap pixmap;
# };
# #endif // QTBOXSTYLELABEL2_H



# #include "qtboxstylelabel2.h"
# #include <QPainter>
# #include <Qt>
# #include <QBrush>
# #include <QPointF>

# QtBoxStyleLabel2::QtBoxStyleLabel2(QWidget *parent)
#     : QLabel(parent)
# {
#     setFixedSize(90, 90);
#     pixmap = QPixmap(":res/images/qt.png").scaled(width(), height());
# }

# void QtBoxStyleLabel2::paintEvent(QPaintEvent *event)
# {
#     QPainter painter(this);
#     painter.setRenderHint(QPainter::Antialiasing);
#     painter.setPen(Qt::NoPen);
#     QBrush brush = QBrush(pixmap);
#     painter.setBrush(brush);

#     QPointF points[4] = {
#         QPointF(10.0, 80.0),
#         QPointF(20.0, 10.0),
#         QPointF(80.0, 30.0),
#         QPointF(90.0, 70.0)
#     };
#     painter.drawPolygon(points, 4);
# }
# C++/Qt