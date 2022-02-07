import numpy as np


class Sinusoidal_wave:

    def __init__(self,amp=1,freq=1,phase=0,time=[]):
        self.amp=amp
        self.freq=freq
        self.phase=phase
        self.time =time
        self.PI = np.pi
        self.values = self.creat_sin_wave()



    def creat_sin_wave(self):
        self.values = self.amp*np.sin(2*self.PI*self.freq*self.time + self.phase*(self.PI/180))
        return self.values


    def get_freq(self):
        return self.freq

    def get_values(self):
        return self.values


