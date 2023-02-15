# PyQt
from PyQt5.QtWidgets import QLabel
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QLabel = createWidgetMenuBase(QLabel)
PATH_TO_IMG = str(Path(__file__).parent.parent.parent / "res/images/qt.png").replace("\\", "/")

class QtBoxStyleLabel1(QLabel):
    def __init__(self):
        super(QtBoxStyleLabel1, self).__init__(str(Path(__file__)))
        self.setFixedSize(90, 90)
        self.setStyleSheet("""
        QLabel {
            border-radius: 45px;
            border-image: url(%s)
        }
        """ % (PATH_TO_IMG))
# PyQt

# PySide
# from PySide2.QtWidgets import QLabel


# class QtBoxStyleLabel1(QLabel):
#     def __init__(self):
#         super(QtBoxStyleLabel1, self).__init__()
#         self.setFixedSize(90, 90)
#         self.setStyleSheet("""
#         QLabel {
#             border-radius: 45px;
#             border-image: url(%s)
#         }
#         """ % (PATH_TO_IMG))
# PySide