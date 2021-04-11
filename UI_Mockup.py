import serial
import tkinter as tk
import math
import random

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.tray = tk.Canvas(self, width = "1000", height = "700")
        self.tray.pack()
        self.buttonfont = "Helvetica 24"
        self.buttonfontmain = "Helvetica 36"

        self.samples = [[0 for x in range(12)] for x in range(15)]
        self.sampletext = [[0 for x in range(12)] for x in range(15)]

        for x in range(15):
            for y in range(12):
                self.samples[x][y] = self.tray.create_oval((200 * math.floor(x/3)) + (55 * (x % 3)) + 5, 55 * y + 5, (200 * math.floor(x/3)) + (55 * (x % 3)) + 55, 55 * y + 55, fill = "gray")
                self.sampletext[x][y] = self.tray.create_text((200 * math.floor(x/3)) + (55 * (x % 3)) + 30, 55 * y + 30, text = "0", justify = tk.CENTER, font = "Helvetica 16")

        self.run = tk.Button(self, font = self.buttonfont)
        self.run["text"] = "Run"
        self.run["command"] = self.run_button
        self.run.pack(side="left")

        self.pause = tk.Button(self, font = self.buttonfont)
        self.pause["text"] = "Pause"
        self.pause.pack(side="left")

        self.terminate = tk.Button(self, font = self.buttonfont)
        self.terminate["text"] = "Terminate"
        self.terminate["command"] = self.term_button
        self.terminate.pack(side="left")

        self.setup = tk.Button(self, font = self.buttonfont)
        self.setup["text"] = "Setup Parameters"
        self.setup["command"] = self.setup_param
        self.setup.pack(side="left")


    def term_button(self):
        for x in range(15):
            for y in range(12):
                self.tray.itemconfig(self.samples[x][y], fill = "gray")
                self.tray.itemconfig(self.sampletext[x][y], text = "0")

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
        for x in range(15):
            for y in range(12):
                weight = round(random.gauss(50, 5), 2)
                color = "green"
                if weight < 45:
                    color = "red"
                elif weight > 55:
                    color = "blue"
                self.tray.itemconfig(self.samples[x][y], fill = color)
                self.tray.itemconfig(self.sampletext[x][y], text = str(weight))

root = tk.Tk()
root.geometry("1100x800")
robot = serial.Serial()
robot.port = 'COM3'
robot.baudrate = 9600
robot.open()
app = Application(master=root)
app.mainloop()
