from tkinter import *

ventana = Tk()

ventana.geometry("700x700")

texto = Label(ventana, text="Bienvenido a mi aplicacion")

texto.config(fg="Green", bg="Black", padx="20", pady="20", font=("Arial", 30))

texto.pack(anchor=SE)

ventana.mainloop()