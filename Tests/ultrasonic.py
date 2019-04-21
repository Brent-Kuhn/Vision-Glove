import atexit
import RPi.GPIO as GPIO
from time import sleep, time

import matplotlib.pyplot as plt
import numpy
from random import *

Sensor_Array = [[4, 17], [18, 27], [22, 23]]

def Ultrasonic_Sensor(GPIO_Numbers):
    TRIG = GPIO_Numbers[0]
    ECHO = GPIO_Numbers[1]
    GPIO.setmode(GPIO.BCM)

    #print("Distance Measurement In Progress")

    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)

    GPIO.output(TRIG, 0)
    #print("Waiting for sensor to settle")
    sleep(.1)

    GPIO.output(TRIG, 1)
    sleep(0.00001)
    GPIO.output(TRIG, 0)

    while GPIO.input(ECHO) == 0:
        pass
    pulse_start = time()

    while GPIO.input(ECHO) == 1:
        pass
    pulse_end = time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = distance//1

    GPIO.cleanup()

    return str(distance)

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
    		new_y = Ultrasonic_Sensor(Sensor_Array[0])
    		x += 1
    		print((x, new_y))
    		chart.addData(x, new_y)
    		# time.sleep(1)

try:
    if __name__ == "__main__":
	main()

except KeyboardInterrupt:
    print("exited")

except:
    print("finished")

finally:  
    GPIO.cleanup() # this ensures a clean exit


atexit.register(GPIO.cleanup)