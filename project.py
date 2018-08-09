import sys
from Tkinter import*
def mhello():
    mtext=name.get()
    mlabel=Label(s,text=name).pack()
def sel():
    selection="ypu"+str(var.get())
    label.config(text=selection)


s=Tk()

name=StringVar()
age=IntVar()
gnr=IntVar()
wt=IntVar()
hgt=IntVar()
bpl=IntVar()
bph=IntVar()
plt=IntVar()
rcb=DoubleVar()
wbc=IntVar()
pal=IntVar()
hb=DoubleVar()
uri=DoubleVar()
chl=DoubleVar()
re1=DoubleVar()
abc=IntVar()
def result1():
    
    s.destroy()
    global e
    e=Tk()


    a=plt.get()
    if (a<15000):
        namery=Label(e,text="low").grid(row=11,column=1)
    elif (a>15000 and a<45000):
        namery1=Label(e,text="medium").grid(row=11,column=1)
    else:
        namery2=Label(e,text="high").grid(row=11,column=1)
        
    b=wbc.get()
    if (b<4500):
        namery=Label(e,text="low").grid(row=9,column=1)
    elif (b>=4500 and b<=10000):
        namery1=Label(e,text="medium").grid(row=9,column=1)
    else:
        namery2=Label(e,text="high").grid(row=9,column=1)
        
    c=rcb.get()
    if (c<4.2):
        namery=Label(e,text="low").grid(row=7,column=1)
    elif (c>=4.2 and c<=5.4):
        namery1=Label(e,text="medium").grid(row=7,column=1)
    else:
        namery2=Label(e,text="high").grid(row=7,column=1)
        
    d=bpl.get()
    if (d<80):
        namery=Label(e,text="low").grid(row=3,column=1)
    elif (d>=80 and d<=120):
        namery1=Label(e,text="medium").grid(row=3,column=1)
    else:
        namery2=Label(e,text="high").grid(row=3,column=1)

    g=hb.get()
    if (g<12.0):
        namery=Label(e,text="low").grid(row=13,column=1)
    elif (g>=12.0 and g<=15.5):
        namery1=Label(e,text="medium").grid(row=13,column=1)
    else:
        namery2=Label(e,text="high").grid(row=13,column=1)

    h=uri.get()
    if (h<2.5):
        namery=Label(e,text="low").grid(row=15,column=1)
    elif (h>=2.5 and h<=7.5):
        namery1=Label(e,text="medium").grid(row=15,column=1)
    else:
        namery2=Label(e,text="high").grid(row=15,column=1)

    i=pal.get()
    if (i<60):
        namery=Label(e,text="low").grid(row=5,column=1)
    elif (i>=60 and i<=100):
        namery1=Label(e,text="medium").grid(row=5,column=1)
    else:
        namery2=Label(e,text="high").grid(row=5,column=1)

    

    f=chl.get()
    if (f<40):
        namery=Label(e,text="low").grid(row=17,column=1)
    elif (f>=40 and f<=49):
        namery1=Label(e,text="medium").grid(row=17,column=1)
    else:
        namery2=Label(e,text="high").grid(row=17,column=1)
        




    lable2=Label(e,text='BMI:').grid(row=1,column=0)
    lable2=Label(e,text='BP:').grid(row=3,column=0)
    lable2=Label(e,text='Pulse rate:').grid(row=5,column=0)
    lable2=Label(e,text='RCB Count:').grid(row=7,column=0)
    lable2=Label(e,text='WBC Count:').grid(row=9,column=0)
    lable2=Label(e,text='Platelets:').grid(row=11,column=0)
    lable2=Label(e,text='HB:').grid(row=13,column=0)
    lable2=Label(e,text='Uric Acid:').grid(row=15,column=0)
    lable2=Label(e,text='Cholestrale:').grid(row=17,column=0)

    bm()  
    
    e.geometry('500x500')

def bm():
    hi=hgt.get()
    we=wt.get()
    re1=0.0
    re1=(we/((hi*0.01)**2))
    namery=Label(e,text=re1).grid(row=1,column=1)
def result():
    
    s.destroy()
    global e
    e=Tk()


    a=plt.get()
    if (a<15000):
        namery=Label(e,text="low").grid(row=11,column=1)
    elif (a>15000 and a<45000):
        namery1=Label(e,text="medium").grid(row=11,column=1)
    else:
        namery2=Label(e,text="high").grid(row=11,column=1)
        
    b=wbc.get()
    if (b<4500):
        namery=Label(e,text="low").grid(row=9,column=1)
    elif (b>=4500 and b<=10000):
        namery1=Label(e,text="medium").grid(row=9,column=1)
    else:
        namery2=Label(e,text="high").grid(row=9,column=1)
    c=rcb.get()
    if (c<4.7):
        namery=Label(e,text="low").grid(row=7,column=1)
    elif (c>=4.7 and c<=6.1):
        namery1=Label(e,text="medium").grid(row=7,column=1)
    else:
        namery2=Label(e,text="high").grid(row=7,column=1)
    d=bpl.get()
    if (d<80):
        namery=Label(e,text="low").grid(row=3,column=1)
    elif (d>=80 and d<=120):
        namery1=Label(e,text="medium").grid(row=3,column=1)
    else:
        namery2=Label(e,text="high").grid(row=3,column=1)

    g=hb.get()
    if (g<13.5):
        namery=Label(e,text="low").grid(row=13,column=1)
    elif (g>=13.5 and g<=17.5):
        namery1=Label(e,text="medium").grid(row=13,column=1)
    else:
        namery2=Label(e,text="high").grid(row=13,column=1)

    h=uri.get()
    if (h<4.0):
        namery=Label(e,text="low").grid(row=15,column=1)
    elif (h>=4.0 and h<=8.5):
        namery1=Label(e,text="medium").grid(row=15,column=1)
    else:
        namery2=Label(e,text="high").grid(row=15,column=1)

    i=pal.get()
    if (i<60):
        namery=Label(e,text="low").grid(row=5,column=1)
    elif (i>=60 and i<=100):
        namery1=Label(e,text="medium").grid(row=5,column=1)
    else:
        namery2=Label(e,text="high").grid(row=5,column=1)

    

    f=chl.get()
    if (f<40):
        namery=Label(e,text="low").grid(row=17,column=1)
    elif (f>=40 and f<=49):
        namery1=Label(e,text="medium").grid(row=17,column=1)
    else:
        namery2=Label(e,text="high").grid(row=17,column=1)
        




    lable2=Label(e,text='BMI:').grid(row=1,column=0)
    lable2=Label(e,text='BP:').grid(row=3,column=0)
    lable2=Label(e,text='Pulse rate:').grid(row=5,column=0)
    lable2=Label(e,text='RCB Count:').grid(row=7,column=0)
    lable2=Label(e,text='WBC Count:').grid(row=9,column=0)
    lable2=Label(e,text='Platelets:').grid(row=11,column=0)
    lable2=Label(e,text='HB:').grid(row=13,column=0)
    lable2=Label(e,text='Uric Acid:').grid(row=15,column=0)
    lable2=Label(e,text='Cholestrale:').grid(row=17,column=0)

    bm()  
    
    e.geometry('500x500')



    
s.geometry('500x600')
s.title('fitness calculator')
mlabel=Label(s,text='NAME:').grid(row=0,column=0)


mlabel=Label(s,text='Age:').grid(row=0,column=5)
#mlabel=Label=(s,text='OK',command=mhello)
namery=Entry(s,textvariable=age).grid(row=0,column=6)

namery=Entry(s,textvariable=name).grid(row=0,column=1)



lable2=Label(s,text='Gender:').grid(row=2,column=0)
lable2=Label(s,text='weight:').grid(row=4,column=0)
lable2=Label(s,text='Height:').grid(row=6,column=0)
lable2=Label(s,text='BP low:').grid(row=8,column=0)
lable2=Label(s,text='BP high:').grid(row=10,column=0)
lable2=Label(s,text='Pulse rate:').grid(row=12,column=0)
lable2=Label(s,text='RCB Count:').grid(row=14,column=0)
lable2=Label(s,text='WBC Count:').grid(row=16,column=0)
lable2=Label(s,text='Platelets:').grid(row=18,column=0)
lable2=Label(s,text='HB:').grid(row=20,column=0)
lable2=Label(s,text='Uric Acid:').grid(row=22,column=0)
lable2=Label(s,text='Cholestrale:').grid(row=24,column=0)


lable2=Label(s,text='').grid(row=3,column=0)
lable2=Label(s,text='').grid(row=5,column=0)
lable2=Label(s,text='').grid(row=7,column=0)
lable2=Label(s,text='').grid(row=9,column=0)
lable2=Label(s,text='').grid(row=11,column=0)
lable2=Label(s,text='').grid(row=13,column=0)
lable2=Label(s,text='').grid(row=15,column=0)
lable2=Label(s,text='').grid(row=17,column=0)
lable2=Label(s,text='').grid(row=19,column=0)
lable2=Label(s,text='').grid(row=21,column=0)
lable2=Label(s,text='').grid(row=23,column=0)
lable2=Label(s,text='').grid(row=25,column=0)




def ma():
    btn=Button(s,text="Generate Report",bg="green",command=result).grid(row=25,column=6)
def fe():
    btn=Button(s,text="Generate Report",bg="red",command=result1).grid(row=25,column=6)





#namery=Entry(s,textvariable=wt).grid(row=,column=1)

namery=Entry(s,textvariable=wt).grid(row=4,column=1)
namery=Entry(s,textvariable=hgt).grid(row=6,column=1)
namery=Entry(s,textvariable=bpl).grid(row=8,column=1)

namery=Entry(s,textvariable=bph).grid(row=10,column=1)
namery=Entry(s,textvariable=pal).grid(row=12,column=1)
namery=Entry(s,textvariable=rcb).grid(row=14,column=1)
namery=Entry(s,textvariable=wbc).grid(row=16,column=1)
namery=Entry(s,textvariable=plt).grid(row=18,column=1)
namery=Entry(s,textvariable=hb).grid(row=20,column=1)
namery=Entry(s,textvariable=uri).grid(row=22,column=1)
namery=Entry(s,textvariable=chl).grid(row=24,column=1)


Radio_1=Radiobutton(s,text="Male",value=1,variable=abc,command=ma).place(x=70,y=20)
Radio_2=Radiobutton(s,text="Female",value=2,variable=abc,command=fe).place(x=140,y=20)






#canvas_1= Canvas(s,height=10,width=10,bg="yellow").pack()




#frame=Fram(s)
#frame.pack()
#bottomframe=Fram(s)
#bottomframe.pack(side=Bottom)






s.mainloop()
           
           
           
