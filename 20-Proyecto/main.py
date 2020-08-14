import login

print("Acciones disponibles:")
print("     1. -Registrarse")
print("     2. -Iniciar Sesion")

op = int(input())
login.loguear(op)