# PyQt
from PyQt5.QtGui import QPainter, QColor, QLinearGradient, QFont, QFontMetricsF, QPen
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtWidgets import QDial
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path
import math

QDial = createWidgetMenuBase(QDial)

class QtBoxStyleDial2(QDial):
    def __init__(self):
        super(QtBoxStyleDial2, self).__init__(str(Path(__file__)))
        self.setFixedSize(100, 100)
        self.setRange(100, 200)
        self.setWrapping(True)
        self.mouse_x = 0
        self.mouse_y = 0
        self.is_first_paint = True

    def mousePressEvent(self, event):
        super(QtBoxStyleDial2, self).mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self.mouse_x = event.x()
            self.mouse_y = event.y()

    def mouseMoveEvent(self, event):
        super(QtBoxStyleDial2, self).mouseMoveEvent(event)
        if event.buttons() == Qt.LeftButton:
            self.mouse_x = event.x()
            self.mouse_y = event.y()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        pen = QPen()
        pen.setColor(Qt.lightGray)
        painter.setPen(pen)

        linear_gradient = QLinearGradient(self.rect().topLeft(), self.rect().bottomRight())
        linear_gradient.setColorAt(0, QColor(Qt.white))
        linear_gradient.setColorAt(1, QColor(Qt.black))
        painter.setBrush(linear_gradient)
        painter.drawEllipse(self.rect())

        if self.is_first_paint:
            self.mouse_x = self.rect().center().x()
            self.mouse_y = self.rect().bottom()
            self.is_first_paint = False

        handle_radius = 10
        painter.setBrush(Qt.white)
        handle_x, handle_y = self.get_handle_pos()
        painter.drawEllipse(QPointF(handle_x, handle_y), handle_radius, handle_radius)

        angle = self.get_angle([handle_x, handle_y])
        self.setValue(round(angle / 360 * (self.maximum() - self.minimum())) + self.minimum())

        font = QFont()
        font.setPixelSize(18)
        painter.setFont(font)
        font_metrics = QFontMetricsF(font)
        text_width = font_metrics.width(str(self.value()))
        painter.drawText(int(self.width() / 2 - text_width / 2), int(self.height() / 2), str(self.value()))

    def get_handle_pos(self):
        center_x = self.rect().center().x()
        center_y = self.rect().center().y()

        if self.mouse_x - center_x == 0 and self.mouse_y - center_y == 0:
            diff_x = center_x
            diff_y = center_y
        else:
            diff_x = self.mouse_x - center_x
            diff_y = self.mouse_y - center_y

        pos_adjust_value = 1.5
        length = math.sqrt(diff_x ** 2 + diff_y ** 2)
        ratio = length / (self.rect().width() / 2) * pos_adjust_value
        handle_x = diff_x / ratio + center_x
        handle_y = diff_y / ratio + center_y
        return handle_x, handle_y

    def get_angle(self, handle_pos):
        """get the angle between handle and the start pos"""
        center_x = self.rect().center().x()
        center_y = self.rect().center().y()
        start_pos = [self.rect().center().x(), self.rect().bottom()]

        vx1 = start_pos[0] - center_x
        vy1 = start_pos[1] - center_y
        vx2 = handle_pos[0] - center_x
        vy2 = handle_pos[1] - center_y
        angle1 = math.atan2(vy1, vx1)
        angle1 = angle1 * 180 / math.pi
        angle2 = math.atan2(vy2, vx2)
        angle2 = angle2 * 180 / math.pi
        if angle2 >= 0:
            diff_angle = angle2 - angle1
            if diff_angle < 0:
                diff_angle = 360 - abs(diff_angle)
        else:
            diff_angle = 180 + angle2 + angle1
        return diff_angle
# PyQt

# PySide
# from PySide2.QtGui import QPainter, QColor, QLinearGradient, QFont, QFontMetricsF, QPen
# from PySide2.QtCore import Qt, QPointF
# from PySide2.QtWidgets import QDial
# import math


# class QtBoxStyleDial2(QDial):
#     def __init__(self):
#         super(QtBoxStyleDial2, self).__init__(str(Path(__file__)))
#         self.setFixedSize(100, 100)
#         self.setRange(100, 200)
#         self.setWrapping(True)
#         self.mouse_x = 0
#         self.mouse_y = 0
#         self.is_first_paint = True

#     def mousePressEvent(self, event):
#         super(QtBoxStyleDial2, self).mousePressEvent(event)
#         if event.button() == Qt.LeftButton:
#             self.mouse_x = event.x()
#             self.mouse_y = event.y()

#     def mouseMoveEvent(self, event):
#         super(QtBoxStyleDial2, self).mouseMoveEvent(event)
#         if event.buttons() == Qt.LeftButton:
#             self.mouse_x = event.x()
#             self.mouse_y = event.y()

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.Antialiasing)
#         pen = QPen()
#         pen.setColor(Qt.lightGray)
#         painter.setPen(pen)

#         linear_gradient = QLinearGradient(self.rect().topLeft(), self.rect().bottomRight())
#         linear_gradient.setColorAt(0, QColor(Qt.white))
#         linear_gradient.setColorAt(1, QColor(Qt.black))
#         painter.setBrush(linear_gradient)
#         painter.drawEllipse(self.rect())

#         if self.is_first_paint:
#             self.mouse_x = self.rect().center().x()
#             self.mouse_y = self.rect().bottom()
#             self.is_first_paint = False

#         handle_radius = 10
#         painter.setBrush(Qt.white)
#         handle_x, handle_y = self.get_handle_pos()
#         painter.drawEllipse(QPointF(handle_x, handle_y), handle_radius, handle_radius)

#         angle = self.get_angle([handle_x, handle_y])
#         self.setValue(round(angle / 360 * (self.maximum() - self.minimum())) + self.minimum())

#         font = QFont()
#         font.setPixelSize(18)
#         painter.setFont(font)
#         font_metrics = QFontMetricsF(font)
#         text_width = font_metrics.width(str(self.value()))
#         painter.drawText(int(self.width() / 2 - text_width / 2), int(self.height() / 2), str(self.value()))

#     def get_handle_pos(self):
#         center_x = self.rect().center().x()
#         center_y = self.rect().center().y()

#         if self.mouse_x - center_x == 0 and self.mouse_y - center_y == 0:
#             diff_x = center_x
#             diff_y = center_y
#         else:
#             diff_x = self.mouse_x - center_x
#             diff_y = self.mouse_y - center_y

#         pos_adjust_value = 1.5
#         length = math.sqrt(diff_x ** 2 + diff_y ** 2)
#         ratio = length / (self.rect().width() / 2) * pos_adjust_value
#         handle_x = diff_x / ratio + center_x
#         handle_y = diff_y / ratio + center_y
#         return handle_x, handle_y

#     def get_angle(self, handle_pos):
#         """get the angle between handle and the start pos"""
#         center_x = self.rect().center().x()
#         center_y = self.rect().center().y()
#         start_pos = [self.rect().center().x(), self.rect().bottom()]

#         vx1 = start_pos[0] - center_x
#         vy1 = start_pos[1] - center_y
#         vx2 = handle_pos[0] - center_x
#         vy2 = handle_pos[1] - center_y
#         angle1 = math.atan2(vy1, vx1)
#         angle1 = angle1 * 180 / math.pi
#         angle2 = math.atan2(vy2, vx2)
#         angle2 = angle2 * 180 / math.pi

#         if angle2 >= 0:
#             diff_angle = angle2 - angle1
#             if diff_angle < 0:
#                 diff_angle = 360 - abs(diff_angle)
#         else:
#             diff_angle = 180 + angle2 + angle1
#         return diff_angle
# PySide

# C++/Qt
# #ifndef QTBOXSTYLEDIAL2_H
# #define QTBOXSTYLEDIAL2_H
# #include <QDial>

# class QtBoxStyleDial2 : public QDial
# {
#     Q_OBJECT

# public:
#     QtBoxStyleDial2(QWidget *parent = nullptr);

# protected:
#     void mousePressEvent(QMouseEvent *event);
#     void mouseMoveEvent(QMouseEvent *event);
#     void paintEvent(QPaintEvent *event);

# private:
#     int mouseX = 0;
#     int mouseY = 0;
#     bool isFirstPaint = true;

#     float* getHandlePos();
#     float getAngle(float *handlePos);
# };
# #endif // QTBOXSTYLEDIAL2_H



# #include "qtboxstyledial2.h"
# #include <math.h>
# #include <QMouseEvent>
# #include <QPainter>
# #include <QPen>
# #include <QLinearGradient>
# #include <QColor>
# #include <QPointF>
# #include <QFont>
# #include <QFontMetricsF>
# #include <Qt>

# QtBoxStyleDial2::QtBoxStyleDial2(QWidget *parent)
#     : QDial(parent)
# {
#     setFixedSize(100, 100);
#     setRange(100, 200);
#     setWrapping(true);
# }

# void QtBoxStyleDial2::mousePressEvent(QMouseEvent *event)
# {
#     QDial::mousePressEvent(event);
#     if (event->button() == Qt::LeftButton) {
#         mouseX = event->x();
#         mouseY = event->y();
#     }
# }
#
# void QtBoxStyleDial2::mouseMoveEvent(QMouseEvent *event)
# {
#     QDial::mouseMoveEvent(event);
#     if (event->buttons() == Qt::LeftButton) {
#         mouseX = event->x();
#         mouseY = event->y();
#     }
# }

# void QtBoxStyleDial2::paintEvent(QPaintEvent *event)
# {
#     QPainter painter(this);
#     painter.setRenderHint(QPainter::Antialiasing);
#     QPen pen = QPen();
#     pen.setColor(Qt::lightGray);
#     painter.setPen(pen);

#     QLinearGradient linearGradient = QLinearGradient(rect().topLeft(), rect().bottomRight());
#     linearGradient.setColorAt(0, QColor(Qt::white));
#     linearGradient.setColorAt(1, QColor(Qt::black));
#     painter.setBrush(linearGradient);
#     painter.drawEllipse(rect());

#     if (isFirstPaint) {
#         mouseX = rect().center().x();
#         mouseY = rect().bottom();
#         isFirstPaint = false;
#     }

#     int handleRadius = 10;
#     painter.setBrush(Qt::white);
#     float *handlePos = getHandlePos();
#     float handleX = handlePos[0];
#     float handleY = handlePos[1];
#     painter.drawEllipse(QPointF(handleX, handleY), handleRadius, handleRadius);

#     float angle = getAngle(handlePos);
#     setValue(round(angle / 360 * (maximum()-minimum())) + minimum());
#     delete[] handlePos;

#     QFont font = QFont();
#     font.setPixelSize(18);
#     painter.setFont(font);
#     QFontMetricsF fontMetrics = QFontMetrics(font);
#     float textWidth = fontMetrics.size(Qt::TextSingleLine, QString("%1").arg(value())).width();
#     painter.drawText(int(width()/2-textWidth/2), int(height()/2), QString("%1").arg(value()));
# }

# float* QtBoxStyleDial2::getHandlePos()
# {
#     int centerX = rect().center().x();
#     int centerY = rect().center().y();

#     int diffX;
#     int diffY;
#     if (mouseX-centerX == 0 && mouseY-centerY == 0) {
#         diffX = centerX;
#         diffY = centerY;
#     }
#     else {
#         diffX = mouseX - centerX;
#         diffY = mouseY - centerY;
#     }

#     float posAdjustValue = 1.5;
#     float length = sqrt(pow(diffX, 2) + pow(diffY, 2));
#     float ratio = length / (rect().width()/2) * posAdjustValue;
#     float handleX = diffX / ratio + centerX;
#     float handleY = diffY / ratio + centerY;

#     float *result = new float[2];
#     result[0] = handleX;
#     result[1] = handleY;
#     return result;
# }

# float QtBoxStyleDial2::getAngle(float *handlePos)
# {
#     int centerX = rect().center().x();
#     int centerY = rect().center().y();
#     int startPos[2] = {rect().center().x(), rect().bottom()};

#     float vx1 = startPos[0] - centerX;
#     float vy1 = startPos[1] - centerY;
#     float vx2 = handlePos[0] - centerX;
#     float vy2 = handlePos[1] - centerY;
#     float angle1 = atan2(vy1, vx1);
#     angle1 = angle1 * 180 / M_PI;
#     float angle2 = atan2(vy2, vx2);
#     angle2 = angle2 * 180 / M_PI;

#     float diffAngle;
#     if (angle2 >= 0) {
#         diffAngle = angle2 - angle1;
#         if (diffAngle < 0) {
#             diffAngle = 360 - abs(diffAngle);
#         }
#     }
#     else {
#         diffAngle = 180 + angle2 + angle1;
#     }
#     return diffAngle;
# }
# C++/Qt