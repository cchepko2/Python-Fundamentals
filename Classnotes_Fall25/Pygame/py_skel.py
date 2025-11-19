import pygame, math, random, time

pygame.init()           # prepare the pygame module for use

# Create a new surface and window.
surface_size_x = 500   # Pixels X
surface_size_y = 500    # Pixels Y
iterations = 100
triangle_points = [(surface_size_x/2, 0),(0, surface_size_y-1),(surface_size_x-1, surface_size_y-1)]

main_surface = pygame.display.set_mode((surface_size_x,surface_size_y))
my_clock = pygame.time.Clock()

def mid_point(pt1, pt2):
    new_x = int((pt1[0] + pt2[0])/2)
    new_y = int((pt1[1] + pt2[1])/2)
    return (new_x, new_y)

def gameloop():
    run = True

    current_point = (0,0)
    # put a background color in, before the main loop, so it's only drawn once
    main_surface.fill((30, 0, 35)) #fill background color

    while run:

        # Handle evente from keyboard, mouse, etc.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYUP:
                if(event.key == pygame.K_ESCAPE):
                    run = False
                    
        for i in range(iterations):
            
            sleep_time = random.random()/100
            green = int(sleep_time*25500)

            time.sleep(sleep_time)

            # Calculate new point
            plot_pt = mid_point(current_point, random.choice(triangle_points))
            # Draw everything
            # Draw stuff

            main_surface.set_at(plot_pt, (255,green,0))

            current_point = plot_pt
        
        pygame.display.flip() # Put all the drawing up to the display
       # my_clock.tick(120) #Keeps a contant framerate for smoother animation
        # If you don't include the above line, the loop executes as fast as it can
        

gameloop()
pygame.quit()