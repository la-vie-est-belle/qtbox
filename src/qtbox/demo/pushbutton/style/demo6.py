# PyQt
from PyQt5.QtWidgets import QPushButton
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QPushButton = createWidgetMenuBase(QPushButton)

class QtBoxStyleButton6(QPushButton):
    def __init__(self):
        super(QtBoxStyleButton6, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 40)
        self.setText("BUTTON")
        self.setStyleSheet("""
        QPushButton {
            background-color: #57bd6a;
            color: #f9ffff;
            font-size: 20px;
            font-weight: bold;
            border-radius: 5px;
        }

        QPushButton:pressed {
            background-color: #4eaa5f;
        }
        """)
# PyQt

# PySide
# from PySide2.QtWidgets import QPushButton


# class QtBoxStyleButton6(QPushButton):
#     def __init__(self):
#         super(QtBoxStyleButton6, self).__init__()
#         self.setFixedSize(150, 40)
#         self.setText("BUTTON")
#         self.setStyleSheet("""
#         QPushButton {
#             background-color: #57bd6a;
#             color: #f9ffff;
#             font-size: 20px;
#             font-weight: bold;
#             border-radius: 5px;
#         }

#         QPushButton:pressed {
#             background-color: #4eaa5f;
#         }
#         """)
# PySide

# C++/Qt
# #ifndef QTBOXSTYLEPUSHBUTTON6_H
# #define QTBOXSTYLEPUSHBUTTON6_H
# #include <QPushButton>

# class QtBoxStylePushButton6 : public QPushButton
# {
#     Q_OBJECT

# public:
#     QtBoxStylePushButton6(QWidget *parent = nullptr);
# };
# #endif // QTBOXSTYLEPUSHBUTTON6_H



# #include "qtboxstylepushbutton6.h"

# QtBoxStylePushButton6::QtBoxStylePushButton6(QWidget *parent)
#     : QPushButton(parent)
# {
#     setFixedSize(150, 40);
#     setText("BUTTON");
#     setStyleSheet(R"(
#     QPushButton {
#         background-color: #57bd6a;
#         color: #f9ffff;
#         font-size: 20px;
#         font-weight: bold;
#         border-radius: 5px;
#     }

#     QPushButton:pressed {
#         background-color: #4eaa5f;
#     }
#     )");
# }
# C++/Qt