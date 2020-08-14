from io import open
import pathlib 
import shutil
import os

#Abrir archivo
archivo = open(str(pathlib.Path().absolute()) + "/fichero_texto.txt", "a+")

#Escribir
#archivo.write("Vamos a dar el rol prro\n")

#Cerrar archivo
archivo.close()

root = str(pathlib.Path().absolute()) + "/fichero_texto.txt";
#Abrir con otro permiso 
archivo = open(root, "r+")

#Leer contenido
contenido = archivo.read()
print(contenido)
#print(contenido)
print(archivo.readlines())
#Leer y guardarlo 
lista = archivo.readlines()

archivo.close()

for ele in lista:
    print(ele)

#Copiar

rootnew = str(pathlib.Path().absolute()) + "/fichero_textocopiado.txt";
shutil.copyfile(root, rootnew)

#Mover


#Eliminar
os.remove(rootnew)

#saca la ruta absoluta
os.path(os.path.abspath("./"))

#El archivo existe o no
if os.path.isfile(os.path.abs("./") + "/fichero_texto.txt"):
    print(True)
else:
    print(False)