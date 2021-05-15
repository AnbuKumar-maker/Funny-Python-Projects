from tkinter import * 
import tkinter.messagebox as tmsg
import math as m

root = Tk()

root.minsize(520,340)
root.maxsize(520,340)

root.title("Scientific Calculator")
root.wm_iconbitmap("calculator.ico")


sc = StringVar()
sc = Entry(root,width=31,textvariable=sc,relief=SUNKEN,font="cosmicsansms 20")
sc.grid(row=0,column=0,columnspan=10,padx=11,pady=12) 

def helper():
    help = '''1. For the following functions please enter the number first and then press the required function:
sin, cos, tan, log, ln, √, !, rad, degree, 1/x, π, e 

2. For multiplication with float numbers, say 5*0.4 multiply like 5*4/10'''
    tmsg.showinfo("Help",help)

def abt():
    abt = "This calculator was developed using Tkinter, by Abhishek Ralhan, who is a student of Delhi Technological University." 
    tmsg.showinfo("About",abt)

def const():
    msg = '''If you press constants like:  π and e, 2 times, the result will be square of that constant. 
That means number of times you press the constant, the result will be constant to the power that number. '''
    tmsg.showinfo("Help",msg)


mainmenu = Menu(root)

submenu = Menu(mainmenu,tearoff=0)
submenu.add_command(label="General",command=helper)
submenu.add_command(label="Constants",command=const)
mainmenu.add_cascade(label="Help",menu=submenu)

mainmenu.add_command(label="About",command=abt) 
mainmenu.add_command(label="Exit",command=quit)

root.config(menu=mainmenu)

def sciCal(event):
    key = event.widget
    text = key['text']
    val = sc.get()
    sc.delete(0,END)
    if text=="sin":
        sc.insert(0,m.sin(float(val)))
    elif text=="cos":
        sc.insert(0,m.cos(float(val)))  
    elif text=="tan":
        sc.insert(0,m.tan(float(val)))
    elif text=="log":
        if(float(val)<=0.00):
            sc.insert(0,"Not Possible")
        else:
            sc.insert(0,m.log10(float(val)))
    elif text=="ln":
        if(float(val)<=0.00):
            sc.insert(0,"Not Possible")
        else:
            sc.insert(0,m.log(float(val)))
    elif text=="√":
        sc.insert(0,m.sqrt(float(val)))
    elif text=="!":
        sc.insert(0,m.factorial(int(val)))
    elif text=="rad":
        sc.insert(0,m.radians(float(val)))
    elif text=="deg":
        sc.insert(0,m.degrees(float(val)))
    elif text=="1/x":
        if(val=="0"):
            sc.insert(0,"ꝏ")
        else:
            sc.insert(0,1/float(val))
    elif text=="π":
        if val=="":
             ans = str(m.pi)
             sc.insert(0,ans)
        else:
            ans = str(float(val) * (m.pi))
            sc.insert(0,ans)

    elif text=="e":
        if val=="":
            sc.insert(0,str(m.e))
        else:
            sc.insert(0, str(float(val) * (m.e)))
    

def click(event):
    key = event.widget
    text = key['text']
    oldValue = sc.get()
    sc.delete(0,END)
    newValue = oldValue + text
    sc.insert(0,newValue)
              

def clr(event):
    sc.delete(0,END)
    

def backspace(event):
    entered = sc.get()
    length = len(entered)-1
    sc.delete(length,END)
    

def calculate(event):
    answer = sc.get()
    if "^" in answer:
        answer = answer.replace("^","**")
    answer = eval(answer)
    sc.delete(0,END)
    sc.insert(0,answer)
    
    


class Calculator:
    def __init__(self,txt,r,c,funcName,color="black"):
        self.var = Button(root,text=txt,padx=3,pady=5,fg="white",bg=color,width=10,font="cosmicsansms 12")
        self.var.bind("<Button-1>",funcName)
        self.var.grid(row=r,column=c)


btn0 = Calculator("sin",1,0,sciCal,"grey")

btn1 = Calculator("cos",1,1,sciCal,"grey")

btn2 = Calculator("tan",1,2,sciCal,"grey")

btn3 = Calculator("log",1,3,sciCal)

btn4 = Calculator("ln",1,4,sciCal)

btn5 = Calculator("(",2,0,click)

btn6 = Calculator(")",2,1,click)

btn7 = Calculator("^",2,2,click)

btn8 = Calculator("√",2,3,sciCal)

btn9 = Calculator("!",2,4,sciCal)

btn10 = Calculator("π",3,0,sciCal,"blue")

btn11 = Calculator("1/x",3,1,sciCal)

btn12 = Calculator("deg",3,2,sciCal)

btn13 = Calculator("rad",3,3,sciCal)

btn14 = Calculator("e",3,4,sciCal,"blue")

btn15 = Calculator("/",4,0,click,"#DBA800")

btn16 = Calculator("*",4,1,click,"#DBA800")

btn17 = Calculator("-",4,2,click,"#DBA800")

btn18 = Calculator("+",4,3,click,"#DBA800")

btn19 = Calculator("%",4,4,click,"#DBA800")

btn20 = Calculator("9",5,0,click)

btn21 = Calculator("8",5,1,click)

btn22 = Calculator("7",5,2,click)

btn23 = Calculator("6",5,3,click)

btn24 = Calculator("5",5,4,click)

btn25 = Calculator("4",6,0,click)

btn26 = Calculator("3",6,1,click)

btn27 = Calculator("2",6,2,click)

btn28 = Calculator("1",6,3,click)

btn29 = Calculator("0",6,4,click)

btn30 = Calculator("C",7,0,clr,"red")

btn31 = Calculator("⌦",7,1,backspace,"red")

btn32 = Calculator("00",7,2,click)

btn33 = Calculator(".",7,3,click)

btn34 = Calculator("=",7,4,calculate)

root.mainloop()
