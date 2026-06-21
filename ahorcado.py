import random

palabras = ["python", "programacion", "algoritmo", "software", "computadora"]

palabra_secreta = random.choice(palabras)

print("Bienvenido al juego del ahorcado")
print("La palabra tiene", len(palabra_secreta), "letras")
