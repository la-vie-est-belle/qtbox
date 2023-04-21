# PyQt
from PyQt5.QtWidgets import QComboBox
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QComboBox = createWidgetMenuBase(QComboBox)

class QtBoxFuncComboBox1(QComboBox):
    def __init__(self):
        super(QtBoxFuncComboBox1, self).__init__(str(Path(__file__)))
        self.setEditable(True)
        self.addItems(['1', '2', '3', '4', '5', '6'])
        self.currentTextChanged.connect(self.update_item)

    def update_item(self, txt):
        self.setItemText(self.currentIndex(), txt)
# PyQt

# PySide
# from PySide2.QtWidgets import QComboBox


# class QtBoxFuncComboBox1(QComboBox):
#     def __init__(self):
#         super(QtBoxFuncComboBox1, self).__init__()
#         self.setEditable(True)
#         self.addItems(['1', '2', '3', '4', '5', '6'])
#         self.currentTextChanged.connect(self.update_item)

#     def update_item(self, txt):
#         self.setItemText(self.currentIndex(), txt)
# PySide

# C++/Qt
# #ifndef QTBOXFUNCCOMBOBOX1_H
# #define QTBOXFUNCCOMBOBOX1_H
# #include <QComboBox>

# class QtBoxFuncComboBox1 : public QComboBox
# {
#     Q_OBJECT

# public:
#     QtBoxFuncComboBox1(QWidget *parent = nullptr);

# private slots:
#     void updateItem(const QString &txt);
# };
# #endif // QTBOXFUNCCOMBOBOX1_H



# #include "qtboxfunccombobox1.h"

# QtBoxFuncComboBox1::QtBoxFuncComboBox1(QWidget *parent)
#     : QComboBox(parent)
# {
#     setEditable(true);
#     addItems({"1", "2", "3", "4", "5", "6"});
#     connect(this, SIGNAL(currentTextChanged(const QString &)), this, SLOT(updateItem(const QString &)));
# }

# void QtBoxFuncComboBox1::updateItem(const QString &txt)
# {
#     setItemText(currentIndex(), txt);
# }
# C++/Qt