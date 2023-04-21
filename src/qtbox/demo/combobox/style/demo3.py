# PyQt
from PyQt5.QtWidgets import QComboBox
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QComboBox = createWidgetMenuBase(QComboBox)
PATH_TO_IMG = str(Path(__file__).parent.parent.parent.parent / "res/images/up_down.png").replace("\\", "/")

class QtBoxStyleComboBox3(QComboBox):
    def __init__(self):
        super(QtBoxStyleComboBox3, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 30)
        self.addItems(['1', '2', '3', '4', '5', '6'])
        self.setStyleSheet("""
        QComboBox {
            background-color: qlineargradient(x1:1, y1:0, x2:1, y2:1, stop:0 #f5f5f7, stop:1 #dedee0);
            border: 1px solid whitesmoke;
            border-radius: 3px;
            padding-left: 15px;
            color: gray;
        }

        QComboBox::drop-down {
            width: 22px;
            border-top-right-radius: 3px;
            border-bottom-right-radius: 3px;
        }

        QComboBox::down-arrow {
            width: 16px;
            height: 16px;
            image: url(%s);
        }

        QComboBox QAbstractItemView {
            color: gray;
            border: none;
            outline: none;
            background-color: #dedee0;
        }

        QComboBox QScrollBar:vertical {
            width: 2px;
            background-color: white;
        }

        QComboBox QScrollBar::handle:vertical {
            background-color: #b2bdaf;
        }
        """ % (PATH_TO_IMG))
# PyQt

# PySide
# from PySide2.QtWidgets import QComboBox


# class QtBoxStyleComboBox3(QComboBox):
#     def __init__(self):
#         super(QtBoxStyleComboBox3, self).__init__()
#         self.setFixedSize(150, 30)
#         self.addItems(['1', '2', '3', '4', '5', '6'])
#         self.setStyleSheet("""
#         QComboBox {
#             background-color: qlineargradient(x1:1, y1:0, x2:1, y2:1, stop:0 #f5f5f7, stop:1 #dedee0);
#             border: 1px solid whitesmoke;
#             border-radius: 3px;
#             padding-left: 15px;
#             color: gray;
#         }

#         QComboBox::drop-down {
#             width: 22px;
#             border-top-right-radius: 3px;
#             border-bottom-right-radius: 3px;
#         }

#         QComboBox::down-arrow {
#             width: 16px;
#             height: 16px;
#             image: url(%s);
#         }

#         QComboBox QAbstractItemView {
#             color: gray;
#             border: none;
#             outline: none;
#             background-color: #dedee0;
#         }

#         QComboBox QScrollBar:vertical {
#             width: 2px;
#             background-color: white;
#         }

#         QComboBox QScrollBar::handle:vertical {
#             background-color: #b2bdaf;
#         }
#         """ % (PATH_TO_IMG))
# PySide

# C++/Qt
# #ifndef QTBOXSTYLECOMBOBOX3_H
# #define QTBOXSTYLECOMBOBOX3_H
# #include <QComboBox>

# class QtBoxStyleComboBox3 : public QComboBox
# {
#     Q_OBJECT

# public:
#     QtBoxStyleComboBox3(QWidget *parent = nullptr);
# };
# #endif // QTBOXSTYLECOMBOBOX3_H



# #include "qtboxstylecombobox3.h"

# QtBoxStyleComboBox3::QtBoxStyleComboBox3(QWidget *parent)
#     : QComboBox(parent)
# {
#     setFixedSize(150, 30);
#     addItems({"1", "2", "3", "4", "5", "6"});
#     setStyleSheet(R"(
#     QComboBox {
#         background-color: qlineargradient(x1:1, y1:0, x2:1, y2:1, stop:0 #f5f5f7, stop:1 #dedee0);
#         border: 1px solid whitesmoke;
#         border-radius: 3px;
#         padding-left: 15px;
#         color: gray;
#     }

#     QComboBox::drop-down {
#         width: 22px;
#         border-top-right-radius: 3px;
#         border-bottom-right-radius: 3px;
#     }

#     QComboBox::down-arrow {
#         width: 16px;
#         height: 16px;
#         image: url(PATH_TO_IMG);
#     }

#     QComboBox QAbstractItemView {
#         color: gray;
#         border: none;
#         outline: none;
#         background-color: #dedee0;
#     }

#     QComboBox QScrollBar:vertical {
#         width: 2px;
#         background-color: white;
#     }

#     QComboBox QScrollBar::handle:vertical {
#         background-color: #b2bdaf;
#     }
#     )");
# }
# C++/Qt
