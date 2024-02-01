import scipy.special as sc
from tkinter import*
from tkinter import ttk
import matplotlib.pyplot as plt
global xi_binom
global pi_binom
global window_binom
import math
def binom_raspred():
    global xi_binom
    global pi_binom

    window_binom = Toplevel()
    window_binom.title("Биноминальное распределение")
    window_binom.geometry("500x200")
    Label(window_binom, text= "Задайте последовательность и вероятную величину").grid(column=0, row= 0)
    Label(window_binom, text= "Xi").grid(column=0, row= 1,pady=5, padx= 5)
    Label(window_binom, text="Pi").grid(column=0, row=2, pady=5, padx= 5)
    xi_binom = Entry(window_binom, width=10)
    xi_binom.grid(column = 1, row = 1)
    pi_binom = Entry(window_binom, width = 10)
    pi_binom.grid(column=1, row = 2)
    Button(window_binom, text="Получить ряд распределения", command = row_raspred ).grid(column=0, row= 3)

def show_graf():

    plt.plot(plt_x ,slushainaya_velexnhiina, ':o')
    plt.show()
def show_teory():
    labl1 = PhotoImage(file="Теорема Бином.png")
    window_teory = Toplevel()
    window_teory.geometry("300x300")
    label = ttk.Label(image=labl1, text="Python", compound="top")
    label.pack()
def row_raspred():
    global plt_x
    global slushainaya_velexnhiina
    summ = 0.0
    global window_binom
    global window_binom_2
    window_binom_2 = Toplevel()
    window_binom_2.geometry("600x600")
    n = int( xi_binom.get())
    p = float( pi_binom.get())
    slushainaya_velexnhiina = [i for i in range(n + 1)]
    q = (1 - p)
    plt_x = []
    for i in range(len(slushainaya_velexnhiina)):
        check = sc.binom(n, i) * (p ** i) * (q ** (n - i))
        slushainaya_velexnhiina[i] = '{:.7f}'.format(check)
        plt_x.append(i)
    for i in range(len(slushainaya_velexnhiina)):
        xi = Label(window_binom_2, text = i)
        pi = Label(window_binom_2, text = str(slushainaya_velexnhiina[i]))
        font_text = Label(window_binom_2, text= "Получим ряд распределение")
        font_text.grid(column= 0, row = 0,columnspan = len(slushainaya_velexnhiina))
        pi.grid(column= i, row = 2, pady=5, padx= 5)
        xi.grid(column = i , row = 1, pady=5, padx= 5 )

    z  = Label(window_binom_2,text=f"x < 0")
    z.grid(column= 1, row = 3)
    f = Label(window_binom_2, text= f"F(x)= P(X < x)")
    f.grid(column = 0, rowspan  =len(slushainaya_velexnhiina) )
    for i in range(len(slushainaya_velexnhiina)):
        summ = summ + float(slushainaya_velexnhiina[i])
        f_x = Label(window_binom_2, text =f"{'{:.6f}'.format(summ)}, {i} < x <{i+1}")
        f_x.grid(column = 1 , row = 4+i)
    end = Label(window_binom_2, text = f"{'{:.1f}'.format(summ)}, x >{len(slushainaya_velexnhiina)}")
    end.grid(column= 1, row = 5 +(len(slushainaya_velexnhiina)-1 ))
    mx_sum = n*p
    mx = Label(window_binom_2 , text= f"Математическое ожидание MX = n*p = {'{:.1f}'.format(mx_sum)}")
    mx.grid(column= 1, row = 6 +(len(slushainaya_velexnhiina)- 1 ))
    for i in range( len(slushainaya_velexnhiina)):
        slushainaya_velexnhiina[i] = float(slushainaya_velexnhiina[i])
    dx_summ = n * p * q
    dx = Label(window_binom_2, text=f"Дисперсия DX = n *p * q = {'{:.3f}'.format(dx_summ)}")
    dx.grid(column=1, row=7 + (len(slushainaya_velexnhiina) - 1))
    graf = Button(window_binom_2, text=" Показать график  ", command = show_graf)
    graf.grid(column=1, row=9 + (len(slushainaya_velexnhiina) - 1))
    ox_summ = math.sqrt(dx_summ)
    ox = Label(window_binom_2, text=f"Среднее квадратическое oX = {'{:.3f}'.format(ox_summ)}")
    ox.grid(column=1, row=8 + (len(slushainaya_velexnhiina) - 1))
    # Button()
    # Button(window_binom_2, text=" Теория  ", command=show_teory).grid(column=2, row= 9 + (len(slushainaya_velexnhiina) - 1))