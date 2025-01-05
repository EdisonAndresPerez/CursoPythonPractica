#Importanciones para el juego 
import pygame
import random
import time

#Inicializamos pygame
pygame.init()

#Colores
blanco = (255,255,255)
negro = (0,0,0)
rojo = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)

#dimensiones de la pantalla
ancho = 600
alto = 400

#creamos la pantalla
pantalla = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("Juego de la serpiente")

#Reloj del juego
reloj = pygame.time.Clock()

# Tamaño de los bloques y velocidad de la serpiente
tamaño_bloque = 10
velocidad_serpiente = 15

# Fuente
fuente = pygame.font.SysFont("bahnschrift", 25)

# Función para mostrar el puntaje
def mostrar_puntaje(puntaje):
    valor = fuente.render("Puntaje: " + str(puntaje), True, rojo)
    pantalla.blit(valor, [10, 10])


#Funcion principal del juego
def game_loop():
    game_over = False
    game_close = False

