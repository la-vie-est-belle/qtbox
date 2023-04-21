# PyQt
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QPushButton
from qtbox.gui.menu import createWidgetMenuBase
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

# C++/Qt
# #ifndef QTBOXFUNCPUSHBUTTON1_H
# #define QTBOXFUNCPUSHBUTTON1_H
# #include "smsthread.h"
# #include <QPushButton>

# class QtBoxFuncPushButton1 : public QPushButton
# {
#     Q_OBJECT

# public:
#     QtBoxFuncPushButton1(QWidget *parent = nullptr);

# private:
#     SMSThread *smsThread = new SMSThread();

# private slots:
#     void startSMSThread();
#     void countDown(int count);
#     void restore();
# };
# #endif // QTBOXFUNCPUSHBUTTON1_H

# #ifndef SMSTHREAD_H
# #define SMSTHREAD_H
# #include <QThread>

# class SMSThread : public QThread
# {
#     Q_OBJECT

# public:
#     SMSThread();

# protected:
#     void run();

# private:
#     int count;
#     void sendSMS();

# signals:
#     void countSignal(int count);
#     void finishedSignal();
# };
# #endif // SMSTHREAD_H



# #include "qtboxfuncpushbutton1.h"
# #include <QString>

# QtBoxFuncPushButton1::QtBoxFuncPushButton1(QWidget *parent)
#     : QPushButton(parent)
# {
#     setText("Send SMS");
#     connect(this, SIGNAL(clicked()), this, SLOT(startSMSThread()));
#     connect(smsThread, SIGNAL(countSignal(int)), this, SLOT(countDown(int)));
#     connect(smsThread, SIGNAL(finishedSignal()), this, SLOT(restore()));
# }

# void QtBoxFuncPushButton1::startSMSThread()
# {
#     smsThread->start();
# }

# void QtBoxFuncPushButton1::countDown(int count)
# {
#     setEnabled(false);
#     setText(QString("Resend %1").arg(QString::number(count)));
# }

# void QtBoxFuncPushButton1::restore()
# {
#     setEnabled(true);
#     setText("Send SMS");
# }

# #include "smsthread.h"

# SMSThread::SMSThread()
# {

# }

# void SMSThread::run()
# {
#     sendSMS();
#     count = 60;
#     while (count >= 1){
#         emit countSignal(count);
#         count -= 1;
#         sleep(1);
#     }

#     emit finishedSignal();
# }

# void SMSThread::sendSMS()
# {
#     // send verification code to the user here
# }
# C++/Qt