# PyQt
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QLCDNumber
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QLCDNumber = createWidgetMenuBase(QLCDNumber)

class QtBoxFuncLCDNumber2(QLCDNumber):
    def __init__(self):
        super(QtBoxFuncLCDNumber2, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 50)
        self.text = "HELLO"
        self.setDigitCount(len(self.text))
        self.display("")

        self.count = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_display)
        self.timer.start(1000)

    def update_display(self):
        self.count += 1
        if self.count > len(self.text):
            self.display(self.text+(self.count-len(self.text))*" ")
        else:
            self.display(self.text[0:self.count])

        if self.count == 2*len(self.text):
            self.count = 0
# PyQt

# PySide
# from PySide2.QtCore import QTimer
# from PySide2.QtWidgets import QLCDNumber


# class QtBoxFuncLCDNumber2(QLCDNumber):
#     def __init__(self):
#         super(QtBoxFuncLCDNumber2, self).__init__()
#         self.setFixedSize(150, 50)
#         self.text = "HELLO"
#         self.setDigitCount(len(self.text))
#         self.display("")

#         self.count = 0
#         self.timer = QTimer()
#         self.timer.timeout.connect(self.update_display)
#         self.timer.start(1000)

#     def update_display(self):
#         self.count += 1
#         if self.count > len(self.text):
#             self.display(self.text+(self.count-len(self.text))*" ")
#         else:
#             self.display(self.text[0:self.count])

#         if self.count == 2*len(self.text):
#             self.count = 0
# PySide

# C++/Qt
# #ifndef QTBOXFUNCLCDNUMBER2_H
# #define QTBOXFUNCLCDNUMBER2_H
# #include <QLCDNumber>
# #include <QString>
# #include <QTimer>

# class QtBoxFuncLCDNumber2 : public QLCDNumber
# {
#     Q_OBJECT

# public:
#     QtBoxFuncLCDNumber2(QWidget *parent = nullptr);

# private:
#     int count = 0;
#     QString text = "HELLO";
#     QTimer *timer = new QTimer();

# private slots:
#     void updateDisplay();
# };
# #endif // QTBOXFUNCLCDNUMBER2_H



# #include "qtboxfunclcdnumber2.h"

# QtBoxFuncLCDNumber2::QtBoxFuncLCDNumber2(QWidget *parent)
#     : QLCDNumber(parent)
# {
#     setFixedSize(150, 50);
#     setDigitCount(text.size());
#     display("");

#     connect(timer, SIGNAL(timeout()), this, SLOT(updateDisplay()));
#     timer->start(1000);
# }

# void QtBoxFuncLCDNumber2::updateDisplay()
# {
#     count++;
#     if (count > text.size()) {
#         QString emptyString = "";
#         for (int i=0; i<count-text.size(); i++) {
#             emptyString += " ";
#         };
#         display(text+emptyString);
#     }
#     else {
#         display(text.left(count));
#     }

#     if (count == 2*text.size()) {
#         count = 0;
#     }
# }
# C++/Qt