# PyQt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QLabel
from qtbox.gui.menu import createWidgetMenuBase
from pathlib import Path

QLabel = createWidgetMenuBase(QLabel)
PATH_TO_GIF = str(Path(__file__).parent.parent.parent.parent / "res/images/exercise.gif").replace("\\", "/")

class QtBoxFuncLabel4(QLabel):
    def __init__(self):
        super(QtBoxFuncLabel4, self).__init__(str(Path(__file__)))
        movie = QMovie()
        movie.setFileName(PATH_TO_GIF)
        self.setMovie(movie)
        movie.start()
# PyQt

# PySide
# from PySide2.QtGui import QMovie
# from PySide2.QtWidgets import QLabel


# class QtBoxFuncLabel4(QLabel):
#     def __init__(self):
#         super(QtBoxFuncLabel4, self).__init__(str(Path(__file__)))
#         movie = QMovie()
#         movie.setFileName(PATH_TO_GIF)
#         self.setMovie(movie)
#         movie.start()
# PySide

# C++/Qt
# #ifndef QTBOXFUNCLABEL4_H
# #define QTBOXFUNCLABEL4_H
# #include <QLabel>
# #include <QMovie>

# class QtBoxFuncLabel4 : public QLabel
# {
#     Q_OBJECT

# public:
#     QtBoxFuncLabel4(QWidget *parent = nullptr);

# private:
#     QMovie *movie = new QMovie();
# };
# #endif // QTBOXFUNCLABEL4_H



# #include "qtboxfunclabel4.h"

# QtBoxFuncLabel4::QtBoxFuncLabel4(QWidget *parent)
#     : QLabel(parent)
# {
#     movie->setFileName(PATH_TO_GIF);
#     setMovie(movie);
#     movie->start();
# }
# C++/Qt
