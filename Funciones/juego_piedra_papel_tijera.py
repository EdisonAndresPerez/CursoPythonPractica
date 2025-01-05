import random

def jugar_piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]
    
    while True:
        print("\n¡Bienvenido al juego de Piedra, Papel o Tijera!")
        
        # Jugador elige
        jugador = input("\nElige tu jugada (piedra/papel/tijera) o 'salir' para terminar: ").lower()
        
        if jugador == 'salir':
            print("¡Gracias por jugar!")
            break
            
        if jugador not in opciones:
            print("Opción no válida. Por favor elige: piedra, papel o tijera")
            continue
            
        # Computadora elige al azar
        computadora = random.choice(opciones)
        
        print(f"\nTú elegiste: {jugador}")
        print(f"La computadora eligió: {computadora}")
        
        # Determinar ganador
        if jugador == computadora:
            print("¡Empate!")
        elif (jugador == "piedra" and computadora == "tijera") or \
             (jugador == "papel" and computadora == "piedra") or \
             (jugador == "tijera" and computadora == "papel"):
            print("¡Ganaste!")
        else:
            print("¡La computadora gana!")

# Iniciar el juego
jugar_piedra_papel_tijera()
