"""
Ejercicio 4
Crear un script que tenga 4 variables, una lista
un string un entero y un boleano y que imprima un mensaje 
segun el tipo de dato de cada variable Usar funciones
"""
def traducirtipo(tipo):
    if tipo == list:
        return "Lista"
    elif tipo == str:
        return "Cadena"
    elif tipo == int:
        return "Entero"
    elif tipo == bool:
        return "Booleano"

def comprobartipado(dato, tipo):
    test = isinstance(dato, tipo)

    if test:
        return f"Este dato es del tipo {traducirtipo(type(dato))}"
    else:
        return "Este dato no es correcto"


lista = ["Hola mundo", 77, True]

nombre = "Jason Martinez"
numero = 17
boleano = True

print(comprobartipado(lista, list))
print(comprobartipado(nombre, str))
print(comprobartipado(numero, int))
print(comprobartipado(boleano, bool))
