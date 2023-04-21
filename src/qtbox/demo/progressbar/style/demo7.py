# PyQt
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtGui import QPainter, QColor, QPen, QFont, QFontMetricsF
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QProgressBar = createWidgetMenuBase(QProgressBar)

class QtBoxStyleProgressBar7(QProgressBar):
    def __init__(self):
        super(QtBoxStyleProgressBar7, self).__init__(str(Path(__file__)))
        self.setFixedSize(80, 80)
        self.setRange(0, 100)
        self.setValue(80)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        offset = 20
        arc_rect = QRectF(self.rect().left() + offset / 2, self.rect().top() + offset / 2, self.rect().width() - offset, self.rect().height() - offset)

        arc_pen = QPen()
        arc_pen.setColor(QColor(127, 106, 209))
        arc_pen.setWidth(18)
        painter.setPen(arc_pen)
        percent = self.value() / self.maximum() if self.maximum() != 0 else 0
        painter.drawArc(arc_rect, 90*16, int(percent*360*16))

        font = QFont()
        font.setPixelSize(15)
        painter.setFont(font)
        font_metrics = QFontMetricsF(font)
        text_width = font_metrics.width(self.text())
        painter.drawText(int(self.width()/2-text_width/2), 45, self.text())
# PyQt

# PySide
# from PySide2.QtCore import Qt, QRectF
# from PySide2.QtWidgets import QProgressBar
# from PySide2.QtGui import QPainter, QColor, QPen, QFont, QFontMetricsF


# class QtBoxStyleProgressBar7(QProgressBar):
#     def __init__(self):
#         super(QtBoxStyleProgressBar7, self).__init__()
#         self.setFixedSize(80, 80)
#         self.setRange(0, 100)
#         self.setValue(80)

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.Antialiasing)

#         offset = 20
#         arc_rect = QRectF(self.rect().left() + offset / 2, self.rect().top() + offset / 2, self.rect().width() - offset, self.rect().height() - offset)

#         arc_pen = QPen()
#         arc_pen.setColor(QColor(127, 106, 209))
#         arc_pen.setWidth(18)
#         painter.setPen(arc_pen)
#         percent = self.value() / self.maximum() if self.maximum() != 0 else 0
#         painter.drawArc(arc_rect, 90*16, int(percent*360*16))

#         font = QFont()
#         font.setPixelSize(15)
#         painter.setFont(font)
#         font_metrics = QFontMetricsF(font)
#         text_width = font_metrics.width(self.text())
#         painter.drawText(int(self.width()/2-text_width/2), 45, self.text())
# PySide

# C++/Qt
# #ifndef QTBOXSTYLEPROGRESSBAR7_H
# #define QTBOXSTYLEPROGRESSBAR7_H
# #include <QProgressBar>
# #include <QPaintEvent>

# class QtBoxStyleProgressBar7 : public QProgressBar
# {
#     Q_OBJECT

# protected:
#     void paintEvent(QPaintEvent *event);

# public:
#     QtBoxStyleProgressBar7(QWidget *parent = nullptr);
# };
# #endif // QTBOXSTYLEPROGRESSBAR7_H



#include "qtboxstyleprogressbar7.h"
#include <QPainter>
#include <QRectF>
#include <QPen>
#include <QColor>
#include <QFont>
#include <QFontMetricsF>

# QtBoxStyleProgressBar7::QtBoxStyleProgressBar7(QWidget *parent)
#     : QProgressBar(parent)
# {
#     setFixedSize(80, 80);
#     setRange(0, 100);
#     setValue(80);
# }

# void QtBoxStyleProgressBar7::paintEvent(QPaintEvent *event)
# {
#     QPainter painter(this);
#     painter.setRenderHint(QPainter::Antialiasing);

#     int offset = 20;
#     QRectF arcRect = QRectF(rect().left()+offset/2, rect().top()+offset/2, rect().width()-offset, rect().height()-offset);

#     QPen arcPen = QPen();
#     arcPen.setColor(QColor(127, 106, 209));
#     arcPen.setWidth(18);
#     painter.setPen(arcPen);

#     float percent = 0.0;
#     if (maximum() != 0) {
#         percent = float(value()) / float(maximum());
#     }
#     painter.drawArc(arcRect, 90*16, int(percent*360*16));

#     QFont font = QFont();
#     font.setPixelSize(15);
#     painter.setFont(font);
#     QFontMetricsF fontMetricsF = QFontMetricsF(font);
#     float textWidth = fontMetricsF.size(Qt::TextSingleLine, text()).width();
#     painter.drawText(int(width()/2-textWidth/2), 45, text());
# }
# C++/Qt