# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QFont, QFontMetricsF
from PyQt5.QtWidgets import QDial
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QDial = createWidgetMenuBase(QDial)

class QtBoxFuncDial1(QDial):
    def __init__(self):
        super(QtBoxFuncDial1, self).__init__(str(Path(__file__)))
        self.setRange(0, 100)
        self.setWrapping(True)
        self.setNotchTarget(10)
        self.setNotchesVisible(True)

    def paintEvent(self, event):
        super(QtBoxFuncDial1, self).paintEvent(event)
        painter = QPainter(self)

        font = QFont()
        font.setPixelSize(18)
        painter.setFont(font)
        font_metrics = QFontMetricsF(font)
        text_width = font_metrics.width(str(self.value()))
        painter.drawText(int(self.width()/2-text_width/2), int(self.height()/2), str(self.value()))
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtGui import QPainter, QFont, QFontMetricsF
# from PySide2.QtWidgets import QDial


# class QtBoxFuncDial1(QDial):
#     def __init__(self):
#         super(QtBoxFuncDial1, self).__init__(str(Path(__file__)))
#         self.setRange(0, 100)
#         self.setWrapping(True)
#         self.setNotchTarget(10)
#         self.setNotchesVisible(True)

#     def paintEvent(self, event):
#         super(QtBoxFuncDial1, self).paintEvent(event)
#         painter = QPainter(self)

#         font = QFont()
#         font.setPixelSize(18)
#         painter.setFont(font)
#         font_metrics = QFontMetricsF(font)
#         text_width = font_metrics.width(str(self.value()))
#         painter.drawText(int(self.width()/2-text_width/2), int(self.height()/2), str(self.value()))
# PySide

# C++/Qt
# #ifndef QTBOXFUNCDIAL1_H
# #define QTBOXFUNCDIAL1_H
# #include <QDial>

# class QtBoxFuncDial1 : public QDial
# {
#     Q_OBJECT

# public:
#     QtBoxFuncDial1(QWidget *parent = nullptr);

# protected:
#     void paintEvent(QPaintEvent *event);
# };
# #endif // QTBOXFUNCDIAL1_H



# #include "qtboxfuncdial1.h"
# #include <QPainter>
# #include <QFont>
# #include <Qt>
# #include <QString>
# #include <QFontMetricsF>

# QtBoxFuncDial1::QtBoxFuncDial1(QWidget *parent)
#     : QDial(parent)
# {
#     setRange(0, 100);
#     setWrapping(true);
#     setNotchTarget(10);
#     setNotchesVisible(true);
# }

# void QtBoxFuncDial1::paintEvent(QPaintEvent *event)
# {
#     QDial::paintEvent(event);
#     QPainter painter(this);

#     QFont font = QFont();
#     font.setPixelSize(18);
#     painter.setFont(font);
#     QFontMetricsF fontMetrics = QFontMetricsF(font);
#     float textWidth = fontMetrics.size(Qt::TextSingleLine, QString("%1").arg(value())).width();
#     painter.drawText(int(this->width()/2-textWidth/2), int(this->height()/2), QString("%1").arg(value()));
# }
# C++/Qt