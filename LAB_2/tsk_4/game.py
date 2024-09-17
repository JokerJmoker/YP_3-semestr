import pygame, random 
from class_vec2D import Vec2d
from class_knot import Knot
from class_polyline import Polyline
from display import SCREEN_DIM

class Game:
    def __init__(self):
        pygame.init()
        self.game_display = pygame.display.set_mode(SCREEN_DIM)
        pygame.display.set_caption("MyScreenSaver")
        self.steps = 100
        self.working = True
        self.knot = Knot(steps=self.steps)
        self.show_help = False
        self.pause = True
        self.hue = 0
        self.color = pygame.Color(0)

    def draw_help(self):
        self.game_display.fill((50, 50, 50))
        font1 = pygame.font.SysFont("courier", 24)
        font2 = pygame.font.SysFont("serif", 24)
        data = [
            ["F1", "Show Help"],
            ["R", "Restart"],
            ["P", "Pause/Play"],
            ["Num+", "More points"],
            ["Num-", "Less points"],
            ["", ""],
            [str(self.steps), "Current points"]
        ]
        pygame.draw.lines(self.game_display, (255, 50, 50, 255), True, [
            (0, 0), (800, 0), (800, 600), (0, 600)], 5)
        for i, text in enumerate(data):
            self.game_display.blit(font1.render(
                text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
            self.game_display.blit(font2.render(
                text[1], True, (128, 128, 255)), (200, 100 + 30 * i))

    def run(self):
        while self.working:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.working = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.working = False
                    if event.key == pygame.K_r:
                        self.knot = Knot(steps=self.steps)
                    if event.key == pygame.K_p:
                        self.pause = not self.pause
                    if event.key == pygame.K_KP_PLUS:
                        self.steps += 1
                        self.knot.steps = self.steps
                    if event.key == pygame.K_F1:
                        self.show_help = not self.show_help
                    if event.key == pygame.K_KP_MINUS:
                        self.steps -= 1 if self.steps > 1 else 0
                        self.knot.steps = self.steps

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.knot.add_point(Vec2d(*event.pos), Vec2d(random.random() * 2, random.random() * 2))

            self.game_display.fill((0, 0, 0))
            self.hue = (self.hue + 1) % 360
            self.color.hsla = (self.hue, 100, 50, 100)
            self.knot.draw_points(self.game_display, style="line", width=3, color=self.color)
            self.knot.draw_points(self.game_display, style="points", width=3, color=(255, 255, 255))
            if not self.pause:
                self.knot.set_points(SCREEN_DIM)
            if self.show_help:
                self.draw_help()

            pygame.display.flip()

        pygame.display.quit()
        pygame.quit()
