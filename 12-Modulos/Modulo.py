def HolaMundo(nombre):
    return f"Hola mi nombre es {nombre}"

def Tabla(numero):
    print(f"Tabla de multiplicar de {numero} \n")
    contador = 1
    for contador in range(contador, 11):
        print(f"{numero} x {contador} = {numero*contador} \n")