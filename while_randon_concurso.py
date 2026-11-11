import random
numero_secreto = random.randint(1, 10)
print(numero_secreto)
#5

#             2             2
intentos = 1
while intentos <=3:
    numero_usuario = int(input("Intenta de nuevo: "))

    if numero_secreto == numero_usuario:
        print("Ganaste")
        intentos = 4
    else:
        print("Perdiste, intenta nuevamente ")

        intentos=intentos + 1