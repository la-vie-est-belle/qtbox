# PyQt
from PyQt5.QtWidgets import QTableWidget
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QTableWidget = createWidgetMenuBase(QTableWidget)

class QtBoxStyleTableWidget1(QTableWidget):
    def __init__(self):
        super(QtBoxStyleTableWidget1, self).__init__(str(Path(__file__)))
        self.setFixedSize(200, 150)
        self.setColumnCount(3)
        self.setRowCount(5)
        self.setHorizontalHeaderLabels(["A", "B", "C"])

        self.setStyleSheet("""
        QHeaderView::section {
            color: #5e5e5e;
        }
        
        QHeaderView::section:hover
        {   
            border: none;
            background-color: #a2c7ae;
        }
        
        QHeaderView::section::horizontal:checked
        {   
            border: none;
            border-bottom: 1px solid #3a714a;
            background-color: #c0daca;
            color: #2f5b53;
        }
        
        QHeaderView::section::vertical:checked
        {   
            border: none;
            border-right: 1px solid #3a714a;
            background-color: #c0daca;
            color: #2f5b53;
        }
        
        QTableView {
            selection-background-color: transparent;
            selection-color: black;
        }
        
        QTableView::item:selected {
            border: 1px solid #3a714a;
        }
        """)
# PyQt

# PySide
# from PySide2.QtWidgets import QTableWidget


# class QtBoxStyleTableWidget1(QTableWidget):
#     def __init__(self):
#         super(QtBoxStyleTableWidget1, self).__init__()
#         self.setFixedSize(200, 150)
#         self.setColumnCount(3)
#         self.setRowCount(5)
#         self.setHorizontalHeaderLabels(["A", "B", "C"])

#         self.setStyleSheet("""
#         QHeaderView::section {
#             color: #5e5e5e;
#         }

#         QHeaderView::section:hover
#         {
#             border: none;
#             background-color: #a2c7ae;
#         }

#         QHeaderView::section::horizontal:checked
#         {
#             border: none;
#             border-bottom: 1px solid #3a714a;
#             background-color: #c0daca;
#             color: #2f5b53;
#         }

#         QHeaderView::section::vertical:checked
#         {
#             border: none;
#             border-right: 1px solid #3a714a;
#             background-color: #c0daca;
#             color: #2f5b53;
#         }

#         QTableView {
#             selection-background-color: transparent;
#             selection-color: black;
#         }

#         QTableView::item:selected {
#             border: 1px solid #3a714a;
#         }
#         """)
# PySide

# C++/Qt
# #ifndef QTBOXSTYLETABLEWIDGET1_H
# #define QTBOXSTYLETABLEWIDGET1_H
# #include <QTableWidget>

# class QtBoxStyleTableWidget1 : public QTableWidget
# {
#     Q_OBJECT

# public:
#     QtBoxStyleTableWidget1(QWidget *parent = nullptr);
# };
# #endif // QTBOXSTYLETABLEWIDGET1_H



# #include "qtboxstyletablewidget1.h"

# QtBoxStyleTableWidget1::QtBoxStyleTableWidget1(QWidget *parent)
#     : QTableWidget(parent)
# {
#     setFixedSize(200, 150);
#     setColumnCount(3);
#     setRowCount(5);
#     setHorizontalHeaderLabels({"A", "B", "C"});

#     setStyleSheet(R"(
#     QHeaderView::section {
#         color: #5e5e5e;
#     }

#     QHeaderView::section:hover
#     {
#         border: none;
#         background-color: #a2c7ae;
#     }

#     QHeaderView::section::horizontal:checked
#     {
#         border: none;
#         border-bottom: 1px solid #3a714a;
#         background-color: #c0daca;
#         color: #2f5b53;
#     }

#     QHeaderView::section::vertical:checked
#     {
#         border: none;
#         border-right: 1px solid #3a714a;
#         background-color: #c0daca;
#         color: #2f5b53;
#     }

#     QTableView {
#         selection-background-color: transparent;
#         selection-color: black;
#     }

#     QTableView::item:selected {
#         border: 1px solid #3a714a;
#     }
#     )");
# }
# C++/Qt