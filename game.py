import pygame
import sys
from random import randint
from special_moves import *


available_characters = [Serenity, Sora, Kana, Huamao, Shizuo, Rabadon, Zohphia, Chadwick]
# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CARD_WIDTH, CARD_HEIGHT = 100, 150
MENU_FONT_SIZE = 36
MENU_COLOR = (255, 255, 255)
CARD_COLOR = (150, 150, 150)
PLAYER_CARDS = 4
ENEMY_CARDS = randint(4, 8)

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Main Menu")

# Load the background image
background_image = pygame.image.load("img/backgrounds/Ai-Background.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))


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

def party_menu():
    background_image = pygame.image.load("img/backgrounds/char-background.png")
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

    card_width, card_height = 80, 130
    player_cards = [pygame.Rect(100 + i * 150, 400, card_width, card_height) for i in range(PLAYER_CARDS)]

    char_display_x = 100
    char_display_y = 100
    char_display_spacing = 200
    selected_characters = []

    playing = True
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    playing = False  # Exit the "Party" menu when the Esc key is pressed

        # Display the background first
        screen.blit(background_image, (0, 0))

        # Add code to display character cards and handle interactions here
        # for card in player_cards:
        #     pygame.draw.rect(screen, CARD_COLOR, card)

        # Display available characters
        for event in pygame.event.get():
            for i, character in enumerate(available_characters):
                character_rect = pygame.Rect(char_display_x + i * char_display_spacing, char_display_y, CARD_WIDTH, CARD_HEIGHT)
                pygame.draw.rect(screen, CARD_COLOR, character_rect)

                # Display character name and allow selection
                character_name_text = menu_font.render(character.name, True, MENU_COLOR)
                name_x = character_rect.centerx - character_name_text.get_width() // 2
                name_y = character_rect.y - 30
                screen.blit(character_name_text, (name_x, name_y))

                if character in selected_characters:
                    # Draw a border around the selected character
                    pygame.draw.rect(screen, (255, 0, 0), character_rect, 3)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if character_rect.collidepoint(event.pos):
                        # Toggle character selection when clicked
                        if character in selected_characters:
                            selected_characters.remove(character)
                        else:
                            if len(selected_characters) < 4:
                                selected_characters.append(character)

            # Update the display
            pygame.display.flip()

        # Return the selected characters when exiting the party menu
        return selected_characters

# Create fonts for the menu options and title
menu_font = pygame.font.Font(None, MENU_FONT_SIZE)
title_font = pygame.font.Font(None, MENU_FONT_SIZE * 2)

# List of menu options
menu_options = ["Play Game", "Gacha", "Party", "Quit"]
selected_option = 0

# Define player card descriptions
player_card_data = [f"<{Serenity.name}> HP: {Serenity.hp}/{Serenity.max_hp}",
                            f"<{Kana.name}> HP: {Kana.hp}/{Kana.max_hp}",
                            f"<{Sora.name}> HP: {Sora.hp}/{Sora.max_hp}",
                            f"<{Huamao.name}> HP: {Huamao.hp}/{Huamao.max_hp}"]

# Initialize the selected card as None
selected_card = None

# Card battle game function
def card_battle_game():
    global selected_card  # Declare selected_card as a global variable

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
                    # Set the selected card to the clicked card's index
                    selected_card = i

        # Display the background
        screen.fill((0, 0, 0))

        # Display player and enemy cards
        for i, card in enumerate(player_cards):
            pygame.draw.rect(screen, CARD_COLOR, card)
            # Display the card information if it's selected
            if selected_card is not None and i == selected_card:
                character_data = player_card_data[i]
                name_text = menu_font.render(character_data, True, MENU_COLOR)
                # Adjust the position as needed
                screen.blit(name_text, (10, 10))

        # Update the display
        pygame.display.flip()

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
                    card_battle_game()
                elif selected_option == 1:
                    Gacha_menu()
                elif selected_option == 2:
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
