# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QMessageBox
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QLineEdit = createWidgetMenuBase(QLineEdit)

class QtBoxFuncLineEdit1(QLineEdit):
    def __init__(self):
        super(QtBoxFuncLineEdit1, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 30)
        self.setPlaceholderText("press Enter or Return")

    def keyPressEvent(self, event):
        super(QtBoxFuncLineEdit1, self).keyPressEvent(event)
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            QMessageBox.information(self, "Qt Box", "Key Enter or Return pressed")
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QLineEdit, QMessageBox


# class QtBoxFuncLineEdit1(QLineEdit):
#     def __init__(self):
#         super(QtBoxFuncLineEdit1, self).__init__()
#         self.setFixedSize(150, 30)
#         self.setPlaceholderText("press Enter or Return")

#     def keyPressEvent(self, event):
#         super(QtBoxFuncLineEdit1, self).keyPressEvent(event)
#         if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
#             QMessageBox.information(self, "Qt Box", "Key Enter or Return pressed")
# PySide

# C++/Qt
# #ifndef QTBOXFUNCLINEEDIT1_H
# #define QTBOXFUNCLINEEDIT1_H
# #include <QLineEdit>
# #include <QKeyEvent>

# class QtBoxFuncLineEdit1 : public QLineEdit
# {
#     Q_OBJECT

# protected:
#     void keyPressEvent(QKeyEvent *event);

# public:
#     QtBoxFuncLineEdit1(QWidget *parent = nullptr);
# };
# #endif // QTBOXFUNCLINEEDIT1_H



# #include "qtboxfunclineedit1.h"
# #include <QMessageBox>
# #include <Qt>

# QtBoxFuncLineEdit1::QtBoxFuncLineEdit1(QWidget *parent)
#     : QLineEdit(parent)
# {
#     setFixedSize(150, 30);
#     setPlaceholderText("press Enter or Return");
# }

# void QtBoxFuncLineEdit1::keyPressEvent(QKeyEvent *event)
# {
#     QLineEdit::keyPressEvent(event);
#     if (event->key() == Qt::Key_Enter || event->key() == Qt::Key_Return) {
#         QMessageBox::information(this, "Qt Box", "Key Enter or Return pressed");
#     }
# }
# C++/Qt