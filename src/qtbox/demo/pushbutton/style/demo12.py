# PyQt
from PyQt5.QtCore import pyqtProperty, QPropertyAnimation
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QColor
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QPushButton = createWidgetMenuBase(QPushButton)

class QtBoxStyleButton12(QPushButton):
    def __init__(self):
        super(QtBoxStyleButton12, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 40)
        self.setText("BUTTON")
        self._color = QColor()

        self.color_anim = QPropertyAnimation(self, b"color")
        self.color_anim.setDuration(6000)
        self.color_anim.setStartValue(QColor(0, 0, 0))
        self.color_anim.setEndValue(QColor(255, 255, 255))
        self.color_anim.start()

    @pyqtProperty(QColor)
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
        red = value.red()
        green = value.green()
        blue = value.blue()
        self.setStyleSheet(f"background-color: rgb({red}, {green}, {blue})")
# PyQt

# PySide
# from PySide2.QtCore import Property, QPropertyAnimation
# from PySide2.QtWidgets import QPushButton
# from PySide2.QtGui import QColor


# class QtBoxStyleButton12(QPushButton):
#     def __init__(self):
#         super(QtBoxStyleButton12, self).__init__()
#         self.setFixedSize(150, 40)
#         self.setText("BUTTON")
#         self._color = QColor()

#         self.color_anim = QPropertyAnimation(self, b"color")
#         self.color_anim.setDuration(6000)
#         self.color_anim.setStartValue(QColor(0, 0, 0))
#         self.color_anim.setEndValue(QColor(255, 255, 255))
#         self.color_anim.start()

#     @Property(QColor)
#     def color(self):
#         return self._color

#     @color.setter
#     def color(self, value):
#         self._color = value
#         red = value.red()
#         green = value.green()
#         blue = value.blue()
#         self.setStyleSheet(f"background-color: rgb({red}, {green}, {blue})")
# PySide

# C++/Qt
# #ifndef QTBOXSTYLEPUSHBUTTON12_H
# #define QTBOXSTYLEPUSHBUTTON12_H
# #include <QPushButton>
# #include <QColor>

# class QtBoxStylePushButton12 : public QPushButton
# {
#     Q_OBJECT
#     Q_PROPERTY(QColor color READ color WRITE setColor);

# public:
#     QtBoxStylePushButton12(QWidget *parent = nullptr);
#     QColor color() const;
#     void setColor(const QColor &value);

# private:
#     QColor _color;
# };
# #endif // QTBOXSTYLEPUSHBUTTON12_H



# #include "qtboxstylepushbutton12.h"
# #include <QPropertyAnimation>

# QtBoxStylePushButton12::QtBoxStylePushButton12(QWidget *parent)
#     : QPushButton(parent)
# {
#     setFixedSize(150, 40);
#     setText("BUTTON");

#     QPropertyAnimation *colorAnim = new QPropertyAnimation(this, "color");
#     colorAnim->setDuration(1000);
#     colorAnim->setStartValue(QColor(0, 0, 0));
#     colorAnim->setEndValue(QColor(255, 255, 255));
#     colorAnim->start();
# }

# QColor QtBoxStylePushButton12::color() const
# {
#     return _color;
# }

# void QtBoxStylePushButton12::setColor(const QColor &value)
# {
#     _color = value;
#     int red = value.red();
#     int green = value.green();
#     int blue = value.blue();
#     setStyleSheet(QString("background-color: rgb(%1, %2, %3)").arg(QString::number(red), QString::number(green), QString::number(blue)));
# }
# C++/Qt