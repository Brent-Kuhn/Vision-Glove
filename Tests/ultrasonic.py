import atexit
import RPi.GPIO as GPIO
import time

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

count = 0

ax1.clear()

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
    time.sleep(.1)

    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)

    while GPIO.input(ECHO) == 0:
        pass
    pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pass
    pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = distance//1

    GPIO.cleanup()

    return str(distance)

while(True):
    distance = Ultrasonic_Sensor(Sensor_Array[0])
    print(distance)

    ax1.plot(count, lidar)
    count += count

atexit.register(GPIO.cleanup)