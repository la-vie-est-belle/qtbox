# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidget, QListWidgetItem
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QListWidget = createWidgetMenuBase(QListWidget)

class QtBoxStyleListWidget1(QListWidget):
    def __init__(self):
        super(QtBoxStyleListWidget1, self).__init__(str(Path(__file__)))
        self.setFixedSize(200, 200)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        for i in range(10):
            item = QListWidgetItem()
            item.setText(str(i))
            self.addItem(item)

        self.setStyleSheet("""
        QListView {
            border: none;
            background-color: #edeef3;
        }
        
        QListView::item {
            height: 40px;
            margin: 5px 5px 5px 5px;
            background-color: white;
            border-radius: 6px;
        }
        
        QListView::item:hover{
            background-color: whitesmoke;
        }
        
        QListView::item:selected{
            color: black;
            border: 1px solid lightgray;
        }
        """)
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QListWidget, QListWidgetItem


# class QtBoxStyleListWidget1(QListWidget):
#     def __init__(self):
#         super(QtBoxStyleListWidget1, self).__init__(str(Path(__file__)))
#         self.setFixedSize(200, 200)
#         self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
#         self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

#         for i in range(10):
#             item = QListWidgetItem()
#             item.setText(str(i))
#             self.addItem(item)

#         self.setStyleSheet("""
#         QListView {
#             border: none;
#             background-color: #edeef3;
#         }

#         QListView::item {
#             height: 40px;
#             margin: 5px 5px 5px 5px;
#             background-color: white;
#             border-radius: 6px;
#         }

#         QListView::item:hover{
#             background-color: whitesmoke;
#         }

#         QListView::item:selected{
#             color: black;
#             border: 1px solid lightgray;
#         }
#         """)
# PySide

# C++/Qt
# #ifndef QTBOXSTYLELISTWIDGET1_H
# #define QTBOXSTYLELISTWIDGET1_H
# #include <QListWidget>

# class QtBoxStyleListWidget1 : public QListWidget
# {
#     Q_OBJECT

# public:
#     QtBoxStyleListWidget1(QWidget *parent = nullptr);
# };
# #endif // QTBOXSTYLELISTWIDGET1_H



# #include "qtboxstylelistwidget1.h"
# #include <QListWidgetItem>
# #include <Qt>

# QtBoxStyleListWidget1::QtBoxStyleListWidget1(QWidget *parent)
#     : QListWidget(parent)
# {
#     setFixedSize(200, 200);
#     setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
#     setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);

#     for(int i=0; i<10; i++) {
#         QListWidgetItem *item = new QListWidgetItem();
#         item->setText(QString("%1").arg(i));
#         addItem(item);
#     }

#     setStyleSheet(R"(
#     QListView {
#         border: none;
#         background-color: #edeef3;
#     }

#     QListView::item {
#         height: 40px;
#         margin: 5px 5px 5px 5px;
#         background-color: white;
#         border-radius: 6px;
#     }

#     QListView::item:hover{
#         background-color: whitesmoke;
#     }

#     QListView::item:selected{
#         color: black;
#         border: 1px solid lightgray;
#     }
#     )");
# }
# C++/Qt