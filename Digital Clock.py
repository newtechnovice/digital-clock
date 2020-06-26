import tkinter as tk
import datetime
import time

x = datetime.datetime.now()

window = tk.Tk()
window.title("Digital Clock")

canvas = tk.Canvas(window, height=200, width=500)
canvas.pack()

frame = tk.Canvas(window, bg='#696969')
frame.place(relx=0, rely=0, relheight=1, relwidth=1)


def get_time():
    hour_min = time.strftime("%H:%M")
    clock.config(text=hour_min)
    clock.after(200, get_time)


clock = tk.Label(frame, fg="#8FBC8F", bg='#696969', font="Verdana 110", anchor="nw")
clock.place(relx=0.05, rely=0.15, relheight=0.6, relwidth=0.7)

get_time()


def get_second():
    sec = time.strftime("%S")
    second.config(text=sec)
    second.after(200, get_second)


second = tk.Label(frame, fg="#8FBC8F", bg='#696969', font="Verdana 30", anchor="nw")
second.place(relx=0.7, rely=0.55, relheight=0.3, relwidth=0.1)

get_second()

month = tk.Label(frame, fg='#BDB76B', bg='#696969', text="MONTH", font="Verdana 15")
month.place(relx=0.790, rely=0.1, relheight=0.15, relwidth=0.2)

b = tk.Label(frame, fg='#8FBC8F', bg='#696969', text=x.strftime("%b"), font="Verdana 25 bold")
b.place(relx=0.790, rely=0.230, relheight=0.15, relwidth=0.2)

date = tk.Label(frame, fg='#BDB76B', bg='#696969', text="DATE", font="Verdana 15")
date.place(relx=0.790, rely=0.380, relheight=0.15, relwidth=0.2)

d = tk.Label(frame, fg='#8FBC8F', bg='#696969', text=x.strftime("%d"), font="Verdana 25 bold")
d.place(relx=0.790, rely=0.51, relheight=0.15, relwidth=0.2)

day = tk.Label(frame, fg='#BDB76B', bg='#696969', text="DAY", font="Verdana 15")
day.place(relx=0.790, rely=0.650, relheight=0.15, relwidth=0.2)

a = tk.Label(frame, fg='#8FBC8F', bg='#696969', text=x.strftime("%a"), font="Verdana 25 bold")
a.place(relx=0.790, rely=0.77, relheight=0.15, relwidth=0.2)

window.mainloop()