# -*- coding: utf-8 -*-

import pygame,pygame_menu

from VisualPong import pongGame

speed=9

def start_the_game():
    pongGame(frameWidth,frameHeight,screen,speed)
    
def set_speed(value,my_speed):
    global speed
    speed=my_speed
    





if __name__ == '__main__':
    
    while True:
    
        frameWidth = 640
        frameHeight = 480
        
        
        
        
        
        
        pygame.init()
        screen = pygame.display.set_mode((frameWidth, frameHeight))
        
        menu = pygame_menu.Menu(frameHeight,frameWidth,'VisualPong')
        #poner theme
        menu.add_selector('Speed:', [('Slow', 5), ('Normal', 12), ('Fast', 20), ('Extreme', 30)], onchange=set_speed)
        menu.add_button('Play', start_the_game)
        menu.add_button('Quit', pygame_menu.events.EXIT)
        
        menu.mainloop(screen)