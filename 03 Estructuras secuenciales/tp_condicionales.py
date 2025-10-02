# ejercicio 1
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")

# ejercicio 2

nota = int(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# ejercicio 3

numero = int(input("Ingrese un número par: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor ingrese un número par")

# ejercicio 4

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
elif edad >= 30:
    print("Adulto/a")

# ejercicio 5

contraseña = input("Ingrese una contraseña de 8 a 14 caracteres: ")

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado la contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# ejercicio 6

from statistics import mode, median, mean 
import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("Sin sesgo")

# ejercicio 7

frase = input("Ingrese una frase o palabra: ")

if frase[len(frase) - 1] == "a" or frase[len(frase) - 1] == "e" or frase[len(frase) - 1] == "i" or frase[len(frase) - 1] == "o" or frase[len(frase) - 1] == "u":
    print(frase + "!")
else:
    print(frase)

# ejercicio 8

nombre = input("Ingrese su nombre: ")
numero = int(input("Eliga 1 si quiere su nombre en mayúsculas, 2 en minúscula o 3 solo la primera letra con mayúscula "))

if numero == 1:
    print(nombre.upper())
elif numero == 2:
    print(nombre.lower())
elif numero == 3:
    print(nombre.title())
else:
    print("Elija una de las 3 opciones")

# ejercicio 9

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte (puede causar caños significativos)")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala)")

# ejercicio 10

hemisferio = input("En cúal hemisferio te encontrás?: N/S " )
mes = input("Qué mes del año? : ")
dia = int(input("Qué día? (numero) : "))

if hemisferio == "N":
    if mes == "diciembre" and dia >= 21 or mes == "enero" or mes == "febrero" or mes == "marzo" and dia <= 20:
        print("Invierno")
    elif mes == "marzo" and dia >= 21 or mes == "abril" or mes == "mayo" or mes == "junio" and dia <= 20:
        print("Primavera")
    elif mes == "junio" and dia >= 21 or mes == "julio" or mes == "agosto" or mes == "septiembre" and dia <= 20:
        print("Verano")
    elif mes == "septiembre" and dia >= 21 or mes == "octubre" or mes == "noviembre" or mes == "diciembre" and dia <= 20:
        print("Otoño")
elif hemisferio == "S":
    if mes == "diciembre" and dia >= 21 or mes == "enero" or mes == "febrero" or mes == "marzo" and dia <= 20:
        print("Verano")
    elif mes == "marzo" and dia >= 21 or mes == "abril" or mes == "mayo" or mes == "junio" and dia <= 20:
        print("Otoño")
    elif mes == "junio" and dia >= 21 or mes == "julio" or mes == "agosto" or mes == "septiembre" and dia <= 20:
        print("Invierno")
    elif mes == "septiembre" and dia >= 21 or mes == "octubre" or mes == "noviembre" or mes == "diciembre" and dia <= 20:
        print("Primavera")