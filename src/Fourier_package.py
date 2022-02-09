import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def get_f_max(time,data):
    amp = np.fft.rfft(data)
    freq = np.fft.rfftfreq(len(data), (time[1] - time[0]))

    f_max=0
    for i, a in enumerate(amp):

        if abs(a) > 5 : # (1)
            f_max = freq[i]

    plot_freq_spectrum(freq,amp)
    return f_max

def plot_freq_spectrum(freq,amp):
    fig, axs = plt.subplots(2)
    axs[0].plot(freq, abs(amp))
    plt.show()

fileName= "../ECG.csv"
df = pd.read_csv(fileName)
# val = df.values.col
# time = df.iloc[:, 0]
# valued = df.iloc[:, 1]
# print(time)
time= np.linspace(0,4,1000)
values = np.sin(2*np.pi*time*1200)+ np.sin(2*np.pi*time*50)+ np.sin(2*np.pi*time*12)
f_max= get_f_max(time,values)
print(f_max)

