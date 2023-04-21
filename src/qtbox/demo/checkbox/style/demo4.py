# PyQt
from PyQt5.QtWidgets import QCheckBox
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QCheckBox = createWidgetMenuBase(QCheckBox)
PATH_TO_IMG1 = str(Path(__file__).parent.parent.parent.parent / "res/images/circle_black.png").replace("\\", "/")
PATH_TO_IMG2 = str(Path(__file__).parent.parent.parent.parent / "res/images/circle_blue.png").replace("\\", "/")

class QtBoxStyleCheckBox4(QCheckBox):
    def __init__(self):
        super(QtBoxStyleCheckBox4, self).__init__(str(Path(__file__)))
        self.setText("Qt Box")
        self.setStyleSheet("""
        QCheckBox {
            font-size: 15px;
        }
        
        QCheckBox:hover {
            color: rgba(0, 0, 0, 180);
        }

        QCheckBox::indicator {
            width: 20px;
            height: 20px;
            border: none;
        }

        QCheckBox::indicator:unchecked {
            image: url(%s);
        }

        QCheckBox::indicator:checked {
            image: url(%s);
        }
        """ % (PATH_TO_IMG1, PATH_TO_IMG2))
# PyQt

# PySide
# from PySide2.QtWidgets import QCheckBox


# class QtBoxStyleCheckBox4(QCheckBox):
#     def __init__(self):
#         super(QtBoxStyleCheckBox4, self).__init__()
#         self.setText("Qt Box")
#         self.setStyleSheet("""
#         QCheckBox {
#             font-size: 15px;
#         }

#         QCheckBox:hover {
#             color: rgba(0, 0, 0, 180);
#         }

#         QCheckBox::indicator {
#             width: 20px;
#             height: 20px;
#             border: none;
#         }

#         QCheckBox::indicator:unchecked {
#             image: url(%s);
#         }

#         QCheckBox::indicator:checked {
#             image: url(%s);
#         }
#         """ % (PATH_TO_IMG1, PATH_TO_IMG2))
# PySide

# C++/Qt
# #ifndef QTBOXSTYLECHECKBOX4_H
# #define QTBOXSTYLECHECKBOX4_H
# #include <QCheckBox>

# class QtBoxStyleCheckBox4 : public QCheckBox
# {
#     Q_OBJECT

# public:
#     QtBoxStyleCheckBox4(QWidget *parent = nullptr);
# };
# #endif // QTBOXSTYLECHECKBOX4_H



# #include "qtboxstylecheckbox4.h"

# QtBoxStyleCheckBox4::QtBoxStyleCheckBox4(QWidget *parent)
#     : QCheckBox(parent)
# {
#     setText("Qt Box");
#     setStyleSheet(R"(
#     QCheckBox {
#         font-size: 15px;
#     }

#     QCheckBox:hover {
#         color: rgba(0, 0, 0, 180);
#     }

#     QCheckBox::indicator {
#         width: 20px;
#         height: 20px;
#         border: none;
#     }

#     QCheckBox::indicator:unchecked {
#         image: url(PATH_TO_IMG);
#     }

#     QCheckBox::indicator:checked {
#         image: url(PATH_TO_IMG);
#     }
#     )");
# }
# C++/Qt