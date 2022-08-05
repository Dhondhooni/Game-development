import pygame
pygame.init()
#pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

player = pygame.image.load (r"Doll.png")
x = y = 0
#clicks = 0

#Doll = pygame.image.load(r'Doll.png')
#Doll = pygame.transform.scale(Doll, (20, 20))

screen = pygame.display.set_mode((700, 600))
running = True

fpsClock = pygame.time.Clock()
fps = 60

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type in [pygame.KEYDOWN, pygame.KEYUP]:
            print(event.key, event.type)
            
            keys=pygame.key.get_pressed()
            
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
                
    screen.fill((255, 255, 255))
    screen.blit(player, (x, y))

    pygame.display.flip()
    fpsClock.tick(fps)

