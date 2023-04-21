# PyQt
from PyQt5.QtWidgets import QLCDNumber
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QLCDNumber = createWidgetMenuBase(QLCDNumber)

class QtBoxStyleLCDNumber4(QLCDNumber):
    def __init__(self):
        super(QtBoxStyleLCDNumber4, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 50)
        self.setDigitCount(6)
        self.display(123456)
        self.setSegmentStyle(QLCDNumber.Flat)
        self.setStyleSheet("""
        QLCDNumber {
            background-color: transparent;
            border: none;
            color: black;
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
#             background-color: transparent;
#             border: none;
#             color: black;
#         }
#         """)
# PySide

# C++/Qt
# #ifndef QTBOXSTYLELCDNUMBER4_H
# #define QTBOXSTYLELCDNUMBER4_H
# #include <QLCDNumber>

# class QtBoxStyleLCDNumber4 : public QLCDNumber
# {
#     Q_OBJECT

# public:
#     QtBoxStyleLCDNumber4(QWidget *parent = nullptr);
# };
# #endif // QTBOXSTYLELCDNUMBER4_H



# #include "qtboxstylelcdnumber4.h"

# QtBoxStyleLCDNumber4::QtBoxStyleLCDNumber4(QWidget *parent)
#     : QLCDNumber(parent)
# {
#     setFixedSize(150, 50);
#     setDigitCount(6);
#     display(123456);
#     setSegmentStyle(QLCDNumber::Flat);
#     setStyleSheet(R"(
#     QLCDNumber {
#         background-color: transparent;
#         border: none;
#         color: black;
#     }
#     )");
# }
# C++/Qt