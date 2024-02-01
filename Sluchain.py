
from tkinter import*


cluch_window = Tk()


cluch_window.geometry("600x600")

xi = [ Entry(cluch_window, width= 20) for i in range(7)]
pi = [ Entry(cluch_window, width= 20) for i in range(7)]

for i in range(len(xi)):
 xi[i].grid(column=i, row=0)
 pi[i].grid(column=i, row=1)


def in_put(event):
 for i in range(len(xi)):
  z.append(xi[i].get().strip())
  z1.append(pi[i].get().strip())
  print(z, z1)


pi[-1].bind('<Return>', in_put)
z = []
z1 =[]
print(len(xi), len(pi))



cluch_window.mainloop()