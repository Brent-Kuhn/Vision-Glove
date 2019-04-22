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

# Implementation
def main():
    while (True):
        print(Ultrasonic_Sensor(Sensor_Array[0]))


try:
    main()

except KeyboardInterrupt:
    print("exited")

except:
    print("finished")

finally:  
    GPIO.cleanup() # this ensures a clean exit


atexit.register(GPIO.cleanup())