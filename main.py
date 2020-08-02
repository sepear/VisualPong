import pygame,cv2
import numpy as np

size_X= 640
size_Y= 480

frameWidth = 640
frameHeight = 480

largo=300
ancho=60



rect_width=10
rect_height=50

x_red=int(frameWidth/8)
x_blue=frameWidth-x_red

y_red= int(frameHeight/2)
y_blue= int(frameHeight/2)


BLACK =(0,0,0)
        
WHITE =(255,255,255)
GREEN =(0,255,0)
RED =(255,0,0)
BLUE =(0,0,255)

def main():
    pygame.init()
    size = (size_X,size_Y)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    
    ##CONFIGURAR LECTURA DE CAMARA
    camara = cv2.VideoCapture(0)
    success=True
    
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('INICIAR PARTIDA', False, WHITE)
    
    screen.fill((255,0,0))
     
    while True:
    
        
    
        mouse_pos = pygame.mouse.get_pos()
    
        
    
        success,img = camara.read()
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img = np.rot90(img)
        img=pygame.surfarray.make_surface(img)
        
        
        

        screen.blit(img,[0,0])
        
        
        red_rect = pygame.draw.rect(screen,RED,(x_red,y_red,rect_width,rect_height))
         
        blue_rect= pygame.draw.rect(screen,BLUE,(x_blue,y_blue,rect_width,rect_height))
         
        
        caja = pygame.draw.rect(screen,RED,(   int((size_X/2)-(largo/2))   ,int(size_Y/1.25),largo,ancho))
        screen.blit(textsurface,(caja.x,caja.y))
        
        if caja.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                screen.fill(BLACK)
      
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == '__main__':
    main()