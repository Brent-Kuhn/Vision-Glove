import matplotlib.pyplot as plt
import numpy
from random import *
import time

# Dynamic chart that automatically rescales axis to show all data
class DynamicChart():
	def __init__(self):
		# Enable interactive charts
		plt.ion()
		# Create subplot
		self.fig, (self.ax) = plt.subplots(1,1)
		self.line, = self.ax.plot([], [])


	def addData(self, new_data_x, new_data_y):
		self.line.set_xdata(numpy.append(self.line.get_xdata(), new_data_x))
		self.line.set_ydata(numpy.append(self.line.get_ydata(), new_data_y))
		self.ax.relim()
		self.ax.autoscale_view()
		self.fig.canvas.draw()
		self.fig.canvas.flush_events()

# Implementation
def main():
	# Instantiate Chart
	chart = DynamicChart()

	x = 0
	while True:
    		new_y = randint(0, 5)
    		x += 1
    		print((x, new_y))
    		chart.addData(x, new_y)
    		# time.sleep(1)

if __name__ == "__main__":
	main()




