#Hayden Whitney
#9/18
#Clock

from tkinter import*
from tkinter import ttk
from tkinter import font
import time
import calendar
import datetime

def gmtnow():
    total_seconds = calendar.timegm(time.gmtime())
    current_second = total_seconds % 60
    total_minutes = total_seconds //60
    current_minute = total_minutes % 60
    total_hours = total_minutes // 60
    current_hour = total_hours % 24
    current_hour = current_hour - 6
    if current_hour >= 12:
        tag = " PM"
    else:
        tag = " AM"
    timex = str(current_hour) + ":" + str(current_minute) + ":" + str(current_second) + tag
    return timex

def quit(*args):
    root.destroy()

def show_time():
    time = gmtnow()
    txt.set(time)
    root.after(1000, show_time)

root = Tk()
root.attributes("-fullscreen", False)
root.configure(background = 'White')
root.bind("x", quit)
root.after(1000, show_time)

fnt = font.Font(family = 'Courier', size = 60)
txt = StringVar()
lbl = ttk.Label(root, textvariable = txt, font = fnt, foreground = 'Black', background = 'White')
lbl.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()

    



