#Herencia: Es la posibilidad de compartir atributos y metodos
# entre clases. Y que diferentes clases hereden de otras

class Animal:

    def getNombre(self):
        return self.nombre
    
    def getTipo(self):
        return self.tipo
    
    def getComportamiento(self):
        return self.comportamiento

    def getCome(self):
        return self.come
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setTipo(self, tipo):
        self.tipo = tipo
    
    def setComportamiento(self, comportamiento):
        self.comportamiento = comportamiento

    def setCome(self, come):
        self.come = come
    
    def andar(self):
        return "Esta andando"
class Volador(Animal):

    
    def __init__(self):
        self.alas = 2
    
    def getVolador(self):
        return self.alas

    def picada(self):
        return "En picada"

class Austronautico(Volador):

    def __init__(self):
        super().__init__()#Asigna el constructor de la clase padre los valores por defecto
        self.austronautico = True
    
    def espacio(self):
        return "Estoy en el espacio"