from tkinter import *
screen = Tk()

#To change Title of Screen
screen.title("MyCalculator")
#To set size
screen.configure(bg='blue')
screen.maxsize(width=340,height=430)
screen.minsize(width=340,height=430)
screen.iconbitmap('image/cal.ico')

def click(number):
    global operator
    operator += str(number)
    tex.set(operator)

def clear():
    global operator
    operator = ''
    tex.set(operator)

def equal():
    global operator
    result = eval(operator)
    operator = str(result)
    tex.set(result)

#.......................Binding Function
def on_enter7(e):
    btn7.configure(bg='light grey')
def on_leave7(e):
    btn7.configure(bg='white')

def on_enter8(e):
    btn8.configure(bg='light grey')
def on_leave8(e):
    btn8.configure(bg='white')

def on_enter9(e):
    btn9.configure(bg='light grey')
def on_leave9(e):
    btn9.configure(bg='white')

def on_enteradd(e):
    btnadd.configure(bg='light grey')
def on_leaveadd(e):
    btnadd.configure(bg='white')

def on_enter4(e):
    btn4.configure(bg='light grey')
def on_leave4(e):
    btn4.configure(bg='white')

def on_enter5(e):
    btn5.configure(bg='light grey')
def on_leave5(e):
    btn5.configure(bg='white')

def on_enter6(e):
    btn6.configure(bg='light grey')
def on_leave6(e):
    btn6.configure(bg='white')

def on_entersub(e):
    btnsub.configure(bg='light grey')
def on_leavesub(e):
    btnsub.configure(bg='white')

def on_enter1(e):
    btn1.configure(bg='light grey')
def on_leave1(e):
    btn1.configure(bg='white')

def on_enter2(e):
    btn2.configure(bg='light grey')
def on_leave2(e):
    btn2.configure(bg='white')

def on_enter3(e):
    btn3.configure(bg='light grey')
def on_leave3(e):
    btn3.configure(bg='white')

def on_entermult(e):
    btnmult.configure(bg='light grey')
def on_leavemult(e):
    btnmult.configure(bg='white')

def on_enterzero(e):
    btnzero.configure(bg='light grey')
def on_leavezero(e):
    btnzero.configure(bg='white')

def on_enterclr(e):
    btnclr.configure(bg='light grey')
def on_leaveclr(e):
    btnclr.configure(bg='white')

def on_enterequal(e):
    btnequal.configure(bg='light grey')
def on_leaveequal(e):
    btnequal.configure(bg='white')

def on_enterdiv(e):
    btndiv.configure(bg='light grey')
def on_leavediv(e):
    btndiv.configure(bg='white')

def on_entryenter(e):
    entry1.configure(bg='light grey')
def on_entryleave(e):
    entry1.configure(bg='white')

tex = StringVar()
operator = ''

#TextBox
entry1 = Entry(screen,bg='white',font=('arial',20,'italic bold'),bd='20',justify='right',textvariable=tex)
#Display TextBox
entry1.grid(row=0,columnspan=4)

btn7 = Button(screen,text='7',font=('arial',18,'italic bold'),bd=8, padx='18',pady='15',command=lambda:click(7),activebackground='green',activeforeground='white',bg='white')
btn7.grid(row=1,column=0)

btn8 = Button(screen,text='8',font=('arial',18,'italic bold'),bd=8, padx='18',pady='15',command=lambda:click(8),activebackground='green',activeforeground='white',bg='white')
btn8.grid(row=1,column=1)

btn9 = Button(screen,text='9',font=('arial',18,'italic bold'),bd=8, padx='18',pady='15',command=lambda:click(9),activebackground='green',activeforeground='white',bg='white')
btn9.grid(row=1,column=2)

btnadd = Button(screen,text='+',font=('arial',18,'italic bold'),bd=8, padx='18',pady='15',command=lambda:click('+'),activebackground='green',activeforeground='white',bg='white')
btnadd.grid(row=1,column=3)

btn4 = Button(screen,text='4',font=('arial',18,'italic bold'),bd=8, padx='18',pady='15',command=lambda:click(4),activebackground='green',activeforeground='white',bg='white')
btn4.grid(row=2,column=0)

btn5 = Button(screen,text='5',font=('arial',18,'italic bold'),bd=8, padx='18',pady='15',command=lambda:click(5),activebackground='green',activeforeground='white',bg='white')
btn5.grid(row=2,column=1)

btn6 = Button(screen,text='6',font=('arial',18,'italic bold'),bd=8, padx='18',pady='15',command=lambda:click(6),activebackground='green',activeforeground='white',bg='white')
btn6.grid(row=2,column=2)

btnsub = Button(screen,text='-',font=('arial',18,'italic bold'),bd=8, padx='21',pady='15',command=lambda:click('-'),activebackground='green',activeforeground='white',bg='white')
btnsub.grid(row=2,column=3)

btn1 = Button(screen,text='1',font=('arial',18,'italic bold'),bd=8, padx='18',pady='15',command=lambda:click(1),activebackground='green',activeforeground='white',bg='white')
btn1.grid(row=3,column=0)

btn2 = Button(screen,text='2',font=('arial',18,'italic bold'),bd=8, padx='18',pady='15',command=lambda:click(2),activebackground='green',activeforeground='white',bg='white')
btn2.grid(row=3,column=1)

btn3 = Button(screen,text='3',font=('arial',18,'italic bold'),bd=8, padx='18',pady='15',command=lambda:click(3),activebackground='green',activeforeground='white',bg='white')
btn3.grid(row=3,column=2)

btnmult = Button(screen,text='*',font=('arial',18,'italic bold'),bd=8, padx='20',pady='15',command=lambda:click('*'),activebackground='green',activeforeground='white',bg='white')
btnmult.grid(row=3,column=3)

btnzero = Button(screen,text='0',font=('arial',18,'italic bold'),bd=8, padx='18',pady='15',command=lambda:click(0),activebackground='green',activeforeground='white',bg='white')
btnzero.grid(row=4,column=0)

btnclr = Button(screen,text='C',font=('arial',18,'italic bold'),bd=8, padx='18',pady='15',command=clear,activebackground='green',activeforeground='white',bg='white')
btnclr.grid(row=4,column=1)

btnequal = Button(screen,text='=',font=('arial',18,'italic bold'),bd=8, padx='18',pady='15',command=equal,activebackground='green',activeforeground='white',bg='white')
btnequal.grid(row=4,column=2)

btndiv = Button(screen,text='/',font=('arial',18,'italic bold'),bd=8, padx='21',pady='15',command=lambda:click('/'),activebackground='green',activeforeground='white',bg='white')
btndiv.grid(row=4,column=3)


entry1.bind('<Enter>',on_entryenter)
entry1.bind('<Leave>',on_entryleave)

btn7.bind('<Enter>',on_enter7)
btn7.bind('<Leave>',on_leave7)

btn8.bind('<Enter>',on_enter8)
btn8.bind('<Leave>',on_leave8)

btn9.bind('<Enter>',on_enter9)
btn9.bind('<Leave>',on_leave9)

btnadd.bind('<Enter>',on_enteradd)
btnadd.bind('<Leave>',on_leaveadd)

btn4.bind('<Enter>',on_enter4)
btn4.bind('<Leave>',on_leave4)

btn5.bind('<Enter>',on_enter5)
btn5.bind('<Leave>',on_leave5)

btn6.bind('<Enter>',on_enter6)
btn6.bind('<Leave>',on_leave6)

btnsub.bind('<Enter>',on_entersub)
btnsub.bind('<Leave>',on_leavesub)

btn1.bind('<Enter>',on_enter1)
btn1.bind('<Leave>',on_leave1)

btn2.bind('<Enter>',on_enter2)
btn2.bind('<Leave>',on_leave2)

btn3.bind('<Enter>',on_enter3)
btn3.bind('<Leave>',on_leave3)

btnmult.bind('<Enter>',on_entermult)
btnmult.bind('<Leave>',on_leavemult)

btnzero.bind('<Enter>',on_enterzero)
btnzero.bind('<Leave>',on_leavezero)

btnclr.bind('<Enter>',on_enterclr)
btnclr.bind('<Leave>',on_leaveclr)

btnequal.bind('<Enter>',on_enterequal)
btnequal.bind('<Leave>',on_leaveequal)

btndiv.bind('<Enter>',on_enterdiv)
btndiv.bind('<Leave>',on_leavediv)

#this will run screen
screen.mainloop()
