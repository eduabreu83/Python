#abri um arquivo mp3
import pygame
pygame.init()
pygame.mixer.music.load('C:/Users/Eduardo Abreu/Desktop/soja.mp3')
pygame.mixer.music.play()
pygame.event.wait()

