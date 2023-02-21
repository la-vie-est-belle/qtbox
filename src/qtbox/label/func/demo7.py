# PyQt
from PyQt5.QtWidgets import QLabel
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QLabel = createWidgetMenuBase(QLabel)

class QtBoxFuncLabel7(QLabel):
    def __init__(self):
        super(QtBoxFuncLabel7, self).__init__(str(Path(__file__)))
        self.setText("Drop a txt file on me.\n"
                     "I will show its content.")
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        super(QtBoxFuncLabel7, self).dragEnterEvent(event)
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        super(QtBoxFuncLabel7, self).dropEvent(event)
        url = event.mimeData().urls()[0].toLocalFile()
        if not url.endswith(".txt"):
            return

        with open(url, "r", encoding="utf-8") as f:
            self.setText(f.read())
# PyQt

# PySide
# from PySide2.QtWidgets import QLabel


# class QtBoxFuncLabel7(QLabel):
#     def __init__(self):
#         super(QtBoxFuncLabel7, self).__init__()
#         self.setText("Drop a txt file on me.\n"
#                      "I will show its content.")
#         self.setAcceptDrops(True)

#     def dragEnterEvent(self, event):
#         super(QtBoxFuncLabel7, self).dragEnterEvent(event)
#         if event.mimeData().hasUrls():
#             event.acceptProposedAction()

#     def dropEvent(self, event):
#         super(QtBoxFuncLabel7, self).dropEvent(event)
#         url = event.mimeData().urls()[0].toLocalFile()
#         if not url.endswith(".txt"):
#             return

#         with open(url, "r", encoding="utf-8") as f:
#             self.setText(f.read())
# PySide