print("🎮 Adivina el número en binario + Álgebra de Boole")
print("Primero resolverás una conversión decimal a binario, luego una expresión lógica.")
print("¡Buena suerte!\n")

puntos = 0

# ----- Parte 1: Decimal a Binario -----

print("🔢 Ronda 1 - Conversión")
print("¿Cuál es el binario de 5? (4 bits)")
respuesta = input("Tu respuesta: ")

while respuesta != "0101":
    print("❌ Incorrecto. Intentá de nuevo.")
    respuesta = input("Tu respuesta: ")

print("✅ ¡Correcto!\n")
puntos = puntos + 1

# ----- Parte 2: Álgebra de Boole -----

print("🧠 Ronda 2 - Álgebra de Boole")
print("""
Se sabe que:
- A = 0
- B = 1

¿Cuál es el resultado de (A OR B)? (Responde 0 o 1)
""")

respuesta = input("Tu respuesta: ")

while respuesta != "1":
    print("❌ Incorrecto. Intentá de nuevo.")
    respuesta = input("Tu respuesta: ")

print("✅ ¡Correcto!\n")
puntos = puntos + 1

# ----- Resultado final -----

print("🏁 Fin del juego.")
print("Tu puntaje fue:", puntos, "de 2 posibles.")
