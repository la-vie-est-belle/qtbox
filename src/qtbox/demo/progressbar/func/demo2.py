# PyQt
from PyQt5.QtWidgets import QProgressBar
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QProgressBar = createWidgetMenuBase(QProgressBar)

class QtBoxFuncProgressBar2(QProgressBar):
    def __init__(self):
        super(QtBoxFuncProgressBar2, self).__init__(str(Path(__file__)))
        self.setInvertedAppearance(True)
        self.setRange(0, 100)
        self.setValue(80)
# PyQt

# PySide
# from PySide2.QtWidgets import QProgressBar


# class QtBoxFuncProgressBar2(QProgressBar):
#     def __init__(self):
#         super(QtBoxFuncProgressBar2, self).__init__()
#         self.setInvertedAppearance(True)
#         self.setRange(0, 100)
#         self.setValue(80)
# PySide

# C++/Qt
# #ifndef QTBOXFUNCPROGRESSBAR2_H
# #define QTBOXFUNCPROGRESSBAR2_H
# #include <QProgressBar>

# class QtBoxFuncProgressBar2 : public QProgressBar
# {
#     Q_OBJECT

# public:
#     QtBoxFuncProgressBar2(QWidget *parent = nullptr);
# };
# #endif // QTBOXFUNCPROGRESSBAR2_H



# #include "qtboxfuncprogressbar2.h"

# QtBoxFuncProgressBar2::QtBoxFuncProgressBar2(QWidget *parent)
#     : QProgressBar(parent)
# {
#     setInvertedAppearance(true);
#     setRange(0, 100);
#     setValue(80);
# }
# C++/Qt