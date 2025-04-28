# Juego de adivinanzas en Python
import random
print("                      JUEGO DE ADIVINANZAS")
print("En este juego pondremos a prueba sus conocimientos en Álgebra de Boole y el Sistema Binario.")

#Adivinanza 1
print(""" 
Nivel 1:
Tenemos cuatro Interruptores A, B, C, D, que al combinarlos abren una puerta...

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
respuesta_correcta1 = str("0110")

#Contador de intentos
cont = 1

#Bucle que compara la rta del usuario con el número que hay que adivinar
while num1 != respuesta_correcta1:
    if not all(bit in "01" for bit in num1):
        print("Error. Solo se permiten dígitos binarios (0 y 1). Por favor vuelva a intentarlo.")
        num1 = input("Adivine qué valor debe tener A y luego ingrese el número que forman ABCD en binario respetando el formato de 4 bits: ")
    elif len(num1) != 4:
        print("Error, no se está respetando el formato de 4 bits, intente nuevamente.")
        num1 = input("Adivine qué valor debe tener A y luego ingrese el número que forman ABCD en binario respetando el formato de 4 bits: ")
    else:
        print("INCORRECTO, por favor vuelva a intentarlo.")
        num1 = input("Adivine qué valor debe tener A y luego ingrese el número que forman ABCD en binario respetando el formato de 4 bits: ")
    cont += 1
# Si el usuario ingresa respuesta correcta: 
print(f"CORRECTO, la respuesta es {respuesta_correcta1}.")
print("Puede avanzar al siguiente nivel. \n")

#Adivinanza 2
print("Nivel 2: \n Conversion de binario a decimal ")
num2 = input("¿Cual es el decimal del resultado de esta cuenta en binario: 1100 - 0011? ")
respuesta_correcta2 = 9
#Bucle que retiene al usuario si se equivoca en la respuesta
while int(num2) != respuesta_correcta2:
    print("INCORRECTO, por favor vuelva a intentarlo.")
    num2 = input("¿Cual es el decimal del resultado de esta cuenta en binario: 1100 - 0011? ")
    cont += 1
cont +=1
print(f"CORRECTO, la respuesta es {respuesta_correcta2}.")
print("Puede avanzar al siguiente nivel. \n")

#Adivinanza 3
print("Nivel 3: \n Aleatoriedad ")
num3 = input("Adivine el numero en binario (4 bits), se dara una ayuda en cada intento: ")
# creación de lista de todos los numeros binarios de 4 bits
lista_respuestas_3 = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"]
# Se elige un elemento al azar de la lista
respuesta_correcta3 = random.choice(lista_respuestas_3)
print(respuesta_correcta3)
#Bucle que retiene al usuario si se equivoca en la respuesta
while num3 != respuesta_correcta3:
    if not all(bit in "01" for bit in num1):
        print("Error. Solo se permiten dígitos binarios (0 y 1). Por favor vuelva a intentarlo.")
        num3 = input("Adivine el numero en binario (4 bits): ")
    elif len(num3) != 4:
        print("Error, no se está respetando el formato de 4 bits, intente nuevamente.")
        num3 = input("Adivine el numero en binario (4 bits): ")
    else:
        if int(num3, 2) < int(respuesta_correcta3, 2):
            print("INCORRECTO, el numero binario ingresado es menor que la respuesta, intente de nuevo")
            num3 = input("Adivine el numero en binario (4 bits): ")
        else:
            print("INCORRECTO, el numero binario ingresado es mayor que la respuesta, intente de nuevo")
            num3 = input("Adivine el numero en binario (4 bits): ")
    cont += 1
cont +=1
print(f"CORRECTO, la respuesta es {respuesta_correcta3}.")
print("Puede avanzar al siguiente nivel. \n")

# PARTE DE LA SUMA
#Ingresar el resultado en decimal
print("Sume los números que obtuvo de cada adivinanza e ingrese el resultado en sistema decimal.")
print(f"Recuerde que... \nnumero 1: {respuesta_correcta1} \nnumero 2: 1001 \nnumero 3: {respuesta_correcta3}")
suma = input("Ingrese su respuesta: ")
# Suma de los numeros adivinados
suma_correcta = int("0110", 2) + int("1001", 2) + int(respuesta_correcta3, 2) 
# Bucle que permite más intentos al usuario en caso de haber escrito mal la respuesta de la suma
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
    cont +=1
print("¡Felicidades, lograste superar cada prueba que se te puso, bien hecho!")
print(f"Lo lograste en {cont} intentos en total.")

