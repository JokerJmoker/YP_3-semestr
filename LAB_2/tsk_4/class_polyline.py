import pygame 
from class_vec2D import Vec2d


class Polyline:
    def __init__(self):
        self.points = []
        self.speeds = []

    def add_point(self, point, speed):
        self.points.append(point)
        self.speeds.append(speed)

    def set_points(self, screen_dim):
        for i in range(len(self.points)):
            self.points[i] = self.points[i] + self.speeds[i]
            if self.points[i].x > screen_dim[0] or self.points[i].x < 0:
                self.speeds[i] = Vec2d(-self.speeds[i].x, self.speeds[i].y)
            if self.points[i].y > screen_dim[1] or self.points[i].y < 0:
                self.speeds[i] = Vec2d(self.speeds[i].x, -self.speeds[i].y)

    def draw_points(self, game_display, style="line", width=3, color=(255, 255, 255)):
        if style == "line":
            for p_n in range(-1, len(self.points) - 1):
                pygame.draw.line(game_display, color,
                                 self.points[p_n].int_pair(),
                                 self.points[p_n + 1].int_pair(), width)
        elif style == "points":
            for point in self.points:
                pygame.draw.circle(game_display, color,
                                   point.int_pair(), width)
