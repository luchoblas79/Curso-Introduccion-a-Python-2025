import random
print("Bienvenido al juego de adivinar el numero!")
print("Estoy pensando en un número entre 1 y 50.")
numero_secreto = random.randint(1, 50)
intentos = 0
valor = True
while intentos < 5:
    print("Tienes", 5 - intentos, "intentos restantes.")
    entrada = input("Ingresa un numero entre 1 y 50: ")
    intentos += 1
    valor = entrada.isdigit()
    if valor == True:
        entrada = int(entrada)
        if entrada < 1 or entrada > 50:
            print("El numero debe ser entre 1 y 50.")
        elif entrada < numero_secreto:
            print("El número es mayor que", entrada)
        elif entrada > numero_secreto:
            print("El número es menor que", entrada)

        else:
            break
    if valor == False:
        print("Por favor, ingrese un numero valido.")
if entrada == numero_secreto:
    print("¡Felicidades! Adivinaste el número",
          numero_secreto, "en", intentos, "intentos.")
else:
    print("Lo siento, no adivinaste el número. El número era", numero_secreto)
print("Gracias por jugar.")
