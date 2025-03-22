from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
xy=Tk()
xy.title('StudEase')
xy.geometry("1000x600")
xy.resizable(0,0)
img2=Image.open("C:\\Users\\Sneha\\Pictures\\Saved Pictures\\backgrd.png")
img1=ImageTk.PhotoImage(img2)
label1=Label(xy, image=img1)
label1.place(x=0,y=0)
label2=Label(xy, text="STUD EASE",fg="royal blue",bg="gray75",font=("Broadway",56, "underline","bold"),width=20)
label2.place(x=0,y=0)
label3=Label(xy, text="'Online Education At One Place'",bg="gray75",fg="orange red", font=("Times 30 underline italic"),width=48)
label3.place(x=0,y=90)
img3 =Image.open("C:\\Users\\Sneha\\Pictures\\Saved Pictures\\logonew2.png")  
img4 = ImageTk.PhotoImage(img3)
label1=Label(xy, image=img4, bg="gray75",height=140)
label1.place(x=0,y=0)

def page1():
    import pymysql as pm
    mydb=pm.connect(host="localhost", user="root", passwd="sneha_15")
    mycur=mydb.cursor()
    mycur.execute("use project2022")
    mydb.commit()

    stu_pg=Tk()
    stu_pg.title('student info')
    stu_pg.geometry("1000x600")
    stu_pg.resizable(0,0)
    stu_pg.configure(bg="salmon1")
    label1=Label(stu_pg,text="STUDENT INFO",bg="salmon1",fg="ORANGERED4",font=("Copperplate Gothic Bold",36,"underline"))
    label1.place(x=320, y=0)
    
    l1=Label(stu_pg,text="STUDENT NAME",bg="peach puff",fg="gray16",font=("Candara",15,"bold"),width=14)
    l1.place(x=100, y=80)
    l2=Label(stu_pg,text="EMAIL",bg="peach puff",fg="gray16",font=("Candara",15,"bold"),width=14)
    l2.place(x=100, y=140)
    l3=Label(stu_pg,text="PHONE NO.",bg="peach puff",fg="gray16",font=("Candara",15,"bold"),width=14)
    l3.place(x=100, y=200)
    l4=Label(stu_pg,text="COURSE1",bg="peach puff",fg="gray16",font=("Candara",15,"bold"),width=14)
    l4.place(x=100, y=260)
    l5=Label(stu_pg,text="COURSE2",bg="peach puff",fg="gray16",font=("Candara",15,"bold"),width=14)
    l5.place(x=100, y=320)
    l6=Label(stu_pg,text="COURSE3",bg="peach puff",fg="gray16",font=("Candara",15,"bold"),width=14)
    l6.place(x=100, y=380)
    l7=Label(stu_pg,text="COURSE TYPE",bg="peach puff",fg="gray16",font=("Candara",15,"bold"),width=14)
    l7.place(x=100, y=440)

    name=StringVar(stu_pg)
    mail=StringVar(stu_pg)
    phone=StringVar(stu_pg)
    course1=StringVar(stu_pg)
    course2=StringVar(stu_pg)
    course3=StringVar(stu_pg)
    course_type=StringVar(stu_pg)
    
    ent1=Entry(stu_pg,textvariable = name, font=('Times New Roman',15), width=60)
    ent1.place(x=300,y=80)
    ent1.insert(0, "Enter your name")
    ent2=Entry(stu_pg,textvariable = mail, font=('Times New Roman',15), width=60)
    ent2.place(x=300,y=140)
    ent2.insert(0, "Enter your email")
    ent3=Entry(stu_pg,textvariable = phone, font=('Times New Roman',15), width=60)
    ent3.place(x=300,y=200)
    ent3.insert(0,"Enter phone no.")
    ent4=Entry(stu_pg,textvariable = course1,font=('Times New Roman',15), width=60) 
    ent4.place(x=300,y=260)
    ent4.insert(0,"Enter Course1 (Eg. JEE XII, UPSC, etc.)")
    ent5=Entry(stu_pg,textvariable = course2,font=('Times New Roman',15), width=60) 
    ent5.place(x=300,y=320)
    ent5.insert(0,"Enter Course2 (Eg. JEE XII, UPSC, etc.)")
    ent6=Entry(stu_pg,textvariable = course3,font=('Times New Roman',15), width=60) 
    ent6.place(x=300,y=380)
    ent6.insert(0,"Enter Course3 (Eg. JEE XII, UPSC, etc.)")
    ent7=OptionMenu(stu_pg, course_type,"PRIVATE","BATCH","GROUP")
    menu = stu_pg.nametowidget(ent7)
    menu.config(font=('Times New Roman',15),width=56)
    ent7.place(x=300,y=440)
    
    b1=Button(stu_pg,text ="Submit",bg="slate grey",fg="yellow",bd=15,font=("Courier",15,"bold"),width=15, command="savedata")
    b1.place(x=250,y=500)
    b2=Button(stu_pg,text ="Show database",bg="slate grey",fg="yellow",bd=15,font=("Courier",15,"bold"),width=15, command=page3)
    b2.place(x=550,y=500)
    
    stu_pg.mainloop()
    
    values=(name.get(),mail.get(),phone.get(),course1.get(),course2.get(),course3.get(),course_type.get())
    sql="insert into student_table values(%s,%s,%s,%s,%s,%s,%s)"
    mycur.execute(sql,values)
    mydb.commit()
    
def page2():
    import pymysql as pm
    mydb=pm.connect(host="localhost", user="root", passwd="sneha_15")
    mycur=mydb.cursor()
    mycur.execute("use project2022")
    mydb.commit()
    
    onl_pg=Tk()
    onl_pg.title('Teaching Info')
    onl_pg.geometry("1000x600")
    onl_pg.resizable(0,0)
    onl_pg.configure(bg="steelblue")
    l2=Label(onl_pg,text="ONLINE PLATFORM INFO",bg="steelblue",fg="cyan",font=("Copperplate Gothic Bold",36,"underline"))
    l2.place(x=200, y=0)
    
    l1=Label(onl_pg,text="Teacher/Platform Name",bg="sky blue",fg="gray16",font=("Candara",15,"bold"),width=20)
    l1.place(x=100, y=100)
    l2=Label(onl_pg,text="Course Name",bg="sky blue",fg="gray16",font=("Candara",15,"bold"),width=20)
    l2.place(x=100, y=180)
    l3=Label(onl_pg,text="Course Details",bg="sky blue",fg="gray16",font=("Candara",15,"bold"),width=20)
    l3.place(x=100, y=260)
    l4=Label(onl_pg,text="Price",bg="sky blue",fg="gray16",font=("Candara",15,"bold"),width=20)
    l4.place(x=100, y=340)
    l5=Label(onl_pg,text="Course Type",bg="sky blue",fg="gray16",font=("Candara",15,"bold"),width=20)
    l5.place(x=100, y=420)
    
    t_name=StringVar(onl_pg)
    co_name=StringVar(onl_pg)
    co_det=StringVar(onl_pg)
    price=StringVar(onl_pg)
    co_type=StringVar(onl_pg)
    
    ent1=Entry(onl_pg,textvariable = t_name,font=('Times New Roman',15), width=55)
    ent1.place(x=350,y=100)
    ent1.insert(0, "Enter your platform name")
    ent2=Entry(onl_pg,textvariable = co_name,font=('Times New Roman',15), width=55)
    ent2.place(x=350,y=180)
    ent2.insert(0, "Enter course name")
    ent3=Entry(onl_pg,textvariable = co_det, font=('Times New Roman',15), width=55)
    ent3.place(x=350,y=260)
    ent3.insert(0, "Enter details (Eg. class, duration)")
    ent4=Entry(onl_pg,textvariable = price,font=('Times New Roman',15), width=55) 
    ent4.place(x=350,y=340)
    ent4.insert(0, "Enter price")
    ent5=OptionMenu(onl_pg, co_type,"PRIVATE","BATCH","GROUP")
    menu = onl_pg.nametowidget(ent5)
    menu.config(font=('Times New Roman',15),width=50)
    ent5.place(x=350,y=420)
   
    b1=Button(onl_pg,text ="Submit",bg="slate grey",fg="yellow",bd=15,font=("Courier",15,"bold"),width=15, command="savedata")
    b1.place(x=250,y=500)
    b2=Button(onl_pg,text ="Show database",bg="slate grey",fg="yellow",bd=15,font=("Courier",15,"bold"),width=15, command=page3)
    b2.place(x=550,y=500)
    
    onl_pg.mainloop()
    
    values=(t_name.get(),co_name.get(),co_det.get(),price.get(),co_type.get())
    sql="insert into teacher_table values(%s,%s,%s,%s,%s)"
    mycur.execute(sql,values)
    mydb.commit()
 
def page3():
     import pymysql as pm
     mydb=pm.connect(host="localhost", user="root", passwd="sneha_15")
     mycur=mydb.cursor()
     mycur.execute("use project2022")
     mydb.commit()
     
     se_rch=Tk()
     se_rch.title('SEARCH')
     se_rch.geometry("1000x600")
     se_rch.resizable(0,0)
     se_rch.configure(bg="khaki")
     
     mycur.execute("select * from teacher_table")
     x=1
     for i in mycur:
         for j in range(len(i)):
             l1=Label(se_rch,text=i[j])
             l1.config(font=('Times New Roman',12),width=22,bd=4,bg="dark khaki")
             l1.grid(row=x, column=j) 
         x=x+1
         
     se_rch.mainloop()

btn2=Button(xy,text ="REGISTER TEACHER",bg="slate grey",fg="yellow",bd=20,command=page2,font=("Courier",15,"italic"),width=18)
btn2.place(x=200,y=230)
   
btn1=Button(xy,text ="REGISTER STUDENT",bg="slate grey",fg="yellow",bd=20,command=page1,font=("Courier",15,"italic"),width=18)
btn1.place(x=550,y=230)

xy.mainloop()
