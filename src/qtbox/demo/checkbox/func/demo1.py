# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QCheckBox
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QCheckBox = createWidgetMenuBase(QCheckBox)

class QtBoxFuncCheckBox1(QCheckBox):
    def __init__(self):
        super(QtBoxFuncCheckBox1, self).__init__(str(Path(__file__)))
        self.setTristate(True)
        self.setText("UnChecked")
        self.stateChanged.connect(self.update_text)

    def update_text(self):
        if self.checkState() == Qt.Unchecked:
            self.setText("UnChecked")
        elif self.checkState() == Qt.PartiallyChecked:
            self.setText("PartiallyChecked")
        elif self.checkState() == Qt.Checked:
            self.setText("Checked")
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtWidgets import QCheckBox


# class QtBoxFuncCheckBox1(QCheckBox):
#     def __init__(self):
#         super(QtBoxFuncCheckBox1, self).__init__()
#         self.setTristate(True)
#         self.setText("UnChecked")
#         self.stateChanged.connect(self.update_text)

#     def update_text(self):
#         if self.checkState() == Qt.Unchecked:
#             self.setText("UnChecked")
#         elif self.checkState() == Qt.PartiallyChecked:
#             self.setText("PartiallyChecked")
#         elif self.checkState() == Qt.Checked:
#             self.setText("Checked")
# PySide

# C++/Qt
# #ifndef QTBOXFUNCCHECKBOX1_H
# #define QTBOXFUNCCHECKBOX1_H
# #include <QCheckBox>

# class QtBoxFuncCheckBox1 : public QCheckBox
# {
#     Q_OBJECT

# public:
#     QtBoxFuncCheckBox1(QWidget *parent = nullptr);

# private slots:
#     void updateText();
# };
# #endif // QTBOXFUNCCHECKBOX1_H



# #include "qtboxfunccheckbox1.h"
# #include <Qt>

# QtBoxFuncCheckBox1::QtBoxFuncCheckBox1(QWidget *parent)
#     : QCheckBox(parent)
# {
#     setTristate(true);
#     setText("UnChecked");
#     connect(this, SIGNAL(stateChanged(int)), this, SLOT(updateText()));
# }

# void QtBoxFuncCheckBox1::updateText()
# {
#     if (checkState() == Qt::Unchecked) {
#         setText("UnChecked");
#     }
#     else if (checkState() == Qt::PartiallyChecked) {
#         setText("PartiallyChecked");
#     }
#     else if (checkState() == Qt::Checked) {
#         setText("Checked");
#     }
# }
# C++/Qt
