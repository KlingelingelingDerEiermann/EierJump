import time

import pygame.image
import random

from spawn_entity import SpawnEntity


class EntityManager:
    def __init__(self):
        self.ei_texture = pygame.image.load('ei.png')
        self.gift_texture = pygame.image.load('gift.png')

        self.entities = []

        self.time = time.perf_counter()

    def reset_game_state(self, player):
        player.score = 0
        self.entities.clear()
        player.position_x = 500
        player.position_y = 400
        player.current_texture = player.texture

    def update(self, player, floor):
        self.time = time.perf_counter()
        if self.time % 1 < 0.01:
            x_pos = random.randint(10, 1100)
            y_pos = random.randint(0, 100)
            variant = random.randint(0, 6)

            if variant == 3:
                self.entities.append(SpawnEntity(self.gift_texture, pygame.Rect(x_pos, y_pos, self.gift_texture.get_width(), self.gift_texture.get_height()), True))
            else:
                self.entities.append(SpawnEntity(self.ei_texture, pygame.Rect(x_pos, y_pos, self.ei_texture.get_width(), self.ei_texture.get_height()), False))

        for entity in self.entities:
            entity.rect = pygame.Rect(entity.rect.x, entity.rect.y + 1, entity.rect.width, entity.rect.height)

            if entity.rect.colliderect(floor.rect):
                self.entities.remove(entity)
                player.score -= 1
                if player.score < 0: player.score = 0

            if entity.rect.colliderect(player.get_bounds()):
                if entity.harmless:
                    self.reset_game_state(player)
                else:
                    self.entities.remove(entity)
                    player.score += 1
    def render(self, display):
        for entity in self.entities:
            display.blit(entity.texture, (entity.rect[0], entity.rect[1]))
