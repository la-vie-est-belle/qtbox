import json
from pathlib import Path
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

RES_PATH = Path(__file__).parent.parent / "res"


class MessageBox(QWidget):
    def __init__(self):
        super(MessageBox, self).__init__()
        self.title_label = QLabel()
        self.content_browser = QTextBrowser()
        self.confirm_btn = QPushButton()
        self.close_btn = QPushButton(self)

        self.start_x = None
        self.start_y = None

        self.bg_color = None

        self.set_up()

    def set_up(self):
        self.set_widget()
        self.set_signal()
        self.set_layout()
        self.set_window_attr()
        self.set_object_name()
        self.set_style_sheet()

    def set_widget(self):
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setFixedWidth(220)
        self.content_browser.setMinimumHeight(300)
        self.confirm_btn.setText("OK")
        self.confirm_btn.setFixedSize(100, 30)
        self.close_btn.move(288, 2)
        self.close_btn.setFixedSize(30, 30)
        self.close_btn.setIcon(QIcon(str(RES_PATH / "images/close.png")))

    def set_signal(self):
        self.close_btn.clicked.connect(self.close)
        self.confirm_btn.clicked.connect(self.close)

    def set_layout(self):
        all_v_layout = QVBoxLayout(self)
        title_h_layout = QHBoxLayout()
        btn_h_layout = QHBoxLayout()
        title_h_layout.addWidget(self.title_label)
        title_h_layout.setAlignment(Qt.AlignCenter)
        all_v_layout.addLayout(title_h_layout)
        all_v_layout.addSpacing(5)
        all_v_layout.addWidget(self.content_browser)
        all_v_layout.addSpacing(5)
        btn_h_layout.addWidget(self.confirm_btn)
        btn_h_layout.setAlignment(Qt.AlignCenter)
        all_v_layout.addLayout(btn_h_layout)

    def set_window_attr(self):
        self.setFixedSize(320, 450)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def set_object_name(self):
        self.setObjectName("messageBox")
        self.title_label.setObjectName("titleLabel")
        self.content_browser.setObjectName("contentBrowser")
        self.confirm_btn.setObjectName("confirmBtn")
        self.close_btn.setObjectName("closeBtn")

    def set_style_sheet(self):
        with open(RES_PATH / "config.json", "r", encoding="utf-8") as f:
            theme = json.loads(f.read())["theme"]

        with open(RES_PATH / f"qss/{theme}/message_box.qss", encoding="utf-8") as f:
            self.setStyleSheet(f.read())

        if theme == "black":
            self.bg_color = "#3b3f42"
        else:
            self.bg_color = "#f2f2f2"

    def mousePressEvent(self, event):
        pass

    def paintEvent(self, event):
        super(MessageBox, self).paintEvent(event)
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(self.bg_color))
        painter.setRenderHint(QPainter.Antialiasing)
        painter.drawRoundedRect(self.rect(), 5, 5)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_x = event.x()
            self.start_y = event.y()

    def mouseMoveEvent(self, event):
        if self.start_x is None or self.start_y is None:
            return

        dis_x = event.x() - self.start_x
        dis_y = event.y() - self.start_y
        self.move(self.x() + dis_x, self.y() + dis_y)

    def mouseReleaseEvent(self, event):
        self.start_x = None
        self.start_y = None

    def set_title(self, s):
        self.title_label.setText(s)

    def set_plain_text(self, s):
        self.content_browser.setPlainText(s)

    def set_html(self, s):
        self.content_browser.setHtml(s)

    def reload_style_sheet(self):
        self.set_style_sheet()