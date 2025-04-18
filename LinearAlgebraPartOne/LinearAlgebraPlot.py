#  Copyright (c) 2025.
import numpy as np
import  matplotlib.pyplot as plot
class LinearAlgPlot:
    time = np.linspace(0,40,1000)
    distance_robber = 2.5*time
    distance_cop = 3*(time-5)
    def __init__(self):
        pass
def main():
    plots()

def plots():
    fig,ax=plot.subplots()
    plot.title('Bank Robber Caught')
    plot.xlabel('time(in minutes)')
    plot.ylabel('distance (in km)')
    ax.set_xlim([0, 40])
    ax.set_ylim([0, 100])
    ax.plot(LinearAlgPlot.time,LinearAlgPlot.distance_robber,color='green')
    ax.plot(LinearAlgPlot.time,LinearAlgPlot.distance_cop,color='red')
    plot.axvline(x=30, color='purple', linestyle='--')
    _ = plot.axhline(y=75, color='purple', linestyle='--')
    plot.show()
if __name__ == '__main__':
    main()