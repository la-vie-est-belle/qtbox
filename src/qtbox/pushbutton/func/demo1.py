# PyQt
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QPushButton
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QPushButton = createWidgetMenuBase(QPushButton)

class QtBoxFuncButton1(QPushButton):
    def __init__(self):
        super(QtBoxFuncButton1, self).__init__(str(Path(__file__)))
        self.setText("Send SMS")
        self.clicked.connect(self.start_SMS_thread)

        self.SMS_thread = SMSThread()
        self.SMS_thread.count_signal.connect(self.count_down)
        self.SMS_thread.finished_signal.connect(self.restore)

    def start_SMS_thread(self):
        self.SMS_thread.start()

    def count_down(self, count):
        self.setEnabled(False)
        self.setText(f"Resend ({count})")

    def restore(self):
        self.setEnabled(True)
        self.setText("Send SMS")


class SMSThread(QThread):
    count_signal = pyqtSignal(int)
    finished_signal = pyqtSignal()

    def __init__(self):
        super(SMSThread, self).__init__()

    def run(self):
        self.send_SMS()

        count = 60
        while count >= 1:
            self.count_signal.emit(count)
            count -= 1
            self.sleep(1)

        self.finished_signal.emit()

    def send_SMS(self):
        """send verification code to the user here"""
        ...
# PyQt

# PySide
# from PySide2.QtCore import QThread, Signal
# from PySide2.QtWidgets import QPushButton


# class QtBoxFuncButton1(QPushButton):
#     def __init__(self):
#         super(QtBoxFuncButton1, self).__init__()
#         self.setText("Send SMS")
#         self.clicked.connect(self.start_SMS_thread)

#         self.SMS_thread = SMSThread()
#         self.SMS_thread.count_signal.connect(self.count_down)
#         self.SMS_thread.finished_signal.connect(self.restore)

#     def start_SMS_thread(self):
#         self.SMS_thread.start()

#     def count_down(self, count):
#         self.setEnabled(False)
#         self.setText(f"Resend ({count})")

#     def restore(self):
#         self.setEnabled(True)
#         self.setText("Send SMS")


# class SMSThread(QThread):
#     count_signal = Signal(int)
#     finished_signal = Signal()

#     def __init__(self):
#         super(SMSThread, self).__init__()

#     def run(self):
#         self.send_SMS()

#         count = 60
#         while count >= 1:
#             self.count_signal.emit(count)
#             count -= 1
#             self.sleep(1)

#         self.finished_signal.emit()

#     def send_SMS(self):
#         """send verification code to the user here"""
#         ...
# PySide

