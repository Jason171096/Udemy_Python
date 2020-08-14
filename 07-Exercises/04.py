numero1 = int(input("Ingresa el numero 1: "))
numero2 = int(input("Ingresa el numero 2: "))

print(f"La suma de los dos numeros es {numero1+numero2}")
print(f"La resta de los dos numeros es {numero1-numero2}")
print(f"La multiplicacion de los dos numeros es {numero1*numero2}")
try:
    print(f"La divicion de los dos numeros es {numero1/numero2}")
except ZeroDivisionError as ex:
    print("No se puede dividir " + str(ex))
