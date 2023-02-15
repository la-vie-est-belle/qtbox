# PyQt
from PyQt5.QtWidgets import QCheckBox
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QCheckBox = createWidgetMenuBase(QCheckBox)
PATH_TO_IMG1 = str(Path(__file__).parent.parent.parent / "res/images/off.png").replace("\\", "/")
PATH_TO_IMG2 = str(Path(__file__).parent.parent.parent / "res/images/on.png").replace("\\", "/")

class QtBoxStyleCheckBox3(QCheckBox):
    def __init__(self):
        super(QtBoxStyleCheckBox3, self).__init__(str(Path(__file__)))
        self.setText("Qt Box")
        self.setStyleSheet("""
        QCheckBox {
            font-size: 15px;
        }

        QCheckBox::indicator {
            width: 30px;
            height: 30px;
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


# class QtBoxStyleCheckBox3(QCheckBox):
#     def __init__(self):
#         super(QtBoxStyleCheckBox3, self).__init__()
#         self.setText("Qt Box")
#         self.setStyleSheet("""
#         QCheckBox {
#             font-size: 15px;
#         }

#         QCheckBox::indicator {
#             width: 30px;
#             height: 30px;
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