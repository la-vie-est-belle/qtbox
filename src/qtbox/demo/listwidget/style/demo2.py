# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidget, QListWidgetItem
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QListWidget = createWidgetMenuBase(QListWidget)

class QtBoxStyleListWidget2(QListWidget):
    def __init__(self):
        super(QtBoxStyleListWidget2, self).__init__(str(Path(__file__)))
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
            background-color: #65afdc;
            font-weight: bold;
        }

        QListView::item {
            height: 40px;
            color: white;
            border-bottom: 1px solid #8fcef4;
        }

        QListView::item:hover:!selected{
            background-color: #8fcef4;
            padding-left: 5px;
            padding-bottom: 2px;
        }

        QListView::item:selected{
            background-color: #5da0c7;
        }
        """)
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QListWidget, QListWidgetItem


# class QtBoxStyleListWidget2(QListWidget):
#     def __init__(self):
#         super(QtBoxStyleListWidget2, self).__init__()
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
#             background-color: #65afdc;
#             font-weight: bold;
#         }

#         QListView::item {
#             height: 40px;
#             color: white;
#             border-bottom: 1px solid #8fcef4;
#         }

#         QListView::item:hover:!selected{
#             background-color: #8fcef4;
#             padding-left: 5px;
#             padding-bottom: 2px;
#         }

#         QListView::item:selected{
#             background-color: #5da0c7;
#         }
#         """)
# PySide

# C++/Qt
# #ifndef QTBOXSTYLELISTWIDGET2_H
# #define QTBOXSTYLELISTWIDGET2_H
# #include <QListWidget>

# class QtBoxStyleListWidget2 : public QListWidget
# {
#     Q_OBJECT

# public:
#     QtBoxStyleListWidget2(QWidget *parent = nullptr);
# };
# #endif // QTBOXSTYLELISTWIDGET2_H



# #include "qtboxstylelistwidget2.h"
# #include <QListWidgetItem>
# #include <Qt>

# QtBoxStyleListWidget2::QtBoxStyleListWidget2(QWidget *parent)
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
#         background-color: #65afdc;
#         font-weight: bold;
#     }

#     QListView::item {
#         height: 40px;
#         color: white;
#         border-bottom: 1px solid #8fcef4;
#     }

#     QListView::item:hover:!selected{
#         background-color: #8fcef4;
#         padding-left: 5px;
#         padding-bottom: 2px;
#     }

#     QListView::item:selected{
#         background-color: #5da0c7;
#     }
#     )");
# }
# C++/Qt