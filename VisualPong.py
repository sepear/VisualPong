# -*- coding: utf-8 -*-

import numpy as np
from getContours import getContours
import pygame,cv2,random



    
    


def pongGame(frameWidth,frameHeight,screen,speed):
    RED =(0,0,255)
    BLUE =(255,0,0)
    PINK=(255,105,180)
    GREEN=(50,205,50)
   
    
    rect_width=10
    rect_height=50
    
    x_pink=frameWidth//8
    x_green=frameWidth-x_pink
    
    y_pink= frameWidth//2
    y_green= frameHeight//2
    
    x_ball=frameWidth//2
    y_ball=frameHeight//2
    
    speed_x=0
    speed_y=0
    
    goals_L=0
    goals_R=0
    
    font = pygame.font.Font(None, 60)
    text = font.render(f"{goals_L}-{goals_R}", True, (0,0,0))
    text_rect = text.get_rect(center=(frameWidth//2, frameHeight//2))
    

    ###Parametros de las mascaras
    
    h_min_pink=162
    h_max_pink=179
    s_min_pink=98
    s_max_pink=255
    v_min_pink=188
    v_max_pink=255
    
    h_min_green=41
    h_max_green=67
    s_min_green=88
    s_max_green=255
    v_min_green=0
    v_max_green=255
    
    
    cap = cv2.VideoCapture(0)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
    
    
    #pygame.init()
    #screen = pygame.display.set_mode((frameWidth,frameHeight))
    clock = pygame.time.Clock()
    
    if random.random()>0.5:
        speed_x-=speed
        speed_y-=speed
    else:
        speed_x+=speed
        speed_y+=speed
    
 
    
    while True:
         _, img = cap.read() 
         
         imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
         
         img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
         img = np.rot90(img)
         img=pygame.surfarray.make_surface(img)
         screen.blit(img,[0,0])
         #construimos las mascaras
         
         
         
         lower_pink = np.array([h_min_pink, s_min_pink, v_min_pink])
         upper_pink = np.array([h_max_pink, s_max_pink, v_max_pink])
         mask_pink = cv2.inRange(imgHsv, lower_pink, upper_pink)
         
         
         lower_green = np.array([h_min_green, s_min_green, v_min_green])
         upper_green = np.array([h_max_green, s_max_green, v_max_green])
         mask_green = cv2.inRange(imgHsv, lower_green, upper_green)
         
         
         for event in pygame.event.get():
             if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                     goals_L=0
                     goals_R=0
                     x_ball=frameWidth//2
                     y_ball=frameHeight//2
                     speed_x *= -1
                     speed_y *= -1
         
         
         
         
         
         
         
         
         
         
         #si hay deteccion, actualizamos posicion
         _, y_pink_T=getContours(mask_pink)
         if y_pink_T !=-1:
             y_pink= y_pink_T
                 
                 
         _, y_green_T=getContours(mask_green)
         if y_green_T !=-1:
             y_green= y_green_T
             
        
        
        #fisicas pelota:
         if y_ball > frameHeight or y_ball < 0:
            speed_y *= -1
        
        
         if x_ball > frameWidth:
             
             goals_L+=1
             x_ball=frameWidth//2
             y_ball=frameHeight//2
             speed_x *= -1
             speed_y *= -1
    
    	# Revisa si la pelota sale del lado izquierdo
         if x_ball < 0:
             
             goals_R+=1
             x_ball=frameWidth//2
             y_ball=frameHeight//2
             speed_x *= -1
             speed_y *= -1
     
        
     
         x_ball+=speed_x
         y_ball+=speed_y    
         pink_rect = pygame.draw.rect(screen,PINK,(x_pink,y_pink,rect_width,rect_height))
         
         green_rect= pygame.draw.rect(screen,GREEN,(x_green,y_green,rect_width,rect_height))
        
         #ball= pygame.draw.circle(screen,BLUE,(x_ball,y_ball),8)
         ball= pygame.draw.rect(screen,RED,(x_ball,y_ball,14,14))
        
        #colision
         if ball.colliderect(pink_rect) or ball.colliderect(green_rect):
            speed_x*=-1
            
            
         #show the result   
         text = font.render(f"{goals_L}-{goals_R}", True, (0,0,0))
         screen.blit(text, text_rect)
         
         
         
         print((goals_R,goals_L))
         pygame.display.flip()
         clock.tick(60)
         
    pygame.quit()

if __name__ == '__main__':
    print("Execute from menu pls")