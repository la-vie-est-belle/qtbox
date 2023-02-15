import json
from pathlib import Path
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

RES_PATH = Path(__file__).parent.parent / "res"


class ContextMenu(QMenu):
    view_code_signal = pyqtSignal()
    download_code_signal = pyqtSignal()

    def __init__(self):
        super(ContextMenu, self).__init__()
        self.view_code_action = QAction(QIcon(str(RES_PATH / "images/open_eye.png")), "View Code", self)
        self.download_code_action = QAction(QIcon(str(RES_PATH / "images/download.png")), "Download Code", self)

        self.set_up()

    def set_up(self):
        self.set_action()
        self.set_signal()
        self.set_style_sheet()

    def set_action(self):
        self.addAction(self.view_code_action)
        self.addAction(self.download_code_action)

    def set_signal(self):
        self.view_code_action.triggered.connect(self.view_code_signal.emit)
        self.download_code_action.triggered.connect(self.download_code_signal.emit)

    def set_style_sheet(self):
        with open(RES_PATH / "config.json", "r", encoding="utf-8") as f:
            theme = json.loads(f.read())["theme"]

        with open(RES_PATH / f"qss/{theme}/menu.qss", encoding="utf-8") as f:
            self.setStyleSheet(f.read())

    def reload_style_sheet(self):
        self.set_style_sheet()


def createWidgetMenuBase(cls):
    class WidgetMenuBase(cls):
        view_code_signal = pyqtSignal(str)
        download_code_signal = pyqtSignal(str)

        def __init__(self, code_file_path):
            super(WidgetMenuBase, self).__init__()
            self.code_file_path = code_file_path
            self.context_menu = ContextMenu()

        def contextMenuEvent(self, event):
            self.context_menu.view_code_signal.connect(lambda: self.view_code_signal.emit(self.code_file_path))
            self.context_menu.download_code_signal.connect(lambda: self.download_code_signal.emit(self.code_file_path))
            self.context_menu.exec(event.globalPos())

    return WidgetMenuBase
