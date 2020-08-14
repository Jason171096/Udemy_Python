"""
Ejercicio 3 Programa que compruebe si una variable esta
vacia y si esta vacia, rellenarla con texto en minusculas 
y mostrarlo en mayusculas
"""

texto = ""
if texto == "":
    texto = "Hola mundo"
    print(texto.upper())

else:
    print(f"La varaiable contiene {texto}")