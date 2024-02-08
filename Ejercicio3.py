import pygame

pygame.init()
ventana = pygame.display.set_mode((800,600))
pygame.display.set_caption("ARKANOID JORGE Y RODRIGO")
fuente = pygame.font.Font(None, 60)

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
speed = [3,3]
ballrect.move_ip(0,0)

bate = pygame.image.load("bate.png")
baterect = bate.get_rect()
baterect.move_ip(350,550)

jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and baterect.left > 0:
        baterect = baterect.move(-5,0)
    if keys[pygame.K_RIGHT] and baterect.right < ventana.get_width():
        baterect = baterect.move(5,0)
    
    if baterect.colliderect(ballrect):
        speed[1] = float(-speed[1] * 1.05)
        speed[0] = float(speed[0] * 1.05)
        print(speed)

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0:
        speed[1] = -speed[1]

    if ballrect.bottom > ventana.get_height():
        texto = fuente.render("Game Over", True, (125,125,125))
        texto_rect = texto.get_rect()
        texto_x = ventana.get_width() / 2 - texto_rect.width / 2
        texto_y = ventana.get_height() / 2 - texto_rect.height / 2
        ventana.blit(texto, [texto_x, texto_y])
    else:
        ventana.fill((0, 0, 0))
        ventana.blit(ball, ballrect)
        ventana.blit(bate, baterect)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
