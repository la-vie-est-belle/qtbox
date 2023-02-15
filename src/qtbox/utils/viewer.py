import json
from pathlib import Path
from qtbox.utils.title import TitleWidget as CodeViewerTitle

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter


RES_PATH = Path(__file__).parent.parent / "res"


class CodeViewerBody(QTextBrowser):
    def __init__(self):
        super(CodeViewerBody, self).__init__()
        self.clipboard = QApplication.clipboard()
        self.switch_btn = QPushButton()
        self.copy_btn = QPushButton()
        self.pyside_code = ""
        self.pyqt_code = ""
        self.code = ""
        self.theme = None

        self.set_up()

    def set_up(self):
        self.set_object_name()
        self.set_style_sheet()
        self.set_widget()
        self.set_signal()
        self.set_layout()

    def set_object_name(self):
        self.setObjectName("codeViewer")
        self.switch_btn.setObjectName("switchBtn")
        self.copy_btn.setObjectName("copyBtn")

    def set_style_sheet(self):
        with open(RES_PATH / "config.json", "r", encoding="utf-8") as f:
            self.theme = json.loads(f.read())["theme"]

        with open(RES_PATH / f"qss/{self.theme}/viewer.qss", encoding="utf-8") as f:
            self.setStyleSheet(f.read())

    def set_widget(self):
        self.switch_btn.setToolTip("Switch to PySide")
        self.switch_btn.setCursor(Qt.PointingHandCursor)
        self.switch_btn.setIcon(QIcon(str(RES_PATH / "images/switch.png")))
        self.copy_btn.setToolTip("Click to copy")
        self.copy_btn.setCursor(Qt.PointingHandCursor)
        self.copy_btn.setIcon(QIcon(str(RES_PATH / "images/copy.png")))
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

    def set_signal(self):
        self.copy_btn.clicked.connect(self.copy)
        self.switch_btn.clicked.connect(self.switch_code)
        self.clipboard.dataChanged.connect(self.on_clipboard_changed)

    def set_layout(self):
        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout(self)
        h_layout.addStretch()
        h_layout.addWidget(self.switch_btn)
        h_layout.addWidget(self.copy_btn)
        v_layout.addLayout(h_layout)
        v_layout.addStretch()

    def set_code(self, code):
        self.code = code
        if self.theme == "black":
            formatter = HtmlFormatter(linenos=True, style="paraiso-dark")
            css = "<style>" + formatter.get_style_defs('.highlight').replace("#2f1e2e", "#2b2b2b").replace("#4f424c", "#2b2b2b") + "</style>"
        else:
            formatter = HtmlFormatter(linenos=True, style="tango")
            css = "<style>" + formatter.get_style_defs('.highlight').replace("#ffffcc", "#ffffff").replace("#f8f8f8", "#ffffff") + "</style>"
        html = highlight(self.code, lexer=PythonLexer(), formatter=formatter)
        self.setHtml(css+html)
        self.horizontalScrollBar().move(0, 0)

        self.copy_btn.setIcon(QIcon(str(RES_PATH / "images/copy.png")))
        self.copy_btn.setToolTip("Click to copy")

    def copy(self):
        self.clipboard.setText(self.code)

    def on_clipboard_changed(self):
        data = self.clipboard.mimeData()
        if data.text() == self.code:
            self.copy_btn.setIcon(QIcon(str(RES_PATH / "images/check.png")))
            self.copy_btn.setToolTip("Copied")
        else:
            self.copy_btn.setIcon(QIcon(str(RES_PATH / "images/copy.png")))
            self.copy_btn.setToolTip("Click to copy")

    def contextMenuEvent(self, event):
        pass

    def switch_code(self):
        if self.switch_btn.toolTip() == "Switch to PySide":
            self.switch_btn.setToolTip("Switch to PyQt")
            self.set_code(self.pyside_code)
        else:
            self.switch_btn.setToolTip("Switch to PySide")
            self.set_code(self.pyqt_code)

    def reload_style_sheet(self):
        self.set_style_sheet()


class CodeViewer(QWidget):
    def __init__(self):
        super(CodeViewer, self).__init__()
        self.code_viewer_title = CodeViewerTitle()
        self.code_viewer_body = CodeViewerBody()

        self.start_x = None
        self.start_y = None

        self.bg_color = None

        self.set_up()

    def set_up(self):
        self.set_window_attr()
        self.set_style_sheet()
        self.set_signal()
        self.set_layout()

    def set_window_attr(self):
        self.resize(700, 500)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def set_style_sheet(self):
        with open(RES_PATH / "config.json", "r", encoding="utf-8") as f:
            theme = json.loads(f.read())["theme"]

        if theme == "black":
            self.bg_color = "#3b3f42"
        else:
            self.bg_color = "#f2f2f2"

    def set_signal(self):
        self.code_viewer_title.close_signal.connect(self.close)
        self.code_viewer_title.minimize_signal.connect(self.showMinimized)
        self.code_viewer_title.maximize_signal.connect(self.showMaximized)
        self.code_viewer_title.show_normal_signal.connect(self.showNormal)

    def set_layout(self):
        v_layout = QVBoxLayout(self)
        v_layout.setSpacing(0)
        v_layout.addWidget(self.code_viewer_title)
        v_layout.addWidget(self.code_viewer_body)
        v_layout.setSpacing(5)
        v_layout.setContentsMargins(0, 0, 0, 0)

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

    def paintEvent(self, event):
        super(CodeViewer, self).paintEvent(event)
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(self.bg_color))
        painter.setRenderHint(QPainter.Antialiasing)
        painter.drawRoundedRect(self.rect(), 9, 9)

    def showMaximized(self):
        self.move(0, 0)
        desktop = QApplication.desktop()
        self.resize(desktop.width(), desktop.height())

    def showNormal(self):
        super(CodeViewer, self).showNormal()
        self.resize(700, 500)
        desktop = QApplication.desktop()
        self.move(desktop.width() // 2 - self.width() // 2, desktop.height() // 2 - self.height() // 2)

    def set_pyqt_and_pyside_property(self, pyqt_code, pyside_code):
        self.code_viewer_body.pyqt_code = pyqt_code
        self.code_viewer_body.pyside_code = pyside_code

    def set_code(self, code):
        self.code_viewer_body.set_code(code)

    def reload_style_sheet(self):
        self.set_style_sheet()
        self.code_viewer_title.reload_style_sheet()
        self.code_viewer_body.reload_style_sheet()
        self.code_viewer_body.set_code(self.code_viewer_body.code)
