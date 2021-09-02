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
traytxt1 = "AA" #Initial tray of the run. Temporary variable: should be replaced with traytxt from setup parameters
tray1 = traytxt1 #String that holds tray alphanumerics
tray2 = "AB" #These trays are just examples. Each one should have its own corresponding traytxt(number) derived from the setup parameters
tray3 = "AC"
tray4 = "AD"
tray5 = "AE"
cupnumber = 1 #Initial cup of the run. Temporary variable: Should be replaced with cupnumber from setup parameters
cup = '{0:05d}'.format(cupnumber) #Formats cup number properly
filename = tray1 + cup + "_" + dt + ".txt" #collates the information into the proper file name
file = open(r"./Data_testing/"+filename, "w") #Creates a file with the correct name
file.write("***********************************\n") #This and the next few lines create the header for the text file
file.write("        Weight Data File\n")
file.write("***********************************\n")
file.write("\n")
file.write("Sample, Weight\n")
file.write("\n")
for x in range(3):
    for y in range(12):
        file.write(tray1 + cup + ",  " + sampletext[x][y] + "\n")
        cupnumber = cupnumber + 1
        cup = '{0:05d}'.format(cupnumber)
for x in range(3, 6):
    for y in range(12):
        file.write(tray2 + cup + ",  " + sampletext[x][y] + "\n")
        cupnumber = cupnumber + 1
        cup = '{0:05d}'.format(cupnumber)
for x in range (6, 9):
    for y in range(12):
        file.write(tray3 + cup + ",  " + sampletext[x][y] + "\n")
        cupnumber = cupnumber + 1
        cup = '{0:05d}'.format(cupnumber)
for x in range(9, 12):
    for y in range(12):
        file.write(tray4 + cup + ",  " + sampletext[x][y] + "\n")
        cupnumber = cupnumber + 1
        cup = '{0:05d}'.format(cupnumber)
for x in range (12, 15):
    for y in range(12):
        file.write(tray5 + cup + ",  " + sampletext[x][y] + "\n")
        cupnumber = cupnumber + 1
        cup = '{0:05d}'.format(cupnumber)
