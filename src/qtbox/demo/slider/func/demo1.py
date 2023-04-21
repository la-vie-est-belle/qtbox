# PyQt
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPainter, QColor, QFont, QFontMetricsF
from PyQt5.QtWidgets import QSlider
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QSlider = createWidgetMenuBase(QSlider)

class QtBoxFuncSlider1(QSlider):
    def __init__(self):
        super(QtBoxFuncSlider1, self).__init__(str(Path(__file__)))
        self.setMinimum(0)
        self.setMaximum(100)
        self.setOrientation(Qt.Horizontal)
        self.is_number_shown = False

    def mousePressEvent(self, event):
        super(QtBoxFuncSlider1, self).mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self.is_number_shown = True
            self.update()

    def mouseReleaseEvent(self, event):
        super(QtBoxFuncSlider1, self).mouseReleaseEvent(event)
        if event.button() == Qt.LeftButton:
            self.is_number_shown = False
            self.update()

    def paintEvent(self, event):
        super(QtBoxFuncSlider1, self).paintEvent(event)

        if not self.is_number_shown:
            return

        painter = QPainter(self)
        painter.setBrush(QColor(220, 220, 220, 120))

        font = QFont()
        font.setPixelSize(13)
        painter.setFont(font)
        font_metrics = QFontMetricsF(font)
        text_width = font_metrics.width(str(self.value()))
        text_height = font_metrics.height()
        x = (self.value() - self.minimum()) / (self.maximum() - self.minimum()) * (self.width() - text_width)
        rect = QRectF(x, 0, text_width, text_height)

        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(rect, 3, 3)
        painter.setPen(Qt.SolidLine)
        painter.drawText(int(x), int(text_height), str(self.value()))
# PyQt

# PySide
# from PySide2.QtCore import Qt, QRectF
# from PySide2.QtGui import QPainter, QColor, QFont, QFontMetricsF
# from PySide2.QtWidgets import QSlider


# class QtBoxFuncSlider1(QSlider):
#     def __init__(self):
#         super(QtBoxFuncSlider1, self).__init__(str(Path(__file__)))
#         self.setMinimum(0)
#         self.setMaximum(100)
#         self.setOrientation(Qt.Horizontal)
#         self.is_number_shown = False

#     def mousePressEvent(self, event):
#         super(QtBoxFuncSlider1, self).mousePressEvent(event)
#         if event.button() == Qt.LeftButton:
#             self.is_number_shown = True
#             self.update()

#     def mouseReleaseEvent(self, event):
#         super(QtBoxFuncSlider1, self).mouseReleaseEvent(event)
#         if event.button() == Qt.LeftButton:
#             self.is_number_shown = False
#             self.update()

#     def paintEvent(self, event):
#         super(QtBoxFuncSlider1, self).paintEvent(event)

#         if not self.is_number_shown:
#             return

#         painter = QPainter(self)
#         painter.setBrush(QColor(200, 200, 200, 120))

#         font = QFont()
#         font.setPixelSize(15)
#         painter.setFont(font)
#         font_metrics = QFontMetricsF(font)
#         text_width = font_metrics.width(str(self.value()))
#         text_height = font_metrics.height()
#         x = (self.value() - self.minimum()) / (self.maximum() - self.minimum()) * (self.width() - text_width)
#         rect = QRectF(x, 0, text_width, text_height)

#         painter.setPen(Qt.NoPen)
#         painter.drawRoundedRect(rect, 3, 3)
#         painter.setPen(Qt.SolidLine)
#         painter.drawText(int(x), int(text_height), str(self.value()))
# PySide

# C++/Qt
# #ifndef QTBOXFUNCSLIDER1_H
# #define QTBOXFUNCSLIDER1_H
# #include <QMouseEvent>
# #include <QPaintEvent>
# #include <QSlider>

# class QtBoxFuncSlider1 : public QSlider
# {
#     Q_OBJECT

# public:
#     QtBoxFuncSlider1(QWidget *parent = nullptr);

# protected:
#     void mousePressEvent(QMouseEvent *event);
#     void mouseReleaseEvent(QMouseEvent *event);
#     void paintEvent(QPaintEvent *event);

# private:
#     bool isNumberShown = false;
# };
# #endif // QTBOXFUNCSLIDER1_H



# #include "qtboxfuncslider1.h"
# #include <QFontMetricsF>
# #include <QPainter>
# #include <QRectF>
# #include <QColor>
# #include <QFont>
# #include <Qt>

# QtBoxFuncSlider1::QtBoxFuncSlider1(QWidget *parent)
#     : QSlider(parent)
# {
#     setMinimum(0);
#     setMaximum(100);
#     setOrientation(Qt::Horizontal);
# }

# void QtBoxFuncSlider1::mousePressEvent(QMouseEvent *event)
# {
#     QSlider::mousePressEvent(event);
#     if (event->button() == Qt::LeftButton) {
#         isNumberShown = true;
#         update();
#     }
# }

# void QtBoxFuncSlider1::mouseReleaseEvent(QMouseEvent *event)
# {
#
#     QSlider::mouseReleaseEvent(event);
#     if (event->button() == Qt::LeftButton) {
#         isNumberShown = false;
#         update();
#     }
# }

# void QtBoxFuncSlider1::paintEvent(QPaintEvent *event)
# {
#     QSlider::paintEvent(event);
#     if (!isNumberShown) {
#         return;
#     }

#     QPainter painter = QPainter(this);
#     painter.setBrush(QColor(220, 220, 220, 120));

#     QFont font = QFont();
#     font.setPixelSize(13);
#     painter.setFont(font);
#     QFontMetricsF fontMetrics = QFontMetricsF(font);
#     float textWidth = fontMetrics.size(Qt::TextSingleLine, QString("%1").arg(value())).width();
#     float textHeight = fontMetrics.height();
#     float x = float(value() - minimum()) / float(maximum() - minimum()) * float(width() - textWidth);
#     QRectF rect = QRectF(x, 0, textWidth, textHeight*1.3);

#     painter.setPen(Qt::NoPen);
#     painter.drawRoundedRect(rect, 3, 3);
#     painter.setPen(Qt::SolidLine);
#     painter.drawText(int(x), int(textHeight), QString("%1").arg(value()));
# }
# C++/Qt