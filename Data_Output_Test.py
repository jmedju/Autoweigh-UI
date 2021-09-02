#This file is meant to test the robot's data output functionality
import serial
import tkinter as tk
import math
import random
import threading
import time
import datetime
from datetime import datetime

samples = [[0 for x in range(12)] for x in range(15)]
sampletext = [[0 for x in range(12)] for x in range(15)]


for x in range(15):
    for y in range(12):
        #self.samples[x][y] = self.tray.create_oval((200 * math.floor(x/3)) + (55 * (x % 3)) + 5, 55 * y + 5, (200 * math.floor(x/3)) + (55 * (x % 3)) + 55, 55 * y + 55, fill = "gray")
        sampletext[x][y] = (200 * math.floor(x/3)) + (55 * (x % 3)) + 30, 55 * y + 30

now = datetime.now()

print(now)
dt = now.strftime("%y_%m_%d Time_%Hh%Mm%Ss")

print(dt)

#filename =
