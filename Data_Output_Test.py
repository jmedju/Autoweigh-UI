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
        sampletext[x][y] = str(round(random.gauss(50, 5), 2)) #Fills matrix with random dummy data

now = datetime.now() #Gets the date and time
dt = now.strftime("%y_%m_%d Time_%Hh%Mm%Ss") #Formats dte and time for filename purposes

traytxt = "AA"
tray = traytxt #String that holds tray alphanumerics
startcupnumber = 12 #First cup
cup = '{0:05d}'.format(startcupnumber) #Formats cup number properly

print(sampletext[0][1])
filename = tray + cup + "_" + dt + ".txt" #collates the information into the proper file name


file2 = open(r"./Data_Testing/"+filename, "w") 
print(filename)
