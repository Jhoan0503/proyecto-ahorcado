import random

# Lista de palabras
palabras = ["python", "programacion", "algoritmo", "software", "computadora", "tareas"]

# Elegir palabra aleatoria
palabra_secreta = random.choice(palabras)

# Intentos disponibles
intentos = 5

# Letras descubiertas
letras_correctas = []

print("Bienvenido al juego del ahorcado")

while intentos > 0:

    # Mostrar espacios y letras encontradas
    palabra_mostrar = ""

    for letra in palabra_secreta:
        if letra in letras_correctas:
            palabra_mostrar += letra + " "
        else:
            palabra_mostrar += "_ "

    print("\nPalabra:", palabra_mostrar)

    letra_usuario = input("Ingrese una letra: ")

    if letra_usuario in palabra_secreta:

        print("¡Letra correcta!")
        letras_correctas.append(letra_usuario)

    else:

        intentos -= 1
        print("Letra incorrecta")
        print("Intentos restantes:", intentos)

    gano = True

    for letra in palabra_secreta:
        if letra not in letras_correctas:
            gano = False

    if gano:
        print("\n¡Ganaste!")
        print("La palabra era:", palabra_secreta)
        break

if intentos == 0:
    print("\nPerdiste")
    print("La palabra era:", palabra_secreta)
