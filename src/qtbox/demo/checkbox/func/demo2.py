# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QCheckBox
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QCheckBox = createWidgetMenuBase(QCheckBox)

class QtBoxFuncCheckBox2(QCheckBox):
    def __init__(self):
        super(QtBoxFuncCheckBox2, self).__init__(str(Path(__file__)))
        self.setText("Text on the left")
        self.setLayoutDirection(Qt.RightToLeft)
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QCheckBox


# class QtBoxFuncCheckBox2(QCheckBox):
#     def __init__(self):
#         super(QtBoxFuncCheckBox2, self).__init__()
#         self.setText("Text on the left")
#         self.setLayoutDirection(Qt.RightToLeft)
# PySide

# C++/Qt
# #ifndef QTBOXFUNCCHECKBOX2_H
# #define QTBOXFUNCCHECKBOX2_H
# #include <QCheckBox>

# class QtBoxFuncCheckBox2 : public QCheckBox
# {
#     Q_OBJECT

# public:
#     QtBoxFuncCheckBox2(QWidget *parent = nullptr);
# };
# #endif // QTBOXFUNCCHECKBOX2_H



# #include "qtboxfunccheckbox2.h"
# #include <Qt>

# QtBoxFuncCheckBox2::QtBoxFuncCheckBox2(QWidget *parent)
#     : QCheckBox(parent)
# {
#     setText("Text on the left");
#     setLayoutDirection(Qt::RightToLeft);
# }
# C++/Qt