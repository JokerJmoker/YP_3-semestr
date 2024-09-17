#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math

SCREEN_DIM = (800, 600)


# =======================================================================================
# Функции для работы с векторами
# =======================================================================================
class Vec2D:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Vec2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vec2D(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        if scalar == 0:
            raise ValueError("Деление на ноль!")
        return Vec2D(self.x / scalar, self.y / scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self): # возвращает длину вектора через встроенную функцию len().
        return int(self.length())

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def int_pair(self):  # возвращает кортеж из двух целых чисел, представляющих координаты вектора.
        return int(self.x), int(self.y)


# =======================================================================================
# Функции отрисовки
# =======================================================================================
class Polyline:
    def __init__(self):
        self.points = []  # список точек Vec2D
        self.velocities = []  # список скоростей для каждой точки

    def add_point(self, point, velocity):
        """Добавление точки с её скоростью."""
        self.points.append(point)
        self.velocities.append(velocity)

    def set_points(self): # пересчёт координат точек с учётом их скоростей
        for i in range(len(self.points)):
            self.points[i] += self.velocities[i]

            # обработка выхода точки за границы экрана 
            if self.points[i].x > 800 or self.points[i].x < 0:
                self.velocities[i] = Vec2D(-self.velocities[i].x, self.velocities[i].y)
            if self.points[i].y > 600 or self.points[i].y < 0:
                self.velocities[i] = Vec2D(self.velocities[i].x, -self.velocities[i].y)

    def draw_points(self, surface, style="points", width=3, color=(255, 255, 255)): # без изменений
        if style == "line" and len(self.points) > 1:
            for p_n in range(-1, len(self.points) - 1):
                pygame.draw.line(surface, color, self.points[p_n].int_pair(),
                                 self.points[p_n + 1].int_pair(), width)
        elif style == "points":
            for p in self.points:
                pygame.draw.circle(surface, color, p.int_pair(), width)


def draw_help(surface, steps):
    """Функция отрисовки экрана справки программы"""
    surface.fill((50, 50, 50))
    font1 = pygame.font.SysFont("courier", 24)
    font2 = pygame.font.SysFont("serif", 24)
    data = []
    data.append(["F1", "Show Help"])
    data.append(["R", "Restart"])
    data.append(["P", "Pause/Play"])
    data.append(["Num+", "More points"])
    data.append(["Num-", "Less points"])
    data.append(["", ""])
    data.append([str(steps), "Current points"])

    pygame.draw.lines(surface, (255, 50, 50), True, [
        (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate(data):
        surface.blit(font1.render(text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        surface.blit(font2.render(text[1], True, (128, 128, 255)), (200, 100 + 30 * i))



# =======================================================================================
# Функции, отвечающие за расчет сглаживания ломаной
# =======================================================================================
class Knot(Polyline):
    def __init__(self):
        super().__init__()

    def get_knot(self, count):
        """Расчёт точек кривой по опорным точкам"""
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(self.points) - 2):
            ptn = [
                (self.points[i] + self.points[i + 1]) * 0.5,
                self.points[i + 1],
                (self.points[i + 1] + self.points[i + 2]) * 0.5
            ]
            res.extend(self.get_points(ptn, count))
        return res

    def get_points(self, base_points, count):
        """Получение точек кривой"""
        alpha = 1 / count
        res = []
        for i in range(count):
            res.append(self.get_point(base_points, i * alpha))
        return res

    def get_point(self, points, alpha, deg=None):
        """Вычисление точки на основе рекурсивного деления"""
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return points[deg] * alpha + self.get_point(points, alpha, deg - 1) * (1 - alpha)

    def set_points(self):
        """Пересчёт точек кривой с пересчётом опорных точек"""
        super().set_points()  # пересчёт опорных точек
        return self.get_knot(35)  # получение кривой через опорные точки

    def draw_points(self, surface, style="line", width=5, color=(255, 255, 255)):
        """Отрисовка кривой на экране"""
        curve_points = self.get_knot(35)  # Получаем кривую
        if style == "line" and len(curve_points) > 1:
            for i in range(len(curve_points) - 1):
                pygame.draw.line(surface, color, curve_points[i].int_pair(), curve_points[i + 1].int_pair(), width)
        elif style == "points":
            for p in curve_points:
                pygame.draw.circle(surface, color, p.int_pair(), width)


# =======================================================================================
# Основная программа
# =======================================================================================
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

    knot = Knot()  # Создаем экземпляр класса Knot

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
                    knot = Knot()  # Пересоздаем экземпляр, чтобы сбросить точки
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                point = Vec2D(*event.pos)
                velocity = Vec2D(random.random() * 2, random.random() * 2)
                knot.add_point(point, velocity)

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)

        knot.set_points()  # Обновляем точки с учетом их скоростей
        knot.draw_points(gameDisplay)  # Отрисовка ломаной
        knot.draw_points(gameDisplay, "line", 3, color)  # Отрисовка кривой

        if show_help:
            draw_help(gameDisplay, len(points))

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
