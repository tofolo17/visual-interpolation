import math

import pygame

from constants import *


class Dots:
    def __init__(self):
        self.width = 1
        self.radius = 7
        self.coordinates = []

    def create_dot(self, pos):
        self.coordinates += [pos]

    def delete_dot(self, pos):
        x_click = pos[0]
        y_click = pos[1]
        remove = []

        # Como checar apenas pontos próximos?
        for position in self.coordinates:
            x_dot = position[0]
            y_dot = position[1]

            distance = math.sqrt((x_click - x_dot) ** 2 + (y_click - y_dot) ** 2)
            if distance <= self.radius:
                remove += [position]

        self.coordinates = [position for position in self.coordinates if position not in remove]

    def render(self, screen):
        for position in self.coordinates:
            pygame.draw.circle(screen, WHITE, position, self.radius, self.width)
