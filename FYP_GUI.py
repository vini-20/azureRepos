#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

import FYP_heart_covid_analysis as fyp
from FYP_heart_covid_analysis import *


# In[2]:


def graph(r, img): 
    img = Image.open(img)
    canvas = Canvas(r, width=img.width, height=img.height)
    canvas.place(relx=0.67, rely=0.45, anchor=CENTER)
    img = ImageTk.PhotoImage(img)
    label = Label(r, image=img)
    label.image = img
    canvas.create_image(1, 1, anchor=NW, image=img)
    r.mainloop()

def showResult(r, text):
    border = tk.Label(r, text=text, bg="navy", font=('Palatino',20,'bold'), padx=40, pady=10).place(relx=0.67, rely=0.73, anchor=CENTER)
    result = tk.Label(r, text=text, bg="white", font=('Palatino',20,'bold'), padx=37, pady=7).place(relx=0.67, rely=0.73, anchor=CENTER)
    
def predResult(r, text):
    border = tk.Label(r, text=text, bg="navy", font=('Palatino',20,'bold'), padx=40, pady=50).place(relx=0.67, rely=0.53, anchor=CENTER)
    result = tk.Label(r, text=text, bg="white", font=('Palatino',20,'bold'), padx=37, pady=47).place(relx=0.67, rely=0.53, anchor=CENTER)
    
def taskWindow(r, title, color):
    r.title(title)
    r.geometry('800x445')
    r.configure(background='navy')
    head = tk.Label(r, background='navy', text=title, font=('Palatino',30,'bold'), fg='white')
    head.place(relx=0.5, rely=0.07, anchor=CENTER)
    box = tk.Label(r, bg=color, width=200, height=37).place(relx=0.5, rely=0.57, anchor=CENTER)
    back = Button(r, text='Back', bg="white", fg='black', width="15", height="2", font=('Palatino',17,'bold'), command=r.destroy).place(relx=0.77, rely=0.85, anchor=CENTER)


# In[3]:


def ageanalysis():
    root1 = Toplevel()
    taskWindow(root1, "Analysis Based On Age", "lightskyblue")
   
    def checkOutput():
        hea, cov, age = v1.get(), v2.get(), a.get()
        l, h, text = 0, 0, "HIGH RISK --> For the entered Age"
        if hea == 1 and cov == 1:
            l, h = fyp.root1c()
        elif hea == 1:
            l, h = fyp.root1a()
        elif cov == 1:
            l, h = fyp.root1b()
        else:
            text = "LOW RISK --> For the entered Age"
        if age in range(l, h):
            text = "HIGH RISK --> For the entered Age"
        else:
            text = "LOW RISK --> For the entered Age"
        showResult(root1, text)

    def imgSelect():
        hea, cov = v1.get(), v2.get()
        if hea == 1 and cov == 1:
            graph(root1,"root1c.png")
        elif hea == 1:
            graph(root1,"root1a.png")
        elif cov == 1:
            graph(root1,"root1b.png")

    det = Label(root1, text='Enter Details:-', font=('Palatino',17,'bold'), bg='lightskyblue').place(x=170, y=190)
    age = Label(root1, text='Age:', bg="lightskyblue", font=('Palatino',14)).place(x=170, y=260)
    a = IntVar(value=0)
    enterage = Entry(root1, textvariable=a, font=('Palatino',14)).place(x=220, y=260)
    v1, v2 = BooleanVar(value=0), BooleanVar(value=0)
    ch = Label(root1, text='Select:', bg="lightskyblue", font=('Palatino',15)).place(x=170, y=320)
    c1 = Checkbutton(root1, text='Heart Patient', bg="lightskyblue", font=('Palatino',14), variable=v1, onvalue=1, offvalue=0).place(x=200, y=360)
    c2 = Checkbutton(root1, text='COVID-19 Patient', bg="lightskyblue", font=('Palatino',14), variable=v2, onvalue=1, offvalue=0).place(x=200, y=400)
    analyze = Button(root1, text='Analyze', fg ='black', width="15", height="2", font=('Palatino',17,'bold'), command=imgSelect).place(x=170, y=470)
    res = Button(root1, text='Display Result', bg="white", fg ='black', width="15", height="2", font=('Palatino',17,'bold'), command=checkOutput).place(relx=0.57, rely=0.85, anchor=CENTER)

    root1.mainloop()


# In[4]:


def deathrate():
    root2 = Toplevel()
    taskWindow(root2, "COVID-19 Patient Analysis Based On Heart Condition", "lightcyan")

    def checkOutput():   
        val = v.get()
        text = "HIGH RISK"
        if val == 1:
            text = "HIGH RISK --> High Fatality Rate"
        elif val == 0:
            text = "LOW RISK --> High Survival Rate"
        showResult(root2, text)

    def overall():
        graph(root2, "root2c.png")

    def imgSelect():  
        val = v.get()
        if val == 1:
            graph(root2, "root2a.png")
        elif val == 0:
            graph(root2, "root2b.png")

    det = Label(root2, text='Enter Details:-', font=('Palatino',17,'bold'), bg='lightcyan').place(x=170, y=190)
    v = IntVar()
    ch = Label(root2, text='Choose:', bg="lightcyan", font=('Palatino',15)).place(x=170, y=250)
    r1 = Radiobutton(root2, text='Have Heart Problems', bg="lightcyan", font=('Palatino',14), value=1, variable=v).place(x=200, y=290)
    r2 = Radiobutton(root2, text='Do Not Have Heart Problems', bg="lightcyan", font=('Palatino',14), value=0, variable=v).place(x=200, y=330)
    analyze = Button(root2, text='Analyze', bg="white", fg ='black', width="15", height="2", font=('Palatino',17,'bold'), command=imgSelect).place(x=170, y=410)
    compare = Button(root2, text='Overall Comparison', bg="white", fg ='black', width="15", height="2", font=('Palatino',17,'bold'), command=overall).place(x=170, rely=0.8)
    res = Button(root2, text='Display Result', bg="white", fg ='black', width="15", height="2", font=('Palatino',17,'bold'), command=checkOutput).place(relx=0.57, rely=0.85, anchor=CENTER)

    root2.mainloop()


# In[5]:


def icu():
    root3 = Toplevel()
    taskWindow(root3, "COVID-19 Patient Analysis Based On Criticality", "lightblue")

    def checkOutput():   
        val = v.get()
        text = "HIGH RISK"
        if val == 1:
            text = "HIGH RISK --> High Fatality Rate"
        elif val == 0:
            text = "LOW RISK --> High Survival Rate"
        showResult(root3, text)

    def overall():
        graph(root3, "root3c.png")

    def imgSelect():  
        val = v.get()
        if val == 1:
            graph(root3, "root3a.png")
        elif val == 0:
            graph(root3, "root3b.png")

    det = Label(root3, text='Enter Details:-', font=('Palatino',17,'bold'), bg='lightblue').place(x=170, y=190)
    v = IntVar()
    ch = Label(root3, text='Choose:', bg="lightblue", font=('Palatino',15)).place(x=170, y=250)
    r1 = Radiobutton(root3, text='Patient in ICU', bg="lightblue", font=('Palatino',14), value=1, variable=v).place(x=200, y=290)
    r2 = Radiobutton(root3, text='Patient not in ICU', bg="lightblue", font=('Palatino',14), value=0, variable=v).place(x=200, y=330)
    analyze = Button(root3, text='Analyze', bg="white", fg ='black', width="15", height="2", font=('Palatino',17,'bold'), command=imgSelect).place(x=170, y=410)
    compare = Button(root3, text='Overall Comparison', bg="white", fg ='black', width="15", height="2", font=('Palatino',17,'bold'), command=overall).place(x=170, rely=0.8)
    res = Button(root3, text='Display Result', bg="white", fg ='black', width="15", height="2", font=('Palatino',17,'bold'), command=checkOutput).place(relx=0.57, rely=0.85, anchor=CENTER)

    root3.mainloop()


# In[6]:


def hearthealth():
    root4 = Toplevel()
    taskWindow(root4, "Heart Health Prediction", "powderblue")

    def checkOutput():   
        age = a.get()
        ej_fr = ef.get()
        se_cr = sc.get()
        text = fyp.heaPred(age, ej_fr, se_cr)
        predResult(root4, text)

    det = Label(root4, text='Enter Details:-', font=('Palatino',17,'bold'), bg='powderblue').place(x=190, y=210)
    age = Label(root4, text='Age:', bg="powderblue", font=('Palatino',14)).place(x=190, y=290)
    a = IntVar(value=0)
    inpa = Entry(root4, textvariable=a, font=('Palatino',14)).place(x=240, y=290)
    ej_fr = Label(root4, text='Ejection Fraction:', bg="powderblue", font=('Palatino',14)).place(x=190, y=350)
    ef = IntVar(value=0)
    inpef = Entry(root4, textvariable=ef, font=('Palatino',14)).place(x=340, y=350)
    se_cr = Label(root4, text='Serum Creatinine:', bg="powderblue", font=('Palatino',14)).place(x=190, y=410)
    sc = DoubleVar(value=0.0)
    inpsc = Entry(root4, textvariable=sc, font=('Palatino',14)).place(x=340, y=410)
    res = Button(root4, text='Predict Result', bg="white", fg ='black', width="15", height="2", font=('Palatino',17,'bold'), command=checkOutput).place(relx=0.25, rely=0.85, anchor=CENTER)

    root4.mainloop()


# In[7]:


def fut():
    root5 = Toplevel()
    taskWindow(root5, "Follow-Up Time Prediction", "cornflowerblue")

    def checkOutput():   
        age = a.get()
        anae = an.get()
        hbp = bp.get()
        se_cr = sc.get()
        se_so = ss.get()
        days = fyp.timePred(age, anae, hbp, se_cr, se_so)
        text = "Follow-up needed after "+ str(days) +" days."
        predResult(root5, text)

    det = Label(root5, text='Enter Details:-', font=('Palatino',17,'bold'), bg='cornflowerblue').place(x=170, y=190)
    age = Label(root5, text='Age:', bg="cornflowerblue", font=('Palatino',14)).place(x=170, y=250)
    a = IntVar(value=0)
    inpa = Entry(root5, textvariable=a, font=('Palatino',14)).place(x=220, y=250)
    anae = Label(root5, text='Anaemia (Y/N):', bg="cornflowerblue", font=('Palatino',14)).place(x=170, y=300)
    an = StringVar(value='N')
    inpan = Entry(root5, textvariable=an, font=('Palatino',14)).place(x=300, y=300)
    hbp = Label(root5, text='High Blood Pressure (Y/N):', bg="cornflowerblue", font=('Palatino',14)).place(x=170, y=350)
    bp = StringVar(value='N')
    inpbp = Entry(root5, textvariable=bp, font=('Palatino',14)).place(x=390, y=350)
    se_cr = Label(root5, text='Serum Creatinine:', bg="cornflowerblue", font=('Palatino',14)).place(x=170, y=400)
    sc = DoubleVar(value=0.0)
    inpsc = Entry(root5, textvariable=sc, font=('Palatino',14)).place(x=320, y=400)
    se_so = Label(root5, text='Serum Sodium:', bg="cornflowerblue", font=('Palatino',14)).place(x=170, y=450)
    ss = IntVar(value=0)
    inpss = Entry(root5, textvariable=ss, font=('Palatino',14)).place(x=300, y=450)
    res = Button(root5, text='Predict Result', bg="white", fg ='black', width="15", height="2", font=('Palatino',17,'bold'), command=checkOutput).place(relx=0.25, rely=0.85, anchor=CENTER)

    root5.mainloop()    


# In[8]:


#Main Window
root = tk.Tk()
root.title('Heart Health Analyzer')
root.geometry('800x445')
root.configure(background='navy')
canvas = Canvas(root)
bgimg = PhotoImage(master=canvas, file="bg1.png")
bglabel = tk.Label(root, image=bgimg)
bglabel.place(x=-5, y=90)
head = tk.Label(root, background='navy', text="HEART  HEALTH  ANALYZER", font=('Palatino',40,'bold'), fg='aliceblue')
head.place(relx=0.5, rely=0.07, anchor=CENTER)

button1 = Button(text='Analysis Based On Age', bg='lightskyblue', fg='black', width="25", height="9", 
                 font=('Palatino',15,'bold'), command=ageanalysis).place(x=85, y=130)
button2 = Button(text='COVID-19 Patient Analysis\n Based On\n Heart Condition', bg='lightcyan', fg='black', width="25", height="9", 
                 font=('Palatino',15,'bold'), command=deathrate).place(x=485, y=130)
button3 = Button(text='COVID-19 Patient Analysis\n Based On\n Criticality', bg='lightblue', fg='black', width="25", height="9", 
                 font=('Palatino',15,'bold'), command=icu).place(x=885, y=130)
button4 = Button(text='Predict Heart Health', bg='powderblue', fg='black', width="25", height="9", 
                 font=('Palatino',15,'bold'), command=hearthealth).place(x=285, y=380)
button5 = Button(text='Find Follow-Up Time', bg='cornflowerblue', fg='black', width="25", height="9", 
                 font=('Palatino',15,'bold'), command=fut).place(x=685, y=380)
root.mainloop()


# In[ ]:




