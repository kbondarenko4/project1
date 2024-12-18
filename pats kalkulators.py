import tkinter
from tkinter import *

def plus():
    sk1 = (int(ent1.get()))
    sk2 = (int(ent2.get()))
    saskaiti = sk1 + sk2
    tex.config(text = str(saskaiti))


logs = Tk()
logs.geometry('400x300+600+200')
logs.title('Aprēķinu kalkulators')

def input_info_entry(symbol):
    entry.insert(END, symbol)

def clear():
    entry.delete(0, END)

def result():
    text = entry.get()
    result = 0
    try:

        if '+' in text:
            splitted_text = text.split('+')    
            first = float(splitted_text[0])
            second = float(splitted_text[1])
            result = first + second

           
        elif '-' in text:
            splitted_text = text.split('-')
            first = float(splitted_text[0])
            second = float(splitted_text[1])
            result = first - second

           
        elif '*' in text:
            splitted_text = text.split('*')
            first = float(splitted_text[0])
            second = float(splitted_text[1])
            result = first * second

        elif '/' in text:
            splitted_text = text.split('/')
            first = float(splitted_text[0])
            second = float(splitted_text[1])
            if second == 0:    #== ir precīzi vienāds
                raise ZeroDivisionError('Dalīšana ar 0 nav atļauta')
            result = first / second

        clear()
        entry.insert(0, result)

       
    except ZeroDivisionError:
        clear()
        entry.insert(0, 'Error(0)')
    except Exception as e:
        clear()

tex = Label(logs, text = 'Ievadiet divus skaitļus')
tex.pack()

ent1 = Entry(logs, width = 30)
ent1.pack()

ent2 = Entry(logs, width = 30)
ent2.pack()

btn1 = Button(logs, bg='purple', fg='white', text='Saskaitīt')
btn1.pack()

btn2 = Button(logs, bg='purple', fg='white', text='Atņemt')
btn2.pack()

btn3 = Button(logs, bg='purple', fg='white', text='Reizināt')
btn3.pack()

btn4 = Button(logs, bg='purple', fg='white', text='Dalīt')
btn4.pack()

logs.mainloop()


