import pygame
import sys
from constant import *
from paddle import Paddle
from ball import Ball
import math

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("bgm.mp3")
pygame.mixer.music.set_volume(1)
button_sound = pygame.mixer.Sound("button.mp3")
hit_sound = pygame.mixer.Sound("hit.wav")
win_sound = pygame.mixer.Sound("win.mp3")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong - momo")
clock = pygame.time.Clock()
player_1 = Paddle(x=35, y=265)
player_2 = Paddle(x=WIDTH-45, y=265)
ball = Ball(x=WIDTH//2, y=HEIGHT//2)
score_1 = 0
score_2 = 0
font = pygame.font.SysFont("ariel", 70)
menu_bg = pygame.image.load("menu.png")
menu_bg = pygame.transform.scale(menu_bg, (WIDTH, HEIGHT))
button_img = pygame.image.load("menu_button.png")
button_img = pygame.transform.scale(button_img, (120, 50))
game_state = "menu"
timer = 0
button_rect = pygame.Rect(345, 450, 120, 50)
title_font = pygame.font.Font("PoetsenOne-Regular.ttf", 80)
title1_font = pygame.font.Font("PoetsenOne-Regular.ttf", 48)
def draw_menu(screen, timer):
    screen.blit(menu_bg, (0, 0))
    title = "PONG"
    for i, letter in enumerate(title):
        y_offset = math.sin(timer + i * 0.5) * 10
        letter_surface = title_font.render(letter, True, white)
        screen.blit(letter_surface, (300 + i * 50, 150 + y_offset))
    button_y = 450 + math.sin(timer) * 10
    screen.blit(button_img, (button_rect.x, button_y))
title_img = pygame.image.load("title.png")
title_img = pygame.transform.scale(title_img, (800, 600))
winner = None
def draw_endscreen(screen, winner, timer):
    screen.blit(title_img, (0, 0))
    number_text = title1_font.render(str(winner), True, white)
    screen.blit(number_text, (408 - 30, 189))
pygame.mixer.music.play(-1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "menu":
                if button_rect.collidepoint(pygame.mouse.get_pos()):
                    button_sound.play()
                    game_state = "playing"

    timer += 0.05

    if game_state == "menu":
        draw_menu(screen, timer)
    elif game_state == "playing":
        screen.fill(black)
        player_1.move(pygame.K_w, pygame.K_s)
        player_2.move(pygame.K_UP, pygame.K_DOWN)
        if ball.check_collision(player_1, player_2):
            hit_sound.play()
        point = ball.move()
        if point == 1:
            score_1 += 1
        elif point == 2:
            score_2 += 1
        elif point == "wall":
            hit_sound.play()
        text1 = font.render(str(score_1), True, white)
        text2 = font.render(str(score_2), True, white)
        screen.blit(text1, (WIDTH//2 - 60, 20))
        screen.blit(text2, (WIDTH//2 + 34, 20))
        if score_1 == WINNING_SCORE:
            winner = 1
            win_sound.play()
            game_state = "endscreen"
        elif score_2 == WINNING_SCORE:
            winner = 2
            win_sound.play()
            game_state = "endscreen"
        player_1.draw(screen)
        player_2.draw(screen)
        ball.draw(screen)
        y = 10
        while y < HEIGHT:
            pygame.draw.rect(screen, (204, 204, 204), (WIDTH//2 - 2, y, 5, 20))
            y += 35
    elif game_state == "endscreen":
        draw_endscreen(screen, winner, timer)
    pygame.display.flip()
    clock.tick(FPS)

#you shouldent be reading this 🤨