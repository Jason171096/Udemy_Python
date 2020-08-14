class Coche:
    #Atributos o propiedades(variables)
    #Caracteristicas del coche
    color = "Rojo"
    marca = "Tesla"
    modelo = "X"
    velocidad = 350
    seguridad = True

    public = "Hola soy publico"

    __private = "Yo soy privado"

    def getPrivado(self):
        return self.__private

    def __init__(self, color, marca, modelo, velocidad, seguridad):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.seguridad = seguridad
        

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

    def setMarca(self, pmarca):
        self.marca = pmarca
    
    def getMarca(self):
        return self.marca

    def setModelo(self, pmodelo):
        self.modelo = pmodelo
    
    def getModelo(self):
        return self.modelo
    
    def getSeguridad(self):
        return self.seguridad
    
    def getInfo(self):
        info = "---------Information---------"
        info += f"\n Color: {self.getColor()}"
        info += f"\n Marca: {self.getMarca()}"
        info += f"\n Modelo: {self.getModelo()}"
        info += f"\n Velocidad: {self.getVelocidad()}"
        info += f"\n Seguridad: {self.getSeguridad()}"

        return info
