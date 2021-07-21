import csv
from tkinter import *

filepath = 'productos.csv'
File = open(filepath)
Reader = csv.reader(File)
Data = list(Reader)

#Grab all the column info
products = []

for x in list(range(0, len(Data))):
    # Si se cambia el indice 0 por 1 se muestran las cantidades.
    products.append(Data[x])

root = Tk()
var = StringVar(value = products)
listbox1 = Listbox(root, listvariable=var)

listbox1.grid(row=0, column=0)




root.mainloop()
pass