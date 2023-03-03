import sys
import json
from pathlib import Path
from qtbox.utils.check import check_update
from qtbox.utils.output import suppress_stdout_stderr
from qtbox.utils.title import TitleWidget as QSSEditorTitle

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from pygments import highlight
from pygments.lexers import CssLexer
from pygments.formatters import HtmlFormatter


RES_PATH = Path(__file__).parent.parent / "res"
with open(RES_PATH / "completion.txt", "r", encoding="utf-8") as f:
    COMPLETER_LIST = [keyword.strip() for keyword in f.readlines()]


class LineNumberArea(QWidget):
    def __init__(self, parent):
        super(LineNumberArea, self).__init__(parent)
        self.parent = parent

    def sizeHint(self):
        return QSize(self.parent.get_line_number_area_width(), 0)

    def paintEvent(self, event):
        self.parent.lineNumberAreaPaintEvent(event)


class CustomTextEdit(QPlainTextEdit):
    qss_signal = pyqtSignal(str)

    def __init__(self):
        super(CustomTextEdit, self).__init__()
        self.copy_btn = QPushButton()
        self.clipboard = QApplication.clipboard()
        self.line_number_area = LineNumberArea(self)
        self.completer = QCompleter(COMPLETER_LIST, self)

        self.redo_stack_list = []
        self.undo_stack_list = []
        self.redo_max_count = 50
        self.undo_max_count = 100
        self.theme = None

        self.set_up()

    def set_up(self):
        self.set_window_attr()
        self.set_object_name()
        self.set_style_sheet()
        self.set_widget()
        self.set_signal()
        self.set_layout()

        self.highlight_line()
        self.update_line_number_area_width()

    def set_window_attr(self):
        self.setMinimumWidth(200)

    def set_object_name(self):
        self.setObjectName("customEdit")
        self.verticalScrollBar().setObjectName("customEditVScrollBar")
        self.horizontalScrollBar().setObjectName("customEditHScrollBar")
        self.copy_btn.setObjectName("copyBtn")
        self.completer.popup().setObjectName("completer")

    def set_style_sheet(self):
        with open(RES_PATH / "config.json", "r", encoding="utf-8") as f:
            self.theme = json.loads(f.read())["theme"]

        with open(RES_PATH / f"qss/{self.theme}/editor.qss", encoding="utf-8") as f:
            qss_content = f.read()
            self.setStyleSheet(qss_content)
            self.completer.popup().setStyleSheet(qss_content)

    def set_widget(self):
        self.completer.setWidget(self)
        self.setUndoRedoEnabled(False)
        self.setTabStopWidth(self.fontMetrics().width("a")*4)
        self.copy_btn.setToolTip("Click to copy")
        self.copy_btn.setCursor(Qt.PointingHandCursor)
        self.copy_btn.setIcon(QIcon(str(RES_PATH / "images/copy.png")))

    def set_signal(self):
        self.textChanged.connect(self.on_text_changed)
        self.copy_btn.clicked.connect(self.copy)
        self.clipboard.dataChanged.connect(self.on_clipboard_changed)
        self.cursorPositionChanged.connect(self.highlight_line)
        self.updateRequest.connect(self.update_line_number_area)
        self.blockCountChanged.connect(self.update_line_number_area_width)
        self.completer.activated.connect(self.activate_completer)

    def set_layout(self):
        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout(self)
        h_layout.addStretch()
        h_layout.addWidget(self.copy_btn)
        v_layout.addLayout(h_layout)
        v_layout.addStretch()

    def on_text_changed(self):
        self.qss_signal.emit(self.toPlainText())
        self.copy_btn.setToolTip("Click to copy")
        self.copy_btn.setIcon(QIcon(str(RES_PATH / "images/copy.png")))

    def copy(self):
        self.clipboard.setText(self.toPlainText())

    def on_clipboard_changed(self):
        data = self.clipboard.mimeData()
        if data.text() == self.toPlainText():
            self.copy_btn.setIcon(QIcon(str(RES_PATH / "images/check.png")))
            self.copy_btn.setToolTip("Copied")
        else:
            self.copy_btn.setIcon(QIcon(str(RES_PATH / "images/copy.png")))
            self.copy_btn.setToolTip("Click to copy")

    def highlight_line(self):
        extra_selection_list = []
        selection = QTextEdit.ExtraSelection()
        if self.theme == "black":
            selection.format.setBackground(QColor(59, 63, 66, 150))
        else:
            selection.format.setBackground(QColor(242, 242, 242, 150))
        selection.format.setProperty(QTextFormat.FullWidthSelection, True)
        selection.cursor = self.textCursor()
        selection.cursor.clearSelection()
        extra_selection_list.append(selection)
        self.setExtraSelections(extra_selection_list)

    def get_line_number_area_width(self):
        offset = 10
        digit_num = 3
        max_value = max(1, self.blockCount())
        while max_value >= 1000:
            max_value /= 10
            digit_num += 1
        width = offset + self.fontMetrics().width('9') * digit_num
        return width

    def update_line_number_area_width(self):
        self.setViewportMargins(self.get_line_number_area_width()-3, -4, -2, 0)

    def update_line_number_area(self, rect, dy):
        if dy:
            self.line_number_area.scroll(0, dy)
        else:
            self.line_number_area.update(0, rect.y(), self.line_number_area.width(), rect.height())

        if rect.contains(self.viewport().rect()):
            self.update_line_number_area_width()

    def get_current_line_number(self):
        text_cursor = self.textCursor()
        return text_cursor.blockNumber() + 1

    def activate_completer(self, text):
        completer_prefix = self.get_word_under_cursor()
        inserted_text = text.replace(completer_prefix, "")

        text_cursor = self.textCursor()
        text_cursor.insertText(inserted_text)
        current_cursor_position = text_cursor.position()

        self.highlight_text()
        new_cursor_position = text_cursor.position()

        self.move_back_cursor_after_highlight(current_cursor_position, new_cursor_position)

    def get_word_under_cursor(self):
        text_cursor = self.textCursor()
        for _ in range(text_cursor.positionInBlock()):
            text_cursor.movePosition(QTextCursor.Left, QTextCursor.KeepAnchor)
            if " " in text_cursor.selectedText() or ":" in text_cursor.selectedText():
                break
        return text_cursor.selectedText().replace(" ", "").strip()

    def highlight_text(self):
        current_plain_text = self.toPlainText().strip()

        if self.theme == "black":
            formatter = HtmlFormatter(linenos=False, style="paraiso-dark")
            css = "<style>" + formatter.get_style_defs('.highlight').replace("#2f1e2e", "#2b2b2b").replace("#4f424c", "#2b2b2b") + "</style>"
        else:
            formatter = HtmlFormatter(linenos=False, style="tango")
            css = "<style>" + formatter.get_style_defs('.highlight').replace("#ffffcc", "#ffffff").replace("#f8f8f8", "#ffffff") + "</style>"
        html = highlight(current_plain_text, lexer=CssLexer(), formatter=formatter)

        self.document().setHtml(css+html)
        self.moveCursor(QTextCursor.End)
        self.add_undo_command()

    def move_back_cursor_after_highlight(self, pos1, pos2):
        # pos2-1: leave a space
        if pos1 < pos2-1:
            for _ in range(pos2-pos1):
                self.moveCursor(QTextCursor.Left, QTextCursor.MoveAnchor)
        elif pos1 > pos2:
            for _ in range(pos1-pos2):
                self.moveCursor(QTextCursor.Right, QTextCursor.MoveAnchor)

    def redo(self):
        if not self.redo_stack_list:
            return

        if self.document().toHtml() == self.redo_stack_list[-1][0]:
            self.redo_stack_list.pop()
            if not self.redo_stack_list:
                return

        redo_command = self.redo_stack_list.pop()
        self.document().setHtml(redo_command[0])
        original_cursor_position = redo_command[1]
        current_cursor_position = self.textCursor().position()
        self.move_back_cursor_after_highlight(original_cursor_position, current_cursor_position)

    def add_redo_command(self, command):
        if len(self.redo_stack_list) > self.redo_max_count:
            self.redo_stack_list.pop(0)

        self.redo_stack_list.append(command)

    def undo(self):
        if not self.undo_stack_list:
            return

        if self.document().toHtml() == self.undo_stack_list[-1][0]:
            self.redo_stack_list.append(self.undo_stack_list.pop())
            if not self.undo_stack_list:
                return

        undo_command = self.undo_stack_list.pop()
        self.add_redo_command(undo_command)
        self.document().setHtml(undo_command[0])
        original_cursor_position = undo_command[1]
        current_cursor_position = self.textCursor().position()
        self.move_back_cursor_after_highlight(original_cursor_position, current_cursor_position)

    def add_undo_command(self):
        if len(self.undo_stack_list) > self.undo_max_count:
            self.undo_stack_list.pop(0)

        if self.undo_stack_list:
            if self.document().toHtml() != self.undo_stack_list[-1][0]:
                self.undo_stack_list.append((self.document().toHtml(), self.textCursor().position()))
        else:
            self.undo_stack_list.append((self.document().toHtml(), self.textCursor().position()))

    def is_text_cursor_in_brace_block(self):
        """Check if the text cursor is between { and }"""
        left_brace_pos = None
        right_brace_pos = None

        text_cursor = self.textCursor()
        for i in range(text_cursor.position()):
            text_cursor.movePosition(QTextCursor.Left, QTextCursor.KeepAnchor)
            if "{" in text_cursor.selectedText():
                left_brace_pos = i
            elif "}" in text_cursor.selectedText():
                right_brace_pos = i

            if left_brace_pos is not None and right_brace_pos is not None:
                break

        if left_brace_pos is None and right_brace_pos is None:
            return False
        elif left_brace_pos is not None and right_brace_pos is None:
            return True
        elif left_brace_pos is None and right_brace_pos is not None:
            return False

        if left_brace_pos < right_brace_pos:
            return True
        else:
            return False

    def contextMenuEvent(self, event):
        return

    def resizeEvent(self, event):
        cr = self.contentsRect()
        self.line_number_area.setGeometry(QRect(cr.left(), cr.top(), self.get_line_number_area_width(), cr.height()))

    def keyPressEvent(self, event):
        if self.completer.popup().isVisible():
            if event.key() == Qt.Key_Escape or event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return or event.key() == Qt.Key_Tab:
                event.ignore()
                return

        super(CustomTextEdit, self).keyPressEvent(event)
        if event.modifiers() == Qt.ControlModifier:
            if event.key() == Qt.Key_Z:
                self.undo()
            elif event.key() == Qt.Key_V:
                self.highlight_text()
        elif event.modifiers() == Qt.ControlModifier | Qt.ShiftModifier:
            if event.key() == Qt.Key_Z:
                self.redo()
        else:
            if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return and self.is_text_cursor_in_brace_block():
                self.textCursor().insertText("\t")
            self.add_undo_command()

        word_under_cursor = self.get_word_under_cursor()
        if not word_under_cursor or event.key() == Qt.Key_Left or event.key() == Qt.Key_Right or event.key() == Qt.Key_Up or event.key() == Qt.Key_Down:
            self.completer.popup().setVisible(False)
            return

        if word_under_cursor == "{" and event.key() != Qt.Key_Backspace:
            self.highlight_text()
            return

        if word_under_cursor == "}" and event.key() != Qt.Key_Backspace:
            text_cursor = self.textCursor()
            for _ in range(text_cursor.positionInBlock()):
                text_cursor.movePosition(QTextCursor.Left, QTextCursor.KeepAnchor)
            if text_cursor.selectedText().strip() == "}":
                text_cursor.removeSelectedText()
                text_cursor.insertText("}")
            self.highlight_text()
            return

        self.complete_completer(word_under_cursor)

    def complete_completer(self, word_under_cursor):
        completer_prefix = word_under_cursor
        self.completer.setCompletionPrefix(completer_prefix)

        height = 100
        width = int(self.rect().width() / 2)

        if not self.textCursor().block().text():
            x = 0
        else:
            x = int(self.blockBoundingRect(self.textCursor().block()).width() / len(self.textCursor().block().text()) * self.textCursor().positionInBlock())
            if x >= self.rect().width() - width:
                x = self.rect().width() - width

        y = self.blockBoundingGeometry(self.textCursor().block()).y() - 80

        self.completer.complete(QRect(x, y, width, height))

        # Select the first row by default.
        e = QKeyEvent(QEvent.KeyPress, Qt.Key_Down, Qt.NoModifier)
        QCoreApplication.postEvent(self.completer.popup(), e)

    def lineNumberAreaPaintEvent(self, event):
        painter = QPainter(self.line_number_area)
        if self.theme == "black":
            painter.fillRect(event.rect(), QColor(59, 63, 66, 150))
        else:
            painter.fillRect(event.rect(), QColor(242, 242, 242, 150))

        block = self.firstVisibleBlock()
        block_number = block.blockNumber()
        top = self.blockBoundingGeometry(block).translated(self.contentOffset()).top()
        bottom = top + self.blockBoundingRect(block).height()

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = block_number + 1
                if number == self.get_current_line_number():
                    painter.setPen(QColor(178, 189, 175, 250))
                else:
                    painter.setPen(QColor(178, 189, 175, 160))

                text_rect = QRectF(0, top-4, self.line_number_area.width(), self.fontMetrics().height())
                painter.drawText(text_rect, Qt.AlignCenter, str(number))

            block = block.next()
            top = bottom
            bottom = top + self.blockBoundingRect(block).height()
            block_number += 1

    def reload_style_sheet(self):
        self.set_style_sheet()
        self.highlight_text()


class DisplayWidget(QWidget):
    def __init__(self):
        super(DisplayWidget, self).__init__()
        self.widget_list = ["QCheckBox", "QComboBox", "QDial", "QLabel", "QLCDNumber", "QLineEdit", "QListWidget",
                            "QProgressBar", "QPushButton", "QRadioButton", "QSlider", "QSpinBox", "QTableWidget",
                            "QWidget"]
        self.widget_combo_box = QComboBox()
        self.current_widget = None
        self.qss = None

        self.set_up()

    def set_up(self):
        self.set_window_attr()
        self.set_object_name()
        self.set_style_sheet()
        self.set_widget()
        self.set_signal()
        self.set_layout()
        self.change_widget("QCheckBox")

    def set_window_attr(self):
        self.resize(400, 400)
        self.setMinimumWidth(200)
        self.setMinimumHeight(200)

    def set_object_name(self):
        self.setObjectName("displayWidget")
        self.widget_combo_box.setObjectName("widgetComboBox")

    def set_style_sheet(self):
        with open(RES_PATH / "config.json", "r", encoding="utf-8") as f:
            theme = json.loads(f.read())["theme"]

        with open(RES_PATH / f"qss/{theme}/editor.qss", encoding="utf-8") as f:
            self.setStyleSheet(f.read())

        icon_path = str(RES_PATH / "images/up_down.png").replace("\\", "/")
        self.setStyleSheet("""
        QComboBox#widgetComboBox::down-arrow {
            width: 13px;
            height: 13px;
            image: url(%s);
        }
        """ % icon_path)

    def set_widget(self):
        self.widget_combo_box.addItems(self.widget_list)

    def set_signal(self):
        self.widget_combo_box.currentTextChanged.connect(self.change_widget)

    def set_layout(self):
        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout(self)
        h_layout.addStretch()
        h_layout.addWidget(self.widget_combo_box)
        v_layout.addLayout(h_layout)
        v_layout.addStretch()

    def change_widget(self, text):
        if self.current_widget:
            self.current_widget.deleteLater()

        if text == "QCheckBox":
            self.current_widget = QCheckBox(self)
            self.current_widget.setText("Qt Box")
            self.current_widget.setTristate(True)

        elif text == "QComboBox":
            self.current_widget = QComboBox(self)
            self.current_widget.addItems(["1", "2", "3", "4", "5", "6"])

        elif text == "QDial":
            self.current_widget = QDial(self)
            self.current_widget.setMinimum(0)
            self.current_widget.setMaximum(100)
            self.current_widget.setFixedSize(100, 100)

        elif text == "QLabel":
            self.current_widget = QLabel(self)
            self.current_widget.setText("Qt Box")

        elif text == "QLCDNumber":
            self.current_widget = QLCDNumber(self)
            self.current_widget.setDigitCount(6)
            self.current_widget.display(123456)

        elif text == "QLineEdit":
            self.current_widget = QLineEdit(self)
            self.current_widget.setPlaceholderText("Qt Box")

        elif text == "QListWidget":
            self.current_widget = QListWidget(self)
            self.current_widget.setFixedSize(150, 200)
            for i in range(5):
                item = QListWidgetItem()
                item.setText(str(i+1))
                self.current_widget.addItem(item)

        elif text == "QProgressBar":
            self.current_widget = QProgressBar(self)
            self.current_widget.setMinimum(0)
            self.current_widget.setMaximum(100)
            self.current_widget.setValue(20)

        elif text == "QPushButton":
            self.current_widget = QPushButton(self)
            self.current_widget.setText("BUTTON")

        elif text == "QRadioButton":
            self.current_widget = QRadioButton(self)
            self.current_widget.setText("Qt Box")

        elif text == "QSlider":
            self.current_widget = QSlider(self)
            self.current_widget.setOrientation(Qt.Horizontal)
            self.current_widget.setMinimum(0)
            self.current_widget.setMaximum(100)

        elif text == "QSpinBox":
            self.current_widget = QSpinBox(self)

        elif text == "QTableWidget":
            self.current_widget = QTableWidget(self)
            self.current_widget.setFixedSize(200, 150)
            self.current_widget.setColumnCount(3)
            self.current_widget.setRowCount(5)

        elif text == "QWidget":
            self.current_widget = QWidget(self)
            self.current_widget.setFixedSize(150, 150)
            self.current_widget.setAutoFillBackground(True)

        if self.current_widget:
            self.current_widget.show()
            self.set_current_widget_style_sheet(self.qss)
            self.current_widget.move(int(self.width() / 2 - self.current_widget.width() / 2),
                                     int(self.height() / 2 - self.current_widget.height() / 2))

    def set_current_widget_style_sheet(self, qss):
        with suppress_stdout_stderr():
            self.current_widget.setStyleSheet(qss)
            self.qss = qss

    def resizeEvent(self, event):
        super(DisplayWidget, self).resizeEvent(event)
        if self.current_widget:
            self.current_widget.move(int(self.width()/2-self.current_widget.width()/2), int(self.height()/2-self.current_widget.height()/2))

    def reload_style_sheet(self):
        self.set_style_sheet()


class QSSEditorBody(QSplitter):
    def __init__(self):
        super(QSSEditorBody, self).__init__()
        self.edit = CustomTextEdit()
        self.display_widget = DisplayWidget()

        self.set_up()

    def set_up(self):
        self.set_window_attr()
        self.set_object_name()
        self.set_style_sheet()
        self.set_widget()
        self.set_signal()

    def set_window_attr(self):
        self.resize(800, 600)

    def set_object_name(self):
        self.setObjectName("qssEditorBody")

    def set_style_sheet(self):
        with open(RES_PATH / "config.json", "r", encoding="utf-8") as f:
            theme = json.loads(f.read())["theme"]

        with open(RES_PATH / f"qss/{theme}/editor.qss", encoding="utf-8") as f:
            self.setStyleSheet(f.read())

    def set_widget(self):
        self.addWidget(self.edit)
        self.addWidget(self.display_widget)
        self.setSizes([400, 400])

    def set_signal(self):
        self.edit.qss_signal.connect(self.display_widget.set_current_widget_style_sheet)

    def contextMenuEvent(self, event):
        pass

    def reload_style_sheet(self):
        self.set_style_sheet()
        self.edit.reload_style_sheet()
        self.display_widget.reload_style_sheet()


class QSSEditor(QWidget):
    def __init__(self):
        super(QSSEditor, self).__init__()
        self.qss_editor_title = QSSEditorTitle()
        self.qss_editor_body = QSSEditorBody()

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
        self.resize(850, 650)
        self.qss_editor_title.setMaximumHeight(40)
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
        self.qss_editor_title.close_signal.connect(self.close)
        self.qss_editor_title.minimize_signal.connect(self.showMinimized)
        self.qss_editor_title.maximize_signal.connect(self.showMaximized)
        self.qss_editor_title.show_normal_signal.connect(self.showNormal)

    def set_layout(self):
        v_layout = QVBoxLayout(self)
        v_layout.setSpacing(0)
        v_layout.addWidget(self.qss_editor_title)
        v_layout.addWidget(self.qss_editor_body)
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
        super(QSSEditor, self).paintEvent(event)
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
        super(QSSEditor, self).showNormal()
        self.resize(850, 650)
        desktop = QApplication.desktop()
        self.move(desktop.width() // 2 - self.width() // 2, desktop.height() // 2 - self.height() // 2)

    def reload_style_sheet(self):
        self.set_style_sheet()
        self.qss_editor_title.reload_style_sheet()
        self.qss_editor_body.reload_style_sheet()


def main():
    check_update()
    app = QApplication([])
    qss_editor = QSSEditor()
    qss_editor.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()