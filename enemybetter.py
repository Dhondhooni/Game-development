import pygame
pygame.init

# pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0D,0,0,0,0),(0,0,0,0,0,0,0,0))
#create player
player = pygame.sprite.Sprite()  # <---
img = pygame.image.load((r"Doll.png"))
img = pygame.image.load((r"purple diamond.png"))
img = pygame.image.load((r"green diamond.png"))
img = pygame.image.load((r"blue diamond.png"))

#x = y = t = 0
#clicks = 0

#Doll = pygame.image.load(r'Doll.png')
#Doll = pygame.transform.scale(Doll, (20, 20))

# Necessary definitions
player.image = img
player.rect = img.get_rect()

# Player position
player.rect.x = 0
player.rect.y = 0

class eneymy(pygame.sprite.Sprite):
  def _init_(self, image, pos):
    super() ._init_() #Initialise base class
    self.image = img
    self.rect = image.get_rect()
    self.pos = pos
    self.health = 100
    
    #override "update" method of sprite class
    def update(self):
      self.rect.x = self.pos.x
      self.rect.y = self.pos.y
      
#Create enemy
enemy = pygame.sprite.Sprite() #<---
img = pygame.image.load ((r"Doll2.jpg"))

enemy.image = img
enemy.rect = img.get_rect()
enemy.rect.x = 0
enemy.rect.y = 0
enemy_health = 100

# Sprite group
all_group = pygame.sprite.Group()
all_group.add(player)
all_group.add(enemy)

screen = pygame.display.set_mode((600, 500))
running = True

screen.fill((255, 255, 255))
fpsClock = pygame.time.Clock()
fps = 60

class diamond:
    def _init_ (self, color):
        self.color = color
          
class purple(diamond):
       def _init_ (self, color):
         super() ._init_(color) 
            
class green(diamond):
        def _init_ (self, color):
          super() ._init_(color)        

class blue(diamond):
        def _init_ (self, color):
           super() ._init_(color)  
      
# if a diamond is picked
        def color(self):     
           print("You won")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type in [pygame.KEYDOWN, pygame.KEYUP]:
            print(event.key, event.type)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_s]:
            player.rect.y += 5
        if keys[pygame.K_w]:
            player.rect.y -= 5
        if keys[pygame.K_d]:
            player.rect.x += 5
        if keys[pygame.K_a]:
            player.rect.x -= 5
            
       # screenRect = screen.get_rect() #A "rect" object
        
        #Using .contains() method
        #if not screenRect.contains (player.rect):
          #  print("Player out of bounds!!!")
            
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

            #if keys [pygame.K_s]:
             # y = y + 5
            #if keys [pygame.K_w]:
             # y = y - 5
            #if keys [pygame.K_d]:
             # x = x + 5
            #if keys [pygame.K_a]:
             #   x = x - 5

            #if x < 0: X = 0
            #if y < 0: y = 0

        #screen.blit(player, (x, y))
       

      
        all_group.update()  # Update all the sprites in the group
        all_group.draw(screen)  # Draw the sprites onto the screen

        pygame.display.flip()
        fpsClock.tick(fps)

pygame.quit()
