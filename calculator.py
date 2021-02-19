import tkinter as tk
from tkinter import*
import parser
import tkinter.font as font
import math
from math import factorial

root=tk.Tk()
root.title('Calculator')
canvas=tk.Canvas(root,height=630,width=400,bg='#d1d4f2')
canvas.pack()
#function1
i=0
def get_variables(num):
    global i
    display.insert(i,num)
    i+=1
def clear_all():
    display.delete(0,END)
def calculate():
    input=display.get()
    try:
        a=parser.expr(input).compile()
        result=eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")
def PLusMinus():
    input_data=display.get()
    if input_data.startswith('-'):
        get_data=display.delete(0,1)
        display.insert(0,get_data)
    else:
        display.insert(0,'-')

def get_operation(operator):
    global i
    length=len(operator)
    display.insert(i,operator)
    i+=length
def uponx():
    x_ans=display.get()
    x=float(x_ans)
    ans=1/x
    ans=float(ans)
    display.insert(0,ans)
def back_space():
    input_string=display.get()
    if len(input_string):
        new_string=input_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"Error")
def logvalue():
    x=display.get()
    ans=math.log(int(x))
    clear_all()
    display.insert(0,ans)

def fact():
    value_string=display.get()
    try:
        result=factorial(int(value_string))
        clear_all()
        display.insert(0,result)
    except:
        clear_all()
        display.insert(0,Error)


def onbutton(e):
    button0['bg']='grey'
def onbutton1(e):
    button1['bg']='grey'
def onbutton2(e):
    button2['bg']='grey'
def onbutton3(e):
    button3['bg']='grey'
def onbutton4(e):
    button4['bg']='grey'
def onbutton5(e):
    button5['bg']='grey'
def onbutton6(e):
    button6['bg']='grey'
def onbutton7(e):
    button7['bg']='grey'
def onbutton8(e):
    button8['bg']='grey'
def onbutton9(e):
    button9['bg']='grey'
def onbutton10(e):
    plus['bg']='grey'
def onbutton11(e):
    subtraction['bg']='grey'
def onbutton12(e):
    multiply['bg']='grey'
def onbutton13(e):
    equal['bg']='#0492C2'
def onbutton14(e):
    dot['bg']='grey'
def onbutton15(e):
    plusminus['bg']='grey'
def onbutton16(e):
    divison['bg']='grey'
def onbutton17(e):
    but['bg']='grey'
def onbutton18(e):
    but1['bg']='grey'
def onbutton19(e):
    but2['bg']='grey'
def onbutton20(e):
    backspace['bg']='grey'
def onbutton21(e):
    clearall['bg']='grey'
def onbutton22(e):
    log['bg']='grey'
def onbutton23(e):
    fac['bg']='grey'


def leavebutton(e):
    button0['bg']='white'
def leavebutton1(e):
    button1['bg']='white'
def leavebutton2(e):
    button2['bg']='white'
def leavebutton3(e):
    button3['bg']='white'
def leavebutton4(e):
    button4['bg']='white'
def leavebutton5(e):
    button5['bg']='white'
def leavebutton6(e):
    button6['bg']='white'
def leavebutton7(e):
    button7['bg']='white'
def leavebutton8(e):
    button8['bg']='white'
def leavebutton9(e):
    button9['bg']='white'
def leavebutton10(e):
    plus['bg']='#DAEAFA'
def leavebutton11(e):
    subtraction['bg']='#DAEAFA'
def leavebutton12(e):
    multiply['bg']='#DAEAFA'
def leavebutton13(e):
    equal['bg']='#90BBFF'
def leavebutton14(e):
    dot['bg']='white'
def leavebutton15(e):
    plusminus['bg']='white'
def leavebutton16(e):
    divison['bg']='#DAEAFA'
def leavebutton17(e):
    but['bg']='#DAEAFA'
def leavebutton18(e):
    but1['bg']='#DAEAFA'
def leavebutton19(e):
    but2['bg']='#DAEAFA'
def leavebutton20(e):
    backspace['bg']='#DAEAFA'
def leavebutton21(e):
    clearall['bg']='#DAEAFA'
def leavebutton22(e):
    log['bg']='#DAEAFA'
def leavebutton23(e):
    fac['bg']='#DAEAFA'

display=Entry(root,bd=0,bg='#d1d4f2',justify='right',font=('Courier',30,'bold'))
canvas.create_window(200,100,width=400,height=100,window=display)
button1=tk.Button(root,text='1',bd=0,bg='white',font=('helvetica',15,'bold'),command=lambda:get_variables('1'))
canvas.create_window(53,530,width=98,height=68,window=button1)
button2=tk.Button(root,text='2',bd=0,bg='white',font=('helvetica',15,'bold'),command=lambda:get_variables('2'))
canvas.create_window(153,530,width=98,height=68,window=button2)
button3=tk.Button(root,text='3',bd=0,bg='white',font=('helvetica',15,'bold'),command=lambda:get_variables('3'))
canvas.create_window(253,530,width=98,height=68,window=button3)
plus=tk.Button(root,text='+',bd=0,bg='#DAEAFA',font=('Courier',20),command=lambda:get_operation('+'))
canvas.create_window(353,530,width=98,height=68,window=plus)
button4=tk.Button(root,text='4',bd=0,bg='white',font=('helvetica',15,'bold'),command=lambda:get_variables('4'))
canvas.create_window(53,460,width=98,height=68,window=button4)
button5=tk.Button(root,text='5',bd=0,bg='white',font=('helvetica',15,'bold'),command=lambda:get_variables('5'))
canvas.create_window(153,460,width=98,height=68,window=button5)
button6=tk.Button(root,text='6',bd=0,bg='white',font=('helvetica',15,'bold'),command=lambda:get_variables('6'))
canvas.create_window(253,460,width=98,height=68,window=button6)
subtraction=tk.Button(root,text='-',bd=0,bg='#DAEAFA',font=('Courier',18),command=lambda:get_operation('-'))
canvas.create_window(353,460,width=98,height=68,window=subtraction)
button7=tk.Button(root,text='7',bd=0,bg='white',font=('helvetica',15,'bold'),command=lambda:get_variables('7'))
canvas.create_window(53,390,width=98,height=68,window=button7)
button8=tk.Button(root,text='8',bd=0,bg='white',font=('helvetica',15,'bold'),command=lambda:get_variables('8'))
canvas.create_window(153,390,width=98,height=68,window=button8)
button9=tk.Button(root,text='9',bd=0,bg='white',font=('helvetica',15,'bold'),command=lambda:get_variables('9'))
canvas.create_window(253,390,width=98,height=68,window=button9)
multiply=tk.Button(root,text='\u2A09',bd=0,bg='#DAEAFA',font=('Courier',16),command=lambda:get_variables('*'))
canvas.create_window(353,390,width=98,height=68,window=multiply)
button0=tk.Button(root,text='0',bd=0,bg='white',font=('helvetica',15,'bold'),command=lambda:get_variables('0'))
canvas.create_window(153,600,width=98,height=68,window=button0)
butt=tk.Button(root,text='\u2630',bd=0,bg='#d1d4f2',font=('Courier',16))
canvas.create_window(25,25,width=40,height=40,window=butt)
equal=tk.Button(root,text='=',bd=0,bg='#90BBFF',font=('Courier',20),command=lambda:calculate())
canvas.create_window(353,600,width=98,height=68,window=equal)
dot=tk.Button(root,text='.',bd=0,bg='white',font=('Courier',18),command=lambda:get_variable('.'))
canvas.create_window(253,600,width=98,height=68,window=dot)
plusminus=tk.Button(root,text='+/-',bd=0,bg='white',font=('Courier',18),command=lambda:PLusMinus())
canvas.create_window(53,600,width=98,height=68,window=plusminus)
label=tk.Label(root,text='Standard',bg='#d1d4f2',font=('Courier',18))
canvas.create_window(110,25,window=label)
divison=Button(root,text='\u00f7',bd=0,bg='#DAEAFA',font=('Courier',16),command=lambda:get_operation('%'))
canvas.create_window(353,320,width=98,height=68,window=divison)
but=Button(root,text='1/x',bd=0,bg='#DAEAFA',font=('Courier',16),command=lambda:uponx())
canvas.create_window(253,320,width=98,height=68,window=but)
but1=Button(root,text=('x''\u00b2'),bd=0,bg='#DAEAFA',font=('Courier',16,'normal'),command=lambda:get_operation('**2'))
canvas.create_window(153,320,width=98,height=68,window=but1)
but2=Button(root,text=('\u00b2''\u221a''x'),bd=0,bg='#DAEAFA',font=('Courier',16,'normal'),command=lambda:get_operation('**0.5'))
canvas.create_window(53,320,width=98,height=68,window=but2)
backspace=Button(root,text='\u232b',bd=0,bg='#DAEAFA',font=('helvetica',13),command=lambda:back_space())
canvas.create_window(353,250,width=98,height=68,window=backspace)
clearall=Button(root,text='CE',bd=0,bg='#DAEAFA',font=('Courier',16,'normal'),command=lambda:clear_all())
canvas.create_window(253,250,width=98,height=68,window=clearall)
log=Button(root,text='log(x)',bd=0,bg='#DAEAFA',font=('Courier',16,'normal'),command=lambda:logvalue())
canvas.create_window(153,250,width=98,height=68,window=log)
fac=Button(root,text='Fac',bd=0,bg='#DAEAFA',font=('Courier',16,'normal'),command=lambda:fact())
canvas.create_window(53,250,width=98,height=68,window=fac)
button0.bind('<Enter>',onbutton)
button0.bind('<Leave>',leavebutton)
button1.bind('<Enter>',onbutton1)
button1.bind('<Leave>',leavebutton1)
button2.bind('<Enter>',onbutton2)
button2.bind('<Leave>',leavebutton2)
button3.bind('<Enter>',onbutton3)
button3.bind('<Leave>',leavebutton3)
button4.bind('<Enter>',onbutton4)
button4.bind('<Leave>',leavebutton4)
button5.bind('<Enter>',onbutton5)
button5.bind('<Leave>',leavebutton5)
button6.bind('<Enter>',onbutton6)
button6.bind('<Leave>',leavebutton6)
button7.bind('<Enter>',onbutton7)
button7.bind('<Leave>',leavebutton7)
button8.bind('<Enter>',onbutton8)
button8.bind('<Leave>',leavebutton8)
button9.bind('<Enter>',onbutton9)
button9.bind('<Leave>',leavebutton9)
plus.bind('<Enter>',onbutton10)
plus.bind('<Leave>',leavebutton10)
subtraction.bind('<Enter>',onbutton11)
subtraction.bind('<Leave>',leavebutton11)
multiply.bind('<Enter>',onbutton12)
multiply.bind('<Leave>',leavebutton12)
equal.bind('<Enter>',onbutton13)
equal.bind('<Leave>',leavebutton13)
dot.bind('<Enter>',onbutton14)
dot.bind('<Leave>',leavebutton14)
plusminus.bind('<Enter>',onbutton15)
plusminus.bind('<Leave>',leavebutton15)
divison.bind('<Enter>',onbutton16)
divison.bind('<Leave>',leavebutton16)
but.bind('<Enter>',onbutton17)
but.bind('<Leave>',leavebutton17)
but1.bind('<Enter>',onbutton18)
but1.bind('<Leave>',leavebutton18)
but2.bind('<Enter>',onbutton19)
but2.bind('<Leave>',leavebutton19)
backspace.bind('<Enter>',onbutton20)
backspace.bind('<Leave>',leavebutton20)
clearall.bind('<Enter>',onbutton21)
clearall.bind('<Leave>',leavebutton21)
log.bind('<Enter>',onbutton22)
log.bind('<Leave>',leavebutton22)
fac.bind('<Enter>',onbutton23)
fac.bind('<Leave>',leavebutton23)
root.mainloop()
