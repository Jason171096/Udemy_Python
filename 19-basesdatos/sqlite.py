#Importar modulo
import sqlite3

#Conexion
conexion = sqlite3.connect('Pruebas.db')

#Crear cursor
cursor = conexion.cursor()

#Crear tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(255),
    description TEXT,
    precio INT(255)
)""")

#Guardar cambios
conexion.commit()

#Insertar datos 
cursor.execute("""INSERT INTO Productos VALUES(
    null, 'Panditas', 'Gomitas Azucaradas', 10
)""")

conexion.commit()

cursor.execute("DELETE FROM Productos")

conexion.commit()

#Listar datos 
cursor.execute("SELECT * FROM Productos")
producto = cursor.fetchall()

for pro in producto:
    print("ID:", pro[0])
    print("Titulo:", pro[1])
    print("Descripcion:", pro[2])
    print("Precio:", pro[3])

producto = cursor.fetchone()
print(producto)

#Cerrar conexion
conexion.close()