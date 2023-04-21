# PyQt
from PyQt5.QtWidgets import QTableWidget, QPushButton
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QTableWidget = createWidgetMenuBase(QTableWidget)

class QtBoxFuncTableWidget1(QTableWidget):
    def __init__(self):
        super(QtBoxFuncTableWidget1, self).__init__(str(Path(__file__)))
        self.setFixedSize(200, 150)
        self.setColumnCount(3)
        self.setRowCount(5)
        self.add_btns()

    def add_btns(self):
        for row in range(self.rowCount()):
            for col in range(self.columnCount()):
                btn = QPushButton()
                btn.setText("button")
                self.setCellWidget(row, col, btn)
# PyQt

# PySide
# from PySide2.QtWidgets import QTableWidget, QPushButton


# class QtBoxFuncTableWidget1(QTableWidget):
#     def __init__(self):
#         super(QtBoxFuncTableWidget1, self).__init__()
#         self.setFixedSize(200, 150)
#         self.setColumnCount(3)
#         self.setRowCount(5)
#         self.add_btns()

#     def add_btns(self):
#         for row in range(self.rowCount()):
#             for col in range(self.columnCount()):
#                 btn = QPushButton()
#                 btn.setText("button")
#                 self.setCellWidget(row, col, btn)
# PySide

# C++/Qt
# #ifndef QTBOXFUNCTABLEWIDGET1_H
# #define QTBOXFUNCTABLEWIDGET1_H
# #include <QTableWidget>

# class QtBoxFuncTableWidget1 : public QTableWidget
# {
#     Q_OBJECT

# public:
#     QtBoxFuncTableWidget1(QWidget *parent = nullptr);

# private:
#     void addBtns();
# };
# #endif // QTBOXFUNCTABLEWIDGET1_H



# #include "qtboxfunctablewidget1.h"
# #include <QPushButton>

# QtBoxFuncTableWidget1::QtBoxFuncTableWidget1(QWidget *parent)
#     : QTableWidget(parent)
# {
#     setFixedSize(200, 150);
#     setColumnCount(3);
#     setRowCount(5);
#     addBtns();
# }

# void QtBoxFuncTableWidget1::addBtns()
# {
#     for (int row=0; row<rowCount(); row++) {
#         for (int col=0; col<columnCount(); col++) {
#             QPushButton *btn = new QPushButton();
#             btn->setText("button");
#             setCellWidget(row, col, btn);
#         }
#     }
# }
# C++/Qt