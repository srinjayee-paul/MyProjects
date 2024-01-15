from tkinter import *

root=Tk()
root.title("CountdownTimer")
root.geometry("455x585")
root.resizable(0,0)
root.config(bg="gray")
l1=Label(root, text="COUNTDOWN", bg="gray", fg="black", font=("Candara 48 underline bold"))
l1.place(x=35,y=0)
l2=Label(root, text="TIMER", bg="gray", fg="black", font=("Candara 48 underline bold"))
l2.place(x=130,y=70)

hr=StringVar()
mins=StringVar()
sec=StringVar()
hr.set("0")
mins.set("0")
sec.set("0")

e1=Entry(root, textvariable=hr, font=("Times_New_Roman 48"), width=3, justify=RIGHT)
e1.place(x=35,y=170)
l3=Label(root, text=":",bg="gray", fg="black", font=("Candara 40 bold"))
l3.place(x=150,y=170)
e2=Entry(root, textvariable=mins, font=("Times_New_Roman 48"), width=3, justify=RIGHT)
e2.place(x=170,y=170)
l4=Label(root, text=":",bg="gray", fg="black", font=("Candara 40 bold"))
l4.place(x=285,y=170)
e3=Entry(root, textvariable=sec, font=("Times_New_Roman 48"), width=3, justify=RIGHT)
e3.place(x=305,y=170)

l5=Label(root, text="Hours", width=8, bg="gray", fg="black", font=("Candara 20"))
l5.place(x=30,y=240)
l6=Label(root, text="Minutes", width=8, bg="gray", fg="black", font=("Candara 20"))
l6.place(x=165,y=240)
l7=Label(root, text="Seconds", width=8, bg="gray", fg="black", font=("Candara 20"))
l7.place(x=295,y=240)

def submit():
    global run
    run=True
    start()

def start():
    global ini_x
    x=int(hr.get())*3600+int(mins.get())*60+int(sec.get())
    ini_x=x
    while x>=0:
        if run==True:
            cal(x)
            root.after(1000)
            root.update()
        else:
            break
        x-=1
       
def cal(x):
    f_hr=x//(60*60)
    hr_rem=x%(60*60)
    f_min=hr_rem//60
    f_sec=hr_rem%60
    hr.set(str(f_hr))
    mins.set(str(f_min))
    sec.set(str(f_sec))

def reset():
    global run
    run=False
    hr.set("0")
    mins.set("0")
    sec.set("0")
    root.update()

def stop():
    global run
    run=False
    cal(ini_x)
    root.update()

def pause():
    global run
    run=False   

def resume():
    global run
    run=True 
    submit()

b1=Button(root, text="Set Time Countdown", bg="gray70", font=("Times_New_Roman 18"), width=20, command=lambda:submit())
b1.place(x=80,y=310)
b2=Button(root, text="Reset", bg="gray70", font=("Times_New_Roman 18"), width=10, command=lambda:reset())
b2.place(x=60,y=400)
b3=Button(root, text="Stop", bg="gray70", font=("Times_New_Roman 18"), width=10, command=lambda:stop())
b3.place(x=60,y=470)
b4=Button(root, text="Pause", bg="gray70", font=("Times_New_Roman 18"), width=10, command=lambda:pause())
b4.place(x=240,y=400)
b5=Button(root, text="Resume", bg="gray70", font=("Times_New_Roman 18"), width=10, command=lambda:resume())
b5.place(x=240,y=470)

root.mainloop()