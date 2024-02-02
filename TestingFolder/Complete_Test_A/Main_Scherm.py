import pygame
import sys

def MainScherm_prog(rol):
    print("Main Scherm, je rol is " + rol)

    # Set up scherm
    pygame.init()
    WIDTH, HEIGHT = 1500, 750
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) #(WIDTH, HEIGHT)
    WIDTH, HEIGHT = screen.get_size()
    pygame.display.set_caption("Main Scherm, je rol is " + rol)

    # Set up colors
    WHITE = (255, 255, 255)
    LGREEN = (109, 241, 113)
    GREEN = (29, 161, 33)
    LGREY = (200, 200, 200)
    GREY = (20, 20, 20)
    BLACK = (0, 0, 0)
    # Set up fonts
    font = pygame.font.Font(None, 36)

    # Input box
    input_box = pygame.Rect(100, 700, 400, 40)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    response = ''
    history = [rol,"","","","","","","","",""]

    # Define button
    def button_fuel():
        return "Fuel scherm gevraagd"
    # Define button rectangles
    fuel_button_rect = None

    # Main loop
    def Scherm_main():
        nonlocal active, text, response, color
        running = True
        button_clicked = None

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

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if fuel_button_rect.collidepoint(mouse_pos):
                        button_clicked = button_fuel()
            
            # Clear the screen
            screen.fill(GREY)

            # Render text input box
            pygame.draw.rect(screen, color, input_box, 2)
            txt_surface = font.render(text, True, LGREY)
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
            screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
            pygame.draw.rect(screen, LGREY, input_box, 2)

            # Render response
            history_0 = font.render(history[0], True, GREEN)
            screen.blit(history_0, (105, 670))
            for i in range(9):
                history_for = font.render(history[i+1], True, LGREEN)
                screen.blit(history_for, (105, (645 - i*25)))

            # Draw buttons with larger boxes
            button_width, button_height = 200, 50
            #Fuel Knop
            fuel_button = font.render("Fuel", True, GREEN)
            fuel_button_rect = pygame.Rect((WIDTH * 5.5 // 6 - button_width // 2, HEIGHT // 8 - button_height // 2), (button_width, button_height))
            pygame.draw.rect(screen, GREEN, fuel_button_rect, 2)  # Draw box around button
            screen.blit(fuel_button, fuel_button_rect.move((fuel_button_rect.width - fuel_button.get_width()) // 2, (fuel_button_rect.height - fuel_button.get_height()) // 2))


            # Update the display
            pygame.display.flip()
    
    def process_code(input):
        # Draw text above buttons
            for i in range (9):
                history[9-i] = history[8-i]
            history[0] = input
            return input

    Scherm_main()

if __name__ == '__main__':
    MainScherm_prog()