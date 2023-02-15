# PyQt
from PyQt5.QtWidgets import QComboBox
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QComboBox = createWidgetMenuBase(QComboBox)
PATH_TO_IMG1 = str(Path(__file__).parent.parent.parent / "res/images/down.png").replace("\\", "/")
PATH_TO_IMG2 = str(Path(__file__).parent.parent.parent / "res/images/up.png").replace("\\", "/")

class QtBoxStyleComboBox2(QComboBox):
    def __init__(self):
        super(QtBoxStyleComboBox2, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 30)
        self.addItems(['1', '2', '3', '4', '5', '6'])
        self.setStyleSheet("""
        QComboBox {
            background-color: white;
            color: black;
            border: 1px solid lightgray;
            border-radius: 15px;
            padding-left: 15px;
        }
        
        QComboBox:on {
            border: 1px solid #63acfb;
        }

        QComboBox::drop-down {
            width: 22px;
            border-left: 1px solid lightgray;
            border-top-right-radius: 15px;
            border-bottom-right-radius: 15px;
        }
        
        QComboBox::drop-down:on {
            border-left: 1px solid #63acfb;
        }

        QComboBox::down-arrow {
            width: 16px;
            height: 16px;
            image: url(%s);
        }

        QComboBox::down-arrow:on {
            image: url(%s);
        }

        QComboBox QAbstractItemView {
            color: black;
            border: none;
            outline: none;
            background-color: whitesmoke;
        }

        QComboBox QScrollBar:vertical {
            width: 2px;
            background-color: white;
        }

        QComboBox QScrollBar::handle:vertical {
            background-color: #b2bdaf;
        }
        """ % (PATH_TO_IMG1, PATH_TO_IMG2))
# PyQt

# PySide
# from PySide2.QtWidgets import QComboBox


# class QtBoxStyleComboBox2(QComboBox):
#     def __init__(self):
#         super(QtBoxStyleComboBox2, self).__init__()
#         self.setFixedSize(150, 30)
#         self.addItems(['1', '2', '3', '4', '5', '6'])
#         self.setStyleSheet("""
#         QComboBox {
#             background-color: white;
#             color: black;
#             border: 1px solid lightgray;
#             border-radius: 15px;
#             padding-left: 15px;
#         }

#         QComboBox:on {
#             border: 1px solid #63acfb;
#         }

#         QComboBox::drop-down {
#             width: 22px;
#             border-left: 1px solid lightgray;
#             border-top-right-radius: 15px;
#             border-bottom-right-radius: 15px;
#         }

#         QComboBox::drop-down:on {
#             border-left: 1px solid #63acfb;
#         }

#         QComboBox::down-arrow {
#             width: 16px;
#             height: 16px;
#             image: url(%s);
#         }

#         QComboBox::down-arrow:on {
#             image: url(%s);
#         }

#         QComboBox QAbstractItemView {
#             color: black;
#             border: none;
#             outline: none;
#             background-color: whitesmoke;
#         }

#         QComboBox QScrollBar:vertical {
#             width: 2px;
#             background-color: white;
#         }

#         QComboBox QScrollBar::handle:vertical {
#             background-color: #b2bdaf;
#         }
#         """ % (PATH_TO_IMG1, PATH_TO_IMG2))
# PySide