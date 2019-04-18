#!/usr/bin/python
import smbus
import math
from time import sleep
 
# Register
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c
 
def read_byte(reg):
    return bus.read_byte_data(address, reg)
 
def read_word(reg):
    h = bus.read_byte_data(address, reg)
    l = bus.read_byte_data(address, reg+1)
    value = (h << 8) + l
    return value
 
def read_word_2c(reg):
    val = read_word(reg)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val
 
def dist(a,b):
    return math.sqrt((a*a)+(b*b))
 
def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)
 
def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

while (True):
    bus = smbus.SMBus(1) # bus = smbus.SMBus(0) fuer Revision 1
    address = 0x68       # via i2cdetect
    
    # Enable to address the module
    bus.write_byte_data(address, power_mgmt_1, 0)
    
    print("gyro")
    print("--------")
    
    gyro_xout = read_word_2c(0x43)
    gyro_yout = read_word_2c(0x45)
    gyro_zout = read_word_2c(0x47)
    
    print("gyro_xout: ", ("%5d" % gyro_xout), " scaled: ", (gyro_xout / 131))
    print("gyro_yout: ", ("%5d" % gyro_yout), " scaled: ", (gyro_yout / 131))
    print("gyro_zout: ", ("%5d" % gyro_zout), " scaled: ", (gyro_zout / 131))
    
    print()
    print("Accelerometer")
    print("---------------------")
    
    accelleration_xout = read_word_2c(0x3b)
    accelleration_yout = read_word_2c(0x3d)
    accelleration_zout = read_word_2c(0x3f)
    
    accelleration_xout_scaled = accelleration_xout / 16384.0
    accelleration_yout_scaled = accelleration_yout / 16384.0
    accelleration_zout_scaled = accelleration_zout / 16384.0
    
    print("accelleration_xout: ", ("%6d" % accelleration_xout), " scaled: ", accelleration_xout_scaled)
    print("accelleration_yout: ", ("%6d" % accelleration_yout), " scaled: ", accelleration_yout_scaled)
    print("accelleration_zout: ", ("%6d" % accelleration_zout), " scaled: ", accelleration_zout_scaled)
    
    print("X Rotation: " , get_x_rotation(accelleration_xout_scaled, accelleration_yout_scaled, accelleration_zout_scaled))
    print("Y Rotation: " , get_y_rotation(accelleration_xout_scaled, accelleration_yout_scaled, accelleration_zout_scaled))

    sleep(.5)
