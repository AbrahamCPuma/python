import pygame
#Initialize Pygame
pygame.init()

# Create a dipsplay surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Drawing Objects")

#Define colors as RGB tuple
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

#Give a backround color to the display
display_surface.fill(MAGENTA)

#Draw various shapes on our display
#Line(surface, color, starting point, ending point, thickness)
pygame.draw.line(surface=display_surface, color=YELLOW, start_pos=(0,0), end_pos=(100,100), width=5)
pygame.draw.line(surface=display_surface, color=GREEN, start_pos=(100,100), end_pos=(500,300), width=2)


#Circle(surface, color, center, radius, thickness...0 for fill)
pygame.draw.circle(display_surface,WHITE,(WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 200, 6)
pygame.draw.circle(display_surface,YELLOW,(WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 100, 0)

#Rectangle(surface, color, (top-left x, top-left y, width, height))
pygame.draw.rect(display_surface,CYAN,(50,100,20,40))
pygame.draw.rect(display_surface,BLACK,(80,90,30,40))

# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Update  the display
    pygame.display.update()
#End game
pygame.quit()