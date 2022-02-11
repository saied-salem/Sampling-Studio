import matplotlib as matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as navigation_toolbar
from matplotlib.figure import Figure
plt.style.use('dark_background')
matplotlib.use('Qt5Agg')


class Componants_canvas(FigureCanvas):

    def __init__(self, parent=None, width=0.1, height=0.01, dpi=100):
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        for spine in ['right', 'top', 'left', 'bottom']:
            self.axes.spines[spine].set_color('gray')
        # self.axes.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
        super().__init__(self.fig)
        self.fig.tight_layout()



    def add_component_to_graph(self,time,sinusoidal):
        self.axes.plot(time,sinusoidal.get_values(),label="amp:{amp} ,freq:{freq}Hz ,phase{phase}".format(amp = sinusoidal.amp, freq = sinusoidal.freq,phase=sinusoidal.phase))
        self.axes.legend(loc='upper left')
        self.draw()


    def remove_component_from_graph(self,index):
        self.axes.lines.remove(self.axes.lines[index])
        self.axes.legend(loc='upper left')
        self.draw()

    def clear_canvans(self):
        self.axes.clear()
        self.draw()
