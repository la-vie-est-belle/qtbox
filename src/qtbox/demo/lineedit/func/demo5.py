# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QCompleter
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QLineEdit = createWidgetMenuBase(QLineEdit)

class QtBoxFuncLineEdit5(QLineEdit):
    def __init__(self):
        super(QtBoxFuncLineEdit5, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 30)
        self.setPlaceholderText("Type P or Q")

        comp = QCompleter(["PyQt", "Qt", "Qt Box", "PySide", "Python"])
        comp.setFilterMode(Qt.MatchContains)
        self.setCompleter(comp)
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QLineEdit, QCompleter


# class QtBoxFuncLineEdit5(QLineEdit):
#     def __init__(self):
#         super(QtBoxFuncLineEdit5, self).__init__()
#         self.setFixedSize(150, 30)
#         self.setPlaceholderText("Type P or Q")

#         comp = QCompleter(["PyQt", "Qt", "Qt Box", "PySide", "Python"])
#         comp.setFilterMode(Qt.MatchContains)
#         self.setCompleter(comp)
# PySide

# C++/Qt
# #ifndef QTBOXFUNCLINEEDIT5_H
# #define QTBOXFUNCLINEEDIT5_H
# #include <QLineEdit>

# class QtBoxFuncLineEdit5 : public QLineEdit
# {
#     Q_OBJECT

# public:
#     QtBoxFuncLineEdit5(QWidget *parent = nullptr);
# };
# #endif // QTBOXFUNCLINEEDIT5_H



# #include "qtboxfunclineedit5.h"
# #include <QCompleter>
# #include <Qt>

# QtBoxFuncLineEdit5::QtBoxFuncLineEdit5(QWidget *parent)
#     : QLineEdit(parent)
# {
#     setFixedSize(150, 30);
#     setPlaceholderText("Type P or Q");

#     QCompleter *comp = new QCompleter({"PyQt", "Qt", "Qt Box", "PySide", "Python"});
#     comp->setFilterMode(Qt::MatchContains);
#     setCompleter(comp);
# }
# C++/Qt