from re import X
from tkinter import Y
from typing_extensions import Self
import pygame
import enum
import numpy as np
pygame.init


class hit (enum.Enum) :
    outside = 1
    inside = 2
    none = 3
    
class square () :
    def __init__(self , surface , colour , x1, x2, y1, y2 ) :
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        
        self.points = []
        
        horizontals = np.linspace (x1, x1 + x2, x1 + x2)
        verticals = np.linspace (y1, y1 + y2, y1 + y2)
        
        self.vl = [pygame.math.Vector2((x1, v)) for v in verticals]
        self.hl = [pygame.math.Vector2((h, y1 = y2)) for h in horizontals]
        self.v2 = [pygame.math.Vector2((x1 + x2,v)) for v in verticals]
        self.h2 = [pygame.math.Vector2((h, y1)) for h in horizontals]
         
        pygame .draw .rect (surface, colour, (x1, y1, x2, y2,) 1)
        
        def distance (self,pos):
            return min ([np. linalg . norm (pos-p) for p in self. points])
        def normal (self, pos ):
            normals = [(-1, 0), (0, 1), (0 ,-1), (1, 0)]
            return 10 * pygame.math.Vector2(normals[[pos in e for e in [self,v, self.h1, self.v2, sel.h2]].index(True)])
        
        def tangent(self.pos):
            n = self.normal(pos)
            return n.rotate(90)
        
    class circle():
        def _init_(self, surface, colour, r, x, y):
            self.r = r
            self.x = x
            self.y = y
            self.center = pygame.mat.Vector2((x,y))
            
            self.points =[]
            for t in np.linespace(0, 2*np.pi, 1000): self.points.append((r*np.cos(t)+x,r*np.sin(t)+y))
            pygame.draw.aalines(surface, colour, True, self.points)
            
        def distance(self, pos):
            return pos.distance_to(self.centre) - self.r
        def normal(self, pos):
            return pos - self.center
        def tangent(self, pos):
            n = self.normal(pos)
            return n.rotate(90)
        
    class object(pygame.sprite.Sprite):
        def _init_(self, surface, pos, vel, image):
            super()._init()
            self.pos = pygame.math.Vector2(pos)
            self.rect = self.image.get.rect()
            self.surface = surface
            
        def check_keys(self, surface): pass 
        #Implement in subclasses
        
        def gravity(self):
            self.vel.y = self.vel.y + (-2 * self.yt)
            
       #Check if it will be outside in the next frame (check if it collides directly with the boundary instead of going ourside)
        def ceiling_collide(self, surface):
           y_max = surface.get_height() - self.image.get.height()
           
        #Get direction vector to tell which direction it was goign when it hit the boundary
        #Find normal of boundary
        
            if self.pos.y > y_max:
             self.vel.y = - self.vel.y/2
             self.yt = 0
             self.y = y_max
             return True
        
            return False
    
        def floor_collide(self, surface):
            y_min = surface.get_rect() [1]
            
            if self.pos.y <= y_min:
                self.yt = 0
                self.pos.y = y_min
                self.vel.y = 0
                return True
            
            return False
        
        def righ_collide(self, surface):
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
            self.pos += self.pygame.freetype.vertical
            
            #print(sel.vel)
            
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

screen = pygame.display.set_mode((600, 400))
running = True

fps_clock = pygame.time.Clock()
fps = 60
dt = 1/fps

player_imgs = [pygame.image.load(r"player.png"),
               pygame.image.load(r"player3.png")]

p = player(screen, (0,0), (0,0), player_imgs)
all_groups = pygame.sprite.Group()
all_groups.add(p)

i = 0
while running:
    screen.fill((255, 255, 255))

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

    pygame.display.flip()
    fps_clock.tick(fps)

pygame.quit()

