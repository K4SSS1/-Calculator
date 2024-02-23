# Importing tkinter module 
from tkinter import *	
from tkinter import ttk
from tkinter import scrolledtext
result = 0
expression = 0 
a= 0
b= 0
c=0
ist=[]
x= 0 

# window sozdanie
root = Tk() 
root.title('Calculator')

# geomerty of window nahyi			 
root.geometry('450x400')	
root.resizable(0, 0)  

#function nahui
#x is a variale for history. if u delete this,"history" will not work 
#minus
def minus():
    global c
    global x , a ,b
    a = lbl1.get()
    b = lbl2.get()
    a = int(a)
    b = int(b)
    c = a-b
    x = 1
    print(c)
#delenie
def delenie():
    global c
    global x , a ,b
    a = lbl1.get()
    b = lbl2.get()
    a = int(a)
    b = int(b)
    c = a/b
    x=2 
    print(c)
#umnojenie
def umnoj():
    global c
    global x , a ,b
    a = lbl1.get()
    b = lbl2.get()
    a = int(a)
    b = int(b)
    c = a*b
    x=3
    print(c)
#plus
def plus():
    global c 
    global x , a ,b
    a = lbl1.get()
    b = lbl2.get()
    a = int(a)
    b = int(b)
    c = a+b
    x=4
    print(c)
# ravno 
def ravno():
    lbl3.delete(0,'end')
    global c 
    global ist
    global x , a ,b , expression
    c = str(c)
    lbl3.insert(0,c)
    if x == 4: 
        a = str(a)
        b= str(b)
        c = str(c)
        expression = f"{a} + {b} = {c}"
        ist.append(expression)
        result = '\n'.join(ist)

    elif x == 3:
        a = str(a)
        b= str(b)
        c = str(c)
        expression = f"{a} * {b} = {c}"
        ist.append(expression )
        result = '\n'.join(ist)
    elif x == 2:
        a = str(a)
        b= str(b)
        c = str(c)
        expression = f"{a} / {b} = {c}"
        ist.append(expression )
        result = '\n'.join(ist)
    elif x == 1:
        a = str(a)
        b= str(b)
        c = str(c)
        expression = f"{a} - {b} = {c}"
        ist.append(expression )
        result = '\n'.join(ist)
    print (result)
    
def clear():
    lbl1.delete(0,'end')
    lbl2.delete(0,'end')
    lbl3.delete(0,'end')

def history():
     global ist
     txt.delete('1.0', END)
     txt.insert(INSERT,'\n'.join(ist) )


# Creating button blyat
btn1 = Button(root, text = 'umnoj', command=umnoj,relief = 'flat', justify= 'center', activebackground='#006400',background='#228B22', height='4', width='8')
btn2 = Button(root, text = 'delenie', command=delenie ,relief = 'flat', justify= 'center', activebackground='#006400',background='#228B22', height='4', width='8')
btn3 = Button(root, text = 'plus', command=plus ,relief = 'flat', justify= 'center', activebackground='#006400',background='#228B22', height='4', width='8')
btn4 = Button(root, text = 'minus', command=minus,relief = 'flat', justify= 'center', activebackground='#006400',background='#228B22', height='4', width='8')
btn5 = Button(root, text = 'ravno', command=ravno,relief = 'flat', justify= 'center', activebackground='#006400',background='#228B22', height='4', width='8')
btn6 = Button(root, text = 'clear', command=clear,relief = 'flat', justify= 'center', activebackground='#006400',background='#228B22', height='4', width='8')
btn7 = Button(root, text = 'history', command=history,relief = 'flat', justify= 'center', activebackground='#006400',background='#228B22', height='4', width='8')
#creating labl ebana rot
lbl1= Entry(root,width=20)
lbl2= Entry(root,width=20)
lbl3= Entry(root,width=20)
#creating txt suka 
txt = scrolledtext.ScrolledText(root, width = 40, height=10)

# location bitch
btn1.place(x=149, y=8)
btn2.place(x=289, y=8)
btn3.place(x=219, y=8)
btn4.place(x=219, y=85)
btn5.place(x=289, y=85)
btn6.place(x=149, y=85)
btn7.place(x=359, y=200)
lbl1.place(x=9, y=20)
lbl2.place(x=9, y=60)
lbl3.place(x=9, y=100)
txt.place(x= 9, y = 200)
root.mainloop()

#fkn design

