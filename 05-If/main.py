color = "rojo"

if color == "rojo":
    print("El color es ROJO")
else:
    print("El color no es ROJO")


year = int(input("¿En que año estamos?"))
if(year>=2021):
    print("Estamos en 2021 en adelante")
else:
    print("Estamos por debajo del 2021")

edad = int(input("Cuantos años tienes?"))
naci = input("Que nacionalidad eres?")

if(edad>=18):
    print("Muy bien")
    if(naci == "Mexicano"):
        print("Excelente")
    else:
        print("Lo siento pero no eres Mexicano")
else:
    print("Eres menor")

