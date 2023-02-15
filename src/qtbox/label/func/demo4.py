# PyQt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QLabel
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QLabel = createWidgetMenuBase(QLabel)
PATH_TO_GIF = str(Path(__file__).parent.parent.parent / "res/images/exercise").replace("\\", "/")

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