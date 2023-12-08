import json
import requests
import tkinter as tk

def t():
    nm = e.get()
    ss = f'https://api.github.com/repos/{nm}'
    j = requests.get(ss)
    i = j.json()

    f = {
        'company': i.get('company', 'None'),
        'created_at': i.get('created_at', 'None'),
        'email': i.get('email', 'None'),
        'id': i.get('id', 'None'),
        'name': i.get('name', 'None'),
        'url': i.get('url', 'None')
    }
    
    file=open('Daria-Moiseenko_yb32_1.json', 'w')
    json.dump(f, file, indent=1)

# gui
g = tk.Tk()
g.title('Моисеенко Дарья Вячеславовна')
g.geometry("200x200")

label = tk.Label(g, text='Введите имя:')
label.pack()

e = tk.Entry(g)
e.pack()

button = tk.Button(g, text='Запуск', command=t)
button.pack()

g.mainloop()
