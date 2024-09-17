import pygame
from class_polyline import Polyline

class Knot(Polyline):
    def __init__(self, steps=100):
        super().__init__()
        self.steps = steps
        self.smooth_points = []

    def add_point(self, point, speed):
        super().add_point(point, speed)
        self.smooth_points = self.get_knot()

    def set_points(self, screen_dim):
        super().set_points(screen_dim)
        self.smooth_points = self.get_knot()

    def get_point(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return points[deg] * alpha + self.get_point(points, alpha, deg - 1) * (1 - alpha)

    def get_points(self, base_points, count):
        alpha = 1 / count
        return [self.get_point(base_points, i * alpha) for i in range(count)]

    def get_knot(self):
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(self.points) - 2):
            ptn = []
            ptn.append((self.points[i] + self.points[i + 1]) * 0.5)
            ptn.append(self.points[i + 1])
            ptn.append((self.points[i + 1] + self.points[i + 2]) * 0.5)
            res.extend(self.get_points(ptn, self.steps))
        return res

    def draw_points(self, game_display, style="line", width=3, color=(255, 255, 255)):
        if style == "line":
            for p_n in range(-1, len(self.smooth_points) - 1):
                pygame.draw.line(game_display, color,
                                 self.smooth_points[p_n].int_pair(),
                                 self.smooth_points[p_n + 1].int_pair(), width)
        elif style == "points":
            super().draw_points(game_display, style, width, color)
