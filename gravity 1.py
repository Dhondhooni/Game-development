import pygame
pygame.init()
#pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

player = pygame.image.load (r"Doll.png")
player_alt = pygame.image.load(r"Doll2.jpg")
x = y = t = 0
#clicks = 0

#Doll = pygame.image.load(r'Doll.png')
#Doll = pygame.transform.scale(Doll, (20, 20))

width = 600
height = 500
screen = pygame.display.set_mode((width, height))
running = True

screen.fill((255, 255, 255))
fpsClock = pygame.time.Clock()
fps = 60

while running:   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type in [pygame.KEYDOWN, pygame.KEYUP]:
            print(event.key, event.type)
            
            keys=pygame.key.get_pressed()
            
            if keys[pygame.K_d]:
                x += 5
            if keys[pygame.K_a]:
                x -= 5
            
            if keys[pygame.K_SPACE] and y == 0:
                y = height - player.get_height() 
                #y = 0.01
                #u = 20
                
            #Calculating the height of the player 
            # velocity += pygame.math.Vector2((0, -9.81)) *t
            u = 0
            if y > 0:
              #  print(u,t)
               y += u * t + (1/2 * -9.81 * (t**2))
               t += 1/fps
                           
            #Bounding the player
            x_max = width - player.get_width()
            #y_max = height - player.get_height()
            
            if x <= 0: x = 0
            elif x >= x_max: x = x_max
            
            if y <= 0:
                y = 0
                t = 0
                #u = 0
                screen.blit(player, (x, height - y - player.get_height()))
                
            else:
                screen.blit(player_alt, (x, height - y - player.get_height()))
                
            
            if keys [pygame.K_s]:
                y = y + 5
            if keys [pygame.K_w]:
                y = y - 5
            if keys [pygame.K_d]:
                x = x + 5
            if keys [pygame.K_a]:
                 x = x - 5     
                        
            if x < 0: X = 0    
            if y < 0: y = 0    
                
        screen.blit(player, (x, y))

    pygame.display.flip()
    fpsClock.tick(fps)

pygame.quit()