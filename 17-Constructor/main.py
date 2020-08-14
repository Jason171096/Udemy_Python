from coche import Coche

nik = Coche("Azul Fuerte", "Tesla", "X", 150, True)

print(nik.getColor())

print(nik.getSeguridad())

print(nik.getInfo())


#Detectar tipado de objeto
if type(nik) == Coche:
    print(True)
else:
    print(False)

#Visibilidad
print(nik.public)
print(nik.getPrivado())