import pygame
import sys
import main


# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CARD_WIDTH, CARD_HEIGHT = 100, 150
MENU_FONT_SIZE = 36
MENU_COLOR = (255, 255, 255)
CARD_COLOR = (150, 150, 150)
PLAYER_CARDS = 4
ENEMY_CARDS = 8



# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Main Menu")

# Load the background image
background_image = pygame.image.load("img/Ai-Background.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Create fonts for the menu options and title
menu_font = pygame.font.Font(None, MENU_FONT_SIZE)
title_font = pygame.font.Font(None, MENU_FONT_SIZE * 2)

# List of menu options
menu_options = ["Play Game", "Gacha", "Party", "Quit"]
selected_option = 0

# Options menu
def Gacha_menu():
    # Load the background image
    background_image = pygame.image.load("img/options-background.png")
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

    playing = True
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                playing = False

        # Display the background image
        screen.blit(background_image, (0, 0))
        # Add your options menu elements on top of the background
        # ...
        
        pygame.display.flip()

    return

def party_menu():
    background_image = pygame.image.load("img/char-background.png")
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

    character1_image = pygame.image.load("img/serenity.png")
    character1_image = pygame.transform.scale(character1_image, (100, 200))
    character2_image = pygame.image.load("img/swordgirl.png")
    character2_image = pygame.transform.scale(character2_image, (100, 200))
    character3_image = pygame.image.load("img/zohphia.png")
    character3_image = pygame.transform.scale(character3_image, (100, 200))
    character4_image = pygame.image.load("img/rabadon.png")
    character4_image = pygame.transform.scale(character4_image, (100, 200))

# Define the character boxes
    character1_box = pygame.Rect(50, 50, 100, 200)
    character2_box = pygame.Rect(200, 50, 100, 200)
    character3_box = pygame.Rect(350, 50, 100, 200)
    character4_box = pygame.Rect(500, 50, 100, 200)

# Draw the character boxes
    pygame.draw.rect(screen, (255, 255, 255), character1_box)
    pygame.draw.rect(screen, (255, 255, 255), character2_box)
    pygame.draw.rect(screen, (255, 255, 255), character3_box)
    pygame.draw.rect(screen, (255, 255, 255), character4_box)

    screen.blit(background_image, (0, 0))

    screen.blit(character1_image, (50, 50))
    screen.blit(character2_image, (200, 50))
    screen.blit(character3_image, (350, 50))
    screen.blit(character4_image, (500, 50))

    playing = True
# Display the character images when the boxes are clicked
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     if character1_box.collidepoint(event.pos):
                    
            #     elif character2_box.collidepoint(event.pos):
                    
            #     elif character3_box.collidepoint(event.pos):
                    
            #     elif character4_box.collidepoint(event.pos):
                    
        pygame.display.update()


    # When the "Party" menu loop exits, you will return to the main menu
    return



# Card battle game function
# Card battle game function
# Card battle game function
def card_battle_game():
    # Game state variables
    card_width, card_height = 50, 100
    player_cards = [pygame.Rect(100 + i * 150, 400, card_width, card_height) for i in range(PLAYER_CARDS)]
    enemy_cards = [pygame.Rect(100 + i * 75, 50, card_width, card_height) for i in range(ENEMY_CARDS)]

    # Load the enemy card image
    enemy_card_image = pygame.image.load("img/bandit.png")
    enemy_card_image = pygame.transform.scale(enemy_card_image, (card_width, card_height))
    
    character1_image = pygame.image.load("img/serenity.png")
    character1_image = pygame.transform.scale(character1_image, (50, 100))
    character2_image = pygame.image.load("img/swordgirl.png")
    character2_image = pygame.transform.scale(character2_image, (50, 100))
    character3_image = pygame.image.load("img/zohphia.png")
    character3_image = pygame.transform.scale(character3_image, (50, 100))
    character4_image = pygame.image.load("img/rabadon.png")
    character4_image = pygame.transform.scale(character4_image, (50, 100))
    # Game loop
    playing = True
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            for i, card in enumerate(player_cards):
                if event.type == pygame.MOUSEBUTTONDOWN and card.collidepoint(event.pos):
                    # Handle the card click, implement your game logic here
                    print(f"Clicked on player card {i + 1}")
                    main.main()

        # Display the background
        screen.fill((0, 0, 0))

        # Display player and enemy cards
        for card in player_cards:
            pygame.draw.rect(screen, CARD_COLOR, card)
        for i, card in enumerate(enemy_cards):
            screen.blit(enemy_card_image, card)

        screen.blit(character1_image, (100, 400))
        screen.blit(character2_image, (250, 400))
        screen.blit(character3_image, (400, 400))
        screen.blit(character4_image, (550, 400))
        # Update the display
        pygame.display.flip()

    return


# Main menu loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                selected_option = (selected_option + 1) % len(menu_options)
            elif event.key == pygame.K_UP:
                selected_option = (selected_option - 1) % len(menu_options)
            elif event.key == pygame.K_RETURN:
                if selected_option == 0:
                    # Start the card battle game
                    card_battle_game()
                elif selected_option == 1:
                    # Go to the options menu
                    Gacha_menu()
                elif selected_option == 2:
                    # Quit the game
                    party_menu()
                elif selected_option == 3:
                    running = False

    # Display the background image
    screen.blit(background_image, (0, 0))

    # Display the title
    title_text = title_font.render("Gacha Battle", True, MENU_COLOR)
    title_x = WIDTH // 2 - title_text.get_width() // 2
    title_y = HEIGHT // 4
    screen.blit(title_text, (title_x, title_y))

    # Display menu options
    for i, option in enumerate(menu_options):
        text = menu_font.render(option, True, MENU_COLOR)
        x = WIDTH // 2 - text.get_width() // 2
        y = HEIGHT // 2 - (len(menu_options) * MENU_FONT_SIZE // 2) + i * MENU_FONT_SIZE
        if i == selected_option:
            pygame.draw.rect(screen, MENU_COLOR, (x - 10, y, text.get_width() + 20, MENU_FONT_SIZE), 3)
        screen.blit(text, (x, y))

    # Update the display
    pygame.display.flip()

# Quit Pygame and exit the program
pygame.quit()
sys.exit()
