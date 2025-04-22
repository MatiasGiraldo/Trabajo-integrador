print("🎮 Juego de Adivinanzas en Binario")
print("Convertí el número binario a decimal.")
print("Tenés que acertar para pasar a la siguiente ronda.\n")

# Variables de puntaje
puntos = 0

# --------------------
# RONDA 1
binario_1 = "0101"
decimal_1 = 5
acertado = False

while not acertado:
    print("Ronda 1")
    print("¿Cuál es el decimal de este binario:", binario_1, "?")
    respuesta = input("Tu respuesta: ")

    if respuesta == str(decimal_1):
        print("✅ ¡Correcto!\n")
        puntos += 1
        acertado = True
    else:
        print("❌ Incorrecto. Intentá de nuevo.\n")

# --------------------
# RONDA 2
binario_2 = "1010"
decimal_2 = 10
acertado = False

while not acertado:
    print("Ronda 2")
    print("¿Cuál es el decimal de este binario:", binario_2, "?")
    respuesta = input("Tu respuesta: ")

    if respuesta == str(decimal_2):
        print("✅ ¡Correcto!\n")
        puntos += 1
        acertado = True
    else:
        print("❌ Incorrecto. Intentá de nuevo.\n")

# --------------------
# RONDA 3
binario_3 = "0011"
decimal_3 = 3
acertado = False

while not acertado:
    print("Ronda 3")
    print("¿Cuál es el decimal de este binario:", binario_3, "?")
    respuesta = input("Tu respuesta: ")

    if respuesta == str(decimal_3):
        print("✅ ¡Correcto!\n")
        puntos += 1
        acertado = True
    else:
        print("❌ Incorrecto. Intentá de nuevo.\n")

# --------------------
# Resultado final
print("🎉 Fin del juego.")
print("Tu puntaje fue:", puntos, "de 3")
