import bd
def notas(idusuario, nombreusuario):
    print("Acciones disponibles")
    print("     1. Crear nota")
    print("     2. Mostrar notas")
    print("     3. Eliminar nota")
    print("     4. Salir")
    action = int(input())
    if action == 1:
        print("¡1. Crear nota!")
        tituloNota = input("Titulo de nota: ")
        contentNota = input("Contenido: ")
        booleano = bd.insertNota(idusuario, tituloNota, contentNota)
        if booleano == 1:
            print("¡Nota agregada!")
        else:
            print("¡Ocurrio un error!")
    elif action == 2:
        print("¡2. Mostrar notas!")
        notas = bd.showNotas(idusuario)
        for nota in notas:
            print("--------------------------------------")
            print(nota)
    elif action == 3:
        print("¡3. Eliminar nota!")
        notas = bd.showNotas(idusuario)
        for nota in notas:
            print("--------------------------------------")
            print(nota[0], nota[2])
        print()
        delete = int(input("ID de nota a eliminar(0 Para cancelar): "))
        if delete == 0:
            print()
        else:
            booleano = bd.deleteNota(idusuario, delete)
            if booleano:
                print("Nota eliminada")
            else:
                print("No se pudo eliminar la nota")
    elif action == 4:
        print(f"¡Adios {nombreusuario}!")