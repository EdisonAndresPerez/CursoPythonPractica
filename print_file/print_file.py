import time
import os 


#--------------------------------
# Abrir el archivo "fruits.txt" en modo lectura (por defecto)
try:
    with open("./files/fruits.txt") as myfile:
        # Leer todo el contenido del archivo y mostrarlo
        print(myfile.read())
except FileNotFoundError:
    print("No se encontró el archivo 'fruits.txt'.")
#--------------------------------

#--------------------------------
# Abrir otro archivo "games.txt" en modo lectura
try:
    with open("./files/games.txt") as my_file:
        # Leer el contenido completo del archivo y guardarlo en una variable
        content = my_file.read()
        # Imprimir el contenido del archivo
        print(content)
        # Imprimir nuevamente el mismo contenido
        print(content)
except FileNotFoundError:
    print("No se encontró el archivo 'games.txt'.")
#--------------------------------

#--------------------------------
# Forma correcta de leer un archivo usando 'with' para asegurar que el archivo se cierre automáticamente
try:
    with open("./files/games.txt") as my_file:  
        # Leer todo el contenido del archivo
        content = my_file.read()
        # Imprimir el contenido del archivo
        print(content)
except FileNotFoundError:
    print("No se encontró el archivo 'games.txt'.")
#--------------------------------

#--------------------------------
# Escribir en un archivo, usando 'w' para abrirlo en modo escritura (esto sobrescribirá el archivo si ya existe)
with open("./files/movies.txt", "w") as my_file_movies:
    # Escribir la cadena "I like Avengers" en el archivo
    my_file_movies.write("I like Avengers")
#--------------------------------

#--------------------------------
# Definir una función que recibe un carácter y una ruta de archivo, y cuenta las ocurrencias de ese carácter en el archivo
def recibir(caracter, ruta_archivo):
    try:
        with open(ruta_archivo, "r") as var:
            # Leer todo el contenido del archivo
            contenido = var.read()  
        # Contar cuántas veces aparece el carácter en el contenido del archivo
        ocurrencias = contenido.count(caracter)
        # Devolver el número de ocurrencias
        return ocurrencias
    except FileNotFoundError:
        print(f"No se encontró el archivo {ruta_archivo}.")
        return 0
#--------------------------------

#--------------------------------
# Definir la función contar_lineas
def contar_lineas(ruta_archivo):
    try:
        with open(ruta_archivo, "r") as archivo:
            lineas = archivo.readlines()  # Lee el archivo línea por línea
        return len(lineas)  # Devuelve el número de líneas
    except FileNotFoundError:
        print(f"No se encontró el archivo {ruta_archivo}.")
        return 0

# Llamar a la función y pasar el archivo como parámetro
lineas = contar_lineas("myfile.txt")  # Corrección: nombre del archivo

# Imprimir el resultado
print(f"El archivo tiene {lineas} líneas.")
#--------------------------------

#--------------------------------
def escribir_lista_en_archivo(ruta_archivo, lista):
    try:
        with open(ruta_archivo, "w") as archivo:
            for item in lista:
                archivo.write(item + "\n")
    except FileNotFoundError:
        print(f"No se pudo abrir el archivo {ruta_archivo} para escribir.")
# Lista de datos a escribir
datos = ["Fruta: Manzana", "Fruta: Plátano", "Fruta: Naranja"]
escribir_lista_en_archivo("frutas.txt", datos)
#--------------------------------

#--------------------------------
def agregar_a_archivo(ruta_archivo, texto):
    try:
        with open(ruta_archivo, "a") as archivo:
            archivo.write(texto + "\n")
    except FileNotFoundError:
        print(f"No se pudo abrir el archivo {ruta_archivo} para agregar texto.")
# Agregar texto
agregar_a_archivo("notas.txt", "Comprar leche")
agregar_a_archivo("notas.txt", "Estudiar Python")
#--------------------------------

#--------------------------------
def reemplazar_palabra(ruta_archivo, palabra_a_reemplazar, palabra_nueva):
    try:
        with open(ruta_archivo, "r") as archivo:
            contenido = archivo.read()
        contenido_nuevo = contenido.replace(palabra_a_reemplazar, palabra_nueva)
        with open(ruta_archivo, "w") as archivo:
            archivo.write(contenido_nuevo)
    except FileNotFoundError:
        print(f"No se pudo abrir el archivo {ruta_archivo} para reemplazar la palabra.")
# Reemplazar palabra
reemplazar_palabra("documento.txt", "Python", "Java")
#--------------------------------

#--------------------------------
# Leer y escribir en un archivo
try:
    with open("bear.txt", "r") as mi_file:
        leer = mi_file.read()
        first_90_caracters = leer[:90]

    with open("first.txt", "w") as mi_file2:
        escribir = mi_file2.write(first_90_caracters)
except FileNotFoundError:
    print("No se pudo abrir el archivo 'bear.txt' para leer o 'first.txt' para escribir.")
#--------------------------------

#--------------------------------
with open("./files/games_add.txt", "a+") as filegames:
    filegames.write("\nalbion online")
    filegames.seek(0)
    content = filegames.read()

print(content)
#--------------------------------

#--------------------------------
try:
    with open("bear.txt", "r") as mi_file:
        leer = mi_file.read()
        first_90_caracters = leer[:90]
    with open("first.txt", "w") as mi_file2:
        mi_file2.write(first_90_caracters)
except FileNotFoundError:
    print("El archivo 'bear.txt' no existe.")
except Exception as e:
    print(f"Ha ocurrido un error: {e}")

#--------------------------------


#--------------------------------
try:
    # Paso 1: Leer el contenido actual del archivo
    with open('data.txt', 'r') as file:
        contenido = file.read()

    # Paso 2: Repetir el contenido tres veces
    nuevo_contenido = contenido * 3

    # Paso 3: Escribir el contenido repetido en el archivo
    with open('data.txt', 'w') as file:
        file.write(nuevo_contenido)

    print("El contenido se ha duplicado correctamente.")
except FileNotFoundError:
    print("Error: El archivo 'data.txt' no existe.")
except Exception as e:
    print(f"Ha ocurrido un error: {e}")
#---------------------------------



#---------------------------------
while True:
    if os.path.exists("files/games2.txt"):
        with open("files/games2.txt") as file:
            print(file.read())
    else:
        print("archivo no existe")
        time.sleep(10)

#---------------------------------






#Modos:
#"r": Solo lectura.
#"w": Escritura (sobrescribe el archivo).
#"a": Agregar al final del archivo (sin sobrescribir).

#Métodos:
#read(): Lee el contenido completo.
#readlines(): Lee el contenido línea por línea y devuelve una lista de líneas.
#write(): Escribe una cadena en el archivo.
#replace(): Reemplaza un texto por otro dentro de una cadena.


