 # -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 09:17:55 2020

@author: sergi
"""

import pygame,random,cv2

import numpy as np
import test

def juego():
        pygame.init()
        
        
        size = (800,800)
        
        
        BLACK =(0,0,0)
        
        WHITE =(255,255,255)
        GREEN =(0,255,0)
        RED =(255,0,0)
        BLUE =(0,0,255)
        
        
        #Creacion de ventana
        screen = pygame.display.set_mode(size)
        
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render('COLISION', False, (0, 0, 0))
        
        
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
        while True:
            
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    print("aaaaa")
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
                        
                        
                    
                    
            screen.fill(BLUE)
            
            success,img = camara.read()
            img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            img = np.rot90(img)
            img=pygame.surfarray.make_surface(img)
            
            
            
            
            screen.blit(img,[0,0])
          #LOGICA
            coorX+=x_speed
            coorY+=y_speed
            blanco= pygame.draw.circle(screen,WHITE,((coorX,coorY)),5  )
        
          #FIN LOGICA   
           
            
            for i in range(len(lista_coor)):
                pygame.draw.circle(screen,RED,lista_coor[i],5  )
                lista_coor[i][1]+=1
                if lista_coor[i][1]>size[1]:
                    lista_coor[i][1]=0
                    lista_coor[i][0]=random.randint(0,size[1])
                
                
           
            
           
            
           
            
           
            
           
            
            #DIBUJO
            
          #  for x in range(int(size[0]/10),size[0],int(size[0]/10)):
          #      pygame.draw.line(screen,BLACK,(x,0),(x,size[1]),1)
          #      
          #  for x in range(int(size[1]/10),size[1],int(size[1]/10)):
          #      pygame.draw.line(screen,BLACK,(0,x),(size[0],x),1)
            
            
              #  pygame.draw.line(screen,GREEN,[0,100],[200,300],5)
              #  pygame.draw.rect(screen,BLACK,(100,100,80,80))
             #   pygame.draw.circle(screen,BLACK,(200,200),30)
            
            #FIN DIBUJO
            
            
            #actualizar pantalla
            mouse_pos = pygame.mouse.get_pos()
            
            
            
            
            rojo= pygame.draw.rect(screen,RED,(mouse_pos[0],mouse_pos[1],100,100))
            
            
            if rojo.colliderect(blanco):
                screen.blit(textsurface,(400,400))
               
            pygame.display.flip()
            clock.tick(60)
            
            
            
            
if __name__ == '__main__':
    juego()    
    
    
    
    
    
    
    