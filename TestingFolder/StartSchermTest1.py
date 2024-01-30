import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Window")

# Set up colors
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)
GREEN = (10, 110, 20)

# Set up fonts
font = pygame.font.Font(None, 36)

# Define functions for button commands
def button_commander():
    return "Commander gekozen! (CMDR)"
def button_pilot():
    return "Pilot gekozen! (PLT)"
def button_FD():
    return "Flight Director gekozen! (FD)"
def button_WXT():
    return "Weather Specialist gekozen! (WXT)"
def button_LD():
    return "Launch Director gekozen! (LD)"
def button_ELSS():
    return "Entry, Landing and Spacecraft Systems Specialist gekozen! (ELSS)"
def button_SSO():
    return "Spacecraft Systems Officer gekozen! (SSO)"
def button_PAO():
    return "Public Affairs Officer gekozen! (PAO)"
def button_HELP():
    return "Kies hier je welke positie je bent. \n Als je in de shuttle zit ben je Commander of Pilot, \n als je buiten de shuttel zit ben je èèn van de andere rollen."
def button_START():
    return True

# Define button rectangles
commander_button_rect = None
pilot_button_rect = None
FD_button_rect = None
WXT_button_rect = None
LD_button_rect = None
ELSS_button_rect = None
SSO_button_rect = None
PAO_button_rect = None
HELP_button_rect = None
START_button_rect = None

# Main loop
def main():
    #global commander_button_rect, pilot_button_rect, FD_button_rect
    role_chosen = None
    start_missie = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if commander_button_rect.collidepoint(mouse_pos):
                    role_chosen = button_commander()
                elif pilot_button_rect.collidepoint(mouse_pos):
                    role_chosen = button_pilot()
                elif FD_button_rect.collidepoint(mouse_pos):
                    role_chosen = button_FD()
                elif WXT_button_rect.collidepoint(mouse_pos):
                    role_chosen = button_WXT()
                elif LD_button_rect.collidepoint(mouse_pos):
                    role_chosen = button_LD()
                elif ELSS_button_rect.collidepoint(mouse_pos):
                    role_chosen = button_ELSS()
                elif SSO_button_rect.collidepoint(mouse_pos):
                    role_chosen = button_SSO()
                elif PAO_button_rect.collidepoint(mouse_pos):
                    role_chosen = button_PAO()
                elif HELP_button_rect.collidepoint(mouse_pos):
                    role_chosen = button_HELP()
                elif START_button_rect.collidepoint(mouse_pos):
                    if not role_chosen == (None or button_HELP)():
                        start_missie = button_START()

        # Clear the screen
        screen.fill(GREY)

        # Draw text above buttons
        text = font.render("Kies hier uw rol:", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 8))
        screen.blit(text, text_rect)

        # Draw buttons with larger boxes
        button_width, button_height = 300, 50

        #Eerste Drie knoppen
        commander_button = font.render("Commander", True, BLACK)
        commander_button_rect = pygame.Rect((WIDTH // 6 - button_width // 2, HEIGHT * 2 // 8 - button_height // 2), (button_width, button_height))
        pygame.draw.rect(screen, BLACK, commander_button_rect, 2)  # Draw box around button
        screen.blit(commander_button, commander_button_rect.move((commander_button_rect.width - commander_button.get_width()) // 2, (commander_button_rect.height - commander_button.get_height()) // 2))

        pilot_button = font.render("Pilot", True, BLACK)
        pilot_button_rect = pygame.Rect((WIDTH * 3 // 6 - button_width // 2, HEIGHT * 2 // 8 - button_height // 2), (button_width, button_height))
        pygame.draw.rect(screen, BLACK, pilot_button_rect, 2)  # Draw box around button
        screen.blit(pilot_button, pilot_button_rect.move((pilot_button_rect.width - pilot_button.get_width()) // 2, (pilot_button_rect.height - pilot_button.get_height()) // 2))

        FD_button = font.render("Flight Director", True, BLACK)
        FD_button_rect = pygame.Rect((WIDTH * 5 // 6 - button_width // 2, HEIGHT * 2 // 8 - button_height // 2), (button_width, button_height))
        pygame.draw.rect(screen, BLACK, FD_button_rect, 2)  # Draw box around button
        screen.blit(FD_button, FD_button_rect.move((FD_button_rect.width - FD_button.get_width()) // 2, (FD_button_rect.height - FD_button.get_height()) // 2))

        #2de rij van drie knoppen
        WXT_button = font.render("Weather Specialist", True, BLACK)
        WXT_button_rect = pygame.Rect((WIDTH // 6 - button_width // 2, HEIGHT * 3 // 8 - button_height // 2), (button_width, button_height))
        pygame.draw.rect(screen, BLACK, WXT_button_rect, 2)  # Draw box around button
        screen.blit(WXT_button, WXT_button_rect.move((WXT_button_rect.width - WXT_button.get_width()) // 2, (WXT_button_rect.height - WXT_button.get_height()) // 2))

        LD_button = font.render("Launch Director", True, BLACK)
        LD_button_rect = pygame.Rect((WIDTH * 3 // 6 - button_width // 2, HEIGHT * 3 // 8 - button_height // 2), (button_width, button_height))
        pygame.draw.rect(screen, BLACK, LD_button_rect, 2)  # Draw box around button
        screen.blit(LD_button, LD_button_rect.move((LD_button_rect.width - LD_button.get_width()) // 2, (LD_button_rect.height - LD_button.get_height()) // 2))

        ELSS_button = font.render("ELSS", True, BLACK)
        ELSS_button_rect = pygame.Rect((WIDTH * 5 // 6 - button_width // 2, HEIGHT * 3 // 8 - button_height // 2), (button_width, button_height))
        pygame.draw.rect(screen, BLACK, ELSS_button_rect, 2)  # Draw box around button
        screen.blit(ELSS_button, ELSS_button_rect.move((ELSS_button_rect.width - ELSS_button.get_width()) // 2, (ELSS_button_rect.height - ELSS_button.get_height()) // 2))

        #3de rij van drie knoppen
        SSO_button = font.render("SSO", True, BLACK)
        SSO_button_rect = pygame.Rect((WIDTH // 6 - button_width // 2, HEIGHT * 4 // 8 - button_height // 2), (button_width, button_height))
        pygame.draw.rect(screen, BLACK, SSO_button_rect, 2)  # Draw box around button
        screen.blit(SSO_button, SSO_button_rect.move((SSO_button_rect.width - SSO_button.get_width()) // 2, (SSO_button_rect.height - SSO_button.get_height()) // 2))

        PAO_button = font.render("Public Affairs Officer", True, BLACK)
        PAO_button_rect = pygame.Rect((WIDTH * 3 // 6 - button_width // 2, HEIGHT * 4 // 8 - button_height // 2), (button_width, button_height))
        pygame.draw.rect(screen, BLACK, PAO_button_rect, 2)  # Draw box around button
        screen.blit(PAO_button, PAO_button_rect.move((PAO_button_rect.width - PAO_button.get_width()) // 2, (PAO_button_rect.height - PAO_button.get_height()) // 2))

        HELP_button = font.render("Help mij!", True, BLACK)
        HELP_button_rect = pygame.Rect((WIDTH * 5 // 6 - button_width // 2, HEIGHT * 4 // 8 - button_height // 2), (button_width, button_height))
        pygame.draw.rect(screen, BLACK, HELP_button_rect, 2)  # Draw box around button
        screen.blit(HELP_button, HELP_button_rect.move((HELP_button_rect.width - HELP_button.get_width()) // 2, (HELP_button_rect.height - HELP_button.get_height()) // 2))

        START_button = font.render("Start Missie", True, BLACK)
        START_button_rect = pygame.Rect((WIDTH * 5 // 6 - button_width // 2, HEIGHT * 7 // 8 - button_height // 2), (button_width, button_height))
        pygame.draw.rect(screen, BLACK, START_button_rect, 2)  # Draw box around button
        screen.blit(START_button, START_button_rect.move((START_button_rect.width - START_button.get_width()) // 2, (START_button_rect.height - START_button.get_height()) // 2))


        # Draw chosen role
        if role_chosen:
            chosen_label = font.render(role_chosen, True, BLACK)
            chosen_label_rect = chosen_label.get_rect(center=(WIDTH // 2, HEIGHT * 2.5 // 4))
            screen.blit(chosen_label, chosen_label_rect)
        
        if start_missie:
            screen.fill(GREEN) #is om knop te testen 

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
