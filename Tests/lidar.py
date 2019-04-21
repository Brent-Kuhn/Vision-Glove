import serial
import time

import matplotlib.pyplot as plt
import numpy
from random import *

ser = serial.Serial('/dev/ttyUSB0',115200,timeout = 1)

#ser.write(0x42)
ser.write(bytes(b'B'))

#ser.write(0x57)
ser.write(bytes(b'W'))

#ser.write(0x02)
ser.write(bytes(2))

#ser.write(0x00)
ser.write(bytes(0))

#ser.write(0x00)
ser.write(bytes(0))

#ser.write(0x00)
ser.write(bytes(0))
          
#ser.write(0x01)
ser.write(bytes(1))
          
#ser.write(0x06)
ser.write(bytes(6))

def lidar():
    while(True):
        while(ser.in_waiting >= 9):
            if((b'Y' == ser.read()) and ( b'Y' == ser.read())):

                Dist_L = ser.read()
                Dist_H = ser.read()
                Dist_Total = (ord(Dist_H) * 256) + (ord(Dist_L))
                for i in range (0,5):
                    ser.read()
                    
                return str(Dist_Total)

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
    		new_y = lidar()
    		x += 1
    		print((x, new_y))
    		chart.addData(x, new_y)
    		# time.sleep(1)

if __name__ == "__main__":
	main()