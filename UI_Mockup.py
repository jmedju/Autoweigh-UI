import serial
import tkinter as tk
import math
import random
import threading
import time

robot = serial.Serial()
robot.port = 'COM7'
robot.baudrate = 9600
robot.open()

xposarray = [0, 1270, 2600]
yposarray = [0, 1440, 2880, 4390, 5900, 7410, 8920, 10430, 11920, 13470, 14980, 16590]


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.pauseflag = False
        self.termflag = False

    def create_widgets(self):
        self.tray = tk.Canvas(self, width = "1000", height = "900")
        self.tray.pack()
        self.buttonfont = "Helvetica 24"
        self.buttonfontmain = "Helvetica 36"


        self.run = tk.Button(self, font = self.buttonfont)
        self.run["text"] = "Run"
        self.run["command"] = self.run_button
        self.run.place(x = 5, y = 700)

        self.pause = tk.Button(self, font = self.buttonfont)
        self.pause["text"] = "Pause"
        self.pause["command"] = self.pause_button
        self.pause.place(x = 105, y = 700)

        self.terminate = tk.Button(self, font = self.buttonfont)
        self.terminate["text"] = "Terminate"
        self.terminate["command"] = self.term_button
        self.terminate.place(x = 235, y = 700)

        self.calibrate = tk.Button(self, font = self.buttonfont)
        self.calibrate["text"] = "Calibrate"
        self.calibrate["command"] = self.term_button
        self.calibrate.place(x = 415, y = 700)

        self.maintenance = tk.Button(self, font = self.buttonfont)
        self.maintenance["text"] = "Maintenance"
        self.maintenance["command"] = self.term_button
        self.maintenance.place(x = 5, y = 800)

        self.setup = tk.Button(self, font = self.buttonfont)
        self.setup["text"] = "Setup Parameters"
        self.setup["command"] = self.setup_param
        self.setup.place(x = 230, y = 800)

        self.samples = [[0 for x in range(12)] for x in range(15)]
        self.sampletext = [[0 for x in range(12)] for x in range(15)]

        for x in range(15):
            for y in range(12):
                self.samples[x][y] = self.tray.create_oval((200 * math.floor(x/3)) + (55 * (x % 3)) + 5, 55 * y + 5, (200 * math.floor(x/3)) + (55 * (x % 3)) + 55, 55 * y + 55, fill = "gray")
                self.sampletext[x][y] = self.tray.create_text((200 * math.floor(x/3)) + (55 * (x % 3)) + 30, 55 * y + 30, text = "0", justify = tk.CENTER, font = "Helvetica 16")


    def term_button(self):
        self.termflag = True

    def pause_button(self):
        if(self.pauseflag):
            self.pauseflag = False
        else:
            self.pauseflag = True

    def write_to_sample(self, x, y):
        weight = round(random.gauss(50, 5), 2)
        color = "green"
        if weight < 45:
            color = "red"
        elif weight > 55:
            color = "blue"
        self.tray.itemconfig(self.samples[x][y], fill = color)
        self.tray.itemconfig(self.sampletext[x][y], text = str(weight))

    def robotSer(self):
        x = 0
        y = 0
        xpos = 0
        ypos = 0
        i = 0
        robot.reset_input_buffer()
        cmd = bytes('rr', 'utf-8')
        robot.write(cmd)

        s = robot.read().decode('utf-8')
        while(True):
            while(self.pauseflag):
                time.sleep(.5)
                if(self.termflag):
                    if(i > 2):
                        cmd = bytes('hh', 'utf-8')
                        robot.write(cmd)
                    for x in range(15):
                        for y in range(12):
                            self.tray.itemconfig(self.samples[x][y], fill = "gray")
                            self.tray.itemconfig(self.sampletext[x][y], text = "0")
                    self.termflag = False
                    self.pauseflag = False
                    return
            if(self.termflag):
                if(i > 2):
                    cmd = bytes('hh', 'utf-8')
                    robot.write(cmd)
                for x in range(15):
                    for y in range(12):
                        self.tray.itemconfig(self.samples[x][y], fill = "gray")
                        self.tray.itemconfig(self.sampletext[x][y], text = "0")
                self.termflag = False
                return
            cmdstring = 'hh'
            xmove = xposarray[x] - xpos
            ymove = yposarray[y] - ypos
            if(i == 0 and xmove == 0):
                i = 1

            if(i == 1 and ymove == 0):
                i = 2

            if(i == 0):
                if(xmove > 0):
                    cmdstring = 'i' + '{0:05d}'.format(xmove)
                else:
                    xmove = -xmove
                    cmdstring = 'k' + '{0:05d}'.format(xmove)
                xpos = xposarray[x]
            elif(i == 1):
                if(ymove > 0):
                    cmdstring = 'j' + '{0:05d}'.format(ymove)
                else:
                    ymove = -ymove
                    cmdstring = 'l' + '{0:05d}'.format(ymove)
                ypos = yposarray[y]
            elif(i == 2):
                cmdstring = 'yy'
            elif(i == 3):
                cmdstring = 'nn'
            cmd = bytes(cmdstring, 'utf-8')
            robot.write(cmd)
            time.sleep(.5)

            s = robot.read().decode('utf-8')
            if(s == 'N'):
                self.write_to_sample(x, y)
                self.write_to_sample(x+3, y)
                self.write_to_sample(x+6, y)
                self.write_to_sample(x+9, y)
                self.write_to_sample(x+12, y)
                if(x >= 2):
                    y = y+1
                    x = 0
                else:
                    x = x+1
                if(y >= 12):
                    cmd = bytes('hh', 'utf-8')
                    robot.write(cmd)
                    s = robot.read().decode('utf-8')
                    cmd = bytes('rr', 'utf-8')
                    robot.write(cmd)
                    return
            while(s != 'D'):
                s = robot.read().decode('utf-8')
            i = i+1
            if(i > 4):
                i = 0

    def setup_param(self):
        popup = tk.Tk();
        popup.wm_title("Setup Parameters")
        popup.geometry("800x360")

        optionList = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
        popup.v = tk.StringVar(popup)
        popup.v.set(optionList[0])

        popup.label = tk.Label(popup,  text='Select Tray Labelling:', font = self.buttonfont)
        popup.label.grid(column=0, row=0)

        popup.alphabetical = tk.OptionMenu(popup, popup.v, *optionList)
        popup.alphabetical.config(font = self.buttonfont)
        popup.alphabetical.grid(column=1, row=0)

        popup.traylabel1 = tk.Label(popup,  text='Select Tray Numbering:', font = self.buttonfont)
        popup.traylabel1.grid(column=0, row=1)
        popup.tray1 = tk.Entry(popup, font = self.buttonfont)
        popup.tray1.grid(column=1, row=1)
        popup.checktray1 = tk.Checkbutton(popup)
        popup.checktray1.grid(column=2, row=1)

        popup.traylabel2 = tk.Label(popup,  text='Select Tray Numbering:', font = self.buttonfont)
        popup.traylabel2.grid(column=0, row=2)
        popup.tray2 = tk.Entry(popup, font = self.buttonfont)
        popup.tray2.grid(column=1, row=2)
        popup.checktray2 = tk.Checkbutton(popup)
        popup.checktray2.grid(column=2, row=2)

        popup.traylabel3 = tk.Label(popup,  text='Select Tray Numbering:', font = self.buttonfont)
        popup.traylabel3.grid(column=0, row=3)
        popup.tray3 = tk.Entry(popup, font = self.buttonfont)
        popup.tray3.grid(column=1, row=3)
        popup.checktray3 = tk.Checkbutton(popup)
        popup.checktray3.grid(column=2, row=3)

        popup.traylabel4 = tk.Label(popup,  text='Select Tray Numbering:', font = self.buttonfont)
        popup.traylabel4.grid(column=0, row=4)
        popup.tray4 = tk.Entry(popup, font = self.buttonfont)
        popup.tray4.grid(column=1, row=4)
        popup.checktray4 = tk.Checkbutton(popup)
        popup.checktray4.grid(column=2, row=4)

        popup.traylabel5 = tk.Label(popup,  text='Select Tray Numbering:', font = self.buttonfont)
        popup.traylabel5.grid(column=0, row=5)
        popup.tray5 = tk.Entry(popup, font = self.buttonfont)
        popup.tray5.grid(column=1, row=5)
        popup.checktray5 = tk.Checkbutton(popup)
        popup.checktray5.grid(column=2, row=5)

        popup.okay = tk.Button(popup, font = self.buttonfont)
        popup.okay["text"] = "Apply"
        popup.okay.grid(column=1,row=6)
        popup.mainloop()

    def run_button(self):
        if(threading.active_count() <= 1):
            serthread = threading.Thread(target = self.robotSer)
            serthread.start()

root = tk.Tk()
root.geometry("1100x900")

app = Application(master=root)
app.mainloop()
