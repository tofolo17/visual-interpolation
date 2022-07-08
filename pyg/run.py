from pygame.locals import *

from pyg.Modules.dots import *
from pyg.Modules.interpolation import *


class GameController(object):
    def __init__(self):
        pygame.init()
        self.dots = None
        self.spline = None
        self.linear = None
        self.background = None
        self.screen = pygame.display.set_mode(SCREENSIZE, 0, 32)

    def set_background(self):
        self.background = pygame.surface.Surface(SCREENSIZE).convert()

    def start_game(self):
        self.dots = Dots()
        self.set_background()
        self.spline = Spline(self.dots)
        self.linear = Linear(self.dots)

    def update(self):
        self.check_events()
        self.render()

    def check_events(self):
        for event in pygame.event.get():
            coordinate = pygame.mouse.get_pos()

            if event.type == QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.dots.create_dot(coordinate)

                if event.button == 3:
                    self.dots.delete_dot(coordinate)

            if event.type == pygame.MOUSEMOTION:
                self.dots.start_drag(coordinate)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.dots.stop_drag()

    def render(self):
        self.screen.fill(BLACK)

        self.dots.render(self.screen)
        self.spline.render(self.screen)
        self.linear.render(self.screen)

        pygame.display.update()


if __name__ == "__main__":
    game = GameController()
    game.start_game()

    while True:
        game.update()
