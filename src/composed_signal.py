import numpy as np


class Composed_signal:

    def __init__(self,time,componants):
        self.time = time
        self.componants=componants
        self.values=  self.get_composed_values()



    def get_composed_values(self):
        composed_signal = np.zeros(len(self.time))

        for sinusoidal in self.componants:
            composed_signal+=sinusoidal.get_values()

        return composed_signal

    def get_componants(self):
        return self.componants