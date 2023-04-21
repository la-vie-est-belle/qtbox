# PyQt
from PyQt5.QtWidgets import QCheckBox
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QCheckBox = createWidgetMenuBase(QCheckBox)
PATH_TO_IMG1 = str(Path(__file__).parent.parent.parent.parent / "res/images/close.png").replace("\\", "/")
PATH_TO_IMG2 = str(Path(__file__).parent.parent.parent.parent / "res/images/minimize.png").replace("\\", "/")
PATH_TO_IMG3 = str(Path(__file__).parent.parent.parent.parent / "res/images/check.png").replace("\\", "/")

class QtBoxStyleCheckBox1(QCheckBox):
    def __init__(self):
        super(QtBoxStyleCheckBox1, self).__init__(str(Path(__file__)))
        self.setText("Qt Box")
        self.setTristate(True)
        self.setStyleSheet("""
        QCheckBox {
            spacing: 5px;
            font-size: 15px;
            font-weight: bold;
        }
        
        QCheckBox::indicator {
            width: 16px;
            height: 16px;
            border: 2px solid black;
            border-radius: 6px;
        }
        
        QCheckBox::indicator:unchecked {
            image: url(%s);
            background-color: black;
        }
        
        QCheckBox::indicator:indeterminate {
            image: url(%s);
            background-color: black;
        }
        
        QCheckBox::indicator:checked {
            image: url(%s);
            background-color: black;
        }
        """ % (PATH_TO_IMG1, PATH_TO_IMG2, PATH_TO_IMG3))
# PyQt

# PySide
# from PySide2.QtWidgets import QCheckBox


# class QtBoxStyleCheckBox1(QCheckBox):
#     def __init__(self):
#         super(QtBoxStyleCheckBox1, self).__init__()
#         self.setText("Qt Box")
#         self.setTristate(True)
#         self.setStyleSheet("""
#         QCheckBox {
#             spacing: 5px;
#             font-size: 15px;
#             font-weight: bold;
#         }

#         QCheckBox::indicator {
#             width: 16px;
#             height: 16px;
#             border: 2px solid black;
#             border-radius: 6px;
#         }

#         QCheckBox::indicator:unchecked {
#             image: url(%s);
#             background-color: black;
#         }

#         QCheckBox::indicator:indeterminate {
#             image: url(%s);
#             background-color: black;
#         }

#         QCheckBox::indicator:checked {
#             image: url(%s);
#             background-color: black;
#         }
#         """ % (PATH_TO_IMG1, PATH_TO_IMG2, PATH_TO_IMG3))
# PySide

# C++/Qt
# #ifndef QTBOXSTYLECHECKBOX1_H
# #define QTBOXSTYLECHECKBOX1_H
# #include <QCheckBox>

# class QtBoxStyleCheckBox1 : public QCheckBox
# {
#     Q_OBJECT

# public:
#     QtBoxStyleCheckBox1(QWidget *parent = nullptr);
# };
# #endif // QTBOXSTYLECHECKBOX1_H



# #include "qtboxstylecheckbox1.h"

# QtBoxStyleCheckBox1::QtBoxStyleCheckBox1(QWidget *parent)
#     : QCheckBox(parent)
# {
#     setText("Qt Box");
#     setTristate(true);
#     setStyleSheet(R"(
#     QCheckBox {
#         spacing: 5px;
#         font-size: 15px;
#         font-weight: bold;
#     }

#     QCheckBox::indicator {
#         width: 16px;
#         height: 16px;
#         border: 2px solid black;
#         border-radius: 6px;
#     }

#     QCheckBox::indicator:unchecked {
#         image: url(PATH_TO_IMG);
#         background-color: black;
#     }

#     QCheckBox::indicator:indeterminate {
#         image: url(PATH_TO_IMG);
#         background-color: black;
#     }

#     QCheckBox::indicator:checked {
#         image: url(PATH_TO_IMG);
#         background-color: black;
#     }
#     )");
# }
# C++/Qt