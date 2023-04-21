# PyQt
from PyQt5.QtWidgets import QLCDNumber
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QLCDNumber = createWidgetMenuBase(QLCDNumber)

class QtBoxStyleLCDNumber5(QLCDNumber):
    def __init__(self):
        super(QtBoxStyleLCDNumber5, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 50)
        self.setDigitCount(6)
        self.display(123456)
        self.setSegmentStyle(QLCDNumber.Flat)
        self.setStyleSheet("""
        QLCDNumber {
            background-color: black;
            border: none;
            color: red;
        }
        """)
# PyQt

# PySide
# from PySide2.QtWidgets import QLCDNumber


# class QtBoxStyleLCDNumber3(QLCDNumber):
#     def __init__(self):
#         super(QtBoxStyleLCDNumber3, self).__init__()
#         self.setFixedSize(150, 50)
#         self.setDigitCount(6)
#         self.display(123456)
#         self.setSegmentStyle(QLCDNumber.Flat)
#         self.setStyleSheet("""
#         QLCDNumber {
#             background-color: black;
#             border: none;
#             color: red;
#         }
#         """)
# PySide

# C++/Qt
# #ifndef QTBOXSTYLELCDNUMBER5_H
# #define QTBOXSTYLELCDNUMBER5_H
# #include <QLCDNumber>

# class QtBoxStyleLCDNumber5 : public QLCDNumber
# {
#     Q_OBJECT

# public:
#     QtBoxStyleLCDNumber5(QWidget *parent = nullptr);
# };
# #endif // QTBOXSTYLELCDNUMBER5_H



# #include "qtboxstylelcdnumber5.h"

# QtBoxStyleLCDNumber5::QtBoxStyleLCDNumber5(QWidget *parent)
#     : QLCDNumber(parent)
# {
#     setFixedSize(150, 50);
#     setDigitCount(6);
#     display(123456);
#     setSegmentStyle(QLCDNumber::Flat);
#     setStyleSheet(R"(
#     QLCDNumber {
#         background-color: black;
#         border: none;
#         color: red;
#     }
#     )");
# }
# C++/Qt