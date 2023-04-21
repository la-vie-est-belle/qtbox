# PyQt
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QPushButton
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QListWidget = createWidgetMenuBase(QListWidget)

class QtBoxFuncListWidget1(QListWidget):
    def __init__(self):
        super(QtBoxFuncListWidget1, self).__init__(str(Path(__file__)))
        self.setFixedSize(100, 200)
        self.add_btns()

    def add_btns(self):
        for _ in range(5):
            item = QListWidgetItem()
            item.setSizeHint(QSize(80, 30))
            self.addItem(item)

            btn = QPushButton()
            btn.setText("button")
            self.setItemWidget(item, btn)
# PyQt

# PySide
# from PySide2.QtCore import QSize
# from PySide2.QtWidgets import QListWidget, QListWidgetItem, QPushButton


# class QtBoxFuncListWidget1(QListWidget):
#     def __init__(self):
#         super(QtBoxFuncListWidget1, self).__init__()
#         self.setFixedSize(80, 200)
#         self.add_btns()

#     def add_btns(self):
#         for _ in range(5):
#             item = QListWidgetItem()
#             item.setSizeHint(QSize(100, 30))
#             self.addItem(item)

#             btn = QPushButton()
#             btn.setText("button")
#             self.setItemWidget(item, btn)
# PySide

# C++/Qt
# #ifndef QTBOXFUNCLISTWIDGET1_H
# #define QTBOXFUNCLISTWIDGET1_H
# #include <QListWidget>

# class QtBoxFuncListWidget1 : public QListWidget
# {
#     Q_OBJECT

# public:
#     QtBoxFuncListWidget1(QWidget *parent = nullptr);

# private:
#     void addBtns();
# };
# #endif // QTBOXFUNCLISTWIDGET1_H



# #include "qtboxfunclistwidget1.h"
# #include <QListWidgetItem>
# #include <QPushButton>
# #include <QSize>

# QtBoxFuncListWidget1::QtBoxFuncListWidget1(QWidget *parent)
#     : QListWidget(parent)
# {
#     setFixedSize(100, 200);
#     addBtns();
# }

# void QtBoxFuncListWidget1::addBtns()
# {
#     for(int i=0; i<5; i++) {
#         QListWidgetItem *item = new QListWidgetItem();
#         item->setSizeHint(QSize(80, 30));
#         addItem(item);

#         QPushButton *btn = new QPushButton();
#         btn->setText("button");
#         setItemWidget(item, btn);
#     }
# }
# C++/Qt