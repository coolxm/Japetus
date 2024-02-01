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

    # Input box
    input_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    response = ''

    # Main loop
    def CMDR_main():
        nonlocal active, text, response, color
        running = True

        while running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False  # Exit fullscreen mode when ESC key is pressed
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicks on the input_box rect
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box
                    color = color_active if active else color_inactive
                
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            response = process_code(text)
                            text = ''
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
            
            # Clear the screen
            screen.fill(GREY)

            # Render text input box
            pygame.draw.rect(screen, color, input_box, 2)
            txt_surface = font.render(text, True, BLACK)
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
            screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
            pygame.draw.rect(screen, BLACK, input_box, 2)

            # Render response
            response_text = font.render(response, True, BLACK)
            screen.blit(response_text, (100, 200))

            # Update the display
            pygame.display.flip()
    
    def process_code(code):
        # Here you would process the entered code and return a response
        # For demonstration, I'll provide some hardcoded responses based on codes
        if code == '123':
            return "Response 1: Code 123 processed."
        elif code == '456':
            return "Response 2: Code 456 processed."
        else:
            return "Invalid code. Please try again."

    CMDR_main()
