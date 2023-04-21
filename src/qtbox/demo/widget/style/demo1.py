# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QWidget = createWidgetMenuBase(QWidget)

class QtBoxStyleWidget1(QWidget):
    def __init__(self):
        super(QtBoxStyleWidget1, self).__init__(str(Path(__file__)))
        self.setFixedSize(100, 100)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.lightGray)
        painter.drawRoundedRect(self.rect(), 10, 10)
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtGui import QPainter
# from PySide2.QtWidgets import QWidget


# class QtBoxStyleWidget1(QWidget):
#     def __init__(self):
#         super(QtBoxStyleWidget1, self).__init__()
#         self.setFixedSize(100, 100)
#         self.setWindowFlag(Qt.FramelessWindowHint)
#         self.setAttribute(Qt.WA_TranslucentBackground)

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setPen(Qt.NoPen)
#         painter.setBrush(Qt.lightGray)
#         painter.drawRoundedRect(self.rect(), 10, 10)
# PySide

# C++/Qt
# #ifndef QTBOXSTYLEWIDGET1_H
# #define QTBOXSTYLEWIDGET1_H
# #include <QPaintEvent>
# #include <QWidget>

# class QtBoxStyleWidget1 : public QWidget
# {
#     Q_OBJECT

# public:
#     QtBoxStyleWidget1(QWidget *parent = nullptr);

# protected:
#     void paintEvent(QPaintEvent *event);
# };
# #endif // QTBOXSTYLEWIDGET1_H



# #include "qtboxstylewidget1.h"
# #include <QPainter>
# #include <Qt>

# QtBoxStyleWidget1::QtBoxStyleWidget1(QWidget *parent)
#     : QWidget(parent)
# {
#     setFixedSize(100, 100);
#     setWindowFlag(Qt::FramelessWindowHint);
#     setAttribute(Qt::WA_TranslucentBackground);
# }

# void QtBoxStyleWidget1::paintEvent(QPaintEvent *event)
# {
#     QPainter painter = QPainter(this);
#     painter.setPen(Qt::NoPen);
#     painter.setBrush(Qt::lightGray);
#     painter.drawRoundedRect(rect(), 10, 10);
# }
# C++/Qt