# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QComboBox, QCompleter
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QComboBox = createWidgetMenuBase(QComboBox)

class QtBoxFuncComboBox2(QComboBox):
    def __init__(self):
        super(QtBoxFuncComboBox2, self).__init__(str(Path(__file__)))
        self.setEditable(True)
        self.addItems(['1', '2', '3', '4', '5', '6'])
        comp = QCompleter(["1a", "1b", "1c"])
        comp.setFilterMode(Qt.MatchContains)
        self.setCompleter(comp)
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QComboBox, QCompleter


# class QtBoxFuncComboBox2(QComboBox):
#     def __init__(self):
#         super(QtBoxFuncComboBox2, self).__init__()
#         self.setEditable(True)
#         self.addItems(['1', '2', '3', '4', '5', '6'])
#         comp = QCompleter(["1a", "1b", "1c"])
#         comp.setFilterMode(Qt.MatchContains)
#         self.setCompleter(comp)
# PySide

# C++/Qt
# #ifndef QTBOXFUNCCOMBOBOX2_H
# #define QTBOXFUNCCOMBOBOX2_H
# #include <QComboBox>

# class QtBoxFuncComboBox2 : public QComboBox
# {
#     Q_OBJECT

# public:
#     QtBoxFuncComboBox2(QWidget *parent = nullptr);
# };
# #endif // QTBOXFUNCCOMBOBOX2_H



# #include "qtboxfunccombobox2.h"
# #include <QCompleter>
# #include <Qt>

# QtBoxFuncComboBox2::QtBoxFuncComboBox2(QWidget *parent)
#     : QComboBox(parent)
# {
#     setEditable(true);
#     addItems({"1", "2", "3", "4", "5", "6"});
#     QCompleter *comp = new QCompleter({"1a", "1b", "1c"});
#     comp->setFilterMode(Qt::MatchContains);
#     setCompleter(comp);
# }
# C++/Qt