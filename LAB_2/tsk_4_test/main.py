#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame, random
from class_polyline import Polyline
from class_vec2D import Vec2D
from class_knot import Knot
from help import draw_help

SCREEN_DIM = (800, 600)
if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    steps = 35
    working = True
    points = []
    speeds = []
    show_help = False
    pause = True

    hue = 0
    color = pygame.Color(0)

    main_polyline = Polyline()
    main_knot = Knot()

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    points = []
                    speeds = []
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                points.append(event.pos)
                speeds.append((random.random() * 2, random.random() * 2))

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        main_knot.draw_points(points)
        main_knot.draw_points(main_knot.get_knot(points, steps), "line", 3, color)
        if not pause:
            main_knot.set_points(points, speeds)
        if show_help:
            draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
