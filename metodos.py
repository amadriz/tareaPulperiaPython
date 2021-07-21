import csv


#Se utiliza mode='a' por appendo osea agrega una linea a la lista, no le cae encima.

def agregar_producto(nombre, mis_lineas):
    with open(nombre, mode='a', newline='') as File:
        escritor = csv.writer(File)
        escritor.writerows(mis_lineas)

# Metodo filtrar para busquedas
def filtrar(lista, valor, indice):
    return [i for i in lista if i[indice] == valor]

# Metodo contar
def contar(lista, indice):
    columna = seleccionar_columna(lista, indice)
    unicos = set(columna)
    return (i in columna.count(i) for i in sorted(unicos))


# def consultar_producto():
#     print('Si funciono')

# def agregarProd():
#     print('Producto incluido')

def venderProd():
    print('Producto Vendido')