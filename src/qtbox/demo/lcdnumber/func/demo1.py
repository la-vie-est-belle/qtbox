# PyQt
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import QLCDNumber
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QLCDNumber = createWidgetMenuBase(QLCDNumber)

class QtBoxFuncLCDNumber1(QLCDNumber):
    def __init__(self):
        super(QtBoxFuncLCDNumber1, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 50)
        self.setDigitCount(8)
        self.update_display()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_display)
        self.timer.start(1000)

    def update_display(self):
        self.display(QTime.currentTime().toString())
# PyQt

# PySide
# from PySide2.QtCore import QTimer, QTime
# from PySide2.QtWidgets import QLCDNumber


# class QtBoxFuncLCDNumber1(QLCDNumber):
#     def __init__(self):
#         super(QtBoxFuncLCDNumber1, self).__init__()
#         self.setFixedSize(150, 50)
#         self.setDigitCount(8)
#         self.update_display()

#         self.timer = QTimer()
#         self.timer.timeout.connect(self.update_display)
#         self.timer.start(1000)

#     def update_display(self):
#         self.display(QTime.currentTime().toString())
# PySide

# C++/Qt
# #ifndef QTBOXFUNCLCDNUMBER1_H
# #define QTBOXFUNCLCDNUMBER1_H
# #include <QLCDNumber>
# #include <QTimer>

# class QtBoxFuncLCDNumber1 : public QLCDNumber
# {
#     Q_OBJECT

# public:
#     QtBoxFuncLCDNumber1(QWidget *parent = nullptr);

# private:
#     QTimer *timer = new QTimer();

# private slots:
#     void updateDisplay();
# };
# #endif // QTBOXFUNCLCDNUMBER1_H



# #include "qtboxfunclcdnumber1.h"
# #include <QTime>

# QtBoxFuncLCDNumber1::QtBoxFuncLCDNumber1(QWidget *parent)
#     : QLCDNumber(parent)
# {
#     setFixedSize(150, 50);
#     setDigitCount(8);
#     updateDisplay();

#     connect(timer, SIGNAL(timeout()), this, SLOT(updateDisplay()));
#     timer->start(1000);
# }

# void QtBoxFuncLCDNumber1::updateDisplay()
# {
#     display(QTime::currentTime().toString());
# }
# C++/Qt