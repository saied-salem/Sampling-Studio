import numpy as np
import pandas as pd
import qdarkstyle
from PyQt5 import QtWidgets
from PyQt5 import QtCore as qtc
from PyQt5 import uic
from PyQt5.QtWidgets import QFileDialog

from Composer_canvas import Composer_canvas
from componants_canvas import Componants_canvas
from Sinusoidal_wave import Sinusoidal_wave
from composed_signal import Composed_signal


class Composer(QtWidgets.QWidget):

    to_sampling_process = qtc.pyqtSignal(list, list,float)

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
        self.saved_composed_signals=[]
        self.saved_composed_signal_object=[]
        self.composed_signal=0
        self.Sample_button = self.findChild(QtWidgets.QPushButton,"Sample_button")


        self.signals_and_slots_connection()
        # print(self.Add_button)

    def signals_and_slots_connection(self):
        self.Add_button.clicked.connect(self.add_componant)
        self.Delete_button.clicked.connect(self.delete_component)
        self.Save_signal_button.clicked.connect(self.save_composed_signal)
        self.Sample_button.clicked.connect(self.start_sampling)
        self.Composed_Signals_box.activated.connect(self.get_saved_signal)



    def add_componant(self):
        # print("on addddddddd")
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
        # print("on update_composer_graph")
        composed_sinusoidal=self.get_composed_signal()
        time = self.time
        # print("on update_composer_graph")

        self.composer_canvas.plot(time,composed_sinusoidal)

    def get_composed_signal(self):
        composed_signal = np.zeros(len(self.time))
        # print(composed_signal)
        for sinusoidal in self.sinusoidals_componants:
            composed_signal+=sinusoidal.get_values()
        # print(composed_signal)
        return composed_signal

    def delete_component(self):
        curr_idx=self.componant_box.currentIndex()
        self.componant_canvas.remove_component_from_graph(curr_idx)
        self.sinusoidals_componants.remove(self.sinusoidals_componants[curr_idx])
        self.update_composer_graph()
        self.componant_box.removeItem(curr_idx)

    def save_composed_signal(self):
        sinusoidals_componants = self.sinusoidals_componants.copy()
        self.composed_signal = Composed_signal(self.time,sinusoidals_componants)
        self.saved_composed_signal_object.append( self.composed_signal)

        curr_composed_signal = self.get_composed_signal()
        self.saved_composed_signals.append(curr_composed_signal)
        self.Composed_Signals_box.addItem("Signal : {No_signal}".format(No_signal = len(self.saved_composed_signals)))

    def get_fmax(self):
        combo_box_idx = self.Composed_Signals_box.currentIndex()
        composed_sig =self.saved_composed_signal_object[combo_box_idx]

        freq_list = [sinusoidal.get_freq() for sinusoidal in composed_sig.get_componants()]
        return max(freq_list)

    def start_sampling(self):
        curr_Composed_Signals_box_index = self.Composed_Signals_box.currentIndex()
        # print(curr_Composed_Signals_box_index)
        # print(self.saved_composed_signals)
        curr_composed_signal=self.saved_composed_signals[curr_Composed_Signals_box_index]
        max_freq= self.get_fmax()
        time =self.time.tolist()
        values =curr_composed_signal.tolist()
        self.to_sampling_process.emit(time,values,max_freq)
        # print("emitting signal ")

    def get_saved_signal(self,idx):
        composed_sig = self.saved_composed_signal_object[idx]
        # print("composed_sig_componants")
        # print(idx)

        # print(self.saved_composed_signal_object[idx].componants)
        self.componant_box.clear()
        for sinusoidal in composed_sig.get_componants():

            self.componant_box.addItem("amp:{amp},freq{freq},phase{phase}".format(amp = sinusoidal.amp, freq = sinusoidal.freq,phase=sinusoidal.phase))


        self.plot_componants(composed_sig.componants)
        # print("befor composer_canvas")

        self.composer_canvas.plot(self.time,composed_sig.values)

    def plot_componants(self,composed_sig):
        self.componant_canvas.clear_canvans()
        for sinusoidal in composed_sig:
            # print("inside for loop")
            # print(sinusoidal.get_values())
            self.componant_canvas.add_component_to_graph(self.time, sinusoidal)

        # print("ending")

