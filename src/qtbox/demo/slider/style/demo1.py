# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSlider
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QSlider = createWidgetMenuBase(QSlider)

class QtBoxStyleSlider1(QSlider):
    def __init__(self):
        super(QtBoxStyleSlider1, self).__init__(str(Path(__file__)))
        self.setOrientation(Qt.Horizontal)
        self.setStyleSheet("""
        QSlider::groove:horizontal {
            border: none;
            height: 2px;
            background-color: lightgray;
        }

        QSlider::handle:horizontal {
            background-color: #2f77cb;
            width: 8px;
            margin: -9px 0px -9px 0px;
            border-radius: 4px;
        }

        QSlider::sub-page:horizontal {
            background-color: #4898ec;
        }
        """)
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QSlider


# class QtBoxStyleSlider1(QSlider):
#     def __init__(self):
#         super(QtBoxStyleSlider1, self).__init__()
#         self.setOrientation(Qt.Horizontal)
#         self.setStyleSheet("""
#         QSlider::groove:horizontal {
#             border: none;
#             height: 2px;
#             background-color: lightgray;
#         }

#         QSlider::handle:horizontal {
#             background-color: #2f77cb;
#             width: 8px;
#             margin: -9px 0px -9px 0px;
#             border-radius: 4px;
#         }

#         QSlider::sub-page:horizontal {
#             background-color: #4898ec;
#         }
#         """)
# PySide

# C++/Qt
# #ifndef QTBOXSTYLESLIDER1_H
# #define QTBOXSTYLESLIDER1_H
# #include <QSlider>

# class QtBoxStyleSlider1 : public QSlider
# {
#     Q_OBJECT

# public:
#     QtBoxStyleSlider1(QWidget *parent = nullptr);
# };
# #endif // QTBOXSTYLESLIDER1_H



# #include "qtboxstyleslider1.h"

# QtBoxStyleSlider1::QtBoxStyleSlider1(QWidget *parent)
#     : QSlider(parent)
# {
#     setOrientation(Qt::Horizontal);
#     setStyleSheet(R"(
#     QSlider::groove:horizontal {
#         border: none;
#         height: 2px;
#         background-color: lightgray;
#     }

#     QSlider::handle:horizontal {
#         background-color: #2f77cb;
#         width: 8px;
#         margin: -9px 0px -9px 0px;
#         border-radius: 4px;
#     }
#
#     QSlider::sub-page:horizontal {
#         background-color: #4898ec;
#     }
#     )");
# }
# C++/Qt