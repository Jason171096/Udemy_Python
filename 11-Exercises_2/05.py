"""
Ejercicio 5
Crear una lista con el contenido de esta tabla:
ACCION AVENTURA DEPORTES
GTA      ASSESINS   FIFA 21
COD         CRASH   PRO 21
PUGB        PRINCE  MOTO 21

Mostrar esta informacion ordenada
"""

diccionario = [
    {
        "Categoria":"ACCION",
        "Juegos": ["GTA", "COD", "PUGB"]
    },
    {
        "Categoria":"AVENTURA",
        "Juegos": ["ASSESSINS", "CRASH", "PERSIA"]
    },
    {
        "Categoria":"DEPORTES",
        "Juegos": ["FIFA 21", "PRO 21", "MOTO 21"]
    }
]

for categoria in diccionario:
    print(f"-----------{categoria['Categoria']}----------")
    for juego in categoria['Juegos']:
        print(juego)
