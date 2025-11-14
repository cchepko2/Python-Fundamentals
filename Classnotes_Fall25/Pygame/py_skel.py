import pygame, math, random

pygame.init()           # prepare the pygame module for use

# Create a new surface and window.
surface_size_x = 500   # Pixels X
surface_size_y = 500    # Pixels Y
main_surface = pygame.display.set_mode((surface_size_x,surface_size_y))
my_clock = pygame.time.Clock()

def gameloop():
    run = True

    while run:

        # Handle evente from keyboard, mouse, etc.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYUP:
                if(event.key == pygame.K_ESCAPE):
                    run = False

        # Draw everything
        #main_surface.fill((0, 155, 155)) #fill background color
        # Draw stuff

        x = random.randint(0, surface_size_x-1)
        y = random.randint(0, surface_size_y-1)

        plot_pt = (x, y)
        main_surface.set_at(plot_pt, (255,0,0))
        
        pygame.display.flip() # Put all the drawing up to the display
       # my_clock.tick(120) #Keeps a contant framerate for smoother animation
        # If you don't include the above line, the loop executes as fast as it can
        

gameloop()
pygame.quit()