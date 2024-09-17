import pygame
from class_vec2D import Vec2D
from display import gameDisplay

class Polyline:
    def __init__(self):
        self.points = []  # список точек Vec2D
        self.velocities = []  # список скоростей для каждой точки


    def add_point(self, point, velocity): # \\\ добавлено
        """Добавление точки с её скоростью."""
        self.points.append(point)
        self.velocities.append(velocity)


    def set_points(self): # пересчёт координат точек с учётом их скоростей \\\ добавлено
        for i in range(len(self.points)):
            self.points[i] += self.velocities[i]

            # обработка выхода точки за границы экрана 
            if self.points[i].x > 800 or self.points[i].x < 0:
                self.velocities[i] = Vec2D(-self.velocities[i].x, self.velocities[i].y)
            if self.points[i].y > 600 or self.points[i].y < 0:
                self.velocities[i] = Vec2D(self.velocities[i].x, -self.velocities[i].y)

    @staticmethod
    def draw_points(points, style="points", width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""
        if style == "line":
            for p_n in range(-1, len(points) - 1):
                pygame.draw.line(gameDisplay, color,
                                (int(points[p_n][0]), int(points[p_n][1])),
                                (int(points[p_n + 1][0]), int(points[p_n + 1][1])), width)

        elif style == "points":
            for p in points:
                pygame.draw.circle(gameDisplay, color,
                                (int(p[0]), int(p[1])), width)
