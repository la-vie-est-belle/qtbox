# PyQt
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import QLabel
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QLabel = createWidgetMenuBase(QLabel)

class QtBoxFuncLabel6(QLabel):
    def __init__(self):
        super(QtBoxFuncLabel6, self).__init__(str(Path(__file__)))
        self.update_text()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_text)
        self.timer.start(1000)

    def update_text(self):
        self.setText(QTime.currentTime().toString())
# PyQt

# PySide
# from PySide2.QtCore import QTimer, QTime
# from PySide2.QtWidgets import QLabel


# class QtBoxFuncLabel6(QLabel):
#     def __init__(self):
#         super(QtBoxFuncLabel6, self).__init__(str(Path(__file__)))
#         self.update_text()

#         self.timer = QTimer()
#         self.timer.timeout.connect(self.update_text)
#         self.timer.start(1000)

#     def update_text(self):
#         self.setText(QTime.currentTime().toString())
# PySide

# C++/Qt
# #ifndef QTBOXFUNCLABEL6_H
# #define QTBOXFUNCLABEL6_H
# #include <QLabel>
# #include <QTimer>

# class QtBoxFuncLabel6 : public QLabel
# {
#     Q_OBJECT

# public:
#     QtBoxFuncLabel6(QWidget *parent = nullptr);

# private:
#     QTimer *timer = new QTimer();
#
# private slots:
#     void updateText();
# };
# #endif // QTBOXFUNCLABEL6_H



# #include "qtboxfunclabel6.h"
# #include <QTime>

# QtBoxFuncLabel6::QtBoxFuncLabel6(QWidget *parent)
#     : QLabel(parent)
# {
#     updateText();
#     connect(timer, SIGNAL(timeout()), this, SLOT(updateText()));
#     timer->start(1000);
# }

# void QtBoxFuncLabel6::updateText()
# {
#     setText(QTime::currentTime().toString());
# }
# C++/Qt