import sys

from PyQt5 import QtWidgets
from PyQt5 import QtCore as qtc
from PyQt5 import uic
import qdarkstyle

from composer import Composer
from Sampler import Sampler


class Tab_viewer(QtWidgets.QTabWidget):
    """The main application window"""

    def __init__(self):
        super().__init__()
        uic.loadUi("UI/Tab_viewer.ui", self)
        self.composer = Composer()
        self.sampler = Sampler()
        self.Composer_layout.addWidget(self.composer)
        self.Sampler_layout.addWidget(self.sampler)
        self.setCurrentWidget(self.composer_tap)

        self.composer.to_sampling_process.connect(self.move_to_sampler)


    def move_to_sampler(self,time,values,fmax):
        # print("inside move to sample")
        self.setCurrentWidget(self.sampler_tab)
        self.sampler.move_to_sampler(time,values,fmax)
        self.sampler.init_canvas()




