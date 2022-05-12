import pygame

from entity_manager import EntityManager
from floor import Floor
from player import Player


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode([1280, 720])
        self.running = False
        pygame.display.set_caption('Eier Jump')

        # Game components
        self.floor = Floor()
        self.player = Player()
        self.entity_manager = EntityManager()

        self.font = pygame.font.SysFont(None, 24)

    def run(self):
        self.running = True

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.update()
            self.render()

            pygame.display.flip()

    def update(self):
        self.player.move(self.floor)
        self.entity_manager.update(self.player, self.floor)

    def render_score(self):
        image = self.font.render(str(self.player.score), True, (255, 255, 255))
        self.screen.blit(image, (1, 1))

    def render(self):
        self.screen.fill([80, 120, 250])

        self.floor.render(self.screen)
        self.entity_manager.render(self.screen)
        self.player.render(self.screen)

        self.render_score()
