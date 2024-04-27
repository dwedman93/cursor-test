import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake initial settings
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_speed = 10
direction = 'RIGHT'
change_to = direction

# Food
food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
food_spawn = True

# Game over function
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(len(snake_body) - 3), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (width / 2, height / 4)
    screen.fill(black)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

# Main function
def main():
    global direction, change_to, food_spawn, snake_pos, snake_body, food_pos

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    change_to = 'RIGHT'
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Validate direction
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Move snake
        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10

        # Snake body mechanism
        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            food_spawn = False
        else:
            snake_body.pop()

        # Food spawn
        if not food_spawn:
            food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
        food_spawn = True

        # Background and snake
        screen.fill(black)
        for pos in snake_body:
            pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))

        # Food
        pygame.draw.rect(screen, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

        # Game over conditions
        if snake_pos[0] < 0 or snake_pos[0] > width-10:
            snake_pos[0] = width - snake_pos[0]
        if snake_pos[1] < 0 or snake_pos[1] > height-10:
            snake_pos[1] = height - snake_pos[1]
        for block in snake_body[1:]:
            if snake_pos == block:
                game_over()

        pygame.display.update()
        clock.tick(snake_speed)

if __name__ == '__main__':
    main()
