import sys

from PyQt5 import QtWidgets
from PyQt5 import QtCore as qtc
from PyQt5 import uic
import qdarkstyle

from composer import Composer


class Tab_viewer(QtWidgets.QTabWidget):
    """The main application window"""

    def __init__(self):
        super().__init__()
        uic.loadUi("UI/Tab_viewer.ui", self)
        self.composer = Composer()
        self.Composer_layout.addWidget(self.composer)




