# PyQt
import webbrowser
from PyQt5.QtWidgets import QPushButton
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QPushButton = createWidgetMenuBase(QPushButton)

class QtBoxFuncButton3(QPushButton):
    def __init__(self):
        super(QtBoxFuncButton3, self).__init__(str(Path(__file__)))
        self.setText("Open a website")
        self.clicked.connect(self.open_a_website)

    def open_a_website(self):
        url = "https://github.com/la-vie-est-belle/qtbox"
        webbrowser.open(url)
# PyQt

# PySide
# import webbrowser
# from PySide2.QtWidgets import QPushButton


# class QtBoxFuncButton3(QPushButton):
#     def __init__(self):
#         super(QtBoxFuncButton3, self).__init__()
#         self.setText("Open a website")
#         self.clicked.connect(self.open_a_website)

#     def open_a_website(self):
#         url = "https://github.com/la-vie-est-belle/qtbox"
#         webbrowser.open(url)
# PySide

# C++/Qt
# #ifndef QTBOXFUNCPUSHBUTTON3_H
# #define QTBOXFUNCPUSHBUTTON3_H
# #include <QPushButton>

# class QtBoxFuncPushButton3 : public QPushButton
# {
#     Q_OBJECT

# public:
#     QtBoxFuncPushButton3(QWidget *parent = nullptr);

# private slots:
#     void openAWebsite();
# };
# #endif // QTBOXFUNCPUSHBUTTON3_H



# #include "qtboxfuncpushbutton3.h"
# #include <QDesktopServices>
# #include <QUrl>

# QtBoxFuncPushButton3::QtBoxFuncPushButton3(QWidget *parent)
#     : QPushButton(parent)
# {
#     setText("Open a website");
#     connect(this, SIGNAL(clicked()), this, SLOT(openAWebsite()));
# }

# void QtBoxFuncPushButton3::openAWebsite()
# {
#     QUrl url = QUrl("https://github.com/la-vie-est-belle/qtbox");
#     QDesktopServices::openUrl(url);
# }
# C++/Qt