import numpy as np
import qdarkstyle
from PyQt5 import QtWidgets
from PyQt5 import QtCore as qtc
from PyQt5 import uic

from Composer_canvas import Composer_canvas
from componants_canvas import Componants_canvas
from Sinusoidal_wave import Sinusoidal_wave


class Composer(QtWidgets.QWidget):
    def __init__(self):
        self.NUM_OF_POINTS = 1000
        super().__init__()
        uic.loadUi("UI/Composer.ui", self)
        self.composer_canvas = Composer_canvas()
        self.componant_canvas = Componants_canvas()
        self.Composing_canvas_layout.addWidget(self.composer_canvas )
        self.Componant_canvas_layout.addWidget(self.componant_canvas  )
        self.time = np.linspace(0, 5, self.NUM_OF_POINTS)
        self.sinusoidals_componants=[]



        self.signals_and_slots_connection()
        print(self.Add_button)

    def signals_and_slots_connection(self):
        self.Add_button.clicked.connect(self.add_componant)
        self.Delete_button.clicked.connect(self.delete_component)

    def add_componant(self):
        print("on addddddddd")
        new_sinusoidal = self.creating_sinusoidal()
        self.componant_canvas.add_component_to_graph(self.time,new_sinusoidal)
        self.sinusoidals_componants.append(new_sinusoidal)
        self.update_composer_graph()
        self.componant_box.addItem("amp:{amp},freq{freq},phase{phase}".format(amp = new_sinusoidal.amp, freq = new_sinusoidal.freq,phase=new_sinusoidal.phase))



    def creating_sinusoidal(self):
        amp = self.Amplitude_spin_box.value()
        freq = self.Frequency_spin_box.value()
        phase = self.Phase_spin_box.value()
        time = self.time
        new_sinusoidal = Sinusoidal_wave(amp, freq, phase, time)

        return new_sinusoidal

    def update_composer_graph(self):
        print("on update_composer_graph")
        composed_sinusoidal=self.get_composed_signal()
        time = self.time
        print("on update_composer_graph")

        self.composer_canvas.plot(time,composed_sinusoidal)

    def get_composed_signal(self):
        composed_signal = np.zeros(len(self.time))
        print(composed_signal)
        for sinusoidal in self.sinusoidals_componants:
            composed_signal+=sinusoidal.get_values()
        print(composed_signal)
        return composed_signal

    def delete_component(self):
        curr_idx=self.componant_box.currentIndex()
        self.componant_canvas.remove_component_from_graph(curr_idx)
        self.sinusoidals_componants.remove(self.sinusoidals_componants[curr_idx])
        self.update_composer_graph()
        self.componant_box.removeItem(curr_idx)
