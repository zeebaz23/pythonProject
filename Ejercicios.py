# Ejercicio 1
#Crear un programa que pida al usuario ingresar su nombre y edad y los imprima en pantalla.
nombre = input("Ingrese su nombre:")
edad = int(input("Ingrese su edad:"))
print(f"Hola {nombre} su edad es {edad}")

# Ejercicio 2
#Escribir una función que calcule el área de un círculo dado su radio.
import math
radio = float(input("ingrese el radio del circulo"))
Area = math.pi * radio**2
print(f"el area del circulo es {Area}")

# Ejercicio 3
#Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.
import random
cantidad= int(input("Ingrese la cantidad de numeros que desea en la lista:"))
rango1 = int(input("Ingrese el rango inicial:"))
rango2 = int(input("Ingrese el rango final:"))

lista_numeros=[random.randint(rango1,rango2)for i in range(cantidad)]
print(lista_numeros)

#ejercicio 4
#Escribir un programa que determine si un número dado es par o impar.
numero = int(input("Ingrese un numero:"))
if numero %2 ==0:
    print("El numero ingresado es par")
else:
    print("El numero ingresado es impar")
#ejercicio 5
#Crear una función que convierta grados Fahrenheit a grados Celsius
 def conversion_fahrenheit(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
grados_fahrenheit = float(input("Ingrese los grados fahrenheit:"))
grados_celsius= conversion_fahrenheit(grados_fahrenheit)
print(f"{grados_fahrenheit} grados fahrenheit equivalen a {grados_celsius} grados celsius")
#ejercicio 6
import random
cantidad= int(input("Ingrese la cantidad de numeros que desea en la lista:"))
rango1 = int(input("Ingrese el rango inicial:"))
rango2 = int(input("Ingrese el rango final:"))

lista_numeros=[random.randint(rango1,rango2)for i in range(cantidad)]
print(lista_numeros)

suma=0
for num in lista_numeros:
    suma+=num
print(f"La suma de la lista es ----> {suma}")
#ejercicio 7
#Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada.
import random
cantidad= int(input("Ingrese la cantidad de numeros que desea en la lista:"))
rango1 = int(input("Ingrese el rango inicial:"))
rango2 = int(input("Ingrese el rango final:"))

lista_numeros=[random.randint(rango1,rango2)for i in range(cantidad)]
print(lista_numeros)

maximo =max(lista_numeros)
minimo= min(lista_numeros)

print(f"El numero mayor en la lista es {maximo} y el menor es {minimo}")
#ejercicio 8
# Crear una función que invierta el orden de los elementos en una lista dada.
def invertir(lista):
    lista.reverse()

lista_original = [1, 2, 3, 4, 5]
invertir(lista_original)
print(f"Lista original invertida {lista}")
# ejercicio 9
import random

filas = 3
columnas = 4
rango_inicio = 1
rango_fin = 100

matriz = [[random.randint(rango_inicio, rango_fin) for _ in range(columnas)] for _ in range(filas)]

print("Matriz generada:")
for fila in matriz:
    print(fila)
#ejercicio 10
#Escribir una función que calcule el factorial de un número dado.
numero = 5
factorial = 1
if numero < 0:
    print("El factorial de números negativos no está definido.")
elif numero == 0:
    print("El factorial de 0 es 1.")
else:
    for i in range(1, numero + 1):
        factorial *= i
    print(f"El factorial de {numero} es {factorial}.")
#ejercicio 11
# Generar una lista de números pares entre 1 y 100
numeros_pares = [num for num in range(2, 101,  2)]
print("Lista de números pares entre 1 y 100:")
print(numeros_pares)
# ejercicio 12
# Imprimir los números del 1 al 10 utilizando un ciclo for
for numero in range(1, 11):
    print(numero)
#ejercicio 13
# Solicitar al usuario ingresar dos números y calcular la suma, resta, multiplicación y división
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

if numero2 != 0:
    division = numero1 / numero2
else:
    division = "No se puede dividir por cero"

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
# ejercicio 14
#Escribir una función que calcule la media aritmética de una lista de números.
def calcular_media(lista):
    suma = sum(lista)
    media = suma / len(lista)
    return media
numeros = [1, 2, 3, 4, 5]
media = calcular_media(numeros)
print("La media aritmética de la lista es:", media)
#ejericio 15
#Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no.
# Solicitar al usuario ingresar una cadena de texto
cadena = input("Ingrese una cadena de texto: ")


cadena = cadena.replace(" ", "").lower()


if cadena == cadena[::-1]:
    print("La cadena ingresada es un palíndromo.")
else:
    print("La cadena ingresada no es un palíndromo.")













