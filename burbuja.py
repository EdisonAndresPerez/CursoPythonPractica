# **9. Ordenamiento burbuja (Bubble Sort)**
# Ordenar una lista de números de forma ascendente
my_list = [8, 10, 6, 2, 4, 12, 14, 16, 18, 20]  # lista a ordenar
swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.

while swapped:
    swapped = False  # no hay intercambios hasta ahora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # ¡ocurrió el intercambio!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)
# Explicación:
# - Este código implementa el algoritmo de ordenamiento burbuja.
# - Recorre la lista y realiza intercambios sucesivos para mover el mayor número al final.
# - Se detiene cuando no se realizan más intercambios.
# Salida: `[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]`

# Ordenamiento burbuja interactivo
my_list = []
swapped = True
num = int(input("¿Cuántos elementos deseas ordenar?: "))

for i in range(num):
    val = float(input("Ingresa un elemento de la lista: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nOrdenada:")
print(my_list)
# Explicación:
# - Solicita al usuario la cantidad de elementos y los valores para llenar la lista.
# - Luego, aplica el algoritmo de burbuja para ordenarla.
# Salida: Lista ordenada por el usuario.

# **10. Ordenar cadenas alfabéticamente**
# Ordenar una lista de juegos
lista_juegos = ["minecraft", "fornite", "free fire", "call of duty"]
intercambiado = True

while intercambiado:
    intercambiado = False
    for i in range(len(lista_juegos) - 1):
        if lista_juegos[i] > lista_juegos[i + 1]:
            intercambiado = True
            lista_juegos[i], lista_juegos[i + 1] = lista_juegos[i + 1], lista_juegos[i]

print(lista_juegos)
# Explicación:
# - Similar al algoritmo de burbuja, pero compara cadenas alfabéticamente.
# Salida: Lista de juegos ordenada alfabéticamente: `["call of duty", "fornite", "free fire", "minecraft"]`.

# Ordenar juegos alfabéticamente de forma interactiva
lista_juegos2 = []
intercambiado = True
cantidad_juegos = int(input("¿Cuántos juegos deseas ordenar?: "))
for i in range(cantidad_juegos):
    juegos = str(input("Ingresa un juego: "))
    lista_juegos2.append(juegos)

while intercambiado:
    intercambiado = False
    for i in range(len(lista_juegos2) - 1):
        if lista_juegos2[i] > lista_juegos2[i + 1]:
            intercambiado = True
            lista_juegos2[i], lista_juegos2[i + 1] = lista_juegos2[i + 1], lista_juegos2[i]

print(lista_juegos2)
# Explicación:
# - Solicita al usuario ingresar una lista de juegos.
# - Utiliza el algoritmo de burbuja para ordenarlos alfabéticamente.
# Salida: Lista de juegos ordenada alfabéticamente ingresada por el usuario.