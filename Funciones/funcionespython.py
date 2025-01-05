#import
import math
import random
import string


#Funciones
#Basicos
#Ejercicio 1 Funcion suma
def suma (a, b):
    return a + b
print(suma(5, 5))

#Ejercicio 2 funcion es_par
def es_par(numero):
    return numero % 2 == 0
print(es_par(4))
print(es_par(5))

#Ejercicio 3 funcion area_circulo
def area_circulo(radio):
    return math.pi * radio ** 2
print(area_circulo(5))


#Intermedio
#Ejercicio 4 
def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    return sum(1 for i in cadena if i in vocales)
print(contar_vocales("Hola mundo"))

#Ejercicio 5
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

#Ejercicio 6
def celcius_a_fahrenheit(celcius):
    return (celcius * 9/5) + 32
print(celcius_a_fahrenheit(20))

#Dificil
#Ejercicio 7
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
print(es_primo(7))

#Ejercicio 8
def ordenar_palabras(lista):
    return sorted(lista)
    
lista_palabras = ["manzana", "banana", "cereza", "pera"]
ordenar_palabras = ordenar_palabras(lista_palabras)
print(ordenar_palabras)

#Ejercicio 9
def generar_password(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(caracteres) for _ in range(longitud))
    return password
print(generar_password(10))

guardar_password = []

#Ejercicio 10
def contador_palabras(cadena):
    cadena = cadena.translate(str.maketrans('', '', string.punctuation))
    palabras = cadena.split()   # Divide el texto en una lista de palabras
    diccionario = {}

    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] +=1
        else:
            diccionario[palabra] = 1

    return diccionario

print(contador_palabras("Hola mundo como estas, que tal, todo bien"))
