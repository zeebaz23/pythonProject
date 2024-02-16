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





