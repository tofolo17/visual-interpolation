# Scratch test for the (unfinished) checkbox UI; its constructor has since
# changed, so this file is out of date.
from pyg.UI.checkbox import *

pg.init()


def main():
    WIDTH = 800
    HEIGHT = 600
    display = pg.display.set_mode((WIDTH, HEIGHT))

    checkbox = Checkbox(display, 400, 300)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                quit()
            checkbox.update_checkbox(event)

        display.fill((0, 0, 0))
        checkbox.render()
        pg.display.flip()


if __name__ == '__main__':
    main()
