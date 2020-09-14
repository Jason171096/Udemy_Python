from tkinter import *
import os.path

class Programa:
    def __init__(self): 
        self.title = "Tesla Enginners"
        self.icon = "./tesla.ico"     
        self.iconR = "./21-Tkinter/tesla.ico"
        self.size = "500x400"
        self.resizable = False

    def cargar(self):
        
        #Crear ventana
        ventana = Tk()
        self.ventana = ventana

        #Agregar titulo
        ventana.title(self.title)

        #Comprobar si existeun archivo

        rutaicon = self.icon

        if not os.path.isfile(rutaicon):
            rutaicon = self.iconR

        #Texto en el programa
        texto = Label(ventana, text=rutaicon)

        texto.pack()

        #Agregar Icono
        ventana.iconbitmap(rutaicon)



        #Cambio de tamaño
        ventana.geometry(self.size)
        if self.resizable == False:
        #Bloquear el tamaño de la ventana
            ventana.resizable(0,0) 

        #Arrancar y mostrar 
        

    def addText(self, texto):
        texto = Label(self.ventana, text=texto)
        texto.pack()

    def openwindow(self):
        self.ventana.mainloop()

program = Programa()
program.cargar()
program.addText("Putos")
program.openwindow()