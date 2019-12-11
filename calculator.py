from tkinter import*
root=Tk()
root.title('Calculator')
t=Text(root,height=1,width=20)
t.pack(side=TOP)
frame=Frame(root)
frame.pack()
bottomframe=Frame()
bottomframe.pack(side=BOTTOM)
operation=''
operand2=0
storevalue=0
c=1
def one():
    global c,col
    value = 1
    t.insert(END,value)
    if c==1:
        global storevalue
        storevalue=storevalue*10+int(value)
    else:
        global operand2
        operand2=operand2*10+value
def two():
    global c,col
    value=2
    t.insert(END,value)
    if c==1:
        global storevalue
        storevalue=storevalue*10+value
    else:
        global operand2
        operand2=operand2*10+value
def three():
    global c
    value=3
    t.insert(END,value)
    if c==1:
        global storevalue
        storevalue=storevalue*10+value
    else:
        global operand2
        operand2=operand2*10+value
def four():
    global c
    value=4
    t.insert(END,value)
    if c==1:
        global storevalue
        storevalue=storevalue*10+value
    else:
        global operand2
        operand2=operand2*10+value
def five():
    global c
    value=5
    t.insert(END,value)
    if c==1:
        global storevalue
        storevalue=storevalue*10+value
    else:
        global operand2
        operand2=operand2*10+value
def six():
    global c
    value=6
    t.insert(END,value)
    if c==1:
        global storevalue
        storevalue=storevalue*10+value
    else:
        global operand2
        operand2=operand2*10+value
def seven():
    global c
    value=7
    t.insert(END,value)
    if c==1:
        global storevalue
        storevalue=storevalue*10+value
    else:
        global operand2
        operand2=operand2*10+value
def eight():
    global c
    value=8
    t.insert(END,value)
    if c==1:
        global storevalue
        storevalue=storevalue*10+value
    else:
        global operand2
        operand2=operand2*10+value
def nine():
    global c
    value=9
    t.insert(END,value)
    if c==1:
        global storevalue
        storevalue=storevalue*10+value
    else:
        global operand2
        operand2=operand2*10+value
def zero():
    global c
    value=0
    t.insert(END,value)
    if c==1:
        global storevalue
        storevalue=storevalue*10+value
    else:
        global operand2
        operand2=operand2*10+value
def addition():
    global c
    c=2
    global operation
    operation = '+'
    t.insert(END,operation)
def substraction():
    global c,operation
    c=2
    operation='-'
    t.insert(END,operation)
def multiply():
    global c,operation
    c=2
    operation='*'
    t.insert(END,operation)
def divide():
    global c,operation
    c=2
    operation='/'
    t.insert(END,operation)
def solution():
    global operand2,storevalue
    if operation =='+':
        storevalue=storevalue+operand2
        operand2=0
    elif operation == '-':
        storevalue=storevalue-operand2
        operand2=0
    elif operation == 'x':
        storevalue=storevalue*operand2
        operand2=0
    elif operation == '/':
        try:
            storevalue=storevalue/operand2
        except:
            t.insert(END,"Wrong Value")
    t.insert(END,'='+str(storevalue))
onebutton = Button(frame, text = '1',width=5,command=one)
onebutton.grid(row=1,column=0)
twobutton = Button(frame, text = '2',width=5,command=two)
twobutton.grid(row=1,column=1) 
threebutton = Button(frame, text ='3',width=5,command=three)
threebutton.grid(row=1,column=2)
fourbutton = Button(frame, text ='4',width=5,command=four) 
fourbutton.grid(row=2,column=0)
fivebutton = Button(frame, text ='5',width=5,command=five) 
fivebutton.grid(row=2,column=1)
sixbutton = Button(frame, text ='6',width=5,command=six) 
sixbutton.grid(row=2,column=2)
sevenbutton = Button(frame, text ='7',width=5,command=seven) 
sevenbutton.grid(row=3,column=0)
eightbutton = Button(frame, text ='8',width=5,command=eight) 
eightbutton.grid(row=3,column=1)
ninebutton = Button(frame, text ='9',width=5,command=nine) 
ninebutton.grid(row=3,column=2)
zerobutton = Button(frame, text ='0',width=5,command=zero) 
zerobutton.grid(row=4,column=1)
addbutton=Button(frame,text='+',width=5,command=addition)
addbutton.grid(row=4,column=0)
addbutton=Button(frame,text='=',width=5,command=solution)
addbutton.grid(row=4,column=2)
subbutton=Button(frame,text='-',width=5,command=substraction)
subbutton.grid(row=5,column=0)
mulbutton = Button(frame, text ='x',width=5,command=multiply) 
mulbutton.grid(row=5,column=1)
divbutton = Button(frame, text ='/',width=5,command=divide) 
divbutton.grid(row=5,column=2)
root.mainloop()
