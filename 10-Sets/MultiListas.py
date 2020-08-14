Multilista = [
    {
        1 : "Jason",
        2 : "bboyace10@gmail.com"
    },
    {
        1 : "Pepe",
        2 : "pepe@gmail.com" 
    },
    {
        1 : "Raul",
        2 : "raul@gmail.com"
    }
]

print(Multilista[0][1])

print("Lista de contactos:\n")
for personas in Multilista:
    print("Nombre: "+personas[1])
    print("Email: "+personas[2]+"\n")