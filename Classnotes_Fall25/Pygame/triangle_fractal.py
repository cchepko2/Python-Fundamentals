import pygame, math, random
pygame.init()           # prepare the pygame module for use

# Create a new surface and window.
surface_size_x = 1000   # Pixels X
surface_size_y = 700    # Pixels Y
main_surface = pygame.display.set_mode((surface_size_x,surface_size_y))
my_clock = pygame.time.Clock()

pt1 = (surface_size_x/2, 0)
pt2 = (0, surface_size_y)
pt3 = (surface_size_x, surface_size_y)
vertices = [pt1, pt2, pt3]
point = (0,0)

def half_way(point, vertex):
    x = int((vertex[0]-point[0])//2)
    y = int((vertex[1]-point[1])//2)
    return (x,y)

def gameloop():
    run = True

    old_pt = (0,0)

    while run:

        # Handle evente from keyboard, mouse, etc.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYUP:
                if(event.key == pygame.K_ESCAPE):
                    run = False

        # Draw everything
        #main_surface.fill((30, 0, 30)) #fill background color
        # Draw stuff
        color = (0,0,255)
        p1 = (0,0)
        p2 = (surface_size_x,surface_size_y)
        #pygame.draw.line(main_surface, color, p1, p2)
        vertex = random.choice(vertices)
        new_pt = half_way(old_pt, vertex)
        plot_pt = (new_pt[0]+surface_size_x//3, new_pt[1]+surface_size_y//3)
        #plot_pt = (new_pt[0], new_pt[1])
        main_surface.set_at(plot_pt, (255,255,0)) #Plot a pixel at (mid_point[0],mid_point[1])
        old_pt = new_pt

        pygame.display.flip() # Put all the drawing up to the display
       # my_clock.tick(120) #Keeps a contant framerate for smoother animation
        # If you don't include the above line, the loop executes as fast as it can
        

gameloop()
pygame.quit()