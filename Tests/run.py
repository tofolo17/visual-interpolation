import pygame
from pygame.locals import *

from constants import *
from dots import Dots


class GameController(object):
    def __init__(self):
        pygame.init()
        self.dots = None
        self.background = None
        self.screen = pygame.display.set_mode(SCREENSIZE, 0, 32)

    def set_background(self):
        self.background = pygame.surface.Surface(SCREENSIZE).convert()
        self.background.fill(BLACK)

    def start_game(self):
        self.set_background()
        self.dots = Dots()

    def update(self):
        self.check_events()
        self.render()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            coordinate = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.dots.create_dot(coordinate)
                if event.button == 3:
                    self.dots.delete_dot(coordinate)

    def render(self):
        self.dots.render(self.screen)
        pygame.display.update()


if __name__ == "__main__":
    game = GameController()
    game.start_game()
    while True:
        game.update()
