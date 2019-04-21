import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import random

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.axis([0, 50, 0, 10])

count = 0
number = 0
def lidar():
    number = random.randint(0, 9)
    return number

ax1.clear()

x = []
y = []


while(True):
    # plt.ion()
    distance = lidar()
    print(distance)
    y.append(distance)
    x.append(count)
    ax1.plot(x, y)
    plt.draw()
    plt.show()
    count += count