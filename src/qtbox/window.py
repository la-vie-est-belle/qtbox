import re
import sys
import json
import webbrowser
from pathlib import Path

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from qtbox.utils.check import check_update
from qtbox.utils.editor import QSSEditor
from qtbox.utils.viewer import CodeViewer
from qtbox.utils.message import MessageBox
from qtbox.utils.title import TitleWidget as WindowTitle

from qtbox.checkbox import func as func_checkbox
from qtbox.checkbox import style as style_checkbox
from qtbox.combobox import func as func_combobox
from qtbox.combobox import style as style_combobox
from qtbox.dial import func as func_dial
from qtbox.dial import style as style_dial
from qtbox.label import func as func_label
from qtbox.label import style as style_label
from qtbox.lcdnumber import func as func_lcdnumber
from qtbox.lcdnumber import style as style_lcdnumber
from qtbox.lineedit import func as func_lineedit
from qtbox.lineedit import style as style_lineedit
from qtbox.listwidget import func as func_listwidget
from qtbox.listwidget import style as style_listwidget
from qtbox.progressbar import func as func_progressbar
from qtbox.progressbar import style as style_progressbar
from qtbox.pushbutton import func as func_pushbutton
from qtbox.pushbutton import style as style_pushbutton
from qtbox.slider import func as func_slider
from qtbox.slider import style as style_slider
from qtbox.spinbox import func as func_spinbox
from qtbox.spinbox import style as style_spinbox
from qtbox.tablewidget import func as func_tablewidget
from qtbox.tablewidget import style as style_tablewidget
from qtbox.widget import func as func_widget
from qtbox.widget import style as style_widget

VERSION = "1.1.4"

UPDATES = """
1. Added 1 style demo and 2 func demos for QTableWidget.\n
2. Enriched widget choices in QSS Editor. \n
3. Optimized suppress_stdout_stderr() in output.py. \n
4. Eliminate the framework's QSS effect (e.g. QScrollBar's QSS effect) on demos.
"""

RES_PATH = Path(__file__).parent / "res"


class WindowBody(QWidget):
    switch_theme_signal = pyqtSignal()

    def __init__(self):
        super(WindowBody, self).__init__()
        self.btn_list_widget = QListWidget()
        self.btn_list = [QPushButton(txt) for txt in ["QCheckBox", "QComboBox", "QDial",
                                                      "QLabel", "QLCDNumber", "QLineEdit",
                                                      "QListWidget", "QProgressBar", "QPushButton",
                                                      "QSlider", "QSpinBox", "QTableWidget", "QWidget"]]
        self.func_widget = QWidget()
        self.style_widget = QWidget()
        self.func_tab = QScrollArea()
        self.style_tab = QScrollArea()
        self.tab_widget = QTabWidget()

        self.editor_btn = QPushButton()
        self.sponsor_btn = QPushButton()
        self.doc_btn = QPushButton()
        self.about_btn = QPushButton()
        self.switch_btn = QPushButton()

        self.qss_editor = QSSEditor()
        self.code_viewer = CodeViewer()
        self.updates_message_box = MessageBox()
        self.sponsor_message_box = MessageBox()

        self.grid_layout_children = []
        self.grid_layout = QGridLayout()

        self.checkbox_dict = {
            "func": [func_checkbox.demo1.QtBoxFuncCheckBox1, func_checkbox.demo2.QtBoxFuncCheckBox2],
            "style": [style_checkbox.demo1.QtBoxStyleCheckBox1, style_checkbox.demo2.QtBoxStyleCheckBox2, style_checkbox.demo3.QtBoxStyleCheckBox3,
                      style_checkbox.demo4.QtBoxStyleCheckBox4]
        }

        self.combobox_dict = {
            "func": [func_combobox.demo1.QtBoxFuncComboBox1, func_combobox.demo2.QtBoxFuncComboBox2],
            "style": [style_combobox.demo1.QtBoxStyleComboBox1, style_combobox.demo2.QtBoxStyleComboBox2, style_combobox.demo3.QtBoxStyleComboBox3]
        }

        self.dial_dict = {
            "func": [func_dial.demo1.QtBoxFuncDial1],
            "style": [style_dial.demo1.QtBoxStyleDial1, style_dial.demo2.QtBoxStyleDial2]
        }

        self.label_dict = {
            "func": [func_label.demo1.QtBoxFuncLabel1, func_label.demo2.QtBoxFuncLabel2, func_label.demo3.QtBoxFuncLabel3,
                     func_label.demo4.QtBoxFuncLabel4, func_label.demo5.QtBoxFuncLabel5, func_label.demo6.QtBoxFuncLabel6,
                     func_label.demo7.QtBoxFuncLabel7],
            "style": [style_label.demo1.QtBoxStyleLabel1, style_label.demo2.QtBoxStyleLabel2, style_label.demo3.QtBoxStyleLabel3,
                      style_label.demo4.QtBoxStyleLabel4]
        }

        self.lcdnumber_dict = {
            "func": [func_lcdnumber.demo1.QtBoxFuncLCDNumber1, func_lcdnumber.demo2.QtBoxFuncLCDNumber2, func_lcdnumber.demo3.QtBoxFuncLCDNumber3],
            "style": [style_lcdnumber.demo1.QtBoxStyleLCDNumber1, style_lcdnumber.demo2.QtBoxStyleLCDNumber2, style_lcdnumber.demo3.QtBoxStyleLCDNumber3,
                      style_lcdnumber.demo4.QtBoxStyleLCDNumber4, style_lcdnumber.demo5.QtBoxStyleLCDNumber5]
        }

        self.lineedit_dict = {
            "func": [func_lineedit.demo1.QtBoxFuncLineEdit1, func_lineedit.demo2.QtBoxFuncLineEdit2, func_lineedit.demo3.QtBoxFuncLineEdit3,
                     func_lineedit.demo4.QtBoxFuncLineEdit4, func_lineedit.demo5.QtBoxFuncLineEdit5],
            "style": [style_lineedit.demo1.QtBoxStyleLineEdit1, style_lineedit.demo2.QtBoxStyleLineEdit2, style_lineedit.demo3.QtBoxStyleLineEdit3,
                      style_lineedit.demo4.QtBoxStyleLineEdit4, style_lineedit.demo5.QtBoxStyleLineEdit5, style_lineedit.demo6.QtBoxStyleLineEdit6,
                      style_lineedit.demo7.QtBoxStyleLineEdit7]
        }

        self.listwidget_dict = {
            "func": [func_listwidget.demo1.QtBoxFuncListWidget1],
            "style": [style_listwidget.demo1.QtBoxStyleListWidget1, style_listwidget.demo2.QtBoxStyleListWidget2]
        }

        self.progressbar_dict = {
            "func": [func_progressbar.demo1.QtBoxFuncProgressBar1, func_progressbar.demo2.QtBoxFuncProgressBar2],
            "style": [style_progressbar.demo1.QtBoxStyleProgressBar1, style_progressbar.demo2.QtBoxStyleProgressBar2, style_progressbar.demo3.QtBoxStyleProgressBar3,
                      style_progressbar.demo4.QtBoxStyleProgressBar4, style_progressbar.demo5.QtBoxStyleProgressBar5, style_progressbar.demo6.QtBoxStyleProgressBar6,
                      style_progressbar.demo7.QtBoxStyleProgressBar7, style_progressbar.demo8.QtBoxStyleProgressBar8, style_progressbar.demo9.QtBoxStyleProgressBar9]
        }

        self.pushbutton_dict = {
            "func": [func_pushbutton.demo1.QtBoxFuncButton1, func_pushbutton.demo2.QtBoxFuncButton2, func_pushbutton.demo3.QtBoxFuncButton3],
            "style": [style_pushbutton.demo1.QtBoxStyleButton1, style_pushbutton.demo2.QtBoxStyleButton2, style_pushbutton.demo3.QtBoxStyleButton3,
                      style_pushbutton.demo4.QtBoxStyleButton4, style_pushbutton.demo5.QtBoxStyleButton5, style_pushbutton.demo6.QtBoxStyleButton6,
                      style_pushbutton.demo7.QtBoxStyleButton7, style_pushbutton.demo8.QtBoxStyleButton8, style_pushbutton.demo9.QtBoxStyleButton9,
                      style_pushbutton.demo10.QtBoxStyleButton10, style_pushbutton.demo11.QtBoxStyleButton11, style_pushbutton.demo12.QtBoxStyleButton12]
        }

        self.slider_dict = {
            "func": [func_slider.demo1.QtBoxFuncSlider1],
            "style": [style_slider.demo1.QtBoxStyleSlider1, style_slider.demo2.QtBoxStyleSlider2, style_slider.demo3.QtBoxStyleSlider3,
                      style_slider.demo4.QtBoxStyleSlider4, style_slider.demo5.QtBoxStyleSlider5]
        }

        self.spinbox_dict = {
            "func": [func_spinbox.demo1.QtBoxFuncSpinBox1],
            "style": [style_spinbox.demo1.QtBoxStyleSpinBox1]
        }

        self.tablewidget_dict = {
            "func": [func_tablewidget.demo1.QtBoxFuncTableWidget1, func_tablewidget.demo2.QtBoxFuncTableWidget2],
            "style": [style_tablewidget.demo1.QtBoxStyleTableWidget1]
        }

        self.widget_dict = {
            "func": [func_widget.demo1.QtBoxFuncWidget1, func_widget.demo2.QtBoxFuncWidget2],
            "style": [style_widget.demo1.QtBoxStyleWidget1, style_widget.demo2.QtBoxStyleWidget2]
        }

        self.set_up()

    def set_up(self):
        self.set_object_name()
        self.set_style_sheet()
        self.set_widget()
        self.set_signal()
        self.set_layout()

        self.btn_list[0].setCheckable(True)
        self.btn_list[0].setChecked(True)
        self.set_tab_content("QCheckBox")

    def set_object_name(self):
        self.setObjectName("windowBody")
        self.btn_list_widget.setObjectName("btnList")
        self.btn_list_widget.verticalScrollBar().setObjectName("btnList")

        for btn in self.btn_list:
            btn.setObjectName("listBtn")

        self.editor_btn.setObjectName("editorBtn")
        self.sponsor_btn.setObjectName("sponsorBtn")
        self.doc_btn.setObjectName("docBtn")
        self.about_btn.setObjectName("aboutBtn")
        self.switch_btn.setObjectName("switchBtn")

        self.tab_widget.setObjectName("tabWidget")
        self.func_tab.setObjectName("funcScrollArea")
        self.style_tab.setObjectName("styleScrollArea")
        self.func_tab.verticalScrollBar().setObjectName("funcScrollVBar")
        self.func_tab.horizontalScrollBar().setObjectName("funcScrollHBar")
        self.style_tab.verticalScrollBar().setObjectName("styleScrollVBar")
        self.style_tab.horizontalScrollBar().setObjectName("styleScrollHBar")
        self.func_widget.setObjectName("funcWidget")
        self.style_widget.setObjectName("styleWidget")

    def set_style_sheet(self):
        with open(RES_PATH / "config.json", "r", encoding="utf-8") as f:
            theme = json.loads(f.read())["theme"]

        with open(RES_PATH / f"qss/{theme}/window_body.qss", encoding="utf-8") as f:
            self.setStyleSheet(f.read())

    def set_widget(self):
        self.btn_list_widget.setMaximumWidth(300)
        self.btn_list_widget.setMinimumWidth(150)

        self.func_tab.setWidgetResizable(True)
        self.style_tab.setWidgetResizable(True)
        self.func_tab.setWidget(self.func_widget)
        self.style_tab.setWidget(self.style_widget)
        self.func_tab.setAlignment(Qt.AlignCenter)
        self.style_tab.setAlignment(Qt.AlignCenter)
        self.tab_widget.addTab(self.style_tab, "Style")
        self.tab_widget.addTab(self.func_tab, "Function")

        self.editor_btn.setFixedWidth(30)
        self.sponsor_btn.setFixedWidth(30)
        self.doc_btn.setFixedWidth(30)
        self.about_btn.setFixedWidth(30)
        self.switch_btn.setFixedWidth(30)
        self.editor_btn.setToolTip("Open QSS editor")
        self.sponsor_btn.setToolTip("Sponsor")
        self.doc_btn.setToolTip("Open documentation")
        self.about_btn.setToolTip("Show updates")
        self.switch_btn.setToolTip("Switch theme")
        self.editor_btn.setCursor(Qt.PointingHandCursor)
        self.sponsor_btn.setCursor(Qt.PointingHandCursor)
        self.doc_btn.setCursor(Qt.PointingHandCursor)
        self.about_btn.setCursor(Qt.PointingHandCursor)
        self.switch_btn.setCursor(Qt.PointingHandCursor)
        self.editor_btn.setIcon(QIcon(str(RES_PATH / "images/editor.png")))
        self.sponsor_btn.setIcon(QIcon(str(RES_PATH / "images/sponsor.png")))
        self.doc_btn.setIcon(QIcon(str(RES_PATH / "images/doc.png")))
        self.about_btn.setIcon(QIcon(str(RES_PATH / "images/about.png")))
        self.switch_btn.setIcon(QIcon(str(RES_PATH / "images/switch.png")))

        self.code_viewer.hide()

        desktop = QApplication.desktop()
        self.updates_message_box.move(desktop.width()//2-self.updates_message_box.width()//2, desktop.height()//2-self.updates_message_box.height()//2)
        self.updates_message_box.set_title(f"Qt Box Updates v{VERSION}")
        self.updates_message_box.set_plain_text(UPDATES)
        self.updates_message_box.content_browser.setLineWrapMode(QTextEdit.NoWrap)
        self.updates_message_box.hide()

        self.sponsor_message_box.setFixedSize(320, 205)
        self.sponsor_message_box.content_browser.setMinimumHeight(95)
        self.sponsor_message_box.move(desktop.width()//2-self.sponsor_message_box.width()//2, desktop.height()//2-self.sponsor_message_box.height()//2)
        self.sponsor_message_box.set_title("Customize")
        self.sponsor_message_box.set_html("Contact <a href='mailto:louasure@126.com' style='text-decoration:none'>louasure@126.com</a> to customize a widget. If you have any problems with PyQt or PySide, you may contact me, too. I will be very happy to provide solutions. <a href='https://github.com/la-vie-est-belle/qtbox' style='text-decoration:none'>Sponsors'</a> needs will be treated with top priority. (๑•̀ㅂ•́)و✧")
        self.sponsor_message_box.content_browser.setOpenExternalLinks(True)
        self.sponsor_message_box.content_browser.setAlignment(Qt.AlignJustify)
        self.sponsor_message_box.hide()

    def set_signal(self):
        for btn in self.btn_list:
            btn.clicked.connect(self.change_widget)

        self.editor_btn.clicked.connect(self.open_editor)
        self.sponsor_btn.clicked.connect(self.show_sponsor_message)
        self.doc_btn.clicked.connect(self.open_doc)
        self.about_btn.clicked.connect(self.show_updates)
        self.switch_btn.clicked.connect(self.switch_theme)
        self.tab_widget.currentChanged.connect(self.change_tab)

    def set_layout(self):
        v_layout1 = QVBoxLayout()
        h_layout1 = QHBoxLayout()
        h_layout2 = QHBoxLayout()
        v_layout1.setContentsMargins(0, 0, 0, 0)
        h_layout1.setContentsMargins(0, 0, 0, 0)

        for btn in self.btn_list:
            item = QListWidgetItem()
            item.setSizeHint(QSize(150, 50))
            self.btn_list_widget.addItem(item)
            self.btn_list_widget.setItemWidget(item, btn)

        h_layout1.addWidget(self.editor_btn)
        h_layout1.addWidget(self.sponsor_btn)
        h_layout1.addWidget(self.doc_btn)
        h_layout1.addWidget(self.about_btn)
        h_layout1.addWidget(self.switch_btn)
        h_layout1.setSpacing(30)

        v_layout1.addLayout(h_layout1)
        v_layout1.addWidget(self.btn_list_widget)
        v_layout1.setSpacing(6)
        h_layout2.addLayout(v_layout1)
        h_layout2.addWidget(self.tab_widget)
        self.setLayout(h_layout2)

        self.grid_layout.setVerticalSpacing(70)
        self.grid_layout.setHorizontalSpacing(60)

    def change_widget(self):
        self.update_btn_style()
        self.clear_grid_layout()
        self.set_tab_content(self.sender().text())

    def change_tab(self):
        """change between Style and Function tab"""
        self.clear_grid_layout()

        for btn in self.btn_list:
            if btn.isChecked():
                self.set_tab_content(btn.text())
                break

    def update_btn_style(self):
        for btn in self.btn_list:
            btn.setCheckable(False)
            btn.setChecked(False)

        self.sender().setCheckable(True)
        self.sender().setChecked(True)
        self.btn_list_widget.update()

    def clear_grid_layout(self):
        for widget in self.grid_layout_children:
            widget.deleteLater()
        self.grid_layout_children = []
        self.tab_widget.update()

    def set_tab_content(self, btn_txt):
        widget_list = []
        tab_index = self.tab_widget.currentIndex()

        key = "style" if tab_index == 0 else "func"
        if btn_txt == "QComboBox":
            widget_list = self.combobox_dict[key]

        elif btn_txt == "QCheckBox":
            widget_list = self.checkbox_dict[key]

        elif btn_txt == "QDial":
            widget_list = self.dial_dict[key]

        elif btn_txt == "QLabel":
            widget_list = self.label_dict[key]

        elif btn_txt == "QLCDNumber":
            widget_list = self.lcdnumber_dict[key]

        elif btn_txt == "QLineEdit":
            widget_list = self.lineedit_dict[key]

        elif btn_txt == "QListWidget":
            widget_list = self.listwidget_dict[key]

        elif btn_txt == "QProgressBar":
            widget_list = self.progressbar_dict[key]

        elif btn_txt == "QPushButton":
            widget_list = self.pushbutton_dict[key]

        elif btn_txt == "QSlider":
            widget_list = self.slider_dict[key]

        elif btn_txt == "QSpinBox":
            widget_list = self.spinbox_dict[key]

        elif btn_txt == "QTableWidget":
            widget_list = self.tablewidget_dict[key]

        elif btn_txt == "QWidget":
            widget_list = self.widget_dict[key]

        if tab_index == 0:
            self.set_style_tab_content(widget_list)
        else:
            self.set_func_tab_content(widget_list)

    def set_style_tab_content(self, widget_list):
        self.add_widget_list_to_grid_layout(widget_list)
        self.style_widget.setLayout(self.grid_layout)

    def set_func_tab_content(self, widget_list):
        self.add_widget_list_to_grid_layout(widget_list)
        self.func_widget.setLayout(self.grid_layout)

    def add_widget_list_to_grid_layout(self, widget_list):
        row, column = 0, 0
        for widget in widget_list:
            if column != 0 and column % 3 == 0:
                row += 1
                column = 0

            widget = widget()
            widget.view_code_signal.connect(self.view_code)
            widget.download_code_signal.connect(self.download_code)
            self.grid_layout.addWidget(widget, row, column, 1, 1, Qt.AlignCenter)
            self.grid_layout_children.append(widget)
            column += 1

    def view_code(self, code_file_path):
        pyqt_code, pyside_code = self.get_code_content(code_file_path)
        self.code_viewer.set_pyqt_and_pyside_property(pyqt_code, pyside_code)
        self.code_viewer.set_code(pyqt_code)
        self.code_viewer.show()
        self.code_viewer.raise_()

    def download_code(self, code_file_path):
        path = QFileDialog.getExistingDirectory(self, "Open Directory", "./", QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        if not path:
            return

        pyqt_code, pyside_code = self.get_code_content(code_file_path)
        with open(path+"/pyqt_code.py", "w", encoding="utf-8") as f:
            f.write(pyqt_code)
        with open(path+"/pyside_code.py", "w", encoding="utf-8") as f:
            f.write(pyside_code)

    @staticmethod
    def get_code_content(code_file_path):
        content = ""
        with open(code_file_path, "r", encoding="utf-8") as f:
            for line in f.readlines():
                if "pathlib" not in line and "Base" not in line and '"res/images' not in line:
                    content += line
            content = content.replace("str(Path(__file__))", "").replace("%s", "PATH_TO_IMG")
            content = re.sub(r" % \(.+\)", ")", content)

        try:
            pyqt_code = re.search(r"# PyQt.+# PyQt", content, re.DOTALL).group().replace("# PyQt\n", "").replace("# PyQt", "")
        except AttributeError:
            pyqt_code = ""

        try:
            pyside_code = re.search(r"# PySide.+# PySide", content, re.DOTALL).group().replace("# PySide\n", "").replace("# PySide", "").replace("# ", "")
        except AttributeError:
            pyside_code = ""

        return pyqt_code, pyside_code

    def open_editor(self):
        self.qss_editor.show()

    def show_sponsor_message(self):
        self.sponsor_message_box.show()
        self.sponsor_message_box.raise_()

    @staticmethod
    def open_doc():
        webbrowser.open("https://github.com/la-vie-est-belle/qtbox")

    def show_updates(self):
        self.updates_message_box.show()
        self.updates_message_box.raise_()

    def switch_theme(self):
        self.switch_theme_signal.emit()

    def reload_style_sheet(self):
        self.set_style_sheet()
        self.qss_editor.reload_style_sheet()
        self.code_viewer.reload_style_sheet()
        self.updates_message_box.reload_style_sheet()
        self.sponsor_message_box.reload_style_sheet()

        for widget in self.grid_layout_children:
            widget.context_menu.reload_style_sheet()


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.window_title = WindowTitle()
        self.window_body = WindowBody()

        self.start_x = None
        self.start_y = None

        self.bg_color = None

        self.set_up()

    def set_up(self):
        self.set_window_attr()
        self.set_object_name()
        self.set_style_sheet()
        self.set_signal()
        self.set_layout()

    def set_window_attr(self):
        self.resize(1000, 600)
        self.setWindowTitle("Qt Box")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowIcon(QIcon(str(RES_PATH / "images/icon.png")))

    def set_object_name(self):
        self.setObjectName("window")

    def set_style_sheet(self):
        with open(RES_PATH / "config.json", "r", encoding="utf-8") as f:
            theme = json.loads(f.read())["theme"]

        if theme == "black":
            self.bg_color = "#3b3f42"
        else:
            self.bg_color = "#f2f2f2"

    def set_signal(self):
        self.window_title.close_signal.connect(self.close)
        self.window_title.minimize_signal.connect(self.showMinimized)
        self.window_title.maximize_signal.connect(self.showMaximized)
        self.window_title.show_normal_signal.connect(self.showNormal)
        self.window_body.switch_theme_signal.connect(self.reload_style_sheet)

    def set_layout(self):
        v_layout = QVBoxLayout(self)
        v_layout.setSpacing(0)
        v_layout.addWidget(self.window_title)
        v_layout.addWidget(self.window_body)
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
        super(Window, self).paintEvent(event)
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
        super(Window, self).showNormal()
        self.resize(1000, 600)
        desktop = QApplication.desktop()
        self.move(desktop.width() // 2 - self.width() // 2, desktop.height() // 2 - self.height() // 2)

    def reload_style_sheet(self):
        with open(RES_PATH / "config.json", "r", encoding="utf-8") as f:
            config = json.loads(f.read())

        if config["theme"] == "black":
            config["theme"] = "white"
        else:
            config["theme"] = "black"

        with open(RES_PATH / "config.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(config))

        self.set_style_sheet()
        self.window_title.reload_style_sheet()
        self.window_body.reload_style_sheet()


def main():
    check_update()
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()