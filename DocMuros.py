import pygame
# Clase para los muros
class Muro88:
    
    def __init__(self):
        pass
    #Creamos una lista de muros y sus posiciones
    def CrearMuros():
        muros = []
        for i in range(8):
            for j in range(6):
                muro = pygame.image.load("murorompiendo.png")
                murorect = muro.get_rect()
                murorect.move_ip(105 * i, 45 * J)
                muros.append(murorect)
        
        return muros

    #Comprobamos colisiones de la bola con los muros
    def EliminarMuro():
        for muro in muros:
            if muro.colliderect(ballrect):
                muros.remove(muro)
                speed[1] = -speed[1]

    #Dibujar muro
    def DibujarMuros():
        for muro in muros:
            ventana.blit(pygame.image.load("murorompiendo.png"), muro)
