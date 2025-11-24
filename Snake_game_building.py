#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install pygame')


# In[3]:


import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set the screen size
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Feed the Snake')

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Game clock
clock = pygame.time.Clock()

# Define snake parameters
snake_block = 10  # Size of each block in the snake
snake_speed = 15  # Snake speed


# In[5]:


# Function to draw the snake on the screen
def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], snake_block, snake_block])

# Function to generate random food position
def random_food_position():
    food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
    return food_x, food_y


# In[6]:


def game_loop():
    # Initial position of the snake
    snake_x = screen_width / 2
    snake_y = screen_height / 2

    # Snake movement (initially stationary)
    x_change = 0
    y_change = 0

    # Snake body
    snake_list = []
    snake_length = 1

    # Food position
    food_x, food_y = random_food_position()

    # Main game loop
    game_over = False
    game_close = False

    while not game_over:

        while game_close:
            screen.fill(BLUE)
            font_style = pygame.font.SysFont("bahnschrift", 25)
            msg = font_style.render("Game Over! Press Q-Quit or C-Play Again", True, RED)
            screen.blit(msg, [screen_width / 6, screen_height / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Handle key events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        # Update snake position
        snake_x += x_change
        snake_y += y_change

        # Check for collisions with screen borders
        if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0:
            game_close = True

        # Draw background
        screen.fill(BLACK)

        # Draw food
        pygame.draw.rect(screen, WHITE, [food_x, food_y, snake_block, snake_block])

        # Update the snake's body
        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for collisions with itself
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)

        # Update the screen
        pygame.display.update()

        # Check if the snake has eaten the food
        if snake_x == food_x and snake_y == food_y:
            food_x, food_y = random_food_position()
            snake_length += 1

        # Set the frame rate
        clock.tick(snake_speed)

    # Quit Pygame
    pygame.quit()
    quit()

# Start the game
game_loop()


# In[ ]:




