from re import X
import pygame
import enum
import numpy as np
pygame.init()

# pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0D,0,0,0,0),(0,0,0,0,0,0,0,0))
#create player
player = pygame.sprite.Sprite()  # <---
img = pygame.image.load((r"Doll.png"))
img = pygame.image.load((r"purple diamond.png"))
img = pygame.image.load((r"green diamond.png"))
img = pygame.image.load((r"blue diamond.png"))

#x = y = t = 0
#clicks = 0

Doll = pygame.image.load(r'Doll.png')
Doll = pygame.transform.scale(Doll, (20, 20))

# Necessary definitions
player.image = img
player.rect = img.get_rect()

# Player position
player.rect.x = 0
player.rect.y = 0

#class eneymy(pygame.sprite.Sprite):
#def _init_(self, image, pos):
 #   super() ._init_() #Initialise base class        self.image = img
  #  self.rect = image.get_rect()
   # self.pos = pos
    #self.health = 100

    #override "update" method of sprite class
#def update(self):
 #     self.rect.x = self.pos.x
  #    self.rect.y = self.pos.y
      
#Create enemy
#enemy = pygame.sprite.Sprite() #<---
#img = pygame.image.load ((r"Doll2.jpg"))

#enemy.image = img
#enemy.rect = img.get_rect()
#enemy.rect.x = 0
#enemy.rect.y = 0
#enemy_health = 100

# Sprite group
#all_group = pygame.sprite.Group()
#all_group.add(player)
#all_group.add(enemy)

#class diamond:
 #   def _init_ (self, color):
  #      self.color = color
          
#class purple(diamond):
 #      def _init_ (self, color):
  #       super() ._init_(color) 
            
#class green(diamond):
 #       def _init_ (self, color):
  #        super() ._init_(color)        

#class blue(diamond):
 #       def _init_ (self, color):
  #         super() ._init_(color)  
      
# if a diamond is picked
   #     def color(self):     
    #       print("You won")

class hit(enum.Enum):
    outside = 1
    inside = 2
    none = 3
    
class square():
    def _init_(self, surface, colour, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        
        self.point = []
        
        horizontals = np.linspace(x1, x1 + x2, x1 + x2)
        verticals = np.linspace(y1, y1 + y2, y1 + y2)
        
        self.v1 = [pygame.math.Vector2((x1, v)) for v in verticals]
        self.h1 = [pygame.math.Vector2((h, y1 + y2)) for h in horizontals]
        self.v2 = [pygame.math.Vector2((x1 + x2, v)) for v in verticals]
        self.h2 = [pygame.math.Vector2((h, y1)) for h in horizontals]
        
        pygame.draw.rect(surface, colour, (x1, y1, x2, y2), 1)
            
    def distance(self, pos):
        return min([np.linalg.norm(pos-p) for p in self.points])
    
    def normal(self, pos):
        normals = [(-1, 0), (0, 1), (0, -1), (1, 0)]
        return 10 * pygame.math.Vector2(normals[[pos in e for e in [self.v1, self.h1, self.v2, self.h2]].index(True)])
        
    def tangent(self, pos):
        n = self.normal(pos)
        return n.rotate(90)
    
class circle():
    def __init__(self, surface, colour, r, x, y):
        self.r = r
        self.x = x
        self.y = y
        self.centre = pygame.math.Vector2((x, y))
        
        self.points = []
        for t in np.linespace(0, 2*np.pi, 100):
            self.points.append((r*np.cos(t)+x, r*np.sin(t)+y))
        pygame.draw.aalines(surface, colour, True, self.points)
        
    def distance(self, pos):
        return pos.distance_to(self.centre) - self.r
        
    def normal(self, pos):
        return pos - self.centre
    
    def tangent(self, pos):
        n = self.normal(pos)
        return n.rotate(90)
    
class object(pygame.sprite.Sprite):
    def __init__(self, surface, pos, vel, image):
        super().__init__()
        self.pos = pygame.math.Vector2(pos)
        self.vel = pygame.math.Vector2(vel)
        self.xt = 0
        self.yt = 0
        self.image = image.convert_alpha()
        self.rect = self.image.get_rect()
        self.surface = surface

    def check_keys(self, surface): pass #Implement in subclasses

    def gravity(self):
        self.vel.y = self.vel.y + (-2 * self.yt)

    #Check if it will be outside in the next frame (check if it collides directly with the boundary instead of going oustide)
    def ceiling_collide(self, surface):
        y_max = surface.get_height() - self.image.get_height()

        #Get direction vector to tell which direction it was going when it hit the boundary
        #Find normal of boundary
        
        if self.pos.y > y_max:
            self.vel.y = -self.vel.y/2
            self.yt = 0
            self.y = y_max
            return True
        
        return False

    def floor_collide(self, surface):
        y_min = surface.get_rect()[1]

        if self.pos.y <= y_min:
            self.yt = 0
            self.pos.y = y_min
            self.vel.y = 0
            return True

        return False

    def right_collide(self, surface):
        x_min = surface.get_rect()[1]

        if self.pos.x <= x_min:
            self.pos.x = x_min
            return True

        return False

    def left_collide(self, surface):
        x_max = surface.get_width() - self.image.get_width()

        if self.pos.x >= x_max:
            self.pos.x = x_max
            return True

        return False

    def collision(self, surface):
        self.ceiling_collide(surface)
        self.floor_collide(surface)
        self.left_collide(surface)
        self.right_collide(surface)

    def update(self, dt):
        self.gravity()
        self.check_keys(self.surface)
        self.pos += self.vel

        #print(self.vel)
        
        self.collision(self.surface)
        self.rect.top = self.surface.get_height() - self.pos.y - self.image.get_height()
        self.rect.left = self.pos.x
        
        self.yt += dt
        self.xt += dt

class player(object):
    def __init__(self, surface, pos, vel, images):
        super().__init__(surface, pos, vel, images[0])
        self.acc = 3
        self.max_vel = 5

    def check_keys(self, surface):
        keys=pygame.key.get_pressed()

        if not (keys[pygame.K_d] or keys[pygame.K_a]):
            self.vel.x = 0
            self.xt = 0
            
        elif keys[pygame.K_d] and keys[pygame.K_a]:
            self.vel.x = 0
            self.xt = 0
            
        elif keys[pygame.K_d]:
            if self.vel.x < self.max_vel:
                self.vel.x = self.vel.x + (self.acc * self.xt)
            else:
                self.vel.x = self.max_vel
            
        elif keys[pygame.K_a]:
            if self.vel.x > -self.max_vel:
                self.vel.x = self.vel.x + (-self.acc * self.xt)
            else:
                self.vel.x = -self.max_vel

        if keys[pygame.K_w] and self.floor_collide(surface):
            self.vel.y = 10
            
screen = pygame.display.set_mode((600, 500))
running = True
pygame.display.set_caption('Gem Collector')

screen.fill((255, 255, 255))
fpsClock = pygame.time.Clock()
fps = 60
dt = 1/fps  

player_imgs = [pygame.image.load (r"Doll.png"), pygame.image.load(r"Doll2.jpg")]                
            
p = player (screen, (0,0), (0,0), player_imgs)
all_groups = pygame.sprite.Group()
all_groups.add(p)

i = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    all_groups.update(dt)
    all_groups.draw(screen)            
      
    c = circle(screen, (0,0,0), 100, 200, 200)
    p = pygame.math.Vector2(c.points[i])
    pygame.draw.aalines(screen, (255,0,0), True, (p,p+c.tangent(p)))
    if i < 999: i += 1
    else: i = 0
    
    #s = square(screen, (0,0,0), 0, 100, 0, 100)
    #p = pygame.math.Vector2((100,100))
    #pygame.draw.aalines(screen, (255,0,0), True, (p,p+s.normal(p)))


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
       

      
    #all_group.update()  # Update all the sprites in the group
    #all_group.draw()  # Draw the sprites onto the screen

    pygame.display.flip()
    fpsClock.tick(fps)

pygame.quit()
