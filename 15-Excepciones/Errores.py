try:
    nombre = input("What's your name?")
    if len(nombre) > 1:
        tama = f"nombre {nombre}"
    print(tama)
except:
    print("Mete bien el nombre")
else:
    print("Todo a ido bien")
finally:
    print("Fin de la iteracion")
try:
    numero = int(input("Introduce tu numero :"))
    print(f"El cuadrado es {numero*numero}")
except ValueError as e:
    print("Error de Valor: ", type(e).__name__)

