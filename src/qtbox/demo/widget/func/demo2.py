# PyQt
from PyQt5.QtCore import QPointF
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen, QColor
from qtbox.gui.menu import createWidgetMenuBase
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

# C++/Qt
# #ifndef QTBOXFUNCWIDGET2_H
# #define QTBOXFUNCWIDGET2_H
# #include <QResizeEvent>
# #include <QPaintEvent>
# #include <QPainter>
# #include <QWidget>
# #include <QColor>
# #include <QPen>

# class QtBoxFuncWidget2 : public QWidget
# {
#     Q_OBJECT

# public:
#     QtBoxFuncWidget2(QWidget *parent = nullptr);

# protected:
#     void paintEvent(QPaintEvent *event);
#     void resizeEvent(QResizeEvent *evnet);

# private:
#     int lineGap = 5;
#     float startX;
#     float startY;
#     QPen lightPen = QPen(QColor(222, 222, 222));
#     QPen darkPen = QPen(QColor(222, 222, 222));
#     void drawLines(QPainter &painter);
# };
# #endif // QTBOXFUNCWIDGET2_H



# #include "qtboxfuncwidget2.h"
# #include <QPainter>
# #include <QPointF>

# QtBoxFuncWidget2::QtBoxFuncWidget2(QWidget *parent)
#     : QWidget(parent)
# {
#     setFixedSize(150, 150);
#     startX = width() / 2.0;
#     startY = height() / 2.0;
#     darkPen.setWidth(2);
# }

# void QtBoxFuncWidget2::drawLines(QPainter &painter)
# {
#     painter.setPen(darkPen);

#     int lineCount = 0;
#     bool isRowDrawingStopped = false;
#     bool isColDrawingStopped = false;
#     float x1 = startX;
#     float x2 = startX;
#     float y1 = startY;
#     float y2 = startY;

#     while (true){
#         if (!isColDrawingStopped) {
#             painter.drawLine(QPointF(x1, 0.0), QPointF(x1, height()));
#             painter.drawLine(QPointF(x2, 0.0), QPointF(x2, height()));
#         }

#         if (!isRowDrawingStopped) {
#             painter.drawLine(QPointF(0.0, y1), QPointF(width(), y1));
#             painter.drawLine(QPointF(0.0, y2), QPointF(width(), y2));
#         }

#         x1 -= lineGap;
#         x2 += lineGap;
#         y1 -= lineGap;
#         y2 += lineGap;
#         if (x1 <= 0 || x2 >= width()){
#             isColDrawingStopped = true;
#         }
#         if (y1 <= 0 || y2 >= height()){
#             isRowDrawingStopped = true;
#         }
#         if (isRowDrawingStopped && isColDrawingStopped) {
#             break;
#         }

#         lineCount += 1;
#         if (lineCount % 10 == 0){
#             painter.setPen(darkPen);
#         }
#         else {
#             painter.setPen(lightPen);
#         }
#     }
# }

# void QtBoxFuncWidget2::paintEvent(QPaintEvent *event)
# {
#     QWidget::paintEvent(event);
#     QPainter painter = QPainter(this);
#     drawLines(painter);
# }

# void QtBoxFuncWidget2::resizeEvent(QResizeEvent *event)
# {
#     QWidget::resizeEvent(event);
#     startX = width() / 2.0;
#     startY = height() / 2.0;
#     update();
# }
# C++/Qt