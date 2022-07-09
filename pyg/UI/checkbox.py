import pygame as pg


class Checkbox:
    """
    TODO: relacionar self.click com self.checked
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.color = (230, 230, 230)
        self.check_color = (0, 0, 0)
        self.outline_color = (0, 0, 0)

        self.checkbox_size = 12
        self.checkbox_obj = pg.Rect(self.x, self.y, self.checkbox_size, self.checkbox_size)
        self.checkbox_outline = self.checkbox_obj.copy()

        self.click = False
        self.checked = False
        self.unchecked = True

    def check_click(self, coordinate):
        x = coordinate[0]
        y = coordinate[1]

        px, py, w, h = self.checkbox_obj
        if px < x < px + w and py < y < py + h:
            self.click = True
        else:
            self.click = False

    def render(self, screen):
        if self.checked:
            pg.draw.rect(screen, self.color, self.checkbox_obj)
            pg.draw.rect(screen, self.outline_color, self.checkbox_outline, 1)
            pg.draw.circle(screen, self.check_color, (self.x + 6, self.y + 6), 4)

        elif self.unchecked:
            pg.draw.rect(screen, self.color, self.checkbox_obj)
            pg.draw.rect(screen, self.outline_color, self.checkbox_outline, 1)
