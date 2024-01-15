from tkinter import *
import math
root=Tk()
root.title("Calculator")
root.geometry("455x585")
root.resizable(0,0)
root.config(bg="gray")

l1=Label(root, text="CALCULATOR",bg="gray",fg="black", font=("Candara 48 underline bold"))
l1.place(x=40,y=0)

b1=Button(root, text="7", bg="gray70", font=("Times_New_Roman 18"), width=5, command=lambda:e1.insert(END,7))
b1.place(x=40,y=330)
b2=Button(root, text="8", bg="gray70", font=("Times_New_Roman 18"), width=5, command=lambda:e1.insert(END,8))
b2.place(x=140,y=330)
b3=Button(root, text="9", bg="gray70", font=("Times_New_Roman 18"), width=5, command=lambda:e1.insert(END,9))
b3.place(x=240,y=330)
b4=Button(root, text="x", bg="gray70", font=("Times_New_Roman 18"), width=5, command=lambda:mul(x))
b4.place(x=340,y=330)
b5=Button(root, text="4", bg="gray70", font=("Times_New_Roman 18"), width=5, command=lambda:e1.insert(END,4))
b5.place(x=40,y=390)
b6=Button(root, text="5", bg="gray70", font=("Times_New_Roman 18"), width=5, command=lambda:e1.insert(END,5))
b6.place(x=140,y=390)
b7=Button(root, text="6", bg="gray70", font=("Times_New_Roman 18"), width=5, command=lambda:e1.insert(END,6))
b7.place(x=240,y=390)
b8=Button(root, text="–", bg="gray70", font=("Times_New_Roman 18"), width=5, command=lambda:sub(x))
b8.place(x=340,y=390)
b9=Button(root, text="1", bg="gray70", font=("Times_New_Roman 18"), width=5, command=lambda:e1.insert(END,1))
b9.place(x=40,y=450)
b10=Button(root, text="2", bg="gray70", font=("Times_New_Roman 18"), width=5, command=lambda:e1.insert(END,2))
b10.place(x=140,y=450)
b11=Button(root, text="3", bg="gray70", font=("Times_New_Roman 18"), width=5, command=lambda:e1.insert(END,3))
b11.place(x=240,y=450)
b12=Button(root, text="+", bg="gray70", font=("Times_New_Roman 18"), width=5, command=lambda:add(x))
b12.place(x=340,y=450)
b13=Button(root, text="+/–", bg="gray70", font=("Times_New_Roman 18"), width=5, command=lambda:negative(x))
b13.place(x=40,y=510)
b14=Button(root, text="0", bg="gray70", font=("Times_New_Roman 18"), width=5, command=lambda:e1.insert(END,0))
b14.place(x=140,y=510)
b15=Button(root, text=".", bg="gray70", font=("Times_New_Roman 18"), width=5, command=lambda:decimal(x))
b15.place(x=240,y=510)
b16=Button(root, text="=", bg="gray70", font=("Times_New_Roman 18"), width=5, command=lambda:equal(x))
b16.place(x=340,y=510)
b17=Button(root, text="1/x", bg="gray70", font=("Times_New_Roman 18"), width=5, command=lambda:reciprocal(x))
b17.place(x=40,y=270)
b18=Button(root, text="x²", bg="gray70", font=("Times_New_Roman 18"), width=5, command=lambda:square(x))
b18.place(x=140,y=270)
b19=Button(root, text="√x ", bg="gray70", font=("Times_New_Roman 18"), width=5, command=lambda:square_root(x))
b19.place(x=240,y=270)
b20=Button(root, text="÷", bg="gray70", font=("Times_New_Roman 18"), width=5, command=lambda:div(x))
b20.place(x=340,y=270)
b21=Button(root, text="%", bg="gray70", font=("Times_New_Roman 18"), width=5)
b21.place(x=40,y=210)
b22=Button(root, text="CE", bg="gray70", font=("Times_New_Roman 18"), width=5, command=lambda:clear_entry(x))
b22.place(x=140,y=210)
b23=Button(root, text="C", bg="gray70", font=("Times_New_Roman 18"), width=5, command=lambda:clear(x))
b23.place(x=240,y=210)
b24=Button(root, text="⌫", bg="gray70", font=("Times_New_Roman 18"), width=5, command=lambda:back_space(x))
b24.place(x=340,y=210)

x=StringVar(root)
result=0
string=""
e1=Entry(root, textvariable=x, font=("Times_New_Roman 28"), width=18, justify=RIGHT)
e1.place(x=40,y=140)
l2=Label(root,bg="gray80", text=string, font=("Times_New_Roman 18"), width=27, anchor="e")
l2.place(x=40,y=90)

def cal(string):
    global result
    s=""
    for i in string:
        if i=="x":
            s+="*"
        elif i=="÷":
            s+="/"
        else:
            s+=i
    s1=s[:-1]
    result=eval(s1)

def decimal(x):
    val=x.get()
    if val=="":
        e1.insert(END,"0.")
    else:
        e1.insert(END,".")
    
def add(x):
    global result
    global string
    val=x.get()
    st=val+"+"
    if result==0:
        result=float(val)
        string=st
    else:
        if "=" in string:
            string=str(result)+"+"
        else:
            string+=st
            cal(string)
            string=str(result)+"+"
    e1.delete(0,END)
    l2.config(text=string)
    
def sub(x):
    global result
    global string
    val=x.get()
    st=val+"-"
    if result==0:
        result=float(val)
        string=st
    else:
        if "=" in string:
            string=str(result)+"-"
        else:
            string+=st
            cal(string)
            string=str(result)+"-"
    e1.delete(0,END)
    l2.config(text=string)

def mul(x):
    global result
    global string
    val=x.get()
    st=val+"x"
    if result==0:
        result=float(val)
        string=st
    else:
        if "=" in string:
            string=str(result)+"x"
        else:
            string+=st
            cal(string)
            string=str(result)+"x"
    e1.delete(0,END)
    l2.config(text=string)

def div(x):
    global result
    global string
    val=x.get()
    st=val+"÷"
    if result==0:
        result=float(val)
        string=st
    else:
        if "=" in string:
            string=str(result)+"÷"
        else:
            string+=st
            cal(string)
            string=str(result)+"÷"
    e1.delete(0,END)
    l2.config(text=string)
    
def equal(x):
    global result
    global string
    val=x.get()
    st=val+"="
    string+=st
    cal(string)
    e1.delete(0,END)
    e1.insert(0,result)
    l2.config(text=string)

def square(x):
    global string
    global result
    val=x.get()
    st="sqr("+val+")"
    r=float(val)**2
    if result==0:
        l2.config(text=st)
    else:
        st1=string+st
        l2.config(text=st1)
    e1.delete(0,END)
    e1.insert(0,r)

def square_root(x):
    global string
    global result
    val=x.get()
    st="√"+val
    r=math.sqrt(float(val))
    if result==0:
        l2.config(text=st)
    else:
        st1=string+st
        l2.config(text=st1)
    e1.delete(0,END)
    e1.insert(0,r)

def reciprocal(x):
    global result
    global string
    val=x.get()
    st="1/"+val
    r=1/float(val)
    if result==0:
        l2.config(text=st)
    else:
        st1=string+st
        l2.config(text=st1)
    e1.delete(0,END)
    e1.insert(0,r)

def negative(x):
    e1.insert(0,"-")
        
def clear(x):
    global result
    global string
    result=0
    string=""
    e1.delete(0,END)
    l2.config(text=string)

def clear_entry(x):
    e1.delete(0,END)

def back_space(x):
    val=x.get()
    e1.delete(len(val)-1,END)

root.mainloop()