# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLineEdit, QPushButton
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QLineEdit = createWidgetMenuBase(QLineEdit)
PATH_TO_IMG = str(Path(__file__).parent.parent.parent.parent / "res/images/search.png").replace("\\", "/")

class QtBoxStyleLineEdit1(QLineEdit):
    def __init__(self):
        super(QtBoxStyleLineEdit1, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 30)
        self.setPlaceholderText("search")

        self.search_btn = QPushButton(self)
        self.search_btn.setIcon(QIcon(PATH_TO_IMG))
        self.search_btn.setCursor(Qt.PointingHandCursor)
        self.search_btn.setFixedSize(self.height(), self.height())
        self.search_btn.move(self.width()-self.search_btn.width(), 0)

        self.setStyleSheet("""
        QPushButton {
            border: none;
        }

        QLineEdit {
            background-color: #232324;
            border: 1px solid gray;
            border-radius: 3px;
            padding-left: 2px;
            padding-right: 25px;
            color: #f0f0f0;
        }
        """)
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtGui import QIcon
# from PySide2.QtWidgets import QLineEdit, QPushButton


# class QtBoxStyleLineEdit1(QLineEdit):
#     def __init__(self):
#         super(QtBoxStyleLineEdit1, self).__init__()
#         self.setFixedSize(150, 30)
#         self.setPlaceholderText("search")

#         self.search_btn = QPushButton(self)
#         self.search_btn.setIcon(QIcon(PATH_TO_IMG))
#         self.search_btn.setCursor(Qt.PointingHandCursor)
#         self.search_btn.setFixedSize(self.height(), self.height())
#         self.search_btn.move(self.width()-self.search_btn.width(), 0)

#         self.setStyleSheet("""
#         QPushButton {
#             border: none;
#         }

#         QLineEdit {
#             background-color: #232324;
#             border: 1px solid gray;
#             border-radius: 3px;
#             padding-left: 2px;
#             padding-right: 25px;
#             color: #f0f0f0;
#         }
#         """)
# PySide

# C++/Qt
# #ifndef QTBOXSTYLELINEEDIT1_H
# #define QTBOXSTYLELINEEDIT1_H
# #include <QLineEdit>
# #include <QPushButton>

# class QtBoxStyleLineEdit1 : public QLineEdit
# {
#     Q_OBJECT

# public:
#     QtBoxStyleLineEdit1(QWidget *parent = nullptr);

# private:
#     QPushButton *searchBtn = new QPushButton(this);
# };
# #endif // QTBOXSTYLELINEEDIT1_H



# #include "qtboxstylelineedit1.h"
# #include <QIcon>

# QtBoxStyleLineEdit1::QtBoxStyleLineEdit1(QWidget *parent)
#     : QLineEdit(parent)
# {
#     setFixedSize(150, 30);
#     setPlaceholderText("search");

#     searchBtn->setIcon(QIcon(":res/images/search.png"));
#     searchBtn->setCursor(Qt::PointingHandCursor);
#     searchBtn->setFixedSize(height(), height());
#     searchBtn->move(width()-searchBtn->width(), 0);

#     setStyleSheet(R"(
#     QPushButton {
#         border: none;
#     }

#     QLineEdit {
#         background-color: #232324;
#         border: 1px solid gray;
#         border-radius: 3px;
#         padding-left: 2px;
#         padding-right: 25px;
#         color: #f0f0f0;
#     }
#     )");
# }
# C++/Qt