import math
import scipy.special as sc
from tkinter import*
from tkinter import messagebox as mb
global row_ditsr

from tkinter import*
import matplotlib.pyplot as plt

def show_grafik():
    plt.plot(plt_x, pi, ':o')
    plt.show()

def random_distribution():
    global row_ditsr
    random_dctr_window = Toplevel()
    random_dctr_window.geometry("250x100")
    random_dctr_window.title("Дискретная случайная величина")
    Label(Label(random_dctr_window, text = "Дискретная случайная величина ")).grid(column=0, row = 0)
    Label(random_dctr_window, text = "Задайте длину ряда распределение ", font="Arial 8" , bd = 10).grid(column=0, row = 1,  ipady=1, padx= 5)
    row_ditsr = Entry(random_dctr_window, width = 8)
    row_ditsr.grid(column=0, row =2)
    Button(random_dctr_window, text="Задать", command = show_row_distr ).grid(column=0, row= 3,  pady=5, padx= 5)

pi = []
xi = []
xi_sqere = []
xi_lable = []
xi_sqere_lable = []
plt_x =[]
def calculation_dvs():
    ras.destroy()
    n = int(row_ditsr.get())
    matsh_expectation = 0
    dx = 0
    Label(windom_random_dist_2, text= "X^2", bd = 10 , bg = "#fff",font=("Comic Sans MS", 11, "bold")).grid(column=0, row=1)
    #цыкл считываю данные от пользователя
    for i in range(len(xi_entry)):
        xi.append(xi_entry[i].get().strip())
        pi.append(pi_entry[i].get().strip())

    #Перевод данных в тругой тип для просчёта
    for i in range(len(xi_entry)):
        xi_sqere.append(int(xi[i])**2)
        xi[i] = int(xi[i])
        pi[i] = float(pi[i])
        plt_x.append(i)
    xi_pi = []
    moda = 0
    #Математичекое ожидание, DX
    for i in range(len(xi)):
        matsh_expectation = matsh_expectation + int(xi[i]) * float(pi[i])
        dx = dx + xi_sqere[i] * pi[i]
        xi_pi.append(xi[i] * pi[i])
        last = xi[i] * pi[i]
        if last > moda:
            moda = last
    dispersion =  dx - matsh_expectation**2
    sqere= math.sqrt(dispersion)
    for i in range(len(xi)):
        Label(windom_random_dist_2 , text = str(xi_sqere[i]), font="Arial 8" , bd = 10 , bg = "#fff" ).grid(column=i+1, row=1)
        Label(windom_random_dist_2, text= f"Xi*Pi", font=("Comic Sans MS", 8, "bold") , bd = 10 , bg = "#fff" ).grid(column=0, row=4)
        Label(windom_random_dist_2, text=f"{xi[i]*pi[i]}", font="Arial 8" , bd = 10 , bg = "#fff").grid(column=i+1, row=4,  pady=5, padx= 5)
        Label(windom_random_dist_2, text=f"{((xi[i])**2) * pi[i]}", font="Arial 8" , bd = 10 , bg = "#fff").grid(column=i+1, row=5,  pady=5, padx= 5)
        Label(windom_random_dist_2, text= f"Xi^2 * Pi", font="Arial 8" , bd = 10 , bg = "#fff" ).grid(column=0, row=5, pady=5, padx= 5)
    Label(windom_random_dist_2, text= f"1. Математическое ожидание  = {matsh_expectation}", bd = 10 , bg = "#fff",font=("Comic Sans MS", 8, "bold")).grid(column=0, row = 6)
    Label(windom_random_dist_2, text=f"2.Дисперсия Dx  = {dispersion}", bd = 10 , bg = "#fff",font=("Comic Sans MS", 8, "bold")).grid(column=0, row=7)
    Label(windom_random_dist_2, text=f"3.Среднее квадратическое  = {sqere}", bd = 10 , bg = "#fff",font=("Comic Sans MS", 8, "bold")).grid(column=0, rows=8)
    Button(windom_random_dist_2, text="Посторить График  ", command=show_grafik).grid(column=1, row=0)



    median = (n + 1)/2
    sr1 = median - 0.5
    sr2 = median + 0.5
    index_moda = xi_pi.index(moda)
    max_moda =  xi[index_moda]

    Label(windom_random_dist_2, text=f"4.Мода  = {max_moda}").grid(column=0, row=9, bd = 10 , bg = "#fff",font=("Comic Sans MS", 8, "bold"))
    if n %2 == 0:
        srednee_DSV = pi[int(sr1)] + pi[int(sr2)] / 2
        Label(windom_random_dist_2, text=f"5.Среднее орефмитическре ДСВ  = {srednee_DSV}", bd = 10 , bg = "#fff",font=("Comic Sans MS", 8, "bold")).grid(column=0, row=len(xi))

def show_row_distr():
    global windom_random_dist_2
    global xi_entry
    global pi_entry
    global ras
    ceck = str(row_ditsr.get())
    if not ceck.isdigit():
        mb.showerror("Ошибка",
                     "Должно быть введено число")

    n = int(row_ditsr.get())
    windom_random_dist_2 = Toplevel()
    windom_random_dist_2.title("Решение")
    windom_random_dist_2.geometry("500x500")
    Label(windom_random_dist_2, text="Заполните табличное значение", bd = 10 , bg = "#fff",\
          font=("Comic Sans MS", 11, "bold"), ).grid(columnspan= n , row=0, padx = 10)
    xi_entry = [Entry(windom_random_dist_2, width=10, justify = CENTER) for i in range(n)]
    pi_entry = [Entry(windom_random_dist_2, width=10, justify = CENTER) for i in range(n)]
    Label(windom_random_dist_2, text = "Xi", bd = 5 , bg = "#fff",\
          font=("Comic Sans MS", 11, "bold")).grid(column=0, row=2, padx= 5 )
    Label(windom_random_dist_2, text="Pi", bd = 5 , bg = "#fff",\
          font=("Comic Sans MS", 11, "bold")).grid(column=0, row=3, padx= 5 )
    for i in range(n):
        xi_entry[i].grid(column=i+1, row=2,sticky=S , pady=5, padx= 5)
        pi_entry[i].grid(column=i+1, row=3,sticky=S , pady=5, padx= 5)
    ras = Button(windom_random_dist_2, text ="Расчитать " , command = calculation_dvs)
    ras.grid(column=0, row = 11)