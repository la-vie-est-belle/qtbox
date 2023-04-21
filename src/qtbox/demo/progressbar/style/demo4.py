# PyQt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QProgressBar, QGraphicsDropShadowEffect
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QProgressBar = createWidgetMenuBase(QProgressBar)

class QtBoxStyleProgressBar4(QProgressBar):
    def __init__(self):
        super(QtBoxStyleProgressBar4, self).__init__(str(Path(__file__)))
        self.setTextVisible(False)
        self.setMaximumHeight(10)
        self.setRange(0, 100)
        self.setValue(80)
        self.setStyleSheet("""
        QProgressBar {
            border: 1px solid lightgray;
            background-color: #2b241c;
            border-radius: 5px;
        }

        QProgressBar::chunk {
            background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #f9dc98, stop:1 #f4b543);
            border-radius: 4px;
        }
        """)

        self.add_shadow()

    def add_shadow(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(40)
        shadow.setOffset(0, 0)
        shadow.setColor(QColor(241, 177, 66))
        self.setGraphicsEffect(shadow)
# PyQt

# PySide
# from PySide2.QtGui import QColor
# from PySide2.QtWidgets import QProgressBar, QGraphicsDropShadowEffect


# class QtBoxStyleProgressBar4(QProgressBar):
#     def __init__(self):
#         super(QtBoxStyleProgressBar4, self).__init__()
#         self.setTextVisible(False)
#         self.setMaximumHeight(10)
#         self.setRange(0, 100)
#         self.setValue(80)
#         self.setStyleSheet("""
#         QProgressBar {
#             border: 1px solid lightgray;
#             background-color: #2b241c;
#             border-radius: 5px;
#         }

#         QProgressBar::chunk {
#             background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #f9dc98, stop:1 #f4b543);
#             border-radius: 4px;
#         }
#         """)

#         self.add_shadow()

#     def add_shadow(self):
#         shadow = QGraphicsDropShadowEffect(self)
#         shadow.setBlurRadius(40)
#         shadow.setOffset(0, 0)
#         shadow.setColor(QColor(241, 177, 66))
#         self.setGraphicsEffect(shadow)
# PySide

# C++/Qt
# #ifndef QTBOXSTYLEPROGRESSBAR4_H
# #define QTBOXSTYLEPROGRESSBAR4_H
# #include <QProgressBar>

# class QtBoxStyleProgressBar4 : public QProgressBar
# {
#     Q_OBJECT

# public:
#     QtBoxStyleProgressBar4(QWidget *parent = nullptr);

# private:
#     void addShadow();
# };
# #endif // QTBOXSTYLEPROGRESSBAR4_H



# #include "qtboxstyleprogressbar4.h"
# #include <QGraphicsDropShadowEffect>
# #include <QColor>

# QtBoxStyleProgressBar4::QtBoxStyleProgressBar4(QWidget *parent)
#     : QProgressBar(parent)
# {
#     setTextVisible(false);
#     setMaximumHeight(10);
#     setRange(0, 100);
#     setValue(80);
#     setStyleSheet(R"(
#     QProgressBar {
#         border: 1px solid lightgray;
#         background-color: #2b241c;
#         border-radius: 5px;
#     }

#     QProgressBar::chunk {
#         background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #f9dc98, stop:1 #f4b543);
#         border-radius: 4px;
#     }
#     )");

#     addShadow();
# }

# void QtBoxStyleProgressBar4::addShadow()
# {
#     QGraphicsDropShadowEffect *shadow = new QGraphicsDropShadowEffect(this);
#     shadow->setBlurRadius(40);
#     shadow->setOffset(0, 0);
#     shadow->setColor(QColor(241, 177, 66));
#     setGraphicsEffect(shadow);
# }
# C++/Qt