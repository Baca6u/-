import numpy as np
import math
import scipy.special as sc
import matplotlib.pyplot as plt
from clasic_probability import probability
from tkinter import*
from Binom_raspred import binom_raspred


from random_distribution import random_distribution

main_Window = Tk()
main_Window.title("ТВиМС")
main_Window.geometry("600x200")
welcome = Label(main_Window, text="Добро пожаловать в программу ")
welcome.grid(column=5, row=0)

str_1 = Label(main_Window, text=" Распеределение ")
str_1.grid(column=5, row=1)
main_buten = Button(main_Window, text=" Биномитнальные  ", command=binom_raspred)
random_distribution = Button(main_Window, text=" Табличный закон ", command=random_distribution)
main_buten.grid(column=1, row=2)
random_distribution.grid(column=0, row=2)

Label(main_Window, text='Вероятность событий').grid(column=0, row=3)
Button(main_Window, text=" класическая вероятность событий  ", command = probability).grid(column=1, row=4)

main_Window.mainloop()


# if __name__ == '__main__':
#     main()
#
#


