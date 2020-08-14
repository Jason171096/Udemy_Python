nombres = ["Jason", "Gustavo", "Pancho"]
years = list(range(2020, 2031))
variada = ["Oracio", 23, True, 2.5]

print(nombres)
print(years)
print(variada)

print(variada[1:])

variada[1] = 101

print(variada[1:])

print("*****************")
for nom in nombres:
    print(f"{nombres.index(nom)+1}. {nom}")