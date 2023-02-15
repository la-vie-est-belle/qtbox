# PyQt
import webbrowser
from PyQt5.QtWidgets import QPushButton
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QPushButton = createWidgetMenuBase(QPushButton)

class QtBoxFuncButton3(QPushButton):
    def __init__(self):
        super(QtBoxFuncButton3, self).__init__(str(Path(__file__)))
        self.setText("Open a website")
        self.clicked.connect(self.open_a_website)

    def open_a_website(self):
        url = "https://github.com/la-vie-est-belle/qtbox"
        webbrowser.open(url)
# PyQt

# PySide
# import webbrowser
# from PySide2.QtWidgets import QPushButton


# class QtBoxFuncButton3(QPushButton):
#     def __init__(self):
#         super(QtBoxFuncButton3, self).__init__()
#         self.setText("Open a website")
#         self.clicked.connect(self.open_a_website)

#     def open_a_website(self):
#         url = "https://github.com/la-vie-est-belle/qtbox"
#         webbrowser.open(url)
# PySide