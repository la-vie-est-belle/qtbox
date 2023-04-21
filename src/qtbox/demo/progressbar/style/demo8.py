# PyQt
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtGui import QPainter, QColor, QPen, QFont, QFontMetricsF
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QProgressBar = createWidgetMenuBase(QProgressBar)

class QtBoxStyleProgressBar8(QProgressBar):
    def __init__(self):
        super(QtBoxStyleProgressBar8, self).__init__(str(Path(__file__)))
        self.setFixedSize(80, 80)
        self.setRange(0, 100)
        self.setValue(80)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(33, 33, 33))
        painter.drawEllipse(self.rect())

        offset = 4
        arc_rect = QRectF(self.rect().left() + offset / 2, self.rect().top() + offset / 2, self.rect().width() - offset, self.rect().height() - offset)

        arc_pen = QPen()
        arc_pen.setColor(QColor(57, 57, 57))
        arc_pen.setWidth(4)
        painter.setPen(arc_pen)
        painter.drawArc(arc_rect, 90*16, 360*16)

        arc_pen.setColor(QColor(241, 150, 76))
        painter.setPen(arc_pen)
        percent = self.value() / self.maximum() if self.maximum() != 0 else 0
        painter.drawArc(arc_rect, 90*16, int(percent*360*16))

        font = QFont()
        font.setPixelSize(18)
        painter.setFont(font)
        font_metrics = QFontMetricsF(font)
        text_width = font_metrics.width(self.text())
        painter.drawText(int(self.width()/2-text_width/2), 45, self.text())
# PyQt

# PySide
# from PySide2.QtCore import Qt, QRectF
# from PySide2.QtWidgets import QProgressBar
# from PySide2.QtGui import QPainter, QColor, QPen, QFont, QFontMetricsF


# class QtBoxStyleProgressBar8(QProgressBar):
#     def __init__(self):
#         super(QtBoxStyleProgressBar8, self).__init__()
#         self.setFixedSize(80, 80)
#         self.setRange(0, 100)
#         self.setValue(80)

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.Antialiasing)
#         painter.setPen(Qt.NoPen)
#         painter.setBrush(QColor(33, 33, 33))
#         painter.drawEllipse(self.rect())

#         offset = 4
#         arc_rect = QRectF(self.rect().left() + offset / 2, self.rect().top() + offset / 2, self.rect().width() - offset, self.rect().height() - offset)

#         arc_pen = QPen()
#         arc_pen.setColor(QColor(57, 57, 57))
#         arc_pen.setWidth(4)
#         painter.setPen(arc_pen)
#         painter.drawArc(arc_rect, 90*16, 360*16)

#         arc_pen.setColor(QColor(241, 150, 76))
#         painter.setPen(arc_pen)
#         percent = self.value() / self.maximum() if self.maximum() != 0 else 0
#         painter.drawArc(arc_rect, 90*16, int(percent*360*16))

#         font = QFont()
#         font.setPixelSize(18)
#         painter.setFont(font)
#         font_metrics = QFontMetricsF(font)
#         text_width = font_metrics.width(self.text())
#         painter.drawText(int(self.width()/2-text_width/2), 45, self.text())
# PySide

# C++/Qt
# #ifndef QTBOXSTYLEPROGRESSBAR8_H
# #define QTBOXSTYLEPROGRESSBAR8_H
# #include <QProgressBar>
# #include <QPaintEvent>

# class QtBoxStyleProgressBar8 : public QProgressBar
# {
#     Q_OBJECT

# protected:
#     void paintEvent(QPaintEvent *event);

# public:
#     QtBoxStyleProgressBar8(QWidget *parent = nullptr);
# };
# #endif // QTBOXSTYLEPROGRESSBAR8_H



# #include "qtboxstyleprogressbar8.h"
# #include <QPainter>
# #include <QRectF>
# #include <QPen>
# #include <QColor>
# #include <QFont>
# #include <QFontMetricsF>
# #include <Qt>

# QtBoxStyleProgressBar8::QtBoxStyleProgressBar8(QWidget *parent)
#     : QProgressBar(parent)
# {
#     setFixedSize(80, 80);
#     setRange(0, 100);
#     setValue(80);
# }

# void QtBoxStyleProgressBar8::paintEvent(QPaintEvent *event)
# {
#     QPainter painter(this);
#     painter.setRenderHint(QPainter::Antialiasing);
#     painter.setPen(Qt::NoPen);
#     painter.setBrush(QColor(33, 33, 33));
#     painter.drawEllipse(rect());

#     int offset = 4;
#     QRectF arcRect = QRectF(rect().left()+offset/2, rect().top()+offset/2, rect().width()-offset, rect().height()-offset);

#     QPen arcPen = QPen();
#     arcPen.setColor(QColor(57, 57, 57));
#     arcPen.setWidth(4);
#     painter.setPen(arcPen);
#     painter.drawArc(arcRect, 90*16, 360*16);

#     arcPen.setColor(QColor(241, 150, 76));
#     painter.setPen(arcPen);
#     float percent = 0.0;
#     if (maximum() != 0) {
#         percent = float(value()) / float(maximum());
#     }
#     painter.drawArc(arcRect, 90*16, int(percent*360*16));

#     QFont font = QFont();
#     font.setPixelSize(18);
#     painter.setFont(font);
#     QFontMetricsF fontMetricsF = QFontMetricsF(font);
#     float textWidth = fontMetricsF.size(Qt::TextSingleLine, text()).width();
#     painter.drawText(int(width()/2-textWidth/2), 45, text());
# }
# C++/Qt