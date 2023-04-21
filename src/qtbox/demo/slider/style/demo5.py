# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSlider
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QSlider = createWidgetMenuBase(QSlider)

class QtBoxStyleSlider5(QSlider):
    def __init__(self):
        super(QtBoxStyleSlider5, self).__init__(str(Path(__file__)))
        self.setOrientation(Qt.Horizontal)
        self.setStyleSheet("""
        QSlider::groove:horizontal {
            border: none;
            height: 10px;
            background-color: lightgray;
            border-radius: 5px;
        }

        QSlider::handle:horizontal {
            width: 4px;
            margin: -1px 0px -1px -5px;
            border-radius: 1px;
            background-color: white;
        }

        QSlider::sub-page:horizontal {
            background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);
            border-radius: 5px;
        }
        """)
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QSlider


# class QtBoxStyleSlider5(QSlider):
#     def __init__(self):
#         super(QtBoxStyleSlider5, self).__init__()
#         self.setOrientation(Qt.Horizontal)
#         self.setStyleSheet("""
#         QSlider::groove:horizontal {
#             border: none;
#             height: 10px;
#             background-color: lightgray;
#             border-radius: 5px;
#         }

#         QSlider::handle:horizontal {
#             width: 4px;
#             margin: -1px 0px -1px -5px;
#             border-radius: 1px;
#             background-color: white;
#         }

#         QSlider::sub-page:horizontal {
#             background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);
#             border-radius: 5px;
#         }
#         """)
# PySide

# C++/Qt
# #ifndef QTBOXSTYLESLIDER5_H
# #define QTBOXSTYLESLIDER5_H
# #include <QSlider>

# class QtBoxStyleSlider5 : public QSlider
# {
#     Q_OBJECT

# public:
#     QtBoxStyleSlider5(QWidget *parent = nullptr);
# };
# #endif // QTBOXSTYLESLIDER5_H



# #include "qtboxstyleslider5.h"

# QtBoxStyleSlider5::QtBoxStyleSlider5(QWidget *parent)
#     : QSlider(parent)
# {
#     setOrientation(Qt::Horizontal);
#     setStyleSheet(R"(
#     QSlider::groove:horizontal {
#         border: none;
#         height: 10px;
#         background-color: lightgray;
#         border-radius: 5px;
#     }

#     QSlider::handle:horizontal {
#         width: 4px;
#         margin: -1px 0px -1px -5px;
#         border-radius: 1px;
#         background-color: white;
#     }

#     QSlider::sub-page:horizontal {
#         background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);
#         border-radius: 5px;
#     }
#     )");
# }
# C++/Qt