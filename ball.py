import pygame
from constant import *
import random
import math

class Ball:
    def __init__(self, x,y):
        self.hit_cooldown = 0
        self.ball_width = 15
        self.ball_height = 15
        self.float_x = float(x)
        self.float_y = float(y)
        self.speed = ball_speed
        self.angle = random.uniform(30, 60)
        if random.choice([True, False]):
            self.angle += 180
        self.image = pygame.image.load("ball.png")
        self.image = pygame.transform.scale(self.image, (self.ball_width, self.ball_height))
        self.rect = pygame.Rect(x, y, self.ball_width, self.ball_height)
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def move(self):
        self.float_x += self.speed * math.cos(math.radians(self.angle))
        self.float_y += self.speed * math.sin(math.radians(self.angle))
        self.rect.x = int(self.float_x)
        self.rect.y = int(self.float_y)
        if self.rect.y <= 0 or self.rect.y + self.ball_height >= HEIGHT:
            self.angle *= -1
            return "wall"
        if self.rect.x <= 0:
            self.float_x = WIDTH // 2
            self.float_y = HEIGHT // 2
            self.rect.x = int(self.float_x)
            self.rect.y = int(self.float_y)
            self.angle = random.uniform(30, 60)
            if random.choice([True, False]):
                self.angle += 180
            return 2
        if self.rect.x + self.ball_width >= WIDTH:
            self.float_x = WIDTH // 2
            self.float_y = HEIGHT // 2
            self.rect.x = int(self.float_x)
            self.rect.y = int(self.float_y)
            self.angle = random.uniform(30, 60)
            if random.choice([True, False]):
                self.angle += 180
            return 1
        return None
    def check_collision(self, paddle1, paddle2):
        if self.hit_cooldown > 0:
            self.hit_cooldown -= 1
            return False
        for paddle in [paddle1, paddle2]:
            if self.rect.colliderect(paddle.rect):
                old_angle = self.angle
                hit_pos = (self.rect.centery - paddle.rect.centery) / (paddle.paddle_height / 2)
                self.angle = 180 - self.angle + (hit_pos * 20)
                if math.cos(math.radians(old_angle)) > 0:
                    self.rect.x = paddle.rect.left - self.ball_width - 1
                else:
                    self.rect.x = paddle.rect.right + 1
                self.float_x = float(self.rect.x)
                self.hit_cooldown = 10 
                return True
        return False