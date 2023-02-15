import json
from pathlib import Path
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


RES_PATH = Path(__file__).parent.parent / "res"


class TitleWidget(QWidget):
    close_signal = pyqtSignal()
    minimize_signal = pyqtSignal()
    maximize_signal = pyqtSignal()
    show_normal_signal = pyqtSignal()

    def __init__(self):
        super(TitleWidget, self).__init__()
        self.maximized_or_normal = "normal"

        self.minimize_btn = QPushButton()
        self.maximize_or_normal_btn = QPushButton()
        self.close_window_btn = QPushButton()

        self.set_up()

    def set_up(self):
        self.set_object_name()
        self.set_style_sheet()
        self.set_widget()
        self.set_signal()
        self.set_layout()

    def set_object_name(self):
        self.setObjectName("windowTitle")
        self.minimize_btn.setObjectName("minimizeBtn")
        self.maximize_or_normal_btn.setObjectName("maximizeNormalBtn")
        self.close_window_btn.setObjectName("closeBtn")

    def set_style_sheet(self):
        with open(RES_PATH / "config.json", "r", encoding="utf-8") as f:
            theme = json.loads(f.read())["theme"]

        with open(RES_PATH / f"qss/{theme}/title.qss", encoding="utf-8") as f:
            self.setStyleSheet(f.read())

    def set_widget(self):
        self.minimize_btn.setFixedSize(30, 30)
        self.maximize_or_normal_btn.setFixedSize(30, 30)
        self.close_window_btn.setFixedSize(30, 30)
        self.minimize_btn.setIcon(QIcon(str(RES_PATH / "images/minimize.png")))
        self.maximize_or_normal_btn.setIcon(QIcon(str(RES_PATH / "images/maximize.png")))
        self.close_window_btn.setIcon(QIcon(str(RES_PATH / "images/close.png")))

    def set_signal(self):
        self.minimize_btn.clicked.connect(self.minimize)
        self.maximize_or_normal_btn.clicked.connect(self.maximize_or_show_normal)
        self.close_window_btn.clicked.connect(self.close_window)

    def set_layout(self):
        all_h_layout = QHBoxLayout(self)
        right_h_layout = QHBoxLayout()

        right_h_layout.setSpacing(0)
        right_h_layout.addWidget(self.minimize_btn)
        right_h_layout.addWidget(self.maximize_or_normal_btn)
        right_h_layout.addWidget(self.close_window_btn)

        all_h_layout.addStretch()
        all_h_layout.addLayout(right_h_layout)
        all_h_layout.setContentsMargins(5, 8, 5, 2)

    def minimize(self):
        self.minimize_signal.emit()

    def maximize_or_show_normal(self):
        if self.maximized_or_normal != "maximized":
            self.maximize_or_normal_btn.setIcon(QIcon(str(RES_PATH/"images/orisize.png")))
            self.maximized_or_normal = "maximized"
            self.maximize_signal.emit()
        else:
            self.maximize_or_normal_btn.setIcon(QIcon(str(RES_PATH/"images/maximize.png")))
            self.maximized_or_normal = "normal"
            self.show_normal_signal.emit()

    def close_window(self):
        self.close_signal.emit()

    def reload_style_sheet(self):
        self.set_style_sheet()

    def mouseDoubleClickEvent(self, event):
        super(TitleWidget, self).mouseDoubleClickEvent(event)
        self.maximize_or_show_normal()