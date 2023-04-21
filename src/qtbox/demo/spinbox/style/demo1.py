# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSpinBox
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QSpinBox = createWidgetMenuBase(QSpinBox)
PATH_TO_IMG1 = str(Path(__file__).parent.parent.parent.parent / "res/images/up.png").replace("\\", "/")
PATH_TO_IMG2 = str(Path(__file__).parent.parent.parent.parent / "res/images/down.png").replace("\\", "/")

class QtBoxStyleSpinBox1(QSpinBox):
    def __init__(self):
        super(QtBoxStyleSpinBox1, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 30)
        self.setCursor(Qt.PointingHandCursor)
        self.setAttribute(Qt.WA_MacShowFocusRect, False)
        self.setStyleSheet("""
        QSpinBox {
            border: 1px solid lightgray;
            border-radius: 3px;
        }
        
        QSpinBox::up-button {
            width: 14px;
            height: 14px;
            margin: 0px 3px 0px -3px;
            border-image: url(%s);
        }
        
        QSpinBox::up-button:pressed {
            margin-top: 1px;
        }
            
        QSpinBox::down-button {
            width: 14px;
            height: 14px;
            margin: 0px 3px 0px -3px;
            border-image: url(%s);
        }
        
        QSpinBox::down-button:pressed {
            margin-bottom: 1px;
        }
        """ % (PATH_TO_IMG1, PATH_TO_IMG2))
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QSpinBox


# class QtBoxStyleSpinBox1(QSpinBox):
#     def __init__(self):
#         super(QtBoxStyleSpinBox1, self).__init__()
#         self.setFixedSize(150, 30)
#         self.setCursor(Qt.PointingHandCursor)
#         self.setAttribute(Qt.WA_MacShowFocusRect, False)
#         self.setStyleSheet("""
#         QSpinBox {
#             border: 1px solid lightgray;
#             border-radius: 3px;
#         }

#         QSpinBox::up-button {
#             margin: 0px 3px 0px -3px;
#             border-image: url(%s);
#         }

#         QSpinBox::up-button:pressed {
#             margin-top: 1px;
#         }

#         QSpinBox::down-button {
#             margin: 0px 3px 0px -3px;
#             border-image: url(%s);
#         }

#         QSpinBox::down-button:pressed {
#             margin-bottom: 1px;
#         }
#         """ % (PATH_TO_IMG1, PATH_TO_IMG2))
# PySide

# C++/Qt
# #ifndef QTBOXSTYLESPINBOX1_H
# #define QTBOXSTYLESPINBOX1_H
# #include <QSpinBox>

# class QtBoxStyleSpinBox1 : public QSpinBox
# {
#     Q_OBJECT

# public:
#     QtBoxStyleSpinBox1(QWidget *parent = nullptr);
# };
# #endif // QTBOXSTYLESPINBOX1_H



# #include "qtboxstylespinbox1.h"
# #include <Qt>

# QtBoxStyleSpinBox1::QtBoxStyleSpinBox1(QWidget *parent)
#     : QSpinBox(parent)
# {
#     setFixedSize(150, 30);
#     setCursor(Qt::PointingHandCursor);
#     setAttribute(Qt::WA_MacShowFocusRect, false);
#     setStyleSheet(R"(
#     QSpinBox {
#         border: 1px solid lightgray;
#         border-radius: 3px;
#     }

#     QSpinBox::up-button {
#         width: 14px;
#         height: 14px;
#         margin: 0px 3px 0px -3px;
#         border-image: url(PATH_TO_IMG1);
#     }

#     QSpinBox::up-button:pressed {
#         margin-top: 1px;
#     }

#     QSpinBox::down-button {
#         width: 14px;
#         height: 14px;
#         margin: 0px 3px 0px -3px;
#         border-image: url(PATH_TO_IMG2);
#     }

#     QSpinBox::down-button:pressed {
#         margin-bottom: 1px;
#     }
#     )");
# }
# C++/Qt