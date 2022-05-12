import pygame.draw


class Floor:
    def __init__(self):
        self.rect = pygame.Rect(0, 700, 1280, 20)

    def render(self, display):
        pygame.draw.rect(display, (0, 255, 0), self.rect)