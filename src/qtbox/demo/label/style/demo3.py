# PyQt
from PyQt5.QtWidgets import QLabel, QGraphicsBlurEffect
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QLabel = createWidgetMenuBase(QLabel)

class QtBoxStyleLabel3(QLabel):
    def __init__(self):
        super(QtBoxStyleLabel3, self).__init__(str(Path(__file__)))
        self.setText("Blur")
        self.blur()

    def blur(self):
        blur = QGraphicsBlurEffect(self)
        blur.setBlurRadius(6)
        blur.setBlurHints(QGraphicsBlurEffect.QualityHint)
        self.setGraphicsEffect(blur)
# PyQt

# PySide
# from PySide2.QtWidgets import QLabel, QGraphicsBlurEffect


# class QtBoxStyleLabel3(QLabel):
#     def __init__(self):
#         super(QtBoxStyleLabel3, self).__init__()
#         self.setText("Blur")
#         self.blur()

#     def blur(self):
#         blur = QGraphicsBlurEffect(self)
#         blur.setBlurRadius(6)
#         blur.setBlurHints(QGraphicsBlurEffect.QualityHint)
#         self.setGraphicsEffect(blur)
# PySide

# C++/Qt
# #ifndef QTBOXSTYLELABEL3_H
# #define QTBOXSTYLELABEL3_H
# #include <QLabel>

# class QtBoxStyleLabel3 : public QLabel
# {
#     Q_OBJECT

# public:
#     QtBoxStyleLabel3(QWidget *parent = nullptr);

# private:
#     void blur();
# };
# #endif // QTBOXSTYLELABEL3_H



# #include "qtboxstylelabel3.h"
# #include <QGraphicsBlurEffect>

# QtBoxStyleLabel3::QtBoxStyleLabel3(QWidget *parent)
#     : QLabel(parent)
# {
#     setText("Blur");
#     blur();
# }

# void QtBoxStyleLabel3::blur() {
#     QGraphicsBlurEffect *blur = new QGraphicsBlurEffect(this);
#     blur->setBlurRadius(2);
#     blur->setBlurHints(QGraphicsBlurEffect::QualityHint);
#     setGraphicsEffect(blur);
# }
# C++/Qt