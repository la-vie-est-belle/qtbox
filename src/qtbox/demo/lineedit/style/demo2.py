# PyQt
from PyQt5.QtWidgets import QLineEdit, QLabel
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QLineEdit = createWidgetMenuBase(QLineEdit)

class QtBoxStyleLineEdit2(QLineEdit):
    def __init__(self):
        super(QtBoxStyleLineEdit2, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 50)
        self.setStyleSheet("""
        QLineEdit {
            border: 1px solid gray;
            border-radius: 5px;
            padding-top: 14px;
            padding-left: 2px;
            padding-right: 2px;
        }
        """)

        self.label = QLabel(self)
        self.label.setText("Name")
        self.label.move(5, 16)
        self.label.setStyleSheet("""
        QLabel {
            color: gray;
            font-size: 16px;
        }
        """)

    def focusInEvent(self, event):
        super(QtBoxStyleLineEdit2, self).focusInEvent(event)
        self.label.move(5, 5)
        self.label.setStyleSheet("""
        QLabel {
            color: black;
            font-size: 12px;
        }
        """)

    def focusOutEvent(self, event):
        super(QtBoxStyleLineEdit2, self).focusOutEvent(event)
        if self.text():
            return

        self.label.move(5, 16)
        self.label.setStyleSheet("""
        QLabel {
            color: gray;
            font-size: 16px;
        }
        """)
# PyQt

# PySide
# from PySide2.QtWidgets import QLineEdit, QLabel


# class QtBoxStyleLineEdit2(QLineEdit):
#     def __init__(self):
#         super(QtBoxStyleLineEdit2, self).__init__()
#         self.setFixedSize(150, 50)
#         self.setStyleSheet("""
#         QLineEdit {
#             border: 1px solid gray;
#             border-radius: 5px;
#             padding-top: 14px;
#             padding-left: 2px;
#             padding-right: 2px;
#         }
#         """)

#         self.label = QLabel(self)
#         self.label.setText("Name")
#         self.label.move(5, 16)
#         self.label.setStyleSheet("""
#         QLabel {
#             color: gray;
#             font-size: 16px;
#         }
#         """)

#     def focusInEvent(self, event):
#         super(QtBoxStyleLineEdit2, self).focusInEvent(event)
#         self.label.move(5, 5)
#         self.label.setStyleSheet("""
#         QLabel {
#             color: black;
#             font-size: 12px;
#         }
#         """)

#     def focusOutEvent(self, event):
#         super(QtBoxStyleLineEdit2, self).focusOutEvent(event)
#         if self.text():
#             return

#         self.label.move(5, 16)
#         self.label.setStyleSheet("""
#         QLabel {
#             color: gray;
#             font-size: 16px;
#         }
#         """)
# PySide

# C++/Qt
# #ifndef QTBOXSTYLELINEEDIT2_H
# #define QTBOXSTYLELINEEDIT2_H
# #include <QLineEdit>
# #include <QFocusEvent>
# #include <QLabel>

# class QtBoxStyleLineEdit2 : public QLineEdit
# {
#     Q_OBJECT

# public:
#     QtBoxStyleLineEdit2(QWidget *parent = nullptr);

# protected:
#     void focusInEvent(QFocusEvent *event);
#     void focusOutEvent(QFocusEvent *event);

# private:
#     QLabel *label = new QLabel(this);
# };
# #endif // QTBOXSTYLELINEEDIT2_H



# #include "qtboxstylelineedit2.h"
# #include <QIcon>

# QtBoxStyleLineEdit2::QtBoxStyleLineEdit2(QWidget *parent)
#     : QLineEdit(parent)
# {
#     setFixedSize(150, 50);
#     setStyleSheet(R"(
#     QLineEdit {
#         border: 1px solid gray;
#         border-radius: 5px;
#         padding-top: 14px;
#         padding-left: 2px;
#         padding-right: 2px;
#     }
#     )");

#     label->setText("Name");
#     label->move(5, 16);
#     label->setStyleSheet(R"(
#     QLabel {
#         color: gray;
#         font-size: 16px;
#     }
#     )");
# }

# void QtBoxStyleLineEdit2::focusInEvent(QFocusEvent *event)
# {
#     QLineEdit::focusInEvent(event);
#     label->move(5, 5);
#     label->setStyleSheet(R"(
#     QLabel {
#         color: black;
#         font-size: 12px;
#     }
#     )");
# }

# void QtBoxStyleLineEdit2::focusOutEvent(QFocusEvent *event)
# {
#     QLineEdit::focusOutEvent(event);
#     if (!text().isEmpty()) {
#         return;
#     }

#     label->move(5, 16);
#     label->setStyleSheet(R"(
#     QLabel {
#         color: gray;
#         font-size: 16px;
#     }
#     )");
# }
# C++/Qt