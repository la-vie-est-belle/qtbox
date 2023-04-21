# PyQt
from PyQt5.QtWidgets import QPushButton
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QPushButton = createWidgetMenuBase(QPushButton)

class QtBoxStyleButton1(QPushButton):
    def __init__(self):
        super(QtBoxStyleButton1, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 50)
        self.setText("BUTTON")
        self.setStyleSheet("""
        QPushButton {
            background-color: qlineargradient(x1:1, y1:0, x2:1, y2:0.3, stop:0 #8a9195, stop:1 black);
            color: white;
            font-size: 20px;
            font-weight: bold;
            border-radius: 25px;
        }

        QPushButton:hover {
            background-color: qlineargradient(x1:1, y1:0, x2:1, y2:0.3, stop:0 #7d8488, stop:1 black);
        }

        QPushButton:pressed {
            background-color: qlineargradient(x1:1, y1:0, x2:1, y2:0.3, stop:0 #6a7073, stop:1 black);
        }
        """)
# PyQt

# PySide
# from PySide2.QtWidgets import QPushButton


# class QtBoxStyleButton1(QPushButton):
#     def __init__(self):
#         super(QtBoxStyleButton1, self).__init__()
#         self.setFixedSize(150, 50)
#         self.setText("BUTTON")
#         self.setStyleSheet("""
#         QPushButton {
#             background-color: qlineargradient(x1:1, y1:0, x2:1, y2:0.3, stop:0 #8a9195, stop:1 black);
#             color: white;
#             font-size: 20px;
#             font-weight: bold;
#             border-radius: 25px;
#         }

#         QPushButton:hover {
#             background-color: qlineargradient(x1:1, y1:0, x2:1, y2:0.3, stop:0 #7d8488, stop:1 black);
#         }

#         QPushButton:pressed {
#             background-color: qlineargradient(x1:1, y1:0, x2:1, y2:0.3, stop:0 #6a7073, stop:1 black);
#         }
#         """)
# PySide

# C++/Qt
# #ifndef QTBOXSTYLEPUSHBUTTON1_H
# #define QTBOXSTYLEPUSHBUTTON1_H
# #include <QPushButton>

# class QtBoxStylePushButton1 : public QPushButton
# {
#     Q_OBJECT

# public:
#     QtBoxStylePushButton1(QWidget *parent = nullptr);
# };
# #endif // QTBOXSTYLEPUSHBUTTON1_H



# #include "qtboxstylepushbutton1.h"

# QtBoxStylePushButton1::QtBoxStylePushButton1(QWidget *parent)
#     : QPushButton(parent)
# {
#     setFixedSize(150, 50);
#     setText("BUTTON");
#     setStyleSheet(R"(
#     QPushButton {
#         background-color: qlineargradient(x1:1, y1:0, x2:1, y2:0.3, stop:0 #8a9195, stop:1 black);
#         color: white;
#         font-size: 20px;
#         font-weight: bold;
#         border-radius: 25px;
#     }

#     QPushButton:hover {
#         background-color: qlineargradient(x1:1, y1:0, x2:1, y2:0.3, stop:0 #7d8488, stop:1 black);
#     }

#     QPushButton:pressed {
#         background-color: qlineargradient(x1:1, y1:0, x2:1, y2:0.3, stop:0 #6a7073, stop:1 black);
#     }
#     )");
# }
# C++/Qt