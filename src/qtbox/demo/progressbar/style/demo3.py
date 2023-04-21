# PyQt
from PyQt5.QtWidgets import QProgressBar
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QProgressBar = createWidgetMenuBase(QProgressBar)

class QtBoxStyleProgressBar3(QProgressBar):
    def __init__(self):
        super(QtBoxStyleProgressBar3, self).__init__(str(Path(__file__)))
        self.setRange(0, 100)
        self.setValue(80)
        self.setStyleSheet("""
        QProgressBar {
            border: 2px solid white;
            background-color: black;
            padding-left: 2px;
            padding-right: 2px;
            text-align: center;
        }

        QProgressBar::chunk {
            background-color: white;
            margin-top: 2px;
            margin-bottom: 2px;
        }
        """)
# PyQt

# PySide
# from PySide2.QtWidgets import QProgressBar


# class QtBoxStyleProgressBar3(QProgressBar):
#     def __init__(self):
#         super(QtBoxStyleProgressBar3, self).__init__()
#         self.setRange(0, 100)
#         self.setValue(80)
#         self.setStyleSheet("""
#         QProgressBar {
#             border: 2px solid white;
#             background-color: black;
#             padding-left: 2px;
#             padding-right: 2px;
#             text-align: center;
#         }

#         QProgressBar::chunk {
#             background-color: white;
#             margin-top: 2px;
#             margin-bottom: 2px;
#         }
#         """)
# PySide

# C++/Qt
# #ifndef QTBOXSTYLEPROGRESSBAR3_H
# #define QTBOXSTYLEPROGRESSBAR3_H
# #include <QProgressBar>

# class QtBoxStyleProgressBar3 : public QProgressBar
# {
#     Q_OBJECT

# public:
#     QtBoxStyleProgressBar3(QWidget *parent = nullptr);
# };
# #endif // QTBOXSTYLEPROGRESSBAR3_H



# #include "qtboxstyleprogressbar3.h"

# QtBoxStyleProgressBar3::QtBoxStyleProgressBar3(QWidget *parent)
#     : QProgressBar(parent)
# {
#     setRange(0, 100);
#     setValue(80);
#     setStyleSheet(R"(
#     QProgressBar {
#         border: 2px solid white;
#         background-color: black;
#         padding-left: 2px;
#         padding-right: 2px;
#         text-align: center;
#     }

#     QProgressBar::chunk {
#         background-color: white;
#         margin-top: 2px;
#         margin-bottom: 2px;
#     }
#     )");
# }
# C++/Qt