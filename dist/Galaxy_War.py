import pygame
import random
import math
from pygame import mixer
import io

# Inicializar pyhame
pygame.init()

# Crear pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo e Icono
pygame.display.set_caption("Galaxy's War")
icono = pygame.image.load('Icono.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('Fondo.png')

# Agregar musica
mixer.music.load('fondo_music.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Variables de jugador
img_jugador = pygame.image.load('nave-espacial.png')
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# Variables de enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 6
dificultad = 0

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load('astronave.png'))
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(50, 100))
    enemigo_x_cambio.append(1)
    enemigo_y_cambio.append(50)

# Variables de misil
misiles = []
img_misil = pygame.image.load('misil.png')
misil_x = 0
misil_y = 500
misil_x_cambio = 0
misil_y_cambio = 2.5
misil_visible = False

# Funcion str a byte
def fuente_bytes(fuente):
    with open(fuente, 'rb') as f:
        ttf_bytes = f.read()
    return io.BytesIO(ttf_bytes)

# Puntaje
score = 0
fuente_byte = fuente_bytes('FreeSansBold.ttf')
fuente = pygame.font.Font(fuente_byte, 16)
texto_x = 10
texto_y = 10

# Texto final
fuente_final = pygame.font.Font(fuente_byte, 40)

# Funcion mensaje
def texto_final():
    mi_fuente_final = fuente_final.render('GAME OVER', True, (255,255,255))
    pantalla.blit(mi_fuente_final, (275, 250))

# Funcion mostrar puntaje
def puntaje(x, y):
    texto = fuente.render(f'Score: {score}', True, (255,255,255))
    pantalla.blit(texto, (x, y))

# Funcion jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

# Funcion enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

# Funcion disparar misil
def disparar_misil(x, y):
    global misil_visible
    misil_visible = True
    pantalla.blit(img_misil, (x + 16, y + 10))

# Detectar colisiones
def colision_detectada(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False

# Loop del juego
ejecucion = True

while ejecucion:

    # Imagen de fondo
    pantalla.blit(fondo, (0, 0))

    # Iterar eventos
    for evento in pygame.event.get():

        # Cerrar programa
        if evento.type == pygame.QUIT:
            ejecucion = False

        # Presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -2.5
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 2.5
            if evento.key == pygame.K_SPACE:
                sonido_misil = mixer.Sound('disparo.mp3')
                sonido_misil.play()
                nuevo_misil = {'x':jugador_x, 'y':jugador_y,'velocidad':-5}
                misiles.append(nuevo_misil)
                if not misil_visible:
                    misil_x = jugador_x
                    disparar_misil(misil_x, misil_y)

        # Soltar teclas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # Modificar ubicacion de jugador
    jugador_x += jugador_x_cambio

    # Mantener dentro de los bordes a jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # Modificar ubicacion de enemigo
    for e in range(cantidad_enemigos):

        # Fin del juego
        if enemigo_y[e] > 470:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            misiles.clear()
            sonido_misil.stop()
            texto_final()
            break

        enemigo_x[e] += enemigo_x_cambio[e]

    # Mantener dentro de los bordes a enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 1.2 + dificultad
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -1.2 - dificultad
            enemigo_y[e] += enemigo_y_cambio[e]
        dificultad += 0.000001

        # Colision
        for misil in misiles:
            colision = colision_detectada(enemigo_x[e], enemigo_y[e], misil['x'], misil['y'])
            if colision:
                sonido_golpe = mixer.Sound('golpe.mp3')
                sonido_golpe.play()
                misiles.remove(misil)
                score += 1
                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(50, 100)
                break

        enemigo(enemigo_x[e], enemigo_y[e], e)

    # Movimiento misil
    for misil in misiles:
        misil['y'] +=   misil['velocidad']
        pantalla.blit(img_misil, (misil['x'] + 16, misil['y'] + 10))
        if misil['y'] < 0:
            misiles.remove(misil)

    jugador(jugador_x, jugador_y)

    puntaje(texto_x, texto_y)

    # Actualizar
    pygame.display.update()