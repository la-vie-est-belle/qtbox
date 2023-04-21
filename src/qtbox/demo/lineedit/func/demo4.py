# PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLineEdit, QPushButton
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QLineEdit = createWidgetMenuBase(QLineEdit)
PATH_TO_OPEN_EYE_IMG = str(Path(__file__).parent.parent.parent.parent / "res/images/open_eye.png").replace("\\", "/")
PATH_TO_CLOSED_EYE_IMG = str(Path(__file__).parent.parent.parent.parent / "res/images/closed_eye.png").replace("\\", "/")

class QtBoxFuncLineEdit4(QLineEdit):
    def __init__(self):
        super(QtBoxFuncLineEdit4, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 30)
        self.setEchoMode(QLineEdit.Password)
        self.setPlaceholderText("Enter password")
        self.setStyleSheet("""
        QLineEdit {
            padding-right: 25px;
        }
        """)

        self.eye_btn = QPushButton(self)
        self.eye_btn.setIcon(QIcon(PATH_TO_CLOSED_EYE_IMG))
        self.eye_btn.setFixedSize(self.height(), self.height())
        self.eye_btn.move(self.width()-self.eye_btn.width(), 0)
        self.eye_btn.clicked.connect(self.change_echo_mode)
        self.eye_btn.setCursor(Qt.PointingHandCursor)
        self.eye_btn.setStyleSheet("""
        QPushButton {
            border: none;
        }
        """)

    def change_echo_mode(self):
        if self.echoMode() == QLineEdit.Normal:
            self.setEchoMode(QLineEdit.Password)
            self.eye_btn.setIcon(QIcon(PATH_TO_CLOSED_EYE_IMG))
        else:
            self.setEchoMode(QLineEdit.Normal)
            self.eye_btn.setIcon(QIcon(PATH_TO_OPEN_EYE_IMG))
# PyQt

# PySide
# from PySide2.QtCore import Qt
# from PySide2.QtGui import QIcon
# from PySide2.QtWidgets import QLineEdit, QPushButton


# class QtBoxFuncLineEdit4(QLineEdit):
#     def __init__(self):
#         super(QtBoxFuncLineEdit4, self).__init__(str(Path(__file__)))
#         self.setFixedSize(150, 30)
#         self.setEchoMode(QLineEdit.Password)
#         self.setPlaceholderText("Enter password")
#         self.setStyleSheet("""
#         QLineEdit {
#             padding-right: 25px;
#         }
#         """)

#         self.eye_btn = QPushButton(self)
#         self.eye_btn.setIcon(QIcon(PATH_TO_CLOSED_EYE_IMG))
#         self.eye_btn.setFixedSize(self.height(), self.height())
#         self.eye_btn.move(self.width()-self.eye_btn.width(), 0)
#         self.eye_btn.clicked.connect(self.change_echo_mode)
#         self.eye_btn.setCursor(Qt.PointingHandCursor)
#         self.eye_btn.setStyleSheet("""
#         QPushButton {
#             border: none;
#         }
#         """)

#     def change_echo_mode(self):
#         if self.echoMode() == QLineEdit.Normal:
#             self.setEchoMode(QLineEdit.Password)
#             self.eye_btn.setIcon(QIcon(PATH_TO_CLOSED_EYE_IMG))
#         else:
#             self.setEchoMode(QLineEdit.Normal)
#             self.eye_btn.setIcon(QIcon(PATH_TO_OPEN_EYE_IMG))
# PySide

# C++/Qt
# #ifndef QTBOXFUNCLINEEDIT4_H
# #define QTBOXFUNCLINEEDIT4_H
# #include <QLineEdit>
# #include <QPushButton>

# class QtBoxFuncLineEdit4 : public QLineEdit
# {
#     Q_OBJECT

# public:
#     QtBoxFuncLineEdit4(QWidget *parent = nullptr);

# private:
#     QPushButton *eyeBtn = new QPushButton(this);

# private slots:
#     void changeEchoMode();
# };
# #endif // QTBOXFUNCLINEEDIT4_H



# #include "qtboxfunclineedit4.h"
# #include <QIcon>
# #include <Qt>

# QtBoxFuncLineEdit4::QtBoxFuncLineEdit4(QWidget *parent)
#     : QLineEdit(parent)
# {
#     setFixedSize(150, 30);
#     setEchoMode(QLineEdit::Password);
#     setPlaceholderText("Enter password");
#     setStyleSheet("QLineEdit {padding-right: 25px;}");

#     eyeBtn->setIcon(QIcon(PATH_TO_CLOSED_EYE_IMG));
#     eyeBtn->setFixedSize(height(), height());
#     eyeBtn->move(width()-eyeBtn->width(), 0);
#     connect(eyeBtn, SIGNAL(clicked()), this, SLOT(changeEchoMode()));
#     eyeBtn->setCursor(Qt::PointingHandCursor);
#     eyeBtn->setStyleSheet("QPushButton {border: none;}");
# }

# void QtBoxFuncLineEdit4::changeEchoMode()
# {
#     if (echoMode() == QLineEdit::Normal) {
#         setEchoMode(QLineEdit::Password);
#         eyeBtn->setIcon(QIcon(PATH_TO_CLOSED_EYE_IMG));
#     }
#     else {
#         setEchoMode(QLineEdit::Normal);
#         eyeBtn->setIcon(QIcon(PATH_TO_OPEN_EYE_IMG));
#     }
# }
# C++/Qt