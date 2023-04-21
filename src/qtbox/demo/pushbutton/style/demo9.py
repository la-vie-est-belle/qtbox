# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QGraphicsDropShadowEffect
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QPushButton = createWidgetMenuBase(QPushButton)

class QtBoxStyleButton9(QPushButton):
    def __init__(self):
        super(QtBoxStyleButton9, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 40)
        self.setText("BUTTON")
        self.add_shadow()

    def add_shadow(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setOffset(3, 3)
        shadow.setColor(Qt.gray)
        self.setGraphicsEffect(shadow)
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QPushButton, QGraphicsDropShadowEffect


# class QtBoxStyleButton9(QPushButton):
#     def __init__(self):
#         super(QtBoxStyleButton9, self).__init__()
#         self.setFixedSize(150, 40)
#         self.setText("BUTTON")
#         self.add_shadow()

#     def add_shadow(self):
#         shadow = QGraphicsDropShadowEffect(self)
#         shadow.setBlurRadius(15)
#         shadow.setOffset(3, 3)
#         shadow.setColor(Qt.gray)
#         self.setGraphicsEffect(shadow)
# PySide

# C++/Qt
# #ifndef QTBOXSTYLEPUSHBUTTON9_H
# #define QTBOXSTYLEPUSHBUTTON9_H
# #include <QPushButton>

# class QtBoxStylePushButton9 : public QPushButton
# {
#     Q_OBJECT

# public:
#     QtBoxStylePushButton9(QWidget *parent = nullptr);

# private:
#     void addShadow();
# };
# #endif // QTBOXSTYLEPUSHBUTTON9_H



# #include "qtboxstylepushbutton9.h"
# #include <QGraphicsDropShadowEffect>

# QtBoxStylePushButton9::QtBoxStylePushButton9(QWidget *parent)
#     : QPushButton(parent)
# {
#     setFixedSize(150, 40);
#     setText("BUTTON");
#     addShadow();
# }

# void QtBoxStylePushButton9::addShadow()
# {
#     QGraphicsDropShadowEffect *shadow = new QGraphicsDropShadowEffect(this);
#     shadow->setBlurRadius(15);
#     shadow->setOffset(3, 3);
#     shadow->setColor(Qt::gray);
#     setGraphicsEffect(shadow);
# }
# C++/Qt