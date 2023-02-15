# PyQt
from PyQt5.QtWidgets import QSlider
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QSlider = createWidgetMenuBase(QSlider)

class QtBoxStyleSlider2(QSlider):
    def __init__(self):
        super(QtBoxStyleSlider2, self).__init__(str(Path(__file__)))
        self.setStyleSheet("""
        QSlider::groove:vertical {
            background-color: #eaebed;
            border: none;
            width: 6px;
            border-radius: 3px;
        }

        QSlider::handle:vertical {
            background-color: #d33124;
            height:6px;
            margin: 0px -1px 0px -1px;
            border-radius: 3px;
        }
        
        QSlider::add-page:vertical {
            background-color: #d33124;
        }
        """)
# PyQt

# PySide
# from PySide2.QtWidgets import QSlider


# class QtBoxStyleSlider2(QSlider):
#     def __init__(self):
#         super(QtBoxStyleSlider2, self).__init__()
#         self.setStyleSheet("""
#         QSlider::groove:vertical {
#             background-color: #eaebed;
#             border: none;
#             width: 6px;
#             border-radius: 3px;
#         }

#         QSlider::handle:vertical {
#             background-color: #d33124;
#             height:6px;
#             margin: 0px -1px 0px -1px;
#             border-radius: 3px;
#         }

#         QSlider::add-page:vertical {
#             background-color: #d33124;
#         }
#         """)
# PySide