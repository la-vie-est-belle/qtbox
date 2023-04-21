# PyQt
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QPen, QPalette, QColor
from PyQt5.QtWidgets import QWidget
from qtbox.gui.menu import createWidgetMenuBase
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
        palette.setColor(QPalette.Window, QColor(100, 100, 100, 255))
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
        pen = QPen()
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
#         palette.setColor(QPalette.Window, QColor(100, 100, 100, 255))
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
#         pen = QPen()
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

# C++/Qt
# #ifndef QTBOXFUNCWIDGET1_H
# #define QTBOXFUNCWIDGET1_H
# #include <QMouseEvent>
# #include <QPaintEvent>
# #include <QWidget>
# #include <QPoint>
# #include <QList>

# class QtBoxFuncWidget1 : public QWidget
# {
#     Q_OBJECT

# public:
#     QtBoxFuncWidget1(QWidget *parent = nullptr);

# protected:
#     void mousePressEvent(QMouseEvent *event);
#     void mouseMoveEvent(QMouseEvent *event);
#     void mouseReleaseEvent(QMouseEvent *event);
#     void paintEvent(QPaintEvent *event);

# private:
#     QList<QPoint*> rectList;
#     QPoint rectStartPoint;
#     QPoint rectEndPoint;
#     void setBackgroundColor();
# };
# #endif // QTBOXFUNCWIDGET1_H



# #include "qtboxfuncwidget1.h"
# #include <QPalette>
# #include <QPainter>
# #include <QRect>
# #include <QPen>
# #include <Qt>

# QtBoxFuncWidget1::QtBoxFuncWidget1(QWidget *parent)
#     : QWidget(parent)
# {
#     setFixedSize(150, 150);
#     setBackgroundColor();
# }

# void QtBoxFuncWidget1::setBackgroundColor()
# {
#     QPalette palette = QPalette();
#     palette.setColor(QPalette::Window, QColor(100, 100, 100, 255));
#     setPalette(palette);
#     setAutoFillBackground(true);
# }

# void QtBoxFuncWidget1::mousePressEvent(QMouseEvent *event)
# {
#     if (event->button() == Qt::LeftButton) {
#         rectStartPoint = event->pos();
#         rectEndPoint = event->pos();
#         update();
#     }
# }

# void QtBoxFuncWidget1::mouseMoveEvent(QMouseEvent *event)
# {
#     if (event->buttons() == Qt::LeftButton) {
#         rectEndPoint = event->pos();
#         update();
#     }
# }

# void QtBoxFuncWidget1::mouseReleaseEvent(QMouseEvent *event)
# {
#     if (!rectStartPoint.isNull() && !rectEndPoint.isNull()) {
#         QPoint *pointArray = new QPoint[2];
#         pointArray[0] = rectStartPoint;
#         pointArray[1] = rectEndPoint;
#         rectList.append(pointArray);
#         update();
#     }
#     rectStartPoint = QPoint();
#     rectEndPoint = QPoint();
# }

# void QtBoxFuncWidget1::paintEvent(QPaintEvent *event)
# {
#     QWidget::paintEvent(event);
#     QPainter painter = QPainter(this);
#     QPen pen = QPen();
#     pen.setColor(Qt::green);
#     painter.setPen(pen);

#     if (!rectStartPoint.isNull() && !rectEndPoint.isNull()) {
#         painter.drawText(rectStartPoint, QString("Rect %1").arg(rectList.length()+1));
#         QRect rect = QRect(rectStartPoint, rectEndPoint);
#         painter.drawRect(rect);
#     }

#     for (int i=0; i<rectList.length(); i++){
#         painter.drawText(rectList[i][0], QString("Rect %1").arg(i+1));
#         QRect rect = QRect(rectList[i][0], rectList[i][1]);
#         painter.drawRect(rect);
#     }
# }
# C++/Qt