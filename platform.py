import pygame
from random import randint
pygame.init

# pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
#Create player
#player = pygame.sprite.Sprite()  # <---
img = pygame.image.load((r"Doll.png"))
#x = y = t = 0
#clicks = 0

#Doll = pygame.image.load(r'Doll.png')
#Doll = pygame.transform.scale(Doll, (20, 20))

# Necessary definitions
player.image = img
player.rect = img.get_rect()
player = player (image, 200, 200)

# Player position
player.rect.x = 0
player.rect.y = 0

class player2(pygame.sprite.Sprite):
  def _init_(self,image, pos):
    super().init_() #Initialise base class
    self.image = image
    self.rect = image.get_rect()
    self.rect.x = self.pos.x
    self.rect.y = self.pos.y
    self.last_x = 0
    self.last_y = 0
    #self.pos = pos
    #self.health = 100
    
    #override "updage" method of sprite class
    #def update(self):
     # self.rect.x = self.pos.x
      #self.rect.y = self.pos.y
      
      #Create player2 (enemy)
      player2 = pygame.sprite.Sprite()
      img2 = pygame.image.load(r"Doll2.jpg")
      pos = pygame.math.Vector2 ((0,0))
      player2 = player2(image,pos)
      
      #player2.image = img2
      #player2.rect = img2.get.rect()
#player2.rect.x = 0
#player2.rect.y = 0
#player2_health = 100

# Sprite group
#group = pygame.sprite.Group()
#group.add(player2)
#group.add(player)

#Create group
all_group = pygame.sprite.Group()
all_group.add(player)
all_group.add(player2)

screen = pygame.display.set_mode((600, 500))
running = True

screen.fill((255, 255, 255))
fpsClock = pygame.time.Clock()
fps = 60

        #if event.type in [pygame.KEYDOWN, pygame.KEYUP]:
           # print(event.key, event.type)

     
def update (self, keys):
        if keys[pygame.K_s]:
            player.rect.y += 5
            player.rect.y += self.last_y
            
        if keys[pygame.K_w]:
            player.rect.y -= 5
            player.rect.y += self.last_y
            
        if keys[pygame.K_d]:
            player.rect.x += 5
            player.rect.x += self.last_x
            
        if keys[pygame.K_a]:
            player.rect.x -= 5
            player.rect.x += self.last_x

        if player.rect.x < 0:
            player.rect.x = 0
        if player.rect.y < 0:
            player.rect.y = 0

          # if keys[pygame.K_d]:
            #x += 5
         # if keys[pygame.K_a]:
            # x -= 5

          # if keys[pygame.K_SPACE] and pos.y == 0:
            #pos.y = height - player.get_height()
            #velocity.y = 0
            #y = 0.01
            #u = 20

           # Calculating the height of the player
          #velocity += pygame.math.Vector2((0, -9.81)) *t
          #print(f"position: {pos}")
          #u = 0
          # if y > 0:
            #  print(u,t)
            # y += u * t + (1/2 * -9.81 * (t**2))
          #t += 1/fps
          #pos += velocity

          # Bounding the player
          #x_max = width - player.get_width()
          #y_max = height - player.get_height()

          #if pos.x <= 0: pos.x = 0
          # elif pos.x >= x_max: pos.x = x_max

          # if pos.y <= 0:
            # pos.y = 0
            #velocity.y = 0
            # t = 0
            #screen.blit(player, (pos.x, height - pos.y - player.get_height()))

          # else:
           #   screen.blit(player_alt, (pos.x, height - pos.y - player.get_height()))

         # if keys [pygame.K_s]:
          #    y = y + 5
          # if keys [pygame.K_w]:
           #   y = y - 5
          # if keys [pygame.K_d]:
           #   x = x + 5
          # if keys [pygame.K_a]:
            #    x = x - 5

           #if x < 0: X = 0
           #if y < 0: y = 0

       # screen.blit(player, (x, y))
  #Enemy = player2    
class player2 (pygame.sprite.Sprite):
    def _init_(self, image, x, y):
        super()._init_()
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.t = 0
        
def update(self, keys):
    self.t += 1/60 #update the animation time
    
    if self.t >=1:
        self.rect.x += randint (-10,10) #move sprite in random direction
         self.t = 0 #reset the animation time
         
         print(self, self.t)
         
    image = pygame.image.load (r"Doll.png")
    player = player(image 200,200)  
    
    class Platform(pygame.Rect):
        def _init_(self):
            super()._init_(500, 250, 100, 20)
            self.color = (255, 0, 255)
            
        def update(self, screen):
            self.t += 1/60
            self.x -= 5 #Move platform to the left
            
            if self.x <+ -(self.width +100):
                self.x = 600
                self.t = 0
                
            print(self, self.t)
            pygame.draw.rect(screen, self.color, self)
            
    plat = Platform() 
                       
    all_group = pygame.sprite.Group()
    all.group.add(player)
    all.group.add(player2)  
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
             running = False
             
    keys = pygame.key.get_pressed()

    #all_group.update()  # Update all the sprites in the group
    #all_group.draw(screen)  # Draw the sprites onto the screen

    pygame.display.flip()
    fpsClock.tick(fps)

pygame.quit()
