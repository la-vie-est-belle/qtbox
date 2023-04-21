# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QPushButton
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QLineEdit = createWidgetMenuBase(QLineEdit)

class QtBoxStyleLineEdit5(QLineEdit):
    def __init__(self):
        super(QtBoxStyleLineEdit5, self).__init__(str(Path(__file__)))
        self.setAttribute(Qt.WA_MacShowFocusRect, False)
        self.setPlaceholderText("Enter username")
        self.setFixedSize(150, 30)
        self.setStyleSheet("""
        QLineEdit {
            border-top: none;
            border-left: none;
            border-right: none;
            border-bottom: 1px solid black;
            background-color: transparent;
        }
        
        QLineEdit:focus {
            border-bottom: 1px solid #2a70f4;
        }
        """)
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QLineEdit, QPushButton


# class QtBoxStyleLineEdit5(QLineEdit):
#     def __init__(self):
#         super(QtBoxStyleLineEdit5, self).__init__()
#         self.setAttribute(Qt.WA_MacShowFocusRect, False)
#         self.setPlaceholderText("Enter username")
#         self.setFixedSize(150, 30)
#         self.setStyleSheet("""
#         QLineEdit {
#             border-top: none;
#             border-left: none;
#             border-right: none;
#             border-bottom: 1px solid black;
#             background-color: transparent;
#         }

#         QLineEdit:focus {
#             border-bottom: 1px solid #2a70f4;
#         }
#         """)
# PySide

# C++/Qt
# #ifndef QTBOXSTYLELINEEDIT5_H
# #define QTBOXSTYLELINEEDIT5_H
# #include <QLineEdit>

# class QtBoxStyleLineEdit5 : public QLineEdit
# {
#     Q_OBJECT

# public:
#     QtBoxStyleLineEdit5(QWidget *parent = nullptr);
# };
# #endif // QTBOXSTYLELINEEDIT5_H



# #include "qtboxstylelineedit5.h"

# QtBoxStyleLineEdit5::QtBoxStyleLineEdit5(QWidget *parent)
#     : QLineEdit(parent)
# {
#     setAttribute(Qt::WA_MacShowFocusRect, false);
#     setPlaceholderText("Enter username");
#     setFixedSize(150, 30);
#     setStyleSheet(R"(
#     QLineEdit {
#         border-top: none;
#         border-left: none;
#         border-right: none;
#         border-bottom: 1px solid black;
#         background-color: transparent;
#     }

#     QLineEdit:focus {
#         border-bottom: 1px solid #2a70f4;
#     }
#     )");
# }
# C++/Qt