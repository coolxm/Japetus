import pygame
import sys

def CMDR_prog():
    print("Comander rol programma")

    # Set up scherm
    pygame.init()
    WIDTH, HEIGHT = 1500, 750
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) #(WIDTH, HEIGHT)
    WIDTH, HEIGHT = screen.get_size()
    pygame.display.set_caption("Commander Programma")

    # Set up colors
    WHITE = (255, 255, 255)
    GREY = (200, 200, 200)
    BLACK = (0, 0, 0)
    # Set up fonts
    font = pygame.font.Font(None, 36)

    # Main loop
    def CMDR_main():
        print("jefry")
        running = True

        while running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False  # Exit fullscreen mode when ESC key is pressed


                #if event.type == pygame.MOUSEBUTTONDOWN:
                #    mouse_pos = pygame.mouse.get_pos()
                #    if commander_button_rect.collidepoint(mouse_pos):
                #        role_chosen = button_commander()
                #        rol_in_main = "CMDR"
            
            # Clear the screen
            screen.fill(GREY)

            # Update the display
            pygame.display.flip()
    
    CMDR_main()
