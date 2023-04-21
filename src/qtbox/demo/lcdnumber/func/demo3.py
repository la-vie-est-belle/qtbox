# PyQt
from time import strftime, gmtime
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import QLCDNumber
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QLCDNumber = createWidgetMenuBase(QLCDNumber)

class QtBoxFuncLCDNumber3(QLCDNumber):
    def __init__(self):
        super(QtBoxFuncLCDNumber3, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 50)
        self.setDigitCount(8)

        self.count_down = 3600
        self.update_display()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_display)
        self.timer.start(1000)

    def update_display(self):
        self.count_down -= 1
        self.display(strftime("%H:%M:%S", gmtime(self.count_down)))
        if self.count_down <= 0:
            self.count_down = 3600
# PyQt

# PySide
# from time import strftime, gmtime
# from PySide2.QtCore import QTimer
# from PySide2.QtWidgets import QLCDNumber


# class QtBoxFuncLCDNumber3(QLCDNumber):
#     def __init__(self):
#         super(QtBoxFuncLCDNumber3, self).__init__()
#         self.setFixedSize(150, 50)
#         self.setDigitCount(8)

#         self.count_down = 3600
#         self.update_display()
#         self.timer = QTimer()
#         self.timer.timeout.connect(self.update_display)
#         self.timer.start(1000)

#     def update_display(self):
#         self.count_down -= 1
#         self.display(strftime("%H:%M:%S", gmtime(self.count_down)))
#         if self.count_down <= 0:
#             self.count_down = 3600
# PySide

# C++/Qt
# #ifndef QTBOXFUNCLCDNUMBER3_H
# #define QTBOXFUNCLCDNUMBER3_H
# #include <QLCDNumber>
# #include <QTimer>
# #include <QTime>

# class QtBoxFuncLCDNumber3 : public QLCDNumber
# {
#     Q_OBJECT
#
# public:
#     QtBoxFuncLCDNumber3(QWidget *parent = nullptr);

# private:
#     int count = 0;
#     QTimer *timer = new QTimer();
#     QTime *time = new QTime(1, 0, 0, 0);

# private slots:
#     void updateDisplay();
# };
# #endif // QTBOXFUNCLCDNUMBER3_H



# #include "qtboxfunclcdnumber3.h"

# QtBoxFuncLCDNumber3::QtBoxFuncLCDNumber3(QWidget *parent)
#     : QLCDNumber(parent)
# {
#     setFixedSize(150, 50);
#     setDigitCount(8);
#     updateDisplay();

#     connect(timer, SIGNAL(timeout()), this, SLOT(updateDisplay()));
#     timer->start(1000);
# }

# void QtBoxFuncLCDNumber3::updateDisplay()
# {
#     count++;
#     int timeLeft = time->addSecs(-count).second();
#     display(time->addSecs(-count).toString("hh:mm:ss"));

#     if (timeLeft <= 0) {
#         time->setHMS(1, 0, 0, 0);
#         count = 0;
#     }
# }
# C++/Qt