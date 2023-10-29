import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 800
SCREEN_SIZE = (WIDTH, HEIGHT)
CAR_WIDTH, CAR_HEIGHT = 50, 100
FPS = 60

# Colors
WHITE = (255, 255, 255)
ROAD_COLOR = (100, 100, 100)
STRIPES_COLOR = WHITE

# Create the Pygame window
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("High Speed Craze: Avoid the Cars!")

# Load car image
car_image = pygame.image.load("img/yellow_car.png")
car_image = pygame.transform.scale(car_image, (CAR_WIDTH, CAR_HEIGHT))

# Load other car image
other_image = pygame.image.load("img/red_car.png")
other_image = pygame.transform.scale(other_image, (CAR_WIDTH + 80, CAR_HEIGHT))

# Initialize player's car position
player_car_x = WIDTH // 2 - CAR_WIDTH // 2
car_y = HEIGHT - CAR_HEIGHT - 20
car_speed = 23

# Initialize road parameters
road_width = 400
stripe_width = 10
stripe_height = 100
stripe_distance = 50
road_y = 0
road_speed = 23  # Speed at which the road moves

# Create lists to manage stripes and other cars
other_cars = []
stripes = []

# Create a timer for generating stripes
stripe_timer = 0
stripe_interval = 30  # Adjust to control the stripe generation rate

# Create a timer for spawning other cars
car_spawn_timer = 0
car_spawn_interval = 60  # Adjust to control the other car spawn rate

# Game over flag, score, and font
game_over = False
score = 0
font = pygame.font.Font(None, 36)

# Define a restart and exit button 
restart_button = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 + 100, 100, 50)
exit_button = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 + 160, 100, 50)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a])and player_car_x > 0:
            player_car_x -= car_speed
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player_car_x < WIDTH - CAR_WIDTH:
            player_car_x += car_speed

        # Update the road
        road_y += road_speed

        screen.fill(ROAD_COLOR)

        # Update and draw stripes
        for stripe in stripes:
            pygame.draw.rect(screen, STRIPES_COLOR, stripe)
            stripe.move_ip(0, road_speed)

        # Check the timer for stripe generation
        stripe_timer += 1
        if stripe_timer >= stripe_interval:
            new_stripe = pygame.Rect(WIDTH // 2 - stripe_width // 2, -stripe_width, stripe_width, stripe_height)
            stripes.append(new_stripe)
            stripe_timer = 0

        # Remove stripes that go off the screen
        stripes = [stripe for stripe in stripes if stripe.top <= HEIGHT]

        # Update and draw other cars
        for car in other_cars:
            screen.blit(other_image, (car.left, car.top))
            car.move_ip(0, road_speed)

        # Check for collisions between the player's car and other cars
        player_car_rect = pygame.Rect(player_car_x, car_y, CAR_WIDTH, CAR_HEIGHT)
        for car in other_cars:
            if player_car_rect.colliderect(car):
                game_over = True
            else:
                score += 1  # Increase the score when no collision occurs

        # Check the timer for spawning other cars
        car_spawn_timer += 1
        if car_spawn_timer >= car_spawn_interval:
            car_spawn_interval = random.randint(8, 25)
            lane = random.randint(0, 2)
            # car_x = WIDTH // 6 + lane * (WIDTH // 3) - CAR_WIDTH // 2
            car_x = random.randint(0, 308)
            new_car = pygame.Rect(car_x, - CAR_HEIGHT, CAR_WIDTH, CAR_HEIGHT)
            other_cars.append(new_car)
            car_spawn_timer = 0

        # Remove other cars that go off the screen
        other_cars = [car for car in other_cars if car.top <= HEIGHT]

        # Draw the player's car on top of the road without snapping to other cars' x-coordinates
        screen.blit(car_image, (player_car_x, car_y))

        # Display the score
        score_text = font.render("Score: " + str(score), True, (255, 255, 0))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    # Game over screen
    if game_over:
        screen.fill((255, 0, 0))  # Red background
        text = font.render("Game Over!", True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

        # Display the final score on the game over screen
        final_score_text = font.render("Final Score: " + str(score), True, WHITE)
        final_score_rect = final_score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        screen.blit(final_score_text, final_score_rect)

        # Draw the restart and exit button
        pygame.draw.rect(screen, WHITE, restart_button)
        restart_text = font.render("Restart", True, (0, 0, 0))
        restart_text_rect = restart_text.get_rect(center=restart_button.center)
        screen.blit(restart_text, restart_text_rect)

        pygame.draw.rect(screen, WHITE, exit_button)
        exit_text = font.render("Exit", True, (0, 0, 0))
        exit_text_rect = exit_text.get_rect(center=exit_button.center)
        screen.blit(exit_text, exit_text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    # Reset the game when the restart button is clicked
                    game_over = False
                    score = 0
                    other_cars = []
                    player_car_x = WIDTH // 2 - CAR_WIDTH // 2
                elif exit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
            else:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    game_over = False
                    score = 0
                    other_cars = []
                    player_car_x = WIDTH // 2 - CAR_WIDTH // 2
                elif keys[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()



# Game over screen loop
while game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
