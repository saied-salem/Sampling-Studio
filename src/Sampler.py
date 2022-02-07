import numpy as np
from PyQt5 import QtWidgets
from PyQt5 import QtCore as qtc
from PyQt5 import uic
from scipy import signal

from Sampling_and_reconstruction_canvas import Sampling_and_reconstruction_canvas


class Sampler(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi("UI/Sampler.ui", self)
        self.sampel_and_reco_canvas =Sampling_and_reconstruction_canvas()
        self.Canvas_layout.addWidget(self.sampel_and_reco_canvas )

        self.time=[]
        self.values=[]
        self.max_freq=0
        self.Freq_rate_slider.setValue(10)
        self.Freq_rate_slider.valueChanged.connect(self.sample_signal)
        self.toggel_button.clicked.connect(self.toggel_visability_second_axes)

    def clear_canvas(self):
        self.sampel_and_reco_canvas.clear_canvas()

    def init_canvas(self):
        self.clear_canvas()
        self.sample_signal()

    def move_to_sampler(self,time,values,max_freq):
        self.load_composed_signal(time,values,max_freq)
        self.plot_composed_signal()


    def load_composed_signal(self,time,values,max_freq):
        self.time=time
        self.values=values
        self.max_freq=max_freq
        self.Lcd_max_freq.display(max_freq)

    def plot_composed_signal(self):
        self.sampel_and_reco_canvas.plot_composed_signal(self.time,self.values)


    def sample_signal(self):
        values = np.array(self.values)
        factor = (self.Freq_rate_slider.value()/10)
        self.Slider_lable.setText("{F_max}F-max".format(F_max = factor))
        sampling_freq =factor*self.max_freq
        sampled_time_points = np.arange(self.time[0],self.time[-1],1/sampling_freq)

        sampled_values_points= values[np.searchsorted(self.time,sampled_time_points)]

        reconstructed_signal = self.reconstruct_signal(sampled_values_points,len(self.time))

        self.clear_canvas()
        self.plot_composed_signal()
        self.plot_reconstructed_signal(self.time,sampled_time_points,sampled_values_points,reconstructed_signal)


    def reconstruct_signal(self,sampled_values_points,num_points):
        reconstructed_signal = signal.resample(sampled_values_points, num_points)
        return reconstructed_signal



    def plot_reconstructed_signal(self,time,sampled_time_points,sampled_values_points,reconstructed_signal):
        self.sampel_and_reco_canvas.plot_reconstructed_signal(self.time,reconstructed_signal)
        self.sampel_and_reco_canvas.plot_sampled_scatterd_signal(sampled_time_points,sampled_values_points)
        self.sampel_and_reco_canvas.plot_final_reconstructed_signal(self.time,reconstructed_signal)

    def toggel_visability_second_axes(self):
        print("iiiiiiiiiiiiiiiii")
        self.sampel_and_reco_canvas.toggel_visability_second_axes()