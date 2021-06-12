import pygame


class GUI:
    def __init__(self, WIDTH: int, HEIGHT: int, BASE_COLOR: (int, int), WIN: pygame.surface):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.BASE_COLOR = BASE_COLOR
        self.WIN = WIN
        self.COLORS = {
            "WHITE": (255, 255, 255),
            "BLACK": (0, 0, 0),
            "RED": (255, 0, 0),
            "GREEN": (0, 255, 0),
            "BLUE": (0, 0, 255)
        }

    def draw(self):
        self.WIN.fill(self.BASE_COLOR)

    def set_window(self, TITLE: str):
        pygame.display.set_caption(TITLE)
        # pygame.display.set_icon("icon")

