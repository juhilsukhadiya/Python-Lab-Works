import pygame
import random

pygame.init()

# Screen
WIDTH = 600
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
GRAY = (80, 80, 80)

# Clock
clock = pygame.time.Clock()

# Player car
player_width = 50
player_height = 90
player_x = 275
player_y = 580
player_speed = 7

# Enemy car
enemy_width = 50
enemy_height = 90
enemy_x = random.randint(100, 450)
enemy_y = -100
enemy_speed = 6

# Score
score = 0
font = pygame.font.Font(None, 40)

running = True

while running:

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Keyboard
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_x > 80:
        player_x -= player_speed

    if keys[pygame.K_RIGHT] and player_x < WIDTH - 130:
        player_x += player_speed

    # Enemy movement
    enemy_y += enemy_speed

    # Reset enemy
    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(100, 450)
        score += 1
        enemy_speed += 0.2

    # Background
    screen.fill(GREEN)

    # Road
    pygame.draw.rect(screen, GRAY, (70, 0, 460, HEIGHT))

    # Road lines
    for y in range(0, HEIGHT, 100):
        pygame.draw.rect(screen, WHITE, (295, y, 10, 50))

    # Player car
    player_rect = pygame.Rect(
        player_x, player_y,
        player_width, player_height
    )

    pygame.draw.rect(screen, RED, player_rect)

    # Enemy car
    enemy_rect = pygame.Rect(
        enemy_x, enemy_y,
        enemy_width, enemy_height
    )

    pygame.draw.rect(screen, BLACK, enemy_rect)

    # Collision
    if player_rect.colliderect(enemy_rect):

        game_over = font.render(
            "GAME OVER!",
            True,
            WHITE
        )

        screen.blit(
            game_over,
            (220, 320)
        )

        pygame.display.update()
        pygame.time.delay(2000)

        running = False

    # Score
    score_text = font.render(
        "Score: " + str(score),
        True,
        WHITE
    )

    screen.blit(score_text, (10, 10))

    pygame.display.update()

    clock.tick(60)

pygame.quit()