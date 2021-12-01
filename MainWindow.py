import webbrowser
from UIMainWindowForm import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtCore import QSettings
import app_info


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(app_info.TITLE)
        self.setMinimumWidth(self.width())
        self.setMaximumWidth(self.width())
        self.setMinimumHeight(self.height())
        self.setMaximumHeight(self.height())
