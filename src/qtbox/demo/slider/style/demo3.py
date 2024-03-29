# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSlider
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QSlider = createWidgetMenuBase(QSlider)

class QtBoxStyleSlider3(QSlider):
    def __init__(self):
        super(QtBoxStyleSlider3, self).__init__(str(Path(__file__)))
        self.setOrientation(Qt.Horizontal)
        self.setStyleSheet("""
        QSlider::groove:horizontal {
            border: none;
            height: 2px;
            background-color: lightgray;
        }

        QSlider::handle:horizontal {
            background-color: #f1964c;
            width: 16px;
            margin: -8px 0px -8px 0px;
            border-radius: 8px;
        }

        QSlider::sub-page:horizontal {
            background-color: #f1964c;
        }
        """)
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QSlider


# class QtBoxStyleSlider3(QSlider):
#     def __init__(self):
#         super(QtBoxStyleSlider3, self).__init__()
#         self.setOrientation(Qt.Horizontal)
#         self.setStyleSheet("""
#         QSlider::groove:horizontal {
#             border: none;
#             height: 2px;
#             background-color: lightgray;
#         }

#         QSlider::handle:horizontal {
#             background-color: #f1964c;
#             width: 16px;
#             margin-top: -8px 0px -8px 0px;
#             border-radius: 8px;
#         }

#         QSlider::sub-page:horizontal {
#             background-color: #f1964c;
#         }
#         """)
# PySide

# C++/Qt
# #ifndef QTBOXSTYLESLIDER3_H
# #define QTBOXSTYLESLIDER3_H
# #include <QSlider>

# class QtBoxStyleSlider3 : public QSlider
# {
#     Q_OBJECT

# public:
#     QtBoxStyleSlider3(QWidget *parent = nullptr);
# };
# #endif // QTBOXSTYLESLIDER3_H



# #include "qtboxstyleslider3.h"

# QtBoxStyleSlider3::QtBoxStyleSlider3(QWidget *parent)
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
#         background-color: #f1964c;
#         width: 16px;
#         margin: -8px 0px -8px 0px;
#         border-radius: 8px;
#     }

#     QSlider::sub-page:horizontal {
#         background-color: #f1964c;
#     }
#     )");
# }
# C++/Qt