# Durante la noche de Halloween 🎃, una bruja 🧙‍♀️ está preparando una mezcla mágica.
# Tiene una lista de pociones, cada una con un poder asociado, y quiere combinar dos de ellas para obtener un poder total específico.
# Dada una lista de enteros donde cada número representa el poder de una poción 🧪 y un número entero que representa el poder objetivo,
#debes encontrar el índice de las dos primeras pociones que sumen exactamente el poder objetivo.
pociones = [2, 10, 5, 20, 5, 8]
objetivo = 10

def encontrar_pociones(pociones, objetivo):
    for i in range(len(pociones)):
        for j in range( i + 1, len(pociones)):
            if pociones[i] + pociones[j] == objetivo:
                return [i, j]
    return None

resultado = encontrar_pociones(pociones, objetivo)

if resultado:
    print(f"Las pociones que suman {objetivo} están en los índices: {resultado}")
else:
    print("No se encontraron dos pociones que sumen el poder objetivo.")

#En un bosque mágico, hay varias calabazas mágicas, cada una con un poder asociado.
#Tu tarea es encontrar las tres calabazas cuyo poder total sea exactamente igual al poder objetivo.
#Si encuentras las calabazas, devuelve sus índices. Si no, devuelve None.
calabazas = [3, 4, 6, 8, 2 ]
poder_objectivo = 10

def encontrar_calabazas(calabazas, poder_objectivo):
    vistos = {}
    for i in range(len(calabazas)):
        for j in range(i + 1, len(calabazas)):
            falta = poder_objectivo - (calabazas[i] + calabazas[j])

            if falta in vistos:
                return [vistos[falta], i ,j ]
            vistos[calabazas[j]] = j

    return None

resultado = encontrar_calabazas(calabazas, poder_objectivo)

if resultado:
    print(f"las calabazas que suman{poder_objectivo} estan en los indices {calabazas}")
else:
    print("no se encontraron las 3 calabazas que sumen el poder total")

#🐉 La cueva del dragón y sus tesoros
#Un dragón está cuidando un montón de cofres con oro y quiere repartirlos entre tres aventureros que lo ayudaron.
#Cada cofre tiene una cantidad específica de monedas de oro. El dragón quiere asegurarse de que el oro se pueda dividir exactamente en tres partes iguales.
#Tu tarea es determinar si es posible dividir el oro de los cofres en tres partes iguales sin dejar monedas sobrantes.

def puede_dividir_en_tres(cofres):
    total_oro = sum(cofres)

    if total_oro % 3 != 0;
        return False