import pygame


class GUI:
    def __init__(self, WIDTH: int, HEIGHT: int, BASE_COLOR: tuple, WIN: pygame.surface):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.BASE_COLOR = BASE_COLOR
        self.WIN = WIN

    def draw(self):
        self.WIN.fill(self.BASE_COLOR)
        pygame.display.update()

    def escape(self):
        """
        check if the player has quited the window
        :return: Bool
        """
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                return True
        return False

    def set_window(self, TITLE: str):
        pygame.display.set_caption(TITLE)
        # pygame.display.set_icon("icon")


