def saludo(nombre):
    saludo = f"Hola {nombre}"
    return saludo

print(saludo("Jason"))

#Funcion lambda solo se define en una sola
#Linea

year = lambda year: f"El año es {year}"
print(year(2020))