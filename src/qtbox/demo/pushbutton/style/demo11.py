# PyQt
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPainter, QPen, QColor, QFont
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QPushButton = createWidgetMenuBase(QPushButton)

class QtBoxStyleButton11(QPushButton):
    def __init__(self):
        super(QtBoxStyleButton11, self).__init__(str(Path(__file__)))
        self.btn_state = "off"
        self.setFixedSize(90, 90)
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        if self.btn_state == "on":
            font_size = 15
            shadow_color = QColor(176, 176, 176)
            white_part_color = QColor(238, 238, 238)
        else:
            font_size = 16
            shadow_color = QColor(208, 208, 208)
            white_part_color = QColor(252, 252, 252)

        painter.setPen(Qt.NoPen)
        painter.setBrush(shadow_color)
        btn_shadow_part_rect = self.rect()
        painter.drawRoundedRect(btn_shadow_part_rect, 5, 5)

        offset = 20
        btn_white_part_rect = QRectF(self.rect().left()+offset/2, self.rect().top()+offset/4, self.rect().width()-offset, self.rect().height()-offset)
        painter.setBrush(white_part_color)
        painter.drawRoundedRect(btn_white_part_rect, 5, 5)

        pen = QPen()
        pen.setColor(Qt.black)
        painter.setPen(pen)

        font = QFont()
        font.setBold(True)
        font.setPixelSize(font_size)
        painter.setFont(font)
        painter.drawText(int(btn_white_part_rect.x()+2), int(btn_white_part_rect.y()+font_size), "BTN")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setFixedSize(86, 86)
            self.btn_state = "on"
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setFixedSize(90, 90)
            self.btn_state = "off"
            self.update()
# PyQt

# PySide
# from PySide2.QtCore import Qt, QRectF
# from PySide2.QtWidgets import QPushButton
# from PySide2.QtGui import QPainter, QPen, QColor, QFont


# class QtBoxStyleButton11(QPushButton):
#     def __init__(self):
#         super(QtBoxStyleButton11, self).__init__()
#         self.btn_state = "off"
#         self.setFixedSize(90, 90)
#         self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.Antialiasing)

#         if self.btn_state == "on":
#             font_size = 15
#             shadow_color = QColor(176, 176, 176)
#             white_part_color = QColor(238, 238, 238)
#         else:
#             font_size = 16
#             shadow_color = QColor(208, 208, 208)
#             white_part_color = QColor(252, 252, 252)

#         painter.setPen(Qt.NoPen)
#         painter.setBrush(shadow_color)
#         btn_shadow_part_rect = self.rect()
#         painter.drawRoundedRect(btn_shadow_part_rect, 5, 5)

#         offset = 20
#         btn_white_part_rect = QRectF(self.rect().left() + offset / 2, self.rect().top() + offset / 4, self.rect().width() - offset, self.rect().height() - offset)
#         painter.setBrush(white_part_color)
#         painter.drawRoundedRect(btn_white_part_rect, 5, 5)

#         pen = QPen()
#         pen.setColor(Qt.black)
#         painter.setPen(pen)

#         font = QFont()
#         font.setBold(True)
#         font.setPixelSize(font_size)
#         painter.setFont(font)
#         painter.drawText(int(btn_white_part_rect.x() + 2), int(btn_white_part_rect.y() + font_size), "BTN")

#     def mousePressEvent(self, event):
#         if event.button() == Qt.LeftButton:
#             self.setFixedSize(86, 86)
#             self.btn_state = "on"
#             self.update()

#     def mouseReleaseEvent(self, event):
#         if event.button() == Qt.LeftButton:
#             self.setFixedSize(90, 90)
#             self.btn_state = "off"
#             self.update()
# PySide

# C++/Qt
# #ifndef QTBOXSTYLEPUSHBUTTON11_H
# #define QTBOXSTYLEPUSHBUTTON11_H
# #include <QPushButton>
# #include <QPaintEvent>
# #include <QMouseEvent>
# #include <QString>

# class QtBoxStylePushButton11 : public QPushButton
# {
#     Q_OBJECT

# public:
#     QtBoxStylePushButton11(QWidget *parent = nullptr);

# protected:
#     void paintEvent(QPaintEvent *event);
#     void mousePressEvent(QMouseEvent *event);
#     void mouseReleaseEvent(QMouseEvent *event);

# private:
#     QString btnState = "off";
# };
# #endif // QTBOXSTYLEPUSHBUTTON11_H



# #include "qtboxstylepushbutton11.h"
# #include <QFontMetricsF>
# #include <QPainter>
# #include <QColor>
# #include <QRectF>
# #include <QFont>
# #include <QRect>
# #include <Qt>

# QtBoxStylePushButton11::QtBoxStylePushButton11(QWidget *parent)
#     : QPushButton(parent)
# {
#     setFixedSize(90, 90);
#     setWindowFlags(Qt::WindowCloseButtonHint | Qt::MSWindowsFixedSizeDialogHint);
# }

# void QtBoxStylePushButton11::paintEvent(QPaintEvent *event)
# {
#     QPainter painter = QPainter(this);
#     painter.setRenderHint(QPainter::Antialiasing);

#     int fontSize;
#     QColor shadowColor;
#     QColor whitePartColor;
#     if (btnState == "on") {
#         fontSize = 15;
#         shadowColor = QColor(176, 176, 176);
#         whitePartColor = QColor(238, 238, 238);
#     }
#     else {
#         fontSize = 16;
#         shadowColor = QColor(208, 208, 208);
#         whitePartColor = QColor(252, 252, 252);
#     }

#     painter.setPen(Qt::NoPen);
#     painter.setBrush(shadowColor);
#     QRectF btnShadowPartRect = rect();
#     painter.drawRoundedRect(btnShadowPartRect, 5, 5);

#     int offset = 20;
#     QRectF btnWhitePartRect = QRectF(rect().left()+offset/2, rect().top()+offset/4, rect().width()-offset, rect().height()-offset);
#     painter.setBrush(whitePartColor);
#     painter.drawRoundedRect(btnWhitePartRect, 5, 5);

#     QPen pen = QPen();
#     pen.setColor(Qt::black);
#     painter.setPen(pen);

#     QFont font = QFont();
#     font.setBold(true);
#     font.setPixelSize(fontSize);
#     painter.setFont(font);
#     painter.drawText(int(btnWhitePartRect.x()+2), int(btnWhitePartRect.y()+fontSize), "BTN");
# }

# void QtBoxStylePushButton11::mousePressEvent(QMouseEvent *event)
# {
#     if (event->button() == Qt::LeftButton) {
#         setFixedSize(86, 86);
#         btnState = "on";
#         update();
#     }
# }

# void QtBoxStylePushButton11::mouseReleaseEvent(QMouseEvent *event)
# {
#     if (event->button() == Qt::LeftButton) {
#         setFixedSize(90, 90);
#         btnState = "off";
#         update();
#     }
# }
# C++/Qt