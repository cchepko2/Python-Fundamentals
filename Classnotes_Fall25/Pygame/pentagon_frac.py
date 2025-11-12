import pygame, math, random
pygame.init()           # prepare the pygame module for use

iterations = 1000
# Create a new surface and window.
surface_size_x = 1000
sidea_w = surface_size_x/2

surface_size_y = 700
main_surface = pygame.display.set_mode((surface_size_x,surface_size_y))
my_clock = pygame.time.Clock()

HW_ratio = surface_size_y/surface_size_x

first_y = (math.tan(math.radians(36)))*(surface_size_x/2)
second_x = ((surface_size_y-first_y)*math.tan(math.radians(18)))

pt1 = (surface_size_x//2, 0)
pt2 = (0, int(first_y*HW_ratio))
pt3 = (surface_size_x, int(first_y*HW_ratio))
pt4 = (int(second_x/HW_ratio), surface_size_y)
pt5 = (int((surface_size_x-second_x/HW_ratio)), surface_size_y)
vertices = [pt1, pt2, pt3, pt4, pt5]

print(vertices)

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
        p1 = (0,0)
        p2 = (surface_size_x,surface_size_y)
        #pygame.draw.line(main_surface, color, p1, p2)
        for _ in range(iterations):
            vertex = random.choice(vertices)
            new_pt = half_way(old_pt, vertex)
            red = int(((new_pt[0]+surface_size_x//3)/surface_size_x)*255)
            green = int((new_pt[1]+surface_size_y//3)/surface_size_y*255)
            blue = 255-int(math.sqrt((new_pt[0]+surface_size_x//3)**2+(new_pt[1]+surface_size_y//3)**2)/math.sqrt(surface_size_x**2+surface_size_y**2)*255)
            color = (red,green,blue)

            plot_pt = (new_pt[0]+surface_size_x//3, new_pt[1]+surface_size_y//3)
            #plot_pt = (new_pt[0], new_pt[1])
            main_surface.set_at(plot_pt, color) #Plot a pixel at (mid_point[0],mid_point[1])
            '''
            main_surface.set_at(pt1, (255,0,0))
            main_surface.set_at(pt2, (255,0,0))
            main_surface.set_at(pt3, (255,0,0))
            main_surface.set_at(pt4, (255,0,0))
            main_surface.set_at(pt5, (255,0,0))
            '''
            old_pt = new_pt

        pygame.display.flip() # Put all the drawing up to the display
       # my_clock.tick(120) #Keeps a contant framerate for smoother animation
        # If you don't include the above line, the loop executes as fast as it can
        

gameloop()
pygame.quit()