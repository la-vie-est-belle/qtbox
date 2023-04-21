# PyQt
from PyQt5.QtWidgets import QLCDNumber
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QLCDNumber = createWidgetMenuBase(QLCDNumber)

class QtBoxStyleLCDNumber2(QLCDNumber):
    def __init__(self):
        super(QtBoxStyleLCDNumber2, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 50)
        self.setDigitCount(6)
        self.display(123456)
        self.setSegmentStyle(QLCDNumber.Flat)
        self.setStyleSheet("""
        QLCDNumber {
            background-color: #0130f2;
            border: none;
            color: white;
        }
        """)
# PyQt

# PySide
# from PySide2.QtWidgets import QLCDNumber


# class QtBoxStyleLCDNumber2(QLCDNumber):
#     def __init__(self):
#         super(QtBoxStyleLCDNumber2, self).__init__()
#         self.setFixedSize(150, 50)
#         self.setDigitCount(6)
#         self.display(123456)
#         self.setSegmentStyle(QLCDNumber.Flat)
#         self.setStyleSheet("""
#         QLCDNumber {
#             background-color: #0130f2;
#             border: none;
#             color: white;
#         }
#         """)
# PySide

# C++/Qt
# #ifndef QTBOXSTYLELCDNUMBER2_H
# #define QTBOXSTYLELCDNUMBER2_H
# #include <QLCDNumber>

# class QtBoxStyleLCDNumber2 : public QLCDNumber
# {
#     Q_OBJECT

# public:
#     QtBoxStyleLCDNumber2(QWidget *parent = nullptr);
# };
# #endif // QTBOXSTYLELCDNUMBER2_H



# #include "qtboxstylelcdnumber2.h"

# QtBoxStyleLCDNumber2::QtBoxStyleLCDNumber2(QWidget *parent)
#     : QLCDNumber(parent)
# {
#     setFixedSize(150, 50);
#     setDigitCount(6);
#     display(123456);
#     setSegmentStyle(QLCDNumber::Flat);
#     setStyleSheet(R"(
#     QLCDNumber {
#         background-color: #0130f2;
#         border: none;
#         color: white;
#     }
#     )");
# }
# C++/Qt

