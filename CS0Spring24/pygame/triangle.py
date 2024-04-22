import pygame, math, random
pygame.init()           # prepare the pygame module for use

class Point:
    def __init__(self, xx=0, yy=0):
        self.x = xx
        self.y = yy
    def __str__(self):
        return f"x={self.x}, y={self.y}\n"
    def midPointmv(self, p2):
        midx = int((p2[0]+self.x)/2)
        midy = int((p2[1]+self.y)/2)
        self.x = midx
        self.y = midy
    def givePoint(self):
        return (self.x, self.y)

# Create a new surface and window.
surface_size_x = 1280
surface_size_y = 720
iterations = 10000

vertices = [(int(surface_size_x/2), 0), (0, surface_size_y-1), (surface_size_x-1, surface_size_y-1)]
p1 = Point(int(surface_size_x/2), 0)

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

        for i in range(iterations):
            # Draw everything
            choice = random.choice(vertices)
            p1.midPointmv(choice)
            plot_point = p1.givePoint()
            
            
            # Draw stuff
            red = random.randint(0,255)
            green = random.randint(0,255)
            blue = random.randint(0,255)

            blue= 255 - ((plot_point[0]/surface_size_x)*255)
            green = (plot_point[1]/surface_size_y)*255
            red = 0
            color = (red, green, blue)

            main_surface.set_at(plot_point, color) #Plot a pixel at (mid_point[0],mid_point[1])
            #p2 = (surface_size,surface_size)
        #pygame.draw.line(main_surface, color, p1, p2)

        pygame.display.flip() # Put all the drawing up to the display
        my_clock.tick(120) #Keeps a contant framerate for smoother animation
        # If you don't include the above line, the loop executes as fast as it can


gameloop()
pygame.quit()