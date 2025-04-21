
# Juego de adivinanzas en Python

print("                      JUEGO DE ADIVINANZAS")
print("En este juego pondremos a prueba sus conocimientos en Álgebra de Boole y el Sistema Binario.")

#Adivinanza
print("""
Tenemos cuatro Interruptores A, B, C, D, que al convinarlos abren una puerta...

Se sabe que:
- A = ?
- B = 1
- C = 1
- D = 0

La puerta se abre si:
→ (A OR B) AND NOT C AND NOT D

""")

#Se pide al usuario que ingrese su respuesta
num1 = input("Adivine qué valor debe tener A y luego ingrese el número que forman ABCD en binario respetando el formato de 4 bits: ")

#Lo pasé a cadena de texto porque después usamos un len() y me da error de tipeo.
respuesta_correcta = str("0110")
#Bucle que compara la rta del usuario con el número que hay que adivinar
while num1 != respuesta_correcta:
    if len(num1) != 4:
        print("Error, no se está respetando el formato de 4 bits, intente nuevamente")
        num1 = input("Adivine qué valor debe tener A y luego ingrese el número que forman ABCD en binario respetando el formato de 4 bits: ")
    else:
        print("INCORRECTO, por favor vuelva a intentarlo.")
        num1 = input("Adivine qué valor debe tener A y luego ingrese el número que forman ABCD en binario respetando el formato de 4 bits: ")
print(f"CORRECTO, la respuesta es {respuesta_correcta}(recuerde este número para el último nivel del juego).")
print("Puede avanzar al siguiente nivel.")

# PARTE DE LA SUMA
#Ingresar el resultado en decimal
print("Sume los números que obtuvo de cada adivinanza e ingrese el resultado en sistema decimal.")
suma = input("Ingrese su respuesta: ")
# Suma de los numeros adivinados, xxxx porque desconozco los valores binarios (4 bits)
suma_correcta = int("0110", 2) + int("xxxx", 2) + int("xxxx", 2) #cambiar las xxxx
# Cuando usamos int (valor, 2) estamos queriendo decir que el valor está en la base 2 y al poner int lo pasa a entero (guardo fuente)
# Bucle que permite intentos al usuario en caso de haber escrito mal la respuesta de la suma
correcto = False
while not correcto:
    try: #ejecuta el codigo que puede tener errores
        suma = int(suma)
        if suma < 0:
            print("Error, ha ingresado un número negativo, vuelva a intentarlo")
        elif suma != suma_correcta:
            print("Incorrecto, vuelva a intentarlo")
        else:
            print("¡Correcto!")
            correcto = True  # Se sale del bucle
    except ValueError: #se ejecuta si no se pudo hacer int(suma) por tenes algun caracter
        print("Error, ha ingresado un carácter, vuelva a intentarlo")
    if not correcto: #Pide al usuario que ingrese respuesta si anteriormente le salto error o ingreso incorrectamente.
        suma = input("Ingrese su respuesta: ")
print("¡Felicidades, lograste superar cada prueba que se te puso, bien hecho!")

