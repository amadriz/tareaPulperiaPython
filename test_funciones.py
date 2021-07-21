from metodos import *
from tkinter import *
root = Tk()

def Calcular():
    dias=int(edad.get())*365
    mensaje=nombre.get()+ f' has vivido {dias} dias'
    lblMensaje.config(text=mensaje)

nombre = StringVar()
edad = IntVar()

nombreLabel = Label(root, text="Nombre")
nombreLabel.grid(row=0, column=0, pady=5, padx=10)

name = Entry(root, textvariable=nombre, width=40, borderwidth=5)
name.grid(padx=5, row=0, column=1)


edadLabel = Label(root, text="Edad")
edadLabel.grid(row=3, column=0, pady=5, padx=10)

age = Entry(root, width=40, textvariable=edad, borderwidth=5)
age.grid(padx=5, row=3, column=1)


btn = Button(root, text="Calcular", width=50, command=Calcular)
btn.grid(padx=10, pady=10, row=4, column=0, columnspan=2)

lblMensaje = Label(root, height=20, width=40)
lblMensaje.grid(row=7, column=0)


root.mainloop()

pass