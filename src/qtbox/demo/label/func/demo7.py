# PyQt
from PyQt5.QtWidgets import QLabel
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QLabel = createWidgetMenuBase(QLabel)

class QtBoxFuncLabel7(QLabel):
    def __init__(self):
        super(QtBoxFuncLabel7, self).__init__(str(Path(__file__)))
        self.setText("Drop a txt file on me.\n"
                     "I will show its content.")
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        super(QtBoxFuncLabel7, self).dragEnterEvent(event)
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        super(QtBoxFuncLabel7, self).dropEvent(event)
        url = event.mimeData().urls()[0].toLocalFile()
        if not url.endswith(".txt"):
            return

        with open(url, "r", encoding="utf-8") as f:
            self.setText(f.read())
# PyQt

# PySide
# from PySide2.QtWidgets import QLabel


# class QtBoxFuncLabel7(QLabel):
#     def __init__(self):
#         super(QtBoxFuncLabel7, self).__init__()
#         self.setText("Drop a txt file on me.\n"
#                      "I will show its content.")
#         self.setAcceptDrops(True)

#     def dragEnterEvent(self, event):
#         super(QtBoxFuncLabel7, self).dragEnterEvent(event)
#         if event.mimeData().hasUrls():
#             event.acceptProposedAction()

#     def dropEvent(self, event):
#         super(QtBoxFuncLabel7, self).dropEvent(event)
#         url = event.mimeData().urls()[0].toLocalFile()
#         if not url.endswith(".txt"):
#             return

#         with open(url, "r", encoding="utf-8") as f:
#             self.setText(f.read())
# PySide

# C++/Qt
# #ifndef QTBOXFUNCLABEL7_H
# #define QTBOXFUNCLABEL7_H
# #include <QLabel>
# #include <QDragEnterEvent>
# #include <QDropEvent>

# class QtBoxFuncLabel7 : public QLabel
# {
#     Q_OBJECT

# public:
#     QtBoxFuncLabel7(QWidget *parent = nullptr);

# protected:
#     void dragEnterEvent(QDragEnterEvent *event);
#     void dropEvent(QDropEvent *event);
# };
# #endif // QTBOXFUNCLABEL7_H



# #include "qtboxfunclabel7.h"
# #include <QMimeData>
# #include <QString>
# #include <QFile>
# #include <QIODevice>

# QtBoxFuncLabel7::QtBoxFuncLabel7(QWidget *parent)
#     : QLabel(parent)
# {
#     setText("Drop a txt file on me.\n"
#             "I will show its content.");
#     setAcceptDrops(true);
# }

# void QtBoxFuncLabel7::dragEnterEvent(QDragEnterEvent *event)
# {
#     QLabel::dragEnterEvent(event);
#     if (event->mimeData()->hasUrls()) {
#         event->acceptProposedAction();
#     }
# }

# void QtBoxFuncLabel7::dropEvent(QDropEvent *event)
# {
#     QLabel::dropEvent(event);
#     QString url = event->mimeData()->urls()[0].toLocalFile();
#     if (!url.endsWith(".txt")) {
#         return;
#     }

#     QFile file(url);
#     file.open(QIODevice::ReadOnly);
#     setText(file.readAll());
#     file.close();
# }
# C++/Qt