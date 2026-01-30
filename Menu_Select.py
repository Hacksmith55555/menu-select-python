from pick import pick
import pygame, sys, time

pygame.mixer.init()

pygame.mixer.music.load("")

title = 'Please choose your favorite programming language: '
options = ['Java', 'JavaScript', 'Python', 'PHP', 'C++', 'Erlang', 'Haskell']

option, index = pick(options, title, indicator='=>', default_index=2)

