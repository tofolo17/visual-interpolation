import pygame

from pyg.constants import WHITE


class Linear:
    def __init__(self, dots):
        self.dots = dots

    def render(self, screen):
        coordinates = self.dots.coordinates

        for i in range(1, len(coordinates)):
            pygame.draw.line(screen, WHITE, coordinates[i - 1], coordinates[i])
