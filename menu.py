# -*- coding: utf-8 -*-

import pygame,pygame_menu

from VisualPong import pongGame

def start_the_game():
    print("entró")
    pongGame(frameWidth,frameHeight,screen)





if __name__ == '__main__':
    
    while True:
    
        frameWidth = 640
        frameHeight = 480
        
        
        
        
        
        
        pygame.init()
        screen = pygame.display.set_mode((frameWidth, frameHeight))
        
        menu = pygame_menu.Menu(frameHeight,frameWidth,'VisualPong')
        #poner theme
        
        print("llego")
        menu.add_button('Play', start_the_game)
        menu.add_button('Quit', pygame_menu.events.EXIT)
        
        menu.mainloop(screen)