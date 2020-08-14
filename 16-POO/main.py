#Definir una clase (molde para crear objetos de ese tipo)
#(Coche) con caracteristicas similares

class Coche:
    #Atributos o propiedades(variables)
    #Caracteristicas del coche
    color = "Rojo"
    marca = "Tesla"
    modelo = "X"
    velocidad = 350
    seguridad = True

    #Metodos son acciones que hacen el objeto(funciones)

    def acelerar(self):
        self.velocidad = self.velocidad + 10

    def frenar(self):
        self.velocidad = self.velocidad - 10
    
    def getVelocidad(self):
        return self.velocidad

    def setColor(self, pcolor):
        self.color = pcolor
    
    def getColor(self):
        return self.color

    def setModelo(self, pmodelo):
        self.modelo = pmodelo
    
    def getModelo(self):
        return self.modelo
    
    #Finb definicion clase
#Crear objetos/Instanciar la clase
teslaX = Coche()
print(f"Velocidad actual: {teslaX.getVelocidad()}")
for _ in range(10):
    teslaX.acelerar()
for _ in range(1):
    teslaX.frenar()
#[do() for _ in range(3)]

print(f"Velocidad nueva: {teslaX.getVelocidad()}")

print(f"Color de coche actual: {teslaX.getColor()}")
teslaX.setColor("Azul")
print(f"Color de coche nuevo: {teslaX.getColor()}")

#Crear otro objeto con la misma clase 
nikola = Coche()
print(f"Color de coche actual: {nikola.getColor()}")
