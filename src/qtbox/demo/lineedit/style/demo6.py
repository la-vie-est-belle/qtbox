# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QLineEdit = createWidgetMenuBase(QLineEdit)

class QtBoxStyleLineEdit6(QLineEdit):
    def __init__(self):
        super(QtBoxStyleLineEdit6, self).__init__(str(Path(__file__)))
        self.setMaxLength(1)
        self.setFixedSize(50, 50)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""
        QLineEdit {
            font-size: 25px;
            border: 2px solid black;
        }
        """)
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QLineEdit


# class QtBoxStyleLineEdit6(QLineEdit):
#     def __init__(self):
#         super(QtBoxStyleLineEdit6, self).__init__()
#         self.setMaxLength(1)
#         self.setFixedSize(50, 50)
#         self.setAlignment(Qt.AlignCenter)
#         self.setStyleSheet("""
#         QLineEdit {
#             font-size: 25px;
#             border: 2px solid black;
#         }
#         """)
# PySide

# C++/Qt
# #ifndef QTBOXSTYLELINEEDIT6_H
# #define QTBOXSTYLELINEEDIT6_H
# #include <QLineEdit>

# class QtBoxStyleLineEdit6 : public QLineEdit
# {
#     Q_OBJECT

# public:
#     QtBoxStyleLineEdit6(QWidget *parent = nullptr);
# };
# #endif // QTBOXSTYLELINEEDIT6_H



# #include "qtboxstylelineedit6.h"

# QtBoxStyleLineEdit6::QtBoxStyleLineEdit6(QWidget *parent)
#     : QLineEdit(parent)
# {
#     setMaxLength(1);
#     setFixedSize(50, 50);
#     setAlignment(Qt::AlignCenter);
#     setStyleSheet(R"(
#     QLineEdit {
#         font-size: 25px;
#         border: 2px solid black;
#     }
#     )");
# }
# C++/Qt