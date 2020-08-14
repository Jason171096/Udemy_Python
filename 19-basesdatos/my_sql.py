import mysql.connector


#Conexion
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python"
)
#Cursor permite hacer consultas
cursor = database.cursor(buffered=True)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Vehiculos(
        id int(10) auto_increment not null,
        marca varchar(50) not null,
        modelo varchar(50) not null,
        precio float(10,2) not null,
        CONSTRAINT pk_vehiculo PRIMARY KEY(id)
    )
""")

cursor.execute("show tables")

for table in cursor:
    print(table)

coche = [
    ('Tesla', 'X', 50000),
    ('Ford', 'F150', 100000),
    ('Mercedez', 'Renault', 70000),
    ('GT', 'GT-Z', 150000)
]

cursor.execute("delete from vehiculos")

database.commit()

cursor.executemany("insert into vehiculos values(null, %s, %s, %s)", coche)

database.commit()


cursor.execute("select * from vehiculos")

result = cursor.fetchall()

for coche in result:
    print(coche)