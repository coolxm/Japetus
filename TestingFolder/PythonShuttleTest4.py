import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Window")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up fonts
font = pygame.font.Font(None, 36)

# Define functions for button commands
def button_commander():
    return "Commander gekozen!"

def button_pilot():
    return "Pilot gekozen!"

# Main loop
def main():
    role_chosen = None

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

        # Clear the screen
        screen.fill(WHITE)

        # Draw buttons
        commander_button = font.render("Mijn rol is Commander", True, BLACK)
        commander_button_rect = commander_button.get_rect(center=(WIDTH // 4, HEIGHT // 2))
        screen.blit(commander_button, commander_button_rect)

        pilot_button = font.render("Mijn rol is Pilot", True, BLACK)
        pilot_button_rect = pilot_button.get_rect(center=(WIDTH * 3 // 4, HEIGHT // 2))
        screen.blit(pilot_button, pilot_button_rect)

        # Draw chosen role
        if role_chosen:
            chosen_label = font.render(role_chosen, True, BLACK)
            chosen_label_rect = chosen_label.get_rect(center=(WIDTH // 2, HEIGHT * 3 // 4))
            screen.blit(chosen_label, chosen_label_rect)

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
