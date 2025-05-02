# 1 calificacion
calificacion = int(input("Ingresa tu calificación (0-100): "))

if 90 <= calificacion <= 100:
    print("Sacaste: A")
elif 80 <= calificacion < 90:
    print("Sacaste: B")
elif 70 <= calificacion < 80:
    print("Sacaste: C")
elif 60 <= calificacion < 70:
    print("Sacaste: D")
else:
    print("Sacaste: F")

#2 range
sumapares = 0

for i in range(2, 101, 2):
    sumapares += i

print("La suma de los números pares entre 1 y 100 es:", sumapares)


#bucles
import random

numsecreto = random.randint(1, 100)

intentos = 0
adivinado = False

while not adivinado:
    intento = int(input("Adivina el número entre 1 y 100: "))
    intentos += 1
    
    if intento < numsecreto:
        print("Demasiado bajo")
    elif intento > numsecreto:
        print("Demasiado alto")
    else:
        adivinado = True
        print(f"Adivinaste, lo hiciste en {intentos} intentos.")


# Triangulo
for i in range(1, 6):
    for linea in range(i):
        print("*", end="")
    print()
