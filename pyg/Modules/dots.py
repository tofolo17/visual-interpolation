import math

import pygame

from pyg.constants import *


class Dots:
    def __init__(self):
        self.width = 1
        self.radius = 7
        self.coordinates = []
        self.drag_index = None

    def create_dot(self, pos):
        create = True

        for i in range(len(self.coordinates)):
            position = self.coordinates[i]
            if self.__in_circle(pos, position):
                self.drag_index = i
                create = False
        if create:
            self.coordinates += [pos]

    def delete_dot(self, pos):
        remove = []

        for position in self.coordinates:
            if self.__in_circle(pos, position):
                remove += [position]

        self.coordinates = [position for position in self.coordinates if position not in remove]

    def start_drag(self, pos):
        if self.drag_index is not None:
            self.coordinates[self.drag_index] = pos

    def stop_drag(self):
        self.drag_index = None

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
