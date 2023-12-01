import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog


def calkulator():
    a = h1.get()
    b = h2.get()
    d = combo.get()
    if d == '+':
        res = int(a) + int(b)
        h3.delete(0, tk.END)
        h3.insert(0, res)
    elif d == '-':
        res = int(a) - int(b)
        h3.delete(0, tk.END)
        h3.insert(0, res)
    elif d == '*':
        res = int(a) * int(b)
        h3.delete(0, tk.END)
        h3.insert(0, res)
    else:
        res = int(a) / int(b)
        h3.delete(0, tk.END)
        h3.insert(0, res)


def ChBs():
    message = ''
    if ch1.get() == 1:
        message += '1; '
    if ch2.get() == 1:
        message += '2; '
    if ch3.get() == 1:
        message += '3; '
    messagebox.showinfo('Вы выбрали', message)


def Opfl():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as file:
        text.delete(1.0, tk.END)
        text.insert(tk.END, file.read())


win = tk.Tk()
win.title('Моисеенко-Дарья-Вячеславовна')
win.geometry('800x800')


nbk = ttk.Notebook(win)
nbk.pack(pady=10, padx=10)


tab1 = ttk.Frame(nbk)
tab2 = ttk.Frame(nbk)
tab3 = ttk.Frame(nbk)

nbk.add(tab1, text="Калькулятор")
nbk.add(tab2, text="Чекбоксы")
nbk.add(tab3, text="Текст")

h1 = tk.Entry(tab1, width=10)
h1.grid(row=0, column=0)

combo = ttk.Combobox(tab1, width=3)
combo['values'] = ('+', '-', '*', '/')
combo.current(0)  
combo.grid(row=0, column=1)

h2 = tk.Entry(tab1, width=10)
h2.grid(row=0, column=2)

btn1 = tk.Button(tab1, text='=', command=calkulator)
btn1.grid(row=0, column=3)

h3 = tk.Entry(tab1, width=10)
h3.grid(row=0, column=4)

lab2 = tk.Label(tab1)
lab2.grid(row=0, column=5)

ch1 = tk.IntVar()
ch2 = tk.IntVar()
ch3 = tk.IntVar()

chek1 = tk.Checkbutton(tab2, text='Первый', variable=ch1)
chek2 = tk.Checkbutton(tab2, text='Второй', variable=ch2)
chek3 = tk.Checkbutton(tab2, text='Третий', variable=ch3)

chek1.grid(row=1, column=0)
chek2.grid(row=2, column=0)
chek3.grid(row=3, column=0)

btn2 = tk.Button(tab2, text='Выбрать', command=ChBs)
btn2.grid(row=2, column=1)

menu = tk.Menu(win)
win.config(menu=menu)

file = tk.Menu(menu)
menu.add_cascade(label='Fail', menu=file)
file.add_command(label='Open', command=Opfl)

text = tk.Text(tab3, wrap="word")
text.pack(fill="both", expand=True)

win.mainloop()
