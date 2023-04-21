# PyQt
from PyQt5.QtWidgets import QSpinBox
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QSpinBox = createWidgetMenuBase(QSpinBox)

class QtBoxFuncSpinBox1(QSpinBox):
    def __init__(self):
        super(QtBoxFuncSpinBox1, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 30)
        self.setPrefix("Sth: ")
        self.setSuffix(" PCS")
# PyQt

# PySide
# from PySide2.QtWidgets import QSpinBox


# class QtBoxFuncSpinBox1(QSpinBox):
#     def __init__(self):
#         super(QtBoxFuncSpinBox1, self).__init__(str(Path(__file__)))
#         self.setFixedSize(150, 30)
#         self.setPrefix("Sth: ")
#         self.setSuffix(" PCS")
# PySide

# C++/Qt
# #ifndef QTBOXFUNCSPINBOX1_H
# #define QTBOXFUNCSPINBOX1_H
# #include <QSpinBox>

# class QtBoxFuncSpinBox1 : public QSpinBox
# {
#     Q_OBJECT

# public:
#     QtBoxFuncSpinBox1(QWidget *parent = nullptr);
# };
# #endif // QTBOXFUNCSPINBOX1_H



# #include "qtboxfuncspinbox1.h"

# QtBoxFuncSpinBox1::QtBoxFuncSpinBox1(QWidget *parent)
#     : QSpinBox(parent)
# {
#     setFixedSize(150, 30);
#     setPrefix("Sth: ");
#     setSuffix(" PCS");
# }
# C++/Qt