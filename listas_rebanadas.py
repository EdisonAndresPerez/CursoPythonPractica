# **Documentación de ejercicios en Python**

# **1. Alias en listas**
lista_1 = [1, 2]
lista_2 = lista_1
lista_1[1] = 4
print(lista_2)
# Explicación:
# - `lista_2` es un alias de `lista_1`. Ambas variables apuntan al mismo objeto en memoria.
# - Al modificar `lista_1`, también se refleja en `lista_2`.
# Salida: `[1, 4]`

# **2. Slicing en listas (copias superficiales)**
lista1 = [1, 2, 3, 4, 5]
lista2 = lista1[1:3]
lista1[2] = 4
print(lista2)
# Explicación:
# - `lista2` es una copia superficial que contiene los elementos `[2, 3]` de `lista1`.
# - Modificar `lista1` después de crear `lista2` no afecta a `lista2`.
# Salida: `[2, 3]`

# **3. Slicing para obtener sublistas**
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)
# Explicación:
# - `my_list[1:3]` crea una sublista que incluye los elementos desde el índice `1` hasta el `2` (sin incluir el `3`).
# Salida: `[8, 6]`

# **4. Slicing con diferentes rangos**
lista_nueva = [10, 8, 6, 4, 2]
new_lista = lista_nueva[0:4]
print(new_lista)
# Explicación:
# - `lista_nueva[0:4]` incluye los elementos desde el índice `0` al `3` (sin incluir el `4`).
# Salida: `[10, 8, 6, 4]`

# **5. Eliminar elementos con `del`**
lista_eliminar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del lista_eliminar[1:5]
print(lista_eliminar)
# Explicación:
# - `del lista_eliminar[1:5]` elimina los elementos desde el índice `1` hasta el `4`.
# Salida: `[1, 6, 7, 8, 9, 10]`

# **6. Verificar pertenencia en listas**
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)      # Verifica si 5 está en my_list
print(5 not in my_list)  # Verifica si 5 no está en my_list
print(12 in my_list)     # Verifica si 12 está en my_list
# Explicación:
# - `in`: Retorna `True` si el elemento está en la lista.
# - `not in`: Retorna `True` si el elemento no está en la lista.
# Salida:
# False
# True
# True

# **7. Encontrar el número mayor en una lista**
# Versión 1: Con índice explícito
lista_ejercicio = [17, 20, 60, 341, 43, 21, 80]
numero_mayor = lista_ejercicio[0]

for i in range(1, len(lista_ejercicio)):
    if lista_ejercicio[i] > numero_mayor:
        numero_mayor = lista_ejercicio[i]

print(numero_mayor)
# Explicación:
# - Se inicializa `numero_mayor` con el primer elemento de la lista.
# - Se recorre la lista desde el índice `1` hasta el final, comparando cada elemento con `numero_mayor`.
# Salida: `341`

# Versión 2: Sin índices explícitos
lista_ejercicio_2 = [17, 20, 60, 341, 43, 21, 80]
numero_mayor_2 = lista_ejercicio_2[0]

for i in lista_ejercicio_2:
    if i > numero_mayor_2:
        numero_mayor_2 = i
print(numero_mayor_2)
# Explicación:
# - Similar a la versión 1, pero aquí el bucle recorre directamente los valores de la lista.
# Salida: `341`

# **8. Encontrar un número específico en una lista**
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero_encontrar = 6
encuentra = False

for i in range(len(mi_lista)):
    encuentra = mi_lista[i] == numero_encontrar
    if encuentra:
        break
if encuentra:
    print("Numero encontrado en el indice es", i)
else:
    print("Numero no encontrado")
# Explicación:
# - Se usa un bucle `for` para recorrer la lista.
# - Cuando el número coincide, el bucle se detiene con `break`.
# - Al final, se verifica si el número fue encontrado y se imprime su índice.
# Salida:
# - Si el número está en la lista: `Numero encontrado en el indice es 5`.
# - Si no está: `Numero no encontrado`.


drawn = [5, 11, 9, 42, 3, 49] # Números sorteados
bets = [3, 7, 11, 42, 34, 49] # Números apostados
hits = 0 #cuenta mis aciertos
 
for number in bets:
    if number in drawn:
        hits += 1
 
print(hits)


#Eliminar numero de la lista 
#si esta repetido
lista_repetida = [1, 2, 3, 4, 4, 4, 2, 2, 6, 5, 7, 8, 8, 9, 10, 10]
lista_sin_repetir = list(set(lista_repetida)) # la funcion set elimina los numeros repetidos
print(lista_sin_repetir)  