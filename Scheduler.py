from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import datetime

def validate_spinbox(a, b, c):
    val1 = int(a.get())
    val2 = int(b.get())
    val3 = int(c.get())
    if (val1>=0 and val1<=99) and (val2>=0 and val2<60) and (val3>=0 and val1<60):
        total_time = (val1*3600)+(val2*60)+val3
        os.system(f'shutdown /s /t {total_time}')
        timeshutdown = datetime.datetime.now()
        timedate = timeshutdown.day
        timehour = timeshutdown.hour
        timeminute = timeshutdown.minute
        timesecond = timeshutdown.second
        timemonth = timeshutdown.month
        timeyear = timeshutdown.year
        if (timesecond+val3)>=60:
            timeminute+= (timesecond+val3)//60
            timesecond = (timesecond+val3)%60
        else:
            timesecond = timesecond+val3
        if (timeminute+val2)>=60:
            timehour+= (timeminute+val2)//60
            timeminute = (timeminute+val2)%60
        else:
            timeminute = timeminute+val2
        if timehour+val1>=24:
            timedate+=(timehour+val1)//24
            timehour = (timehour+val1)%24
        else:
            timehour = timehour+val1
        messagebox.showinfo(title = 'Shut Down Scheduled!', message = f'Your System Will Shutdown At:{timedate}//{timemonth}//{timeyear} {timehour}:{timeminute}:{timesecond}')
    else:
        messagebox.showerror(title='Time Error!',message='Please Choose Time Within The Given Limits to Prevent any Overload')

def abortshutdown():
    confirmation = messagebox.askyesno('Confirm!','Do You Want To Abort The Shut Down?')
    print(confirmation)
    if confirmation:
        os.system('shutdown /a')

root = Tk()
root.geometry("800x600+380+110")
root.title("Scheduler")
var1 = IntVar()
var1.set(1)
var2 = IntVar()
var3 = IntVar()
hourButton = Spinbox(root, width=20, textvariable=var1, increment=1, from_=0, to=99, validate='all')
hourButton.pack()
minuteButton = Spinbox(root, width=20, textvariable=var2, increment=1, from_=0, to=99, validate='all')
minuteButton.pack()
secondsButton = Spinbox(root, width=20, textvariable=var3, increment=1, from_=0, to=99, validate='all')
secondsButton.pack()
mainCheckButton = ttk.Button(root, text = 'Set Timer', command = lambda:[validate_spinbox(hourButton, minuteButton, secondsButton)])
mainCheckButton.pack()
abortButton = ttk.Button(root, text = 'Abort Shutdown',command=lambda:[abortshutdown()])
abortButton.pack()
root.mainloop()