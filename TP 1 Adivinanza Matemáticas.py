print("🕵️‍♂️ MISIÓN: OPERACIÓN BINARIA")
print("Estás en una misión para acceder a archivos secretos.")
print("Debes ingresar los códigos correctos en base binaria según las pistas dadas.")
print("⚠️ Tenés 3 niveles. Si fallás, la misión será cancelada.\n")

# Nivel 1 – Decodificación binaria
print("🔐 NIVEL 1: Código de acceso")
print("Pista: el agente dejó anotado el número 7, pero lo transformó al sistema binario.")

codigo = input("Ingrese el código binario de 7 (3 bits): ")

if codigo == "111":
    print("✅ Acceso concedido al siguiente nivel.\n")
else:
    print("❌ Código incorrecto. Misión cancelada.")
    exit()

# Nivel 2 – Lógica de activación de sensor
print("📡 NIVEL 2: Activación del sensor de seguridad")

print("""
Condiciones para activarlo:
- Sensor A está en 0
- Sensor B está en 1
- Sensor C está en ?
- El sistema solo activa si: (A OR C) AND B
""")

sensor_c = input("¿Qué valor debe tener el sensor C? (0 o 1): ")

if sensor_c == "1":
    print("✅ Sensor activado correctamente. Acceso al nivel final.\n")
else:
    print("❌ Fallo en activación. Misión cancelada.")
    exit()

# Nivel 3 – Decodificación final
print("💾 NIVEL 3: Decodificación final")

print("""
Último mensaje interceptado en binario: 0100
Pista: representa el número secreto que coincide con la cantidad de letras en la palabra 'casa'.
""")

respuesta_final = input("¿Qué número es ese en decimal?: ")

if respuesta_final == "4":
    print("🎉 ¡Felicitaciones, agente!")
    print("Has descifrado todos los códigos y completado la operación con éxito.")
else:
    print("❌ Decodificación fallida. Misión cancelada.")
