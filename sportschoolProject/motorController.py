#importeer de benodigde libraries
import serial
import struct
import time

def openDoor():
    data = serial.Serial('com6', 9600, timeout=1)
    data.write(struct.pack('>B', 90))
    time.sleep(5)
    data.write(struct.pack('>B', 0))