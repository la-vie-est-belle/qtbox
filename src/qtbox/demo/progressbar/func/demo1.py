# PyQt
from PyQt5.QtWidgets import QProgressBar
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QProgressBar = createWidgetMenuBase(QProgressBar)

class QtBoxFuncProgressBar1(QProgressBar):
    def __init__(self):
        super(QtBoxFuncProgressBar1, self).__init__(str(Path(__file__)))
        self.setRange(0, 0)
# PyQt

# PySide
# from PySide2.QtWidgets import QProgressBar


# class QtBoxFuncProgressBar1(QProgressBar):
#     def __init__(self):
#         super(QtBoxFuncProgressBar1, self).__init__()
#         self.setRange(0, 0)
# PySide

# C++/Qt
# #ifndef QTBOXFUNCPROGRESSBAR1_H
# #define QTBOXFUNCPROGRESSBAR1_H
# #include <QProgressBar>

# class QtBoxFuncProgressBar1 : public QProgressBar
# {
#     Q_OBJECT

# public:
#     QtBoxFuncProgressBar1(QWidget *parent = nullptr);
# };
# #endif // QTBOXFUNCPROGRESSBAR1_H



# #include "qtboxfuncprogressbar1.h"

# QtBoxFuncProgressBar1::QtBoxFuncProgressBar1(QWidget *parent)
#     : QProgressBar(parent)
# {
#     setRange(0, 0);
# }
# C++/Qt
