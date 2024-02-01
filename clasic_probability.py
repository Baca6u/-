from tkinter import*

import scipy.special as sc

global nonon
global p
global x
global b


def probability():
    global n
    global p
    global x
    global b

    clasic_window  = Toplevel()
    clasic_window.geometry("300x200")
    clasic_window.title("Класическая вероятность")
    Label(clasic_window, text="Подсчёт вероятности событий").grid(column=0, row=0)
    Label(clasic_window, text="Общая група иследование").grid(column=0, row=1, pady=5, padx=5)
    Label(clasic_window, text="количество брака").grid(column=0, row=2, pady=5, padx=5)
    Label(clasic_window, text="Кол-во иследуемых в группе").grid(column=0, row=3, pady=5, padx=5)
    Label(clasic_window, text="количество искомых").grid(column=0, row=4, pady=5, padx=5)
    n = Entry(clasic_window, width=10)
    n.grid(column=1, row=1, pady=5, padx=5)
    b = Entry(clasic_window, width=10)
    b.grid(column=1, row=2, pady=5, padx=5)
    p = Entry(clasic_window, width=10)
    p.grid(column=1, row=3, pady=5, padx=5)
    x = Entry(clasic_window, width=10)
    x.grid(column=1, row=4, pady=5, padx=5)
    Button(clasic_window , command = calcilait).grid(column=1, row=5)


def calcilait():

    N = sc.comb(int(n.get()), int(p.get()))
    x_1 = int(n.get()) - int(b.get())
    x_2 = int(p.get()) - int(x.get())
    M = sc.comb(int(b.get()), int(x.get())) * sc.comb(x_1, x_2)

    print(M/N)