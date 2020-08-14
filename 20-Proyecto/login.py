import bd
import menu
import getpass
import datetime
date = datetime.datetime.now()
def loguear(op):    
    if op == 1:
        print("¡Ok, vamos a registrarte!")
        nom = input("   Nombre: ")
        ape = input("   Apellido: ")
        email = input("   Introduce Email: ")
        password = getpass.getpass("   Introduce contraseña: ")
        checkpass = getpass.getpass("   Verificar contraseña: ")
        if password != checkpass:
            print("¡ERROR!")
            print("¡CONTRASEÑAS NO COINCIDEN INTENTE DE NUEVO!")
            loguear(1)
        else:
            boolean = bd.insertUser(nom, ape, email, password)
            if(boolean):
                print(f"Registro completo {nom}")
            else:
                print(f"Error en el registro")
    elif op == 2:
        print("¡Ok vamos a iniciar sesion!")
        email = input("Introduce Email: ")
        password = getpass.getpass("Introduce contraseña: ")
        boolean = bd.checkUser(email, password)
        if(boolean):
            usuario = bd.returnName(email)
            idusuario = 0
            nombreusuario = ""
            for detailsUsuario in usuario:
                idusuario = int(detailsUsuario[0])
                nombreusuario = str(detailsUsuario[1])
            print("------------------------------")
            print(f"Bienvenido {nombreusuario} Fecha: {date}")
            print("------------------------------")
            menu.notas(idusuario, nombreusuario)
        else:
            print(f"Error al iniciar sesion")
            loguear(2)