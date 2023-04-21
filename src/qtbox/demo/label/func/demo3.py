# PyQt
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QLabel
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QLabel = createWidgetMenuBase(QLabel)

class QtBoxFuncLabel3(QLabel):
    def __init__(self):
        super(QtBoxFuncLabel3, self).__init__(str(Path(__file__)))
        self.text = ""
        self.count = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_text)
        self.type_text("Typewriter effect")

    def type_text(self, txt):
        self.text = txt
        self.count = 0
        self.timer.stop()
        self.timer.start(500)

    def update_text(self):
        self.count += 1
        self.setText(self.text[0:self.count])

        if self.count >= len(self.text):
            self.count = 0
            self.timer.stop()
# PyQt

# PySide
# from PySide2.QtCore import QTimer
# from PySide2.QtWidgets import QLabel


# class QtBoxFuncLabel3(QLabel):
#     def __init__(self):
#         super(QtBoxFuncLabel3, self).__init__()
#         self.text = ""
#         self.count = 0
#         self.timer = QTimer()
#         self.timer.timeout.connect(self.update_text)
#         self.type_text("Typewriter effect")

#     def type_text(self, txt):
#         self.text = txt
#         self.count = 0
#         self.timer.stop()
#         self.timer.start(500)

#     def update_text(self):
#         self.count += 1
#         self.setText(self.text[0:self.count])
#
#         if self.count >= len(self.text):
#             self.count = 0
#             self.timer.stop()
# PySide

# C++/Qt
# #ifndef QTBOXFUNCLABEL3_H
# #define QTBOXFUNCLABEL3_H
# #include <QLabel>
# #include <QTimer>
# #include <QString>

# class QtBoxFuncLabel3 : public QLabel
# {
#     Q_OBJECT

# public:
#     QtBoxFuncLabel3(QWidget *parent = nullptr);

# private:
#     QString text = "";
#     int count = 0;
#     QTimer *timer = new QTimer();
#     void typeText(const QString &txt);

# private slots:
#     void updateText();
# };
# #endif // QTBOXFUNCLABEL3_H



# #include "qtboxfunclabel3.h"

# QtBoxFuncLabel3::QtBoxFuncLabel3(QWidget *parent)
#     : QLabel(parent)
# {
#     connect(timer, SIGNAL(timeout()), this, SLOT(updateText()));
#     typeText("Typewriter effect");
# }

# void QtBoxFuncLabel3::typeText(const QString &txt)
# {
#     text = txt;
#     count = 0;
#     timer->stop();
#     timer->start(500);
# }

# void QtBoxFuncLabel3::updateText()
# {
#     count += 1;
#     setText(text.left(count));

#     if (count >= text.length()) {
#         count = 0;
#         timer->stop();
#     }
# }
# C++/Qt