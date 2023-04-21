# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPainter, QPen, QColor, QPainterPath, QFont, QFontMetricsF
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QPushButton = createWidgetMenuBase(QPushButton)

class QtBoxStyleButton4(QPushButton):
    def __init__(self):
        super(QtBoxStyleButton4, self).__init__(str(Path(__file__)))
        self.btn_state = "normal"
        self.setFixedSize(90, 90)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.setStyleSheet("""
        QPushButton {
            font-size: 20px;
            font-weight: bold;
        }
        """)

    def paintEvent(self, event):
        painter = QPainter(self)

        if self.btn_state == "normal":
            painter.setBrush(QColor(59, 63, 66))
            pen = QPen()
            pen.setColor(Qt.white)
            pen .setWidth(3)
            painter.setPen(pen)

        elif self.btn_state == "hover":
            painter.setBrush(Qt.black)
            pen = QPen()
            pen.setColor(Qt.white)
            pen.setWidth(3)
            painter.setPen(pen)

        elif self.btn_state == "press":
            painter.setBrush(Qt.white)
            pen = QPen()
            pen.setColor(Qt.black)
            pen.setWidth(3)
            painter.setPen(pen)

        path = QPainterPath()
        path.moveTo(self.rect().left()+self.rect().width()/2, self.rect().top())
        path.lineTo(self.rect().bottomLeft())
        path.lineTo(self.rect().bottomRight())
        path.lineTo(self.rect().left()+self.rect().width()/2, self.rect().top())
        painter.drawPath(path)

        font = QFont()
        font.setBold(True)
        font.setPixelSize(20)
        painter.setFont(font)
        font_metrics = QFontMetricsF(font)
        text_width = font_metrics.width("BTN")
        painter.drawText(int(self.rect().width()/2-text_width/2), int(self.rect().height()/2+20), "BTN")

    def mousePressEvent(self, event):
        self.btn_state = "press"
        self.update()

    def mouseReleaseEvent(self, event):
        self.btn_state = "hover"
        self.update()

    def enterEvent(self, event):
        self.btn_state = "hover"
        self.update()

    def leaveEvent(self, event):
        self.btn_state = "normal"
        self.update()
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QPushButton
# from PySide2.QtGui import QPainter, QPen, QColor, QPainterPath, QFont, QFontMetricsF


# class QtBoxStyleButton4(QPushButton):
#     def __init__(self):
#         super(QtBoxStyleButton4, self).__init__()
#         self.btn_state = "normal"
#         self.setFixedSize(90, 90)
#         self.setAttribute(Qt.WA_TranslucentBackground)

#         self.setStyleSheet("""
#         QPushButton {
#             font-size: 20px;
#             font-weight: bold;
#         }
#         """)

#     def paintEvent(self, event):
#         painter = QPainter(self)

#         if self.btn_state == "normal":
#             painter.setBrush(QColor(59, 63, 66))
#             pen = QPen()
#             pen.setColor(Qt.white)
#             pen .setWidth(3)
#             painter.setPen(pen)

#         elif self.btn_state == "hover":
#             painter.setBrush(Qt.black)
#             pen = QPen()
#             pen.setColor(Qt.white)
#             pen.setWidth(3)
#             painter.setPen(pen)

#         elif self.btn_state == "press":
#             painter.setBrush(Qt.white)
#             pen = QPen()
#             pen.setColor(Qt.black)
#             pen.setWidth(3)
#             painter.setPen(pen)

#         path = QPainterPath()
#         path.moveTo(self.rect().left()+self.rect().width()/2, self.rect().top())
#         path.lineTo(self.rect().bottomLeft())
#         path.lineTo(self.rect().bottomRight())
#         path.lineTo(self.rect().left()+self.rect().width()/2, self.rect().top())
#         painter.drawPath(path)

#         font = QFont()
#         font.setBold(True)
#         font.setPixelSize(20)
#         painter.setFont(font)
#         font_metrics = QFontMetricsF(font)
#         text_width = font_metrics.width("BTN")
#         painter.drawText(int(self.rect().width()/2-text_width/2), int(self.rect().height()/2+20), "BTN")

#     def mousePressEvent(self, event):
#         self.btn_state = "press"
#         self.update()

#     def mouseReleaseEvent(self, event):
#         self.btn_state = "hover"
#         self.update()

#     def enterEvent(self, event):
#         self.btn_state = "hover"
#         self.update()

#     def leaveEvent(self, event):
#         self.btn_state = "normal"
#         self.update()
# PySide

# C++/Qt
# #ifndef QTBOXSTYLEPUSHBUTTON4_H
# #define QTBOXSTYLEPUSHBUTTON4_H
# #include <QPushButton>
# #include <QString>
# #include <QPaintEvent>
# #include <QMouseEvent>
# #include <QEnterEvent>
# #include <QEvent>

# class QtBoxStylePushButton4 : public QPushButton
# {
#     Q_OBJECT

# public:
#     QtBoxStylePushButton4(QWidget *parent = nullptr);

# protected:
#     void paintEvent(QPaintEvent *evnet);
#     void mousePressEvent(QMouseEvent *event);
#     void mouseReleaseEvent(QMouseEvent *event);
#     void enterEvent(QEnterEvent *event);
#     void leaveEvent(QEvent *event);

# private:
#     QString btnState = "normal";
# };
# #endif // QTBOXSTYLEPUSHBUTTON4_H



# #include "qtboxstylepushbutton4.h"
# #include <QFontMetricsF>
# #include <QPainterPath>
# #include <QPainter>
# #include <QColor>
# #include <QFont>
# #include <QPen>
# #include <Qt>

# QtBoxStylePushButton4::QtBoxStylePushButton4(QWidget *parent)
#     : QPushButton(parent)
# {
#     setFixedSize(90, 90);
#     setAttribute(Qt::WA_TranslucentBackground);
#     setStyleSheet(R"(
#     QPushButton {
#         font-size: 20px;
#         font-weight: bold;
#     }
#     )");
# }

# void QtBoxStylePushButton4::paintEvent(QPaintEvent *event)
# {
#     QPainter painter = QPainter(this);

#     if (btnState == "normal") {
#         painter.setBrush(QColor(59, 63, 66));
#         QPen pen = QPen();
#         pen.setColor(Qt::white);
#         pen.setWidth(3);
#         painter.setPen(pen);
#     }
#     else if (btnState == "hover") {
#         painter.setBrush(Qt::black);
#         QPen pen = QPen();
#         pen.setColor(Qt::white);
#         pen.setWidth(3);
#         painter.setPen(pen);
#     }
#     else if (btnState == "press") {
#         painter.setBrush(Qt::white);
#         QPen pen = QPen();
#         pen.setColor(Qt::black);
#         pen.setWidth(3);
#         painter.setPen(pen);
#     }

#     QPainterPath path = QPainterPath();
#     path.moveTo(rect().left()+rect().width()/2, rect().top());
#     path.lineTo(rect().bottomLeft());
#     path.lineTo(rect().bottomRight());
#     path.lineTo(rect().left()+rect().width()/2, rect().top());
#     painter.drawPath(path);

#     QFont font = QFont();
#     font.setBold(true);
#     font.setPixelSize(20);
#     painter.setFont(font);
#     QFontMetricsF fontMetrics = QFontMetricsF(font);
#     float textWidth = fontMetrics.size(Qt::TextSingleLine, "BTN").width();
#     painter.drawText(int(rect().width()/2-textWidth/2), int(rect().height()/2+20), "BTN");
# }

# void QtBoxStylePushButton4::mousePressEvent(QMouseEvent *event)
# {
#     btnState = "press";
#     update();
# }

# void QtBoxStylePushButton4::mouseReleaseEvent(QMouseEvent *event)
# {
#     btnState = "hover";
#     update();
# }

# void QtBoxStylePushButton4::enterEvent(QEnterEvent *event)
# {
#     btnState = "hover";
#     update();
# }

# void QtBoxStylePushButton4::leaveEvent(QEvent *event)
# {
#     btnState = "normal";
#     update();
# }
# C++/Qt