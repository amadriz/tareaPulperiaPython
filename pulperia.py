import tkinter as tk
from tkinter import *
from metodos import *
import csv

root = tk.Tk()
root.title("Inventario Pulpería")


##Variables
consultaProducto = StringVar()
agregarProducto = StringVar()
agregarCantidad = IntVar()
vender_producto = StringVar()

filepath = 'productos.csv'
File = open(filepath)
Reader = csv.reader(File)
Data = list(Reader)



#LEER ARCHIVO CSV - DEVUELVE UNA LISTA DE LISTAS ((FUNCION LEER))

products = []

for x in list(range(0, len(Data))):
    # Si se cambia el indice 0 por 1 se muestran las cantidades.
    products.append(Data[x])

print(products)

def agregar_producto():
    agregar = agregarProducto.get()
    cantidad = agregarCantidad.get()
    with open('productos.csv', 'a', newline='') as w:
        w.writelines([agregar,',',cantidad,'\n'])



## FUNCION PARA BORRAR EL PRODUCTO QUE SE VENDE

lines = []

def vender():
    variable = vender_producto.get()
    with open(filepath, mode='r') as r:
        reader = csv.reader(r)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == variable:
                    lines.remove(row)
    with open(filepath, mode='w', newline='') as w:
        writer = csv.writer(w)
        writer.writerows(lines)

# print(lines)

## FUNCION PARA VER SI EL PRODUCTO SE ENCUENTRA DISPONIBLE

def consultProd():
    consultar = consultaProducto.get()
    reader = products
    for i in reader:
        if(i[0] == consultar):
            mensaje = f'Producto Disponible {consultar} + {i[1]}'
            lblMensaje1.config(text=mensaje)


## PRODUCTO CONSULTAR
productoLabel = Label(root, text="Consultar por producto")
productoLabel.grid(row=0, column=0, pady=5, padx=10)

productoConsultar = Entry(root, textvariable=consultaProducto, width=40, borderwidth=5)
productoConsultar.grid(padx=10, pady=10, row=0, column=1)

lblMensaje1 = Label(root, height=5, width=40,)
lblMensaje1.grid(padx=10, pady=10,row=1, column=1)

btnConsulta = Button(root, text="Consultar", width=50, command=consultProd)
btnConsulta.grid(padx=10, pady=10, row=2, column=0, columnspan=2)


# ## AGREGAR PRODUCTOS
#
consultaLabel = Label(root, text="Agregue los productos")
consultaLabel.grid(row=3, column=0, pady=5, padx=10)

agregarProducto = Entry(root, width=40, textvariable=agregarProducto, borderwidth=5)
agregarProducto.grid(padx=5, row=3, column=1)

consultaLabel = Label(root, text="Agregar Cantidad")
consultaLabel.grid(row=5, column=0, pady=5, padx=10)

agregarCantidad = Entry(root, width=40, textvariable=agregarCantidad, borderwidth=5)
agregarCantidad.grid(padx=5, row=5, column=1)

btn = Button(root, text="Agregar Cantidad", width=50, command=agregar_producto)
btn.grid(padx=10, pady=10, row=6, column=0, columnspan=2)


# ## VENDER PRODUCTOS

venderLabel = Label(root, text="Vender productos")
venderLabel.grid(row=7, column=0, pady=5, padx=10)

venderProducto = Entry(root, width=40, textvariable=vender_producto, borderwidth=5)
venderProducto.grid(padx=6, row=7, column=1)

btn = Button(root, text="Vender producto", width=50, command=vender)
btn.grid(padx=10, pady=10, row=8, column=0, columnspan=2)


# ##PRESENTAR INFORMACION

var = StringVar(value = products)
listbox1 = Listbox(root, width=40, listvariable=var)
listbox1.grid(row=9, column=0, padx=10, pady=10, columnspan=2)

# lblMensaje2 = Label(root, height=20, width=40, bg='white', text=leer())
# lblMensaje2.grid(row=9, column=0, padx=10, pady=10, columnspan=2)

root.mainloop()

pass

