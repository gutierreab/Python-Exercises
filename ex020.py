# Programa para realizar a importação de uma música, em .mp3, utilizando PyGame.

import pygame
pygame.init()
pygame.mixer.music.load('rpg.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

# Criado por Amanda Borges Gutierre, em 17 de Agosto de 2022.
