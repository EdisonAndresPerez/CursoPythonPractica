# Crear una lista vacía llamada `row`
row = []

# Agregar 8 peones blancos (WHITE_PAWN) a la lista `row`
for i in range(8):
    row.append(WHITE_PAWN)  # Cada vez que pasa el ciclo, se añade un peón blanco

# Crear una lista llamada `squares` que contiene los cuadrados de los números del 0 al 9
squares = [x ** 2 for x in range(10)]  # List comprehension que genera los cuadrados de 0 a 9

# Crear una lista llamada `twos` que contiene las potencias de 2 desde 2^0 hasta 2^7
twos = [2 ** i for i in range(8)]  # List comprehension que genera las potencias de 2 de 0 a 7

# Crear una lista llamada `odds` que contiene solo los números impares de la lista `squares`
odds = [x for x in squares if x % 2 != 0 ]  # Filtrar los números impares de la lista `squares`

# Crear un tablero vacío de 8x8 (un tablero de ajedrez)
board = []  # Lista que representará el tablero de ajedrez

# Llenar el tablero con 8 filas, cada una con 8 casillas vacías (EMPTY)
for i in range(8):
    row = [EMPTY for i in range(8)]  # Cada fila está compuesta de 8 casillas vacías
    board.append(row)  # Añadir la fila al tablero

#agregar fichas al tablero
board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

#agregar caballo 
board[4][2] = KNIGHT

#agregar peon
board[3][4] = PAWN

