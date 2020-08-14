num = int(input("Primer numero "))
num1 = int(input("Segundo numero "))

for num in range(num, num1+1):
    if num%2!=0:
        print(f"Impar {num}")