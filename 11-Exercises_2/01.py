"""
Ejercicio 1 Hacer un programa que tenga una lista de 
8 numeros enteros y haga lo siguiente:
-Recorrer la lista y mostrarla
-Ordenarla y mostrarla
-Mostrar su longitud
-Buscar algun elemento(que el usuario pida por teclado)
"""
def recorrer(myListaRecorrida):
    for Recorrer in myListaRecorrida:
        print(Recorrer, end = " ")

def short(myListaRecorrida):
    myListaRecorrida.sort()
    for Recorrer in myListaRecorrida:
        print(Recorrer, end = " ")

def tamano(myListaRecorrida):  
    print(len(myListaRecorrida))

def search(x, myListaRecorrida):
    
    if x in myListaRecorrida:
        print("Tu numero fue encontrado")
    else:
        print("Tu numero no fue encontrado")

mylista = [100, 50, 75, 55, 15, 30, 85, 5]
recorrer(mylista)
print()
print("******")
short(mylista)
print()
print("******")
tamano(mylista)
print("******")

busqueda = int(input("Buscar numero: "))

search(busqueda, mylista)




