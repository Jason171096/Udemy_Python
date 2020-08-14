"""
Ejercicio 2
Escribir un programa que añada valores a una lista 
mientras que su longitud sea menor a 120 y luego mostrarla
Usar While y For
"""
introduce = ""
mylist = [];
while introduce != "0":
    introduce = input("Introduce: ")
    mylist.append(introduce)

for mylista in mylist:
    print(mylista, end = " ")
print()

