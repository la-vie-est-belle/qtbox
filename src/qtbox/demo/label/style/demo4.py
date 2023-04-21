# PyQt
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QLabel
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QLabel = createWidgetMenuBase(QLabel)

class QtBoxStyleLabel4(QLabel):
    def __init__(self):
        super(QtBoxStyleLabel4, self).__init__(str(Path(__file__)))
        self.setText("Change text color")
        self.color_list = ["rgb(255, 0, 0)", "rgb(255, 165, 0)", "rgb(255, 255, 0)",
                           "rgb(0, 255, 0)", "rgb(0, 127, 255)", "rgb(0, 0, 255)",
                           "rgb(139, 0, 255)"]

        self.count = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.change_color)
        self.timer.start(100)

    def change_color(self):
        color = self.color_list[self.count]
        self.setStyleSheet(f"""
        color: {color}
        """)

        self.count += 1
        if self.count >= len(self.color_list):
            self.count = 0
# PyQt

# PySide
# from PySide2.QtCore import QTimer
# from PySide2.QtWidgets import QLabel


# class QtBoxStyleLabel4(QLabel):
#     def __init__(self):
#         super(QtBoxStyleLabel4, self).__init__()
#         self.setText("Change text color")
#         self.color_list = ["rgb(255, 0, 0)", "rgb(255, 165, 0)", "rgb(255, 255, 0)",
#                            "rgb(0, 255, 0)", "rgb(0, 127, 255)", "rgb(0, 0, 255)",
#                            "rgb(139, 0, 255)"]

#         self.count = 0
#         self.timer = QTimer()
#         self.timer.timeout.connect(self.change_color)
#         self.timer.start(100)

#     def change_color(self):
#         color = self.color_list[self.count]
#         self.setStyleSheet(f"""
#         color: {color}
#         """)

#         self.count += 1
#         if self.count >= len(self.color_list):
#             self.count = 0
# PySide

# C++/Qt
# #ifndef QTBOXSTYLELABEL4_H
# #define QTBOXSTYLELABEL4_H
# #include <QLabel>
# #include <QString>
# #include <QTimer>

# class QtBoxStyleLabel4 : public QLabel
# {
#     Q_OBJECT

# public:
#     QtBoxStyleLabel4(QWidget *parent = nullptr);

# private:
#     unsigned int count = 0;
#     QTimer *timer = new QTimer();
#     QString colorList[7] = {"rgb(255, 0, 0)", "rgb(255, 165, 0)", "rgb(255, 255, 0)",
#                             "rgb(0, 255, 0)", "rgb(0, 127, 255)", "rgb(0, 0, 255)",
#                             "rgb(139, 0, 255)"};

# private slots:
#     void changeColor();
# };
# #endif // QTBOXSTYLELABEL4_H



# #include "qtboxstylelabel4.h"

# QtBoxStyleLabel4::QtBoxStyleLabel4(QWidget *parent)
#     : QLabel(parent)
# {
#     setText("Change text color");
#     connect(timer, SIGNAL(timeout()), this, SLOT(changeColor()));
#     timer->start(100);
# }

# void QtBoxStyleLabel4::changeColor()
# {
#     QString color = colorList[count];
#     setStyleSheet(QString("color: %1").arg(color));

#     count++;
#     if (count >= (sizeof(colorList)/sizeof(colorList[0]))) {
#         count = 0;
#     }
# }
# C++/Qt