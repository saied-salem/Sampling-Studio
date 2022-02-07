import matplotlib as matplotlib
import matplotlib.pyplot as plt
from matplotlib import gridspec
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as navigation_toolbar
from matplotlib.figure import Figure
plt.style.use('dark_background')
matplotlib.use('Qt5Agg')


class Sampling_and_reconstruction_canvas(FigureCanvas):

    def __init__(self, parent=None, width=0.1, height=0.01, dpi=100):
        self.fig = Figure()
        self.gs = gridspec.GridSpec(2, 1, height_ratios=[1, 1] )
        self.gs2 = gridspec.GridSpec(1, 1, height_ratios=[1])
        self.axes1 = self.fig.add_subplot(self.gs[0])
        self.axes2 = self.fig.add_subplot(self.gs[1])


        self.visible = True
        # self.reconstructed_scatered, = self.axes1.scatter([], [])
        # for spine in ['right', 'top', 'left', 'bottom']:
        #     self.axes.spines[spine].set_color('gray')
        # self.axes.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
        super().__init__(self.fig)
        self.fig.tight_layout()

    def plot_composed_signal(self,time,values):
        self.axes1.plot(time,values)
        self.draw()
    def plot_sampled_scatterd_signal(self,sampled_time_points,sampled_values_points):
        self.axes1.scatter(sampled_time_points,sampled_values_points,c="red")
        self.draw()


    def plot_reconstructed_signal(self , time ,reconstructed_signal):
        self.axes1.plot(time ,reconstructed_signal,"--g")
        self.draw()

    def clear_canvas(self):
        self.axes1.clear()
        self.axes2.clear()
        self.draw()

    def plot_final_reconstructed_signal(self,time ,reconstructed_signal):
        self.axes2.plot(time,reconstructed_signal)
        self.draw()

    def toggel_visability_second_axes(self):
        self.visible = not self.visible
        self.axes2.set_visible(self.visible)
        print("ttttttttttt")

        if self.visible:
            self.axes1.set_position(self.gs[0].get_position(self.fig))

        else:
            self.axes1.set_position(self.gs2[0].get_position(self.fig))

        self.draw()