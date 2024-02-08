import pygame

# Iniciamos PyGame y creamos la ventana
pygame.init()
ventana = pygame.display.set_mode((800,600))
pygame.display.set_caption("ARKANOID JORGE Y RODRIGO")
fuente = pygame.font.Font(None, 60)

# Creamos la bola
ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
speed = [3,3]
ballrect.move_ip(0,0)

# Creamos el bate
bate = pygame.image.load("bate.png")
baterect = bate.get_rect()
baterect.move_ip(350,550)

# Iniciamos el bucle principal del juego
jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    # Movimiento barra
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and baterect.left > 0:
        baterect = baterect.move(-5,0)
    if keys[pygame.K_RIGHT] and baterect.right < ventana.get_width():
        baterect = baterect.move(5,0)
    
    # Si la barra y la bola chocan aumenta la velocidad de la bola y cambia de dirección
    if baterect.colliderect(ballrect):
        speed[1] = float(-speed[1] * 1.05)
        speed[0] = float(speed[0] * 1.05)
        print(speed)

    # Cuando la bola choque con algún borde de la ventana cambia dirección
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0:
        speed[1] = -speed[1]

    # Si la bola toca el borde inferior se muestra GAME OVER y se detiene el juego
    if ballrect.bottom > ventana.get_height():
        texto = fuente.render("Game Over", True, (125,125,125))
        texto_rect = texto.get_rect()
        texto_x = ventana.get_width() / 2 - texto_rect.width / 2
        texto_y = ventana.get_height() / 2 - texto_rect.height / 2
        ventana.blit(texto, [texto_x, texto_y])
    
    # Asignamos color a la ventana y generamos en pantalla la bola y la barra (para iniciar el juego)
    else:
        ventana.fill((0, 0, 0))
        ventana.blit(ball, ballrect)
        ventana.blit(bate, baterect)

    # Generamos los elementos del juego y asignamos los FPS
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
