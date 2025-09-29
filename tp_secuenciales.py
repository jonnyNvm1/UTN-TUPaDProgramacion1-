# ejercicio 1
print("Hola mundo!")

# ejercicio 2
nombre = input("Cómo te llamás?")
print(f"Hola {nombre}!")

# ejercicio 3
nombre = input("Ingrese su nombre ")
apellido = input("Ingrese su apellido ")
edad = int(input("Ingrese su edad "))
pais = input("De donde sos ? ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {pais}")

# ejercicio 4
radio = int(input("Ingrese el radio de un círculo "))
area = 3.1416 * radio ** 2
perimetro = 2 * 3.1416 * radio

print(f"El área es {area} y el perimetro es {perimetro} ")

# ejercicio 5
segundos = int(input("Ingrese los segundos "))
horas = (segundos / 3600)

print(f"equivale a {horas} horas")

# ejercicio 6
num = int(input("Ingrese un número entero "))

print(f"{num} * 0 = {num * 0}")
print(f"{num} * 1 = {num * 1}")
print(f"{num} * 2 = {num * 2}")
print(f"{num} * 3 = {num * 3}")
print(f"{num} * 4 = {num * 4}")
print(f"{num} * 5 = {num * 5}")
print(f"{num} * 6 = {num * 6}")
print(f"{num} * 7 = {num * 7}")
print(f"{num} * 8 = {num * 8}")
print(f"{num} * 9 = {num * 9}")

# ejercicio 7
num1 = int(input("Ingrese un número entero disinto de 0 "))
num2 = int(input("Ingrese un segundo número entero disinto de 0 "))

print(f"La suma de ambos numeros es {num1 + num2}")
print(f"La división de ambos numeros es {num1 // num2}")
print(f"La multiplicación de ambos numeros es {num1 * num2}")
print(f"La resta de ambos numeros es {num1 - num2}")

# ejercicio 8
altura = float(input("Ingrese su altura en metros "))
peso = float(input("Ingrese su peso en kg "))
imc = round(peso / altura ** 2, 2)

print(f"Su índice de masa corporal es : {imc}")

# ejercicio 9
grados_celsius = float(input("Ingrese una temperatura en grados celsius "))
grados_fahrenheit = round(1.8 * grados_celsius + 32, 1)

print(f"En grados Fahrenheit es : {grados_fahrenheit}°")

# ejercicio 10
num1 = float(input("Ingrese un número "))
num2 = float(input("Ingrese un segundo número "))
num3 = float(input("Ingrese un tercer número "))

promedio = round((num1 + num2 + num3) / 3, 2)

print(f"El promedio es : {promedio}")
