# __Author__ __Lencof__
# Vaben.py

import os # use os
from tkinter import * # use tkinter

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def mod(a,b):
    return a % b

def lcm(a,b):
    L = a if a>b else b
    while L <= a*b:
        if L%a == 0 and L%b == 0:
            return L
        L+=1

def hcf(a,b):
    H = a if a<b else b
    while H >= 1:
        if a%H == 0 and b%H == 0:
            return H
        H-=1

def extraxt_from_text(text):
    l = []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass # empty block
    return l # repeat

def calculate():
    text = textin.get()
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l = extraxt_from_text(text)
                r = operations[word.upper()](l[0] , l[1])
                list.delete(0,END)
                list.insert(END,r)
            except:
                list.delete(0,END)
                list.insert(END,'something went wrong please enter again')
            finally:
                break
        elif word.upper() not in operations.keys():
            list.delete(0,END)
            list.insert(END,'something went wrong please enter again')

# add operations
operations = {'ADD':add , 'ADDITION':add , 'SUM':add , 'PLUS':add ,
                'SUB':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,
                 'LCM':lcm , 'HCF':hcf , 'PRODUCT':mul , 'MULTIPLICATION':mul,
                 'MULTIPLY':mul , 'DIVISION':div , 'DIV':div ,'DIVIDE':div, 'MOD':mod ,
                  'REMANDER':mod , 'MODULUS':mod}

win = Tk() # create a window
win.geometry('1200x600') # the size
win.title('Vaben') # Name programm
win.configure(bg='#F781F3') # indicate your color 

l1 = Label(win , text='I am a Program',width=130 , padx=9) # your text
l1.place(x=150,y=10)
l2 = Label(win , text='My name is Vaben' , padx=9) # your text
l2.place(x=200,y=60)
l3 = Label(win , text='What can i help you' , padx=3) # your text
l3.place(x=176,y=130)

textin = StringVar()
e1 = Entry(win , width=30 , textvariable = textin)
e1.place(x=100,y=160)

b1 = Button(win , text='I do not know' ,command=calculate) # your text
b1.place(x=210,y=200)

list = Listbox(win,width=20,height=3)
list.place(x=150,y=230)

win.mainloop()
# win.mainloop() close

# Create Vaben file
Vaben = '''
You use Vaben 
'''

# Open for 'w'riting
f = open('Vaben.txt', 'w')
# Write text to file
f.write(Vaben)
# Close the file
f.close()

# If no mode is specified,
# 'r'ead mode is assumed by default
f = open('Vaben.txt')
while True: # use True
    line = f.readline()
    # Zero length indicates EOF
    if len(line) == 0:
        break
    # The `line` already has a newline
    # at the end of each line
    # since it is reading from a file.
    print(line, end='')
# close the file
f.close()
