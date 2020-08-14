import clases

pajaro = clases.Animal()
pajaro.setNombre("Pelicano")
pajaro.setCome(True)
pajaro.setComportamiento("Pacifico")
pajaro.setTipo("Volador")

print(pajaro.getNombre())
print(pajaro.andar())


guacamaya = clases.Volador()
guacamaya.setNombre("Guacamaya")
guacamaya.setComportamiento("Pacifico")
guacamaya.picada()

print(guacamaya.getNombre())
print(guacamaya.getVolador())
print(guacamaya.picada())

slider = clases.Austronautico()
slider.setNombre("Slider")


print(slider.getNombre()+ ", " +str(slider.getVolador()))