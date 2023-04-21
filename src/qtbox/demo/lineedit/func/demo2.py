# PyQt
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import QRegExp
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QLineEdit = createWidgetMenuBase(QLineEdit)

class QtBoxFuncLineEdit2(QLineEdit):
    def __init__(self):
        super(QtBoxFuncLineEdit2, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 30)
        self.setPlaceholderText("Numbers only")

        reg_exp = QRegExp("[0-9]+")
        self.setValidator(QRegExpValidator(reg_exp))
# PyQt

# PySide
# from PySide2.QtGui import QRegExpValidator
# from PySide2.QtWidgets import QLineEdit
# from PySide2.QtCore import QRegExp


# class QtBoxFuncLineEdit2(QLineEdit):
#     def __init__(self):
#         super(QtBoxFuncLineEdit2, self).__init__()
#         self.setFixedSize(150, 30)
#         self.setPlaceholderText("Numbers only")

#         reg_exp = QRegExp("[0-9]+")
#         self.setValidator(QRegExpValidator(reg_exp))
# PySide

# C++/Qt
# #ifndef QTBOXFUNCLINEEDIT2_H
# #define QTBOXFUNCLINEEDIT2_H
# #include <QLineEdit>

# class QtBoxFuncLineEdit2 : public QLineEdit
# {
#     Q_OBJECT

# public:
#     QtBoxFuncLineEdit2(QWidget *parent = nullptr);
# };
# #endif // QTBOXFUNCLINEEDIT2_H



# #include "qtboxfunclineedit2.h"
# #include <QRegularExpressionValidator>
# #include <QRegularExpression>

# QtBoxFuncLineEdit2::QtBoxFuncLineEdit2(QWidget *parent)
#     : QLineEdit(parent)
# {
#     setFixedSize(150, 30);
#     setPlaceholderText("Numbers Only");
#
#     QRegularExpression regExp = QRegularExpression("[0-9]+");
#     setValidator(new QRegularExpressionValidator(regExp));
# }
# C++/Qt