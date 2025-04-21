# PARTE DE LA SUMA
#Ingresar el resultado en decimal
print("Sume los números que obtuvo de cada adivinanza e ingrese el resultado en sistema decimal.")
suma = input("Ingrese su respuesta: ")
# Suma de los numeros adivinados, xxxx porque desconozco los valores binarios (4 bits)
respuesta_correcta = int("xxxx", 2) + int("xxxx", 2) + int("xxxx", 2) #cambiar las xxxx
# Cuando usamos int (valor, 2) estamos queriendo decir que el valor está en la base 2 y al poner int lo pasa a entero (guardo fuente)
# Bucle que permite intentos al usuario en caso de haber escrito mal la respuesta de la suma
correcto = False
while not correcto:
    try: #ejecuta el codigo que puede tener errores
        suma = int(suma)
        if suma < 0:
            print("Error, ha ingresado un número negativo, vuelva a intentarlo")
        elif suma != respuesta_correcta:
            print("Incorrecto, vuelva a intentarlo")
        else:
            print("¡Correcto!")
            correcto = True  # Se sale del bucle
    except ValueError: #se ejecuta si no se pudo hacer int(suma) por tenes algun caracter
        print("Error, ha ingresado un carácter, vuelva a intentarlo")
    if not correcto: #Pide al usuario que ingrese respuesta si anteriormente le salto error o ingreso incorrectamente.
        suma = input("Ingrese su respuesta: ")
print("¡Felicidades, lograste superar cada prueba que se te puso, bien hecho!")
