import pygame
import random
import game_config as gc

from pygame import display, event, draw, time

colors = gc.colors

pygame.init()
screen = display.set_mode((gc.width, gc.height))
display.set_caption('Pride Snake')
screen.fill(gc.white)

clock = time.Clock()

def snake_add(snake_size, snake_list):
    i = 0
    for s in snake_list:
        pygame.draw.rect(screen, colors[i], (s[0], s[1], snake_size, snake_size))
        if i + 1 < len(colors):
            i = i + 1
        else:
            i = 1

#def score(win):
 #   write = font_style.render("Score: " + str(win), True, fo)
  #  screen.blit(write, (0, 0))
            
def game_loop():
    running = True
    finishedGame = False
    
    snake_head_x = gc.size_snake * random.randint(0, gc.width / 10 - gc.food_margin)
    snake_head_y = gc.size_snake * random.randint(0, gc.width / 10 - gc.food_margin)
    x_move = 0
    y_move = 0
    food_x = gc.size_food * random.randint(0, gc.width / 10 - gc.food_margin)
    food_y = gc.size_food * random.randint(0, gc.height / 10 - gc.food_margin)
    color_index = 0
    frames = gc.frames
    snake = []
    snake_length = 1
    
    while(running):
        while(finishedGame):
            screen.fill(gc.black)
            display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    finishedGame = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                        finishedGame = False
                    elif event.key == pygame.K_p:
                        game_loop()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_DOWN:
                    x_move = 0
                    y_move = gc.move
                elif e.key == pygame.K_UP:
                    x_move = 0
                    y_move = -gc.move
                elif e.key == pygame.K_RIGHT:
                    x_move = gc.move
                    y_move = 0
                elif e.key == pygame.K_LEFT:
                    x_move = -gc.move
                    y_move = 0

        if snake_head_x >= gc.width or snake_head_x < 0 or snake_head_y >= gc.height or snake_head_y < 0:
            finishedGame = True

        snake_head_x += x_move
        snake_head_y += y_move
        screen.fill(gc.white)
        draw.rect(screen, colors[color_index + 1], (food_x, food_y, gc.size_food, gc.size_food))
        
        snake_head = [snake_head_x, snake_head_y]
        snake.append(snake_head)
        
        if len(snake) > snake_length:
            del snake[0]
        
        for square in snake[:-1]:
            if square == snake_head:
                finishedGame = True
        
        snake_add(gc.size_snake, snake)
        
        if snake_head_x == food_x and snake_head_y == food_y:
            snake_length += 1
            food_x = gc.size_snake * random.randint(0, gc.width / 10 - gc.food_margin)
            food_y = gc.size_snake * random.randint(0, gc.height / 10 - gc.food_margin)
            frames += 1
            if color_index + 2 < len(colors):
                color_index += 1
            else:
                color_index = 0
        
        #score(snake_length - 1)
        
        display.flip()
        clock.tick(frames)
        
    pygame.quit()

game_loop()