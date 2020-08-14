import os

#Crear carpeta
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("La carpeta ya existe")

os.rmdir("./mi_carpeta")