#Import modulo propio
import Modulo
#Import solo un modulo propio
from Modulo import HolaMundo
#Import todos los modulos
from Modulo import *

print(Modulo.HolaMundo("Jason Martinez"))

Modulo.Tabla(10)

print(HolaMundo("Agustin Savaleta"))

import datetime

print(datetime.date.today())

fecha_Completa = datetime.datetime.now()
print(fecha_Completa)
print(fecha_Completa.year)

fecha_p = fecha_Completa.strftime("%d/%m/%Y, %H:%M:%S")
print(fecha_p)