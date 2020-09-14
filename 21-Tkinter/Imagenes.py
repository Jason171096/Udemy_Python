from tkinter import *
from PIL import Image, ImageTk


ventana = Tk()

ventana.geometry("700x700")

imagen = Image.open('./21-Tkinter/tesla.png')
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack()


ventana.mainloop()