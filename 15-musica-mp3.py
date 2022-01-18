import pygame
'''ou importa o playsound'''
pygame.init()
pygame.mixer.music.load('nome do audio.mp3')
pygame.mixer.music.play()
pygame.event.wait()
