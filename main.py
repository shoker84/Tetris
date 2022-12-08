import pygame as pg
import math


def main():
    w = 10
    h = 20
    tile = 45
    fps = 60
    run = True
    pg.init()
    screen = pg.display.set_mode((w * tile, h * tile), pg.NOFRAME)
    clock = pg.time.Clock()
    grid = [pg.Rect(x * tile, y * tile, tile, tile) for x in range(w) for y in range(h)]
    figur_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
               [(0, -1), (-1, -1), (-1, 0), (0, 0)],
               [(-1, 0), (-1, 1), (0, 0), (0, -1)],
               [(0, 0), (-1, 0), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, 0)]]
    figures = [[pg.Rect(x+w//2, y+1, 1, 1) for x, y in fig_pos] for fig_pos in figur_pos]
    figur_rect = pg.Rect(0, 0, tile-2, tile-2)
    figur = figures[6]
    while run:
        dx = 0
        screen.fill('black')
        clock.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False
                elif event.key == pg.K_RIGHT:
                    dx = 1
                elif event.key == pg.K_LEFT:
                    dx = -1
        [pg.draw.rect(screen, 'white', i_rect, 1) for i_rect in grid]
        for i in range(4):
            figur[i].x += dx
        for i in range(4):
            figur_rect.x = figur[i].x * tile
            figur_rect.y = figur[i].y * tile
            pg.draw.rect(screen, 'blue', figur_rect)
        pg.display.update()


if __name__ == '__main__':
    main()
