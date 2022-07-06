import math

import pygame

from constants import *


class Dots:
    def __init__(self):
        self.width = 1
        self.radius = 7
        self.drag = None
        self.coordinates = []

    def create_dot(self, pos):
        create = True
        for position in self.coordinates:
            if self.__in_circle(pos, position):
                create = False
        if create:
            self.coordinates += [pos]
            return
        return pos

    def delete_dot(self, pos):
        remove = []

        for position in self.coordinates:
            if self.__in_circle(pos, position):
                remove += [position]

        self.coordinates = [position for position in self.coordinates if position not in remove]

    def drag_dot(self, pos):
        pass

    def render(self, screen):
        for position in self.coordinates:
            pygame.draw.circle(screen, WHITE, position, self.radius, self.width)

    def __in_circle(self, pos_click, pos_dot):
        x_click = pos_click[0]
        y_click = pos_click[1]

        x_dot = pos_dot[0]
        y_dot = pos_dot[1]

        distance = math.sqrt((x_click - x_dot) ** 2 + (y_click - y_dot) ** 2)
        if distance <= self.radius:
            return True
        return False
