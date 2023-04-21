# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QLabel = createWidgetMenuBase(QLabel)

class QtBoxFuncLabel2(QLabel):
    def __init__(self):
        super(QtBoxFuncLabel2, self).__init__(str(Path(__file__)))
        self.setText("I'm editable.")
        self.setTextInteractionFlags(Qt.TextEditorInteraction)
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QLabel


# class QtBoxFuncLabel2(QLabel):
#     def __init__(self):
#         super(QtBoxFuncLabel2, self).__init__()
#         self.setText("I'm editable.")
#         self.setTextInteractionFlags(Qt.TextEditorInteraction)
# PySide

# C++/Qt
# #ifndef QTBOXFUNCLABEL2_H
# #define QTBOXFUNCLABEL2_H
# #include <QLabel>

# class QtBoxFuncLabel2 : public QLabel
# {
#     Q_OBJECT

# public:
#     QtBoxFuncLabel2(QWidget *parent = nullptr);
# };
# #endif // QTBOXFUNCLABEL2_H



# #include "qtboxfunclabel2.h"
# #include <Qt>

# QtBoxFuncLabel2::QtBoxFuncLabel2(QWidget *parent)
#     : QLabel(parent)
# {
#     setText("I'm editable.");
#     setTextInteractionFlags(Qt::TextEditorInteraction);
# }
# C++/Qt