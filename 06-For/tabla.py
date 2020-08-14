num = int(input("Numero que se mostrara la tabla: "))
if num < 1:
    num = 1
for numero in range(1,11):
    print(f"{num} x {numero} = {num*numero}")
else:
    print("Tabla finalizada")