 # -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 09:17:55 2020

@author: sergi
"""

import pygame,random,cv2

import numpy as np

from test import getContours,findColor

def juego():
        pygame.init()
        pygame.mouse.set_visible(False)
        
        size = (640,480)
        color= [[114,128,142,255,73,255],[48,78,56,188,64,255]]
        size_X= 640
        size_Y= 480

        largo=300
        ancho=60
        
        BLACK =(0,0,0)
        
        WHITE =(255,255,255)
        GREEN =(0,255,0)
        RED =(255,0,0)
        BLUE =(0,0,255)
        
        
        
        
        #player.set_colorkey
        
        #Creacion de ventana
        screen = pygame.display.set_mode(size)
        
        pygame.font.init()
        
        #player = pygame.image.load("player.png").convert()
        
        
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(' INICIAR PARTIDA', False, (0, 0, 0))
        
        
        #pygame.mouse.set_visible(1)
        
        #Control del reloj
        
        
        clock = pygame.time.Clock()
        
        
        
        
        lista_coor=list()
            
        for i in range(20):
            num=random.randint(0,size[1])
            num2=random.randint(0,size[1])
            lista_coor.append([num,num2]) 
        
        
        
        y_speed=0
        x_speed=0
        coorX=50
        coorY=50
        
        camara = cv2.VideoCapture(0)
        camara.set(10,150)
        while True:
            
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        x_speed=-3
                    if event.key == pygame.K_d:
                        x_speed=3
                        
                    if event.key == pygame.K_w:
                        y_speed=-3
                    if event.key == pygame.K_s:
                        y_speed=3    
                 
                    
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        x_speed=0
                    if event.key == pygame.K_d:
                        x_speed=0
                    if event.key == pygame.K_w:
                        y_speed=0
                    if event.key == pygame.K_s:
                        y_speed=0
                        
                        
                    
                    
           # screen.fill(BLUE)
            
            success,img = camara.read()
            
            
            
          
           
            #
            
            
            x,y=findColor(img)
            
            img = np.rot90(img)
            
            img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            
            img=pygame.surfarray.make_surface(img)
            
            
            mouse_pos = pygame.mouse.get_pos()
            
            print("x:",x,"y:",y)
            screen.blit(img,[0,0])
            
          #LOGICA
            #coorX+=x_speed
            #coorY+=y_speed
       #     blanco= pygame.draw.circle(screen,WHITE,((coorX,coorY)),5  )
        
          #FIN LOGICA   
           
            
            #for i in range(len(lista_coor)):
            #    pygame.draw.circle(screen,RED,lista_coor[i],5  )
            #    lista_coor[i][1]+=1
            #    if lista_coor[i][1]>size[1]:
            #        lista_coor[i][1]=0
            #        lista_coor[i][0]=random.randint(0,size[1])
                
                
           
            
           
            
           
            
           
            
           
    
            #actualizar pantalla
            
            
            
            
            
            
            
            
            #if rojo.colliderect(blanco):
             #   screen.blit(textsurface,(400,400))
               
                
            caja = pygame.draw.rect(screen,(255,119,0),(   int((size_X/2)-(largo/2))   ,int(size_Y/1.25),largo,ancho))
           
            
           
            rojo= pygame.draw.rect(screen,RED,(mouse_pos[0],mouse_pos[1],50,50))
        
            if caja.colliderect(rojo):
                caja = pygame.draw.rect(screen,(255,171,0),(   int((size_X/2)-(largo/2))   ,int(size_Y/1.25),largo,ancho))
                rojo= pygame.draw.rect(screen,RED,(mouse_pos[0],mouse_pos[1],50,50))
                if pygame.mouse.get_pressed()[0]:
                    
                    screen.fill(prueba())
                    
                    
                    
                   
            screen.blit(textsurface,(caja.x,caja.y))
            
            
            
            pygame.display.flip()
            clock.tick(60)
            
            
            
            
if __name__ == '__main__':
    juego()    
    
    
    
    
    
    
    