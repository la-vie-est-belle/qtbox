# PyQt
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPainter, QPen, QColor, QLinearGradient, QFont, QFontMetricsF
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QPushButton = createWidgetMenuBase(QPushButton)

class QtBoxStyleButton10(QPushButton):
    def __init__(self):
        super(QtBoxStyleButton10, self).__init__(str(Path(__file__)))
        self.btn_rect = None
        self.btn_state = "off"
        self.setFixedSize(90, 90)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        if self.btn_state == "on":
            offset = 40
            font_size = 15
        else:
            offset = 30
            font_size = 20

        painter.setPen(Qt.NoPen)
        base_linear_gradient = QLinearGradient(self.rect().topLeft(), self.rect().bottomRight())
        base_linear_gradient.setColorAt(0, QColor(117, 117, 117))
        base_linear_gradient.setColorAt(1, QColor(97, 97, 97))
        painter.setBrush(base_linear_gradient)
        painter.drawEllipse(self.rect())

        self.btn_rect = QRectF(self.rect().left()+offset/2, self.rect().top()+offset/2, self.rect().width()-offset, self.rect().height()-offset)
        btn_linear_gradient = QLinearGradient(self.btn_rect.topLeft(), self.btn_rect.bottomRight())
        btn_linear_gradient.setColorAt(0, QColor(241, 112, 117))
        btn_linear_gradient.setColorAt(1, QColor(223, 84, 89))
        painter.setBrush(btn_linear_gradient)
        painter.drawEllipse(self.btn_rect)

        pen = QPen()
        pen.setColor(Qt.white)
        painter.setPen(pen)

        font = QFont()
        font.setBold(True)
        font.setPixelSize(font_size)
        painter.setFont(font)
        font_metrics = QFontMetricsF(font)
        text_width = font_metrics.width("BTN")
        painter.drawText(int(self.rect().width()/2-text_width/2), int(self.rect().height()/2+5), "BTN")

    def mousePressEvent(self, event):
        if event.button() != Qt.LeftButton or not self.btn_rect.contains(event.pos()):
            return

        self.btn_state = "on"
        self.update()

    def mouseReleaseEvent(self, event):
        self.btn_state = "off"
        self.update()
# PyQt

# PySide
# from PySide2.QtCore import Qt, QRectF
# from PySide2.QtWidgets import QPushButton
# from PySide2.QtGui import QPainter, QPen, QColor, QLinearGradient, QFont, QFontMetricsF


# class QtBoxStyleButton10(QPushButton):
#     def __init__(self):
#         super(QtBoxStyleButton10, self).__init__()
#         self.btn_rect = None
#         self.btn_state = "off"
#         self.setFixedSize(90, 90)

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.Antialiasing)

#         if self.btn_state == "on":
#             offset = 40
#             font_size = 15
#         else:
#             offset = 30
#             font_size = 20

#         painter.setPen(Qt.NoPen)
#         base_linear_gradient = QLinearGradient(self.rect().topLeft(), self.rect().bottomRight())
#         base_linear_gradient.setColorAt(0, QColor(117, 117, 117))
#         base_linear_gradient.setColorAt(1, QColor(97, 97, 97))
#         painter.setBrush(base_linear_gradient)
#         painter.drawEllipse(self.rect())

#         self.btn_rect = QRectF(self.rect().left()+offset/2, self.rect().top()+offset/2, self.rect().width()-offset, self.rect().height()-offset)
#         btn_linear_gradient = QLinearGradient(self.btn_rect.topLeft(), self.btn_rect.bottomRight())
#         btn_linear_gradient.setColorAt(0, QColor(241, 112, 117))
#         btn_linear_gradient.setColorAt(1, QColor(223, 84, 89))
#         painter.setBrush(btn_linear_gradient)
#         painter.drawEllipse(self.btn_rect)

#         pen = QPen()
#         pen.setColor(Qt.white)
#         painter.setPen(pen)

#         font = QFont()
#         font.setBold(True)
#         font.setPixelSize(font_size)
#         painter.setFont(font)
#         font_metrics = QFontMetricsF(font)
#         text_width = font_metrics.width("BTN")
#         painter.drawText(int(self.rect().width()/2-text_width/2), int(self.rect().height()/2+5), "BTN")

#     def mousePressEvent(self, event):
#         if event.button() != Qt.LeftButton or not self.btn_rect.contains(event.pos()):
#             return

#         self.btn_state = "on"
#         self.update()

#     def mouseReleaseEvent(self, event):
#         self.btn_state = "off"
#         self.update()
# PySide

# C++/Qt
# #ifndef QTBOXSTYLEPUSHBUTTON10_H
# #define QTBOXSTYLEPUSHBUTTON10_H
# #include <QPushButton>
# #include <QPaintEvent>
# #include <QMouseEvent>
# #include <QString>
# #include <QRectF>

# class QtBoxStylePushButton10 : public QPushButton
# {
#     Q_OBJECT

# public:
#     QtBoxStylePushButton10(QWidget *parent = nullptr);

# protected:
#     void paintEvent(QPaintEvent *event);
#     void mousePressEvent(QMouseEvent *event);
#     void mouseReleaseEvent(QMouseEvent *event);

# private:
#     QRectF btnRect;
#     QString btnState;
# };
# #endif // QTBOXSTYLEPUSHBUTTON10_H



# #include "qtboxstylepushbutton10.h"
# #include <QLinearGradient>
# #include <QFontMetricsF>
# #include <QPainter>
# #include <QFont>
# #include <Qt>

# QtBoxStylePushButton10::QtBoxStylePushButton10(QWidget *parent)
#     : QPushButton(parent)
# {
#     setFixedSize(90, 90);
# }

# void QtBoxStylePushButton10::paintEvent(QPaintEvent *event)
# {
#     QPainter painter = QPainter(this);
#     painter.setRenderHint(QPainter::Antialiasing);

#     int offset;
#     int fontSize;
#     if (btnState == "on") {
#         offset = 40;
#         fontSize = 15;
#     }
#     else {
#         offset = 30;
#         fontSize = 20;
#     }

#     painter.setPen(Qt::NoPen);
#     QLinearGradient baseLinearGradient;
#     baseLinearGradient = QLinearGradient(rect().topLeft(), rect().bottomRight());
#     baseLinearGradient.setColorAt(0, QColor(117, 117, 117));
#     baseLinearGradient.setColorAt(1, QColor(97, 97, 97));
#     painter.setBrush(baseLinearGradient);
#     painter.drawEllipse(rect());

#     btnRect = QRectF(rect().left()+offset/2, rect().top()+offset/2, rect().width()-offset, rect().height()-offset);
#     baseLinearGradient = QLinearGradient(rect().topLeft(), rect().bottomRight());
#     baseLinearGradient.setColorAt(0, QColor(241, 112, 117));
#     baseLinearGradient.setColorAt(1, QColor(223, 84, 89));
#     painter.setBrush(baseLinearGradient);
#     painter.drawEllipse(btnRect);

#     QPen pen = QPen();
#     pen.setColor(Qt::white);
#     painter.setPen(pen);

#     QFont font = QFont();
#     font.setBold(true);
#     font.setPixelSize(fontSize);
#     painter.setFont(font);
#     QFontMetricsF fontMetrics = QFontMetricsF(font);
#     float textWidth = fontMetrics.size(Qt::TextSingleLine, "BTN").width();
#     painter.drawText(int(rect().width()/2-textWidth/2), int(rect().height()/2+5), "BTN");
# }

# void QtBoxStylePushButton10::mousePressEvent(QMouseEvent *event)
# {
#     if (event->button() != Qt::LeftButton || !btnRect.contains(event->pos())) {
#         return;
#     }
#     btnState = "on";
#     update();
# }

# void QtBoxStylePushButton10::mouseReleaseEvent(QMouseEvent *event)
# {
#     btnState = "off";
#     update();
# }
# C++/Qt