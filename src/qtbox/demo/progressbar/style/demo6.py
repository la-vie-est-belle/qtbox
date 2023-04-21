# PyQt
from PyQt5.QtWidgets import QProgressBar
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QProgressBar = createWidgetMenuBase(QProgressBar)

class QtBoxStyleProgressBar6(QProgressBar):
    def __init__(self):
        super(QtBoxStyleProgressBar6, self).__init__(str(Path(__file__)))
        self.setTextVisible(False)
        self.setRange(0, 100)
        self.setValue(80)
        self.setStyleSheet("""
        QProgressBar {
            background-color: #c2c6c9;
            border: 2px solid #b0b4b7;
            border-right: 2px solid #d5d8dd;
            border-bottom: 2px solid #d5d8dd;
            border-radius: 2px;
        }

        QProgressBar::chunk {
            background-color: #0c107b;
            border-radius: 1px;
            width: 9px;
            margin: 0.5px;
        }
        """)
# PyQt

# PySide
# from PySide2.QtWidgets import QProgressBar


# class QtBoxStyleProgressBar6(QProgressBar):
#     def __init__(self):
#         super(QtBoxStyleProgressBar6, self).__init__()
#         self.setTextVisible(False)
#         self.setRange(0, 100)
#         self.setValue(80)
#         self.setStyleSheet("""
#         QProgressBar {
#             background-color: #c2c6c9;
#             border: 2px solid #b0b4b7;
#             border-right: 2px solid #d5d8dd;
#             border-bottom: 2px solid #d5d8dd;
#             border-radius: 2px;
#         }

#         QProgressBar::chunk {
#             background-color: #0c107b;
#             border-radius: 1px;
#             width: 9px;
#             margin: 0.5px;
#         }
#         """)
# PySide

# C++/Qt
# #ifndef QTBOXSTYLEPROGRESSBAR6_H
# #define QTBOXSTYLEPROGRESSBAR6_H
# #include <QProgressBar>

# class QtBoxStyleProgressBar6 : public QProgressBar
# {
#     Q_OBJECT

# public:
#     QtBoxStyleProgressBar6(QWidget *parent = nullptr);
# };
# #endif // QTBOXSTYLEPROGRESSBAR6_H



# #include "qtboxstyleprogressbar6.h"

# QtBoxStyleProgressBar6::QtBoxStyleProgressBar6(QWidget *parent)
#     : QProgressBar(parent)
# {
#     setTextVisible(false);
#     setRange(0, 100);
#     setValue(80);
#     setStyleSheet(R"(
#     QProgressBar {
#         background-color: #c2c6c9;
#         border: 2px solid #b0b4b7;
#         border-right: 2px solid #d5d8dd;
#         border-bottom: 2px solid #d5d8dd;
#         border-radius: 2px;
#     }

#     QProgressBar::chunk {
#         background-color: #0c107b;
#         border-radius: 1px;
#         width: 9px;
#         margin: 0.5px;
#     }
#     )");
# }
# C++/Qt