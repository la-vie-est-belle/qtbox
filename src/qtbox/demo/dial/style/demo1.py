# PyQt
from PyQt5.QtWidgets import QDial
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QDial = createWidgetMenuBase(QDial)

class QtBoxStyleDial1(QDial):
    def __init__(self):
        super(QtBoxStyleDial1, self).__init__(str(Path(__file__)))
        self.setStyleSheet("""
        QDial {
            background-color: gray;
        }
        """)
# PyQt

# PySide
# from PySide2.QtWidgets import QDial


# class QtBoxStyleDial1(QDial):
#     def __init__(self):
#         super(QtBoxStyleDial1, self).__init__(str(Path(__file__)))
#         self.setStyleSheet("""
#         QDial {
#             background-color: gray;
#         }
#         """)
# PySide

# C++/Qt
# #ifndef QTBOXSTYLEDIAL1_H
# #define QTBOXSTYLEDIAL1_H
# #include <QDial>

# class QtBoxStyleDial1 : public QDial
# {
#     Q_OBJECT

# public:
#     QtBoxStyleDial1(QWidget *parent = nullptr);
# };
# #endif // QTBOXSTYLEDIAL1_H



# #include "qtboxstyledial1.h"

# QtBoxStyleDial1::QtBoxStyleDial1(QWidget *parent)
#     : QDial(parent)
# {
#     setStyleSheet("QDial {background-color: gray}");
# }
# C++/Qt