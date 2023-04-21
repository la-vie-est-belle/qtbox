# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QLabel = createWidgetMenuBase(QLabel)

class QtBoxFuncLabel5(QLabel):
    def __init__(self):
        super(QtBoxFuncLabel5, self).__init__(str(Path(__file__)))
        text = 'Lay words vertically'.replace(" ", "\n")
        self.setText(text)
        self.setAlignment(Qt.AlignCenter)
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QLabel


# class QtBoxFuncLabel5(QLabel):
#     def __init__(self):
#         super(QtBoxFuncLabel5, self).__init__(str(Path(__file__)))
#         text = 'Lay words vertically'.replace(" ", "\n")
#         self.setText(text)
#         self.setAlignment(Qt.AlignCenter)
# PySide

# C++/Qt
# #ifndef QTBOXFUNCLABEL5_H
# #define QTBOXFUNCLABEL5_H
# #include <QLabel>

# class QtBoxFuncLabel5 : public QLabel
# {
#     Q_OBJECT

# public:
#     QtBoxFuncLabel5(QWidget *parent = nullptr);
# };
# #endif // QTBOXFUNCLABEL5_H



# #include "qtboxfunclabel5.h"
# #include <QString>
# #include <Qt>

# QtBoxFuncLabel5::QtBoxFuncLabel5(QWidget *parent)
#     : QLabel(parent)
# {
#     QString text = "Lay words vertically";
#     text = text.replace(" ", "\n");
#     setText(text);
#     setAlignment(Qt::AlignCenter);
# }
# C++/Qt