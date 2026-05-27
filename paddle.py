from constant import *
import pygame

class Paddle:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.velocity = 0
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.image = pygame.image.load("paddle.png")
        self.image = pygame.transform.scale(self.image, (14, 82))
        self.rect = pygame.Rect(x, y, self.paddle_width, self.paddle_height)
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def move(self, up_key, down_key):
        keys = pygame.key.get_pressed()
        if keys[up_key] == True:
            self.velocity -= paddle_speed
        elif keys[down_key] == True:
            self.velocity += paddle_speed
        else:
            self.velocity *= 0.01
        self.rect.y += self.velocity
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y + self.paddle_height > HEIGHT:
            self.rect.y = HEIGHT - self.paddle_height
