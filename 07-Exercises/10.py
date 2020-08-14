alum = 1 
repro=0 
apro=0
print("Aprueba de 70 para arriba")
for alum in range(1,16):
    cal = int(input(f"Nota del alumno {alum}: "))
    if cal<70:
        repro +=1
    else:
        apro+=1
print(f"La cantidad de reprobados es {repro}, aprobados es {apro}")