#This file is meant to test the robot's data output functionality
import serial
import tkinter as tk
import math
import random
import threading
import time
import datetime
from datetime import datetime

sampletext = [[0 for x in range(12)] for x in range(15)] #12 by 15 matrix from the UI code


for x in range(15):
    for y in range(12):
        sampletext[x][y] = round(random.gauss(50, 5), 2) #Fills matrix with random dummy data

now = datetime.now()

print(now)
dt = now.strftime("%y_%m_%d Time_%Hh%Mm%Ss")

print(dt)


print(sampletext[0][1])
#filename =
