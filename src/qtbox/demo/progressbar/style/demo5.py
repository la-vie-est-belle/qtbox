# PyQt
from PyQt5.QtWidgets import QProgressBar
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QProgressBar = createWidgetMenuBase(QProgressBar)

class QtBoxStyleProgressBar5(QProgressBar):
    def __init__(self):
        super(QtBoxStyleProgressBar5, self).__init__(str(Path(__file__)))
        self.setTextVisible(False)
        self.setRange(0, 100)
        self.setValue(80)
        self.setStyleSheet("""
        QProgressBar {
            border: 1px solid lightgray;
            border-radius: 3px;
            background-color: qlineargradient(x1:1, y1:0, x2:1, y2:0.4, stop:0 white, stop:1 #dedede);
        }

        QProgressBar::chunk {
            background-color: qlineargradient(x1:1, y1:0, x2:1, y2:0.4, stop:0 white, stop:1 #64d651);
            border-radius： 2px;
        }
        """)
# PyQt

# PySide
# from PySide2.QtWidgets import QProgressBar


# class QtBoxStyleProgressBar5(QProgressBar):
#     def __init__(self):
#         super(QtBoxStyleProgressBar5, self).__init__()
#         self.setTextVisible(False)
#         self.setRange(0, 100)
#         self.setValue(80)
#         self.setStyleSheet("""
#         QProgressBar {
#             border: 1px solid lightgray;
#             border-radius: 3px;
#             background-color: qlineargradient(x1:1, y1:0, x2:1, y2:0.4, stop:0 white, stop:1 #dedede);
#         }

#         QProgressBar::chunk {
#             background-color: qlineargradient(x1:1, y1:0, x2:1, y2:0.4, stop:0 white, stop:1 #64d651);
#             border-radius： 2px;
#         }
#         """)
# PySide

# C++/Qt
# #ifndef QTBOXSTYLEPROGRESSBAR5_H
# #define QTBOXSTYLEPROGRESSBAR5_H
# #include <QProgressBar>

# class QtBoxStyleProgressBar5 : public QProgressBar
# {
#     Q_OBJECT

# public:
#     QtBoxStyleProgressBar5(QWidget *parent = nullptr);
# };
# #endif // QTBOXSTYLEPROGRESSBAR5_H



# #include "qtboxstyleprogressbar5.h"

# QtBoxStyleProgressBar5::QtBoxStyleProgressBar5(QWidget *parent)
#     : QProgressBar(parent)
# {
#     setTextVisible(false);
#     setRange(0, 100);
#     setValue(80);
#     setStyleSheet(R"(
#     QProgressBar {
#         border: 1px solid lightgray;
#         border-radius: 3px;
#         background-color: qlineargradient(x1:1, y1:0, x2:1, y2:0.4, stop:0 white, stop:1 #dedede);
#     }

#     QProgressBar::chunk {
#         background-color: qlineargradient(x1:1, y1:0, x2:1, y2:0.4, stop:0 white, stop:1 #64d651);
#         border-radius： 2px;
#     }
#     )");
# }
# C++/Qt