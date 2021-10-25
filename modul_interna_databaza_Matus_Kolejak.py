import tkinter
import random
from tkinter import *
from tkinter import ttk


root = tkinter.Tk()
root.overrideredirect(True)
vyska=root.winfo_screenheight()
sirka=root.winfo_screenwidth()
root.geometry("{0}x{1}+0+0".format(sirka, vyska))
root.config(bg='white')
start = 0

hlavna_tema="Interná databáza "
hlavna_tema2="tovaru"

w = tkinter.Label(root, text=hlavna_tema,justify=tkinter.LEFT,font= ('Roboto',35)).place(x=sirka/25.6,y=vyska/15.428)
w = tkinter.Label(root, text=hlavna_tema2,justify=tkinter.LEFT,font= ('Roboto',35)).place(x=sirka/9.6,y=vyska/8)
wecka=tkinter.Label(root)
wecka.place(x=-10,y=-10)
##c = Canvas(root)
##c.pack()


##create.rectangle( 100, 100, 200, 200,root)
##canvas.create_rectangle(275, 165, 525, 215, fill="#C2B6BF")
canvas=tkinter.Canvas(bg='lightgrey',width=sirka-sirka/3.2,height=vyska)
canvas.place(x=sirka/3.2,y=0)







print(vyska)
print(sirka)


##logo = tk.PhotoImage(file="python_logo_small.gif")
##
##w1 = tk.Label(root, image=logo).pack(side="right")
##
##explanation = """At present, only GIF and PPM/PGM
##formats are supported, but an interface 
##exists to allow additional image file
##formats to be added easily."""
##--------------------------------Buttony--------------------------


w1=0


def zelenina():
    global start,w1,w2,w3,w4,w5,w6,w7,w8,wecka
    if start==0:
        start=1
        m=canvas.create_rectangle(sirka/15,vyska/3.15,sirka/1.745,vyska/1.25,fill='beige',outline='beige')
        wecka.place_forget()
        w1 = tkinter.Label(root, text='Zelenina',font= ('Roboto',30))
        w1.place(x=sirka/2.56,y=vyska/4.32)
        wecka=w1
        
        

    else:start=0
       
def ovocie():
    global start,w1,w2,w3,w4,w5,w6,w7,w8,wecka
    if start==0:
        start=1
        
        wecka.place_forget()
        w2=tkinter.Label(root, text='Ovocie',font= ('Roboto',30))
        w2.place(x=sirka/2.56,y=vyska/4.32)
        wecka=w2
        

    else: start=0

def pecivo():
    global start,w1,w2,w3,w4,w5,w6,w7,w8,wecka
    if start==0:
        start=1
        wecka.place_forget()
        w3=tkinter.Label(root, text='Pečivo',font= ('Roboto',30))
        w3.place(x=sirka/2.56,y=vyska/4.32)
        wecka=w3
    else: start=0

def maso():
    global start,w1,w2,w3,w4,w5,w6,w7,w8,wecka
    if start==0:
        start=1
        wecka.place_forget()
        w4=tkinter.Label(root, text='Mäso',font= ('Roboto',30))
        w4.place(x=sirka/2.56,y=vyska/4.32)
        wecka=w4
    else: start=0

def mliecne_vyrobky():
    global start,w1,w2,w3,w4,w5,w6,w7,w8,wecka
    if start==0:
        start=1
        wecka.place_forget()
        w5=tkinter.Label(root, text='Mliečne výrobky',font= ('Roboto',30))
        w5.place(x=sirka/2.56,y=vyska/4.32)
        wecka=w5
    else: start=0

def napoje():
    global start,w1,w2,w3,w4,w5,w6,w7,w8,wecka
    if start==0:
        start=1
        wecka.place_forget()
        w6=tkinter.Label(root, text='Nápoje',font= ('Roboto',30))
        w6.place(x=sirka/2.56,y=vyska/4.32)
        wecka=w6
    else: start=0

def sladkosti_slanosti():
    global start,w1,w2,w3,w4,w5,w6,w7,w8,wecka
    if start==0:
        start=1
        wecka.place_forget()
        w7=tkinter.Label(root, text='Sladkosti/Slanosti',font= ('Roboto',30))
        w7.place(x=sirka/2.56,y=vyska/4.32)
        wecka=w7
    else: start=0

def ostatne():
    global start,w1,w2,w3,w4,w5,w6,w7,w8,wecka
    if start==0:
        start=1
        wecka.place_forget()
        w8=tkinter.Label(root, text='Ostatné',font= ('Roboto',30))
        w8.place(x=sirka/2.56,y=vyska/4.32)
        wecka=w8
    else: start=0

##----------------------------------------------------------------------------
name = tkinter.StringVar()
nameEntered = ttk.Entry(root, font=("Roboto", int(vyska/54)), textvariable = name)
nameEntered.place(relx=sirka/2193.5, rely=vyska/1245.81,width=sirka/4.267,height=vyska/15.43, anchor='n')

label = ttk.Label(root, text = "Vlož názov a kód tovaru", font=("Roboto", int(vyska/75)))
label.place(x=sirka/1.5311,y=vyska/1.206)
##label.grid(column = 0, row = 0)



def clickMe():
    label.configure(text= 'NAZOV A KOD TOVARU ' + name.get())




##-----------------------------------------------------------------------------------
def menu():
    global start
    if start==0:
        start=1
        menu = Toplevel(root)
        menu.title("New Window")
        menu.geometry('200x200')
        Label(menu,text ="This is a new window").pack()
    else: start=0

buttonstart1=tkinter.Button(text="Zelenina", width=int(sirka/90) ,font="Bahnschrift 20", bg="#98C352", fg="white", activebackground="#E0DA63", activeforeground="black",
                            borderwidth=3,cursor="hand2",command=zelenina).place(x=sirka-sirka/1.05, y=vyska-vyska/1.3)

buttonstart1=tkinter.Button(text="Ovocie",  width=int(sirka/90),font="Bahnschrift 20", bg="#98C352", fg="white", activebackground="#E0DA63", activeforeground="black",
                            borderwidth=3,cursor="hand2",command=ovocie).place(x=sirka-sirka/1.05, y=vyska-vyska/1.46)

buttonstart1=tkinter.Button(text="Pečivo",  width=int(sirka/90),font="Bahnschrift 20", bg="#98C352", fg="white", activebackground="#E0DA63", activeforeground="black",
                            borderwidth=3,cursor="hand2",command=pecivo).place(x=sirka-sirka/1.05, y=vyska-vyska/1.665)

buttonstart1=tkinter.Button(text="Mäso",  width=int(sirka/90),font="Bahnschrift 20", bg="#98C352", fg="white", activebackground="#E0DA63", activeforeground="black",
                            borderwidth=3,cursor="hand2",command=maso).place(x=sirka-sirka/1.05, y=vyska-vyska/1.94)

buttonstart1=tkinter.Button(text="Mliečne výrobky",  width=int(sirka/90),font="Bahnschrift 20", bg="#98C352", fg="white", activebackground="#E0DA63", activeforeground="black",
                            borderwidth=3,cursor="hand2",command=mliecne_vyrobky).place(x=sirka-sirka/1.05, y=vyska-vyska/2.327)

buttonstart1=tkinter.Button(text="Nápoje",  width=int(sirka/90),font="Bahnschrift 20", bg="#98C352", fg="white", activebackground="#E0DA63", activeforeground="black",
                            borderwidth=3,cursor="hand2",command=napoje).place(x=sirka-sirka/1.05, y=vyska-vyska/2.9)

buttonstart1=tkinter.Button(text="Sladkosti/Slanosti",  width=int(sirka/90),font="Bahnschrift 20", bg="#98C352", fg="white", activebackground="#E0DA63", activeforeground="black",
                            borderwidth=3,cursor="hand2",command=sladkosti_slanosti).place(x=sirka-sirka/1.05, y=vyska-vyska/3.86)

buttonstart1=tkinter.Button(text="Ostatné",  width=int(sirka/90),font="Bahnschrift 20", bg="#98C352", fg="white", activebackground="#E0DA63", activeforeground="black",
                            borderwidth=3,cursor="hand2",command=ostatne).place(x=sirka-sirka/1.05, y=vyska-vyska/5.7)



buttonstart1=tkinter.Button(text="Pridat",  width=int(sirka/290),height=int(vyska/400),font="Bahnschrift 20", bg="#98C352", fg="white", activebackground="#E0DA63", activeforeground="black",
                            borderwidth=3,cursor="hand2",command=clickMe).place(x=sirka/1.12, y=vyska-vyska/5.7)
