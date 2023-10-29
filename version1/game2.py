import pygame
import sys
from random import randint
from special_moves import *

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 800
CARD_WIDTH, CARD_HEIGHT = 100, 150
MENU_FONT_SIZE = 36
MENU_COLOR = (255, 255, 255)
CARD_COLOR = (255, 255, 255)
PLAYER_CARDS = 4
ENEMY_CARDS = randint(4, 8)

characters = [Serenity, Sora, Shizuo, Rabadon, Huamao, Zohphia, Kana, Chadwick]

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Main Menu")

# Load the background image
background_image = pygame.image.load("img/backgrounds/Ai-Background.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Create fonts for the menu options and title
menu_font = pygame.font.Font(None, MENU_FONT_SIZE)
title_font = pygame.font.Font(None, MENU_FONT_SIZE * 2)

# List of menu options
menu_options = ["Play Game", "Gacha", "Party", "Quit"]
selected_option = 0

def is_point_inside_rect(point, rect):
    x, y = point
    rx, ry, rw, rh = rect
    return rx <= x <= rx + rw and ry <= y <= ry + rh

# Options menu
def Gacha_menu():
    # Load the background image
    background_image = pygame.image.load("img/backgrounds/options-background.png")
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

serenity = pygame.image.load("img/character cards/serenity.png")
serenity = pygame.transform.scale(serenity, (150, 300))

def party_menu():
    background_image = pygame.image.load("img/backgrounds/char-background.png")
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
    
    card_width, card_height = 150, 300
    player_cards = [pygame.Rect(100 + i * 200, 400, card_width, card_height) for i in range(PLAYER_CARDS)]

    font = pygame.font.Font(None, 36)

    button = pygame.Rect(100, 100, 50, 50)



    playing = True
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    playing = False  # Exit the "Party" menu when the Esc key is pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if button.collidepoint(event.pos):
                    for card in player_cards:
                        pygame.draw.rect(screen, CARD_COLOR, card)
                    screen.blit(serenity, (100, 400))
                    screen.blit(serenity, (300, 400))
                    screen.blit(serenity, (500, 400))
                    screen.blit(serenity, (700, 400))

        # Display the background first
        screen.blit(background_image, (0, 0))
        
        pygame.draw.rect(screen, (255, 255, 255), button)
        text = font.render("Click Me!", True, (0, 0, 0))
        text_rect = text.get_rect(center=button.center)
        screen.blit(text, text_rect)

        # Add code to display character cards and handle interactions here
        for card in player_cards:
            pygame.draw.rect(screen, CARD_COLOR, card)
        # screen.blit(serenity, (100, 400))
        # screen.blit(serenity, (300, 400))
        # screen.blit(serenity, (500, 400))
        # screen.blit(serenity, (700, 400))
        # ...

        pygame.display.flip()

    # When the "Party" menu loop exits, you will return to the main menu
    return



# Card battle game function
# Card battle game function
# Card battle game function
def card_battle_game():
    # Game state variables
    card_width, card_height = 50, 100
    player_cards = [pygame.Rect(100 + i * 150, 400, card_width, card_height) for i in range(PLAYER_CARDS)]
    enemy_cards = [pygame.Rect(100 + i * 100, 50, card_width, card_height) for i in range(ENEMY_CARDS)]

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

        # Display the background
        screen.fill((0, 0, 0))

        # Display player and enemy cards
        for card in player_cards:
            pygame.draw.rect(screen, CARD_COLOR, card)
        for card in enemy_cards:
            pygame.draw.rect(screen, CARD_COLOR, card)

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