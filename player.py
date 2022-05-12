import pygame.image
from pygame import K_LEFT, K_RIGHT, K_UP


class Player:
    def __init__(self):
        self.texture = pygame.image.load('osterhase.png')
        self.texture_flipped = pygame.image.load('osterhase_flipped.png')

        self.current_texture = self.texture

        self.position_x = 500
        self.position_y = 400
        self.speed = 10

        self.max_y_pos = 500

        self.score = 0

    def render(self, display):
        display.blit(self.current_texture, (self.position_x, self.position_y))

    def move(self, floor):
        if self.position_x < 0:
            self.position_x = 0
        if self.position_x > 1280 - self.texture.get_width():
            self.position_x = 1280 - self.texture.get_width()

        keys = pygame.key.get_pressed()

        if keys[K_LEFT]:
            self.current_texture = self.texture_flipped
            self.position_x -= self.speed
        elif keys[K_RIGHT]:
            self.current_texture = self.texture
            self.position_x += self.speed

        if self.is_grounded(floor):
            self.speed = 10
            if keys[K_UP]:
                self.position_y -= 100

        if not self.is_grounded(floor):
            self.speed = 5
            self.position_y += 1.5

    def is_grounded(self, floor):
        return self.get_bounds().colliderect(floor.rect)

    def get_bounds(self):
        return pygame.Rect(self.position_x, self.position_y, self.texture.get_width(), self.texture.get_height())
