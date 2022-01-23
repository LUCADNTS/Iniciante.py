'''faça um programa em python que abra
e reproduza o audio de um arquivo mp3'''

import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex021.mp3') # aqui voce pode alterar para qualquer tipo de arquivo.mp3 que preferir.
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()
