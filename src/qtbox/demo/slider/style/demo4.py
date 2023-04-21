# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSlider
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QSlider = createWidgetMenuBase(QSlider)
PATH_TO_IMG = str(Path(__file__).parent.parent.parent.parent / "res/images/basketball.png").replace("\\", "/")

class QtBoxStyleSlider4(QSlider):
    def __init__(self):
        super(QtBoxStyleSlider4, self).__init__(str(Path(__file__)))
        self.setOrientation(Qt.Horizontal)
        self.setStyleSheet("""
        QSlider::groove:horizontal {
            border: none;
            height: 2px;
            background-color: lightgray;
        }

        QSlider::handle:horizontal {
            border-image: url(%s);
            width: 20px;
            margin: -10px -2px -10px -2px;
        }

        QSlider::sub-page:horizontal {
            background-color: #ef7067;
        }
        """ % (PATH_TO_IMG))
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QSlider


# class QtBoxStyleSlider4(QSlider):
#     def __init__(self):
#         super(QtBoxStyleSlider4, self).__init__()
#         self.setOrientation(Qt.Horizontal)
#         self.setStyleSheet("""
#         QSlider::groove:horizontal {
#             border: none;
#             height: 2px;
#             background-color: lightgray;
#         }

#         QSlider::handle:horizontal {
#             border-image: url(%s);
#             width: 20px;
#             margin: -10px -2px -10px -2px;
#         }

#         QSlider::sub-page:horizontal {
#             background-color: #ef7067;
#         }
#         """ % (PATH_TO_IMG))
# PySide

# C++/Qt
# #ifndef QTBOXSTYLESLIDER4_H
# #define QTBOXSTYLESLIDER4_H
# #include <QSlider>

# class QtBoxStyleSlider4 : public QSlider
# {
#     Q_OBJECT

# public:
#     QtBoxStyleSlider4(QWidget *parent = nullptr);
# };
# #endif // QTBOXSTYLESLIDER4_H



# #include "qtboxstyleslider4.h"

# QtBoxStyleSlider4::QtBoxStyleSlider4(QWidget *parent)
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
#         border-image: url(PATH_TO_IMG);
#         width: 20px;
#         margin: -10px -2px -10px -2px;
#     }

#     QSlider::sub-page:horizontal {
#         background-color: #ef7067;
#     }
#     )");
# }
# C++/Qt