import pygame
pygame.init

screen = pygame.display.set_mode((600, 500))
running = True

screen.fill((255, 255, 255))
fpsClock = pygame.time.Clock()
fps = 60
dt = 1/fps #time elapsed betwwn mainloop iterations
time = 0 #total time elapsed since mainlopp started ruuning

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type in [pygame.KEYDOWN]: #pygame.KEYUP
            if event.key == pygame.K_r:
                time = 0 #reset timer

        #keys = pygame.key.get_pressed()

       # if keys[pygame.K_s]:
       #     player.rect.y += 5
        # if keys[pygame.K_w]:
        #    player.rect.y -= 5
        #if keys[pygame.K_d]:
        #    player.rect.x += 5
        #if keys[pygame.K_a]:
        #    player.rect.x -= 5

       # if player.rect.x < 0:
        #    player.rect.x = 0
       # if player.rect.y < 0:
        #    player.rect.y = 0

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

       # all_group.update()  # Update all the sprites in the group
        #all_group.draw(screen)  # Draw the sprites onto the screen

time += dt #short hand for time = time + dt
second = round (time,0)
print (seconds, "seconds have passed")

        pygame.display.flip()
        fpsClock.tick(fps)

pygame.quit()
