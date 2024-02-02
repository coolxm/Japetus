import pygame
import sys

def PLT_prog():
    print("Pilot rol programma")

    # Set up scherm
    pygame.init()
    WIDTH, HEIGHT = 1500, 750
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) #(WIDTH, HEIGHT)
    WIDTH, HEIGHT = screen.get_size()
    pygame.display.set_caption("Pilot Programma")

    # Set up colors
    WHITE = (255, 255, 255)
    GREY = (200, 200, 200)
    BLACK = (0, 0, 0)
    # Set up fonts
    font = pygame.font.Font(None, 36)

    # Main loop
    def PLT_main():
        running = True

        while running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False  # Exit fullscreen mode when ESC key is pressed
            
            # Clear the screen
            screen.fill(GREY)

            # Update the display
            pygame.display.flip()
    
    PLT_main()
