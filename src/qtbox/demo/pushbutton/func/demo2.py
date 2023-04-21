# PyQt
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QPushButton, QMessageBox
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QPushButton = createWidgetMenuBase(QPushButton)

class QtBoxFuncButton2(QPushButton):
    def __init__(self):
        super(QtBoxFuncButton2, self).__init__(str(Path(__file__)))
        self.setText("Login")
        self.clicked.connect(self.start_verify_thread)

        self.verify_thread = VerifyThread()
        self.verify_thread.verify_signal.connect(self.do_after_verification)

    def start_verify_thread(self):
        self.verify_thread.start()

    def do_after_verification(self, verify_result):
        if not verify_result:
            self.verify_not_ok()
        else:
            self.verify_ok()

    def verify_not_ok(self):
        QMessageBox.critical(self, "Verify", "Wrong username or password")

    def verify_ok(self):
        QMessageBox.information(self, "Verify", "Login successfully")


class VerifyThread(QThread):
    verify_signal = pyqtSignal(bool)

    def __init__(self):
        super(VerifyThread, self).__init__()

    def run(self):
        self.verify_signal.emit(self.verify())

    def verify(self):
        """
        verify username and password here
        :return: True or False
        """
        ...
        return False
# PyQt


# PySide
# from PySide2.QtCore import QThread, Signal
# from PySide2.QtWidgets import QPushButton, QMessageBox


# class QtBoxFuncButton2(QPushButton):
#     def __init__(self):
#         super(QtBoxFuncButton2, self).__init__()
#         self.setText("Login")
#         self.clicked.connect(self.start_verify_thread)

#         self.verify_thread = VerifyThread()
#         self.verify_thread.verify_signal.connect(self.do_after_verification)

#     def start_verify_thread(self):
#         self.verify_thread.start()

#     def do_after_verification(self, verify_result):
#         if not verify_result:
#             self.verify_not_ok()
#         else:
#             self.verify_ok()

#     def verify_not_ok(self):
#         QMessageBox.critical(self, "Verify", "Wrong username or password")

#     def verify_ok(self):
#         QMessageBox.information(self, "Verify", "Login successfully")


# class VerifyThread(QThread):
#     verify_signal = Signal(bool)

#     def __init__(self):
#         super(VerifyThread, self).__init__()

#     def run(self):
#         self.verify_signal.emit(self.verify())

#     def verify(self):
#         """
#         verify username and password here
#         :return: True or False
#         """
#         ...
#         return False
# PySide

# C++/Qt
# #ifndef QTBOXFUNCPUSHBUTTON2_H
# #define QTBOXFUNCPUSHBUTTON2_H
# #include "verifythread.h"
# #include <QPushButton>

# class QtBoxFuncPushButton2 : public QPushButton
# {
#     Q_OBJECT

# public:
#     QtBoxFuncPushButton2(QWidget *parent = nullptr);

# private:
#     VerifyThread *verifyThread = new VerifyThread();

# private slots:
#     void startVerifyThread();
#     void doAfterVerification(bool verifyResult);
#     void verifyNotOk();
#     void verifyOk();
# };
# #endif // QTBOXFUNCPUSHBUTTON2_H

# #ifndef VERIFYTHREAD_H
# #define VERIFYTHREAD_H
# #include <QThread>

# class VerifyThread : public QThread
# {
#     Q_OBJECT

# public:
#     VerifyThread();

# protected:
#     void run();

# private:
#     bool verify();

# signals:
#     void verifySignal(bool verifyResult);
# };
# #endif // VERIFYTHREAD_H



# #include "qtboxfuncpushbutton2.h"
# #include <QMessageBox>

# QtBoxFuncPushButton2::QtBoxFuncPushButton2(QWidget *parent)
#     : QPushButton(parent)
# {
#     setText("Login");
#     connect(this, SIGNAL(clicked()), this, SLOT(startVerifyThread()));
#     connect(verifyThread, SIGNAL(verifySignal(bool)), this, SLOT(doAfterVerification(bool)));
# }

# void QtBoxFuncPushButton2::startVerifyThread()
# {
#     verifyThread->start();
# }

# void QtBoxFuncPushButton2::doAfterVerification(bool verifyResult)
# {
#     if (!verifyResult) {
#         verifyNotOk();
#     }
#     else {
#         verifyOk();
#     }
# }

# void QtBoxFuncPushButton2::verifyNotOk()
# {
#     QMessageBox::critical(this, "Verify", "Wrong username or password");
# }

# void QtBoxFuncPushButton2::verifyOk()
# {
#     QMessageBox::information(this, "Verify", "Login successfully");
#
# }

# #include "verifythread.h"

# VerifyThread::VerifyThread()
# {

# }

# void VerifyThread::run()
# {
#     emit verifySignal(verify());
# }

# bool VerifyThread::verify()
# {
#     // verify username and password here
#     return false;
# }
# C++/Qt