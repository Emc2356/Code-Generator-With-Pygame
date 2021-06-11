import pygame


class Bar:
    def __init__(self, WIDTH, HEIGHT, x, y, width, height, color, WIN, font_size):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.WIN = WIN
        self.font_size = font_size
        self.font = pygame.font.SysFont("comicsans", self.font_size)

    def draw(self):
        """
        draws the bar in the window
        :return: None
        """
        # pygame.draw.rect(pygame.Surface, color: tuple, (x, y, width, height))
        pygame.draw.rect(self.WIN, self.color, (self.x, self.y, self.width, self.height))

    def get_width(self):
        """
        returns the width of the bar
        :return: int
        """
        return self.width

    def get_height(self):
        """
        returns the height of the bar
        :return: int
        """
        return self.height

    def check_for_input(self):
        """
        it checks if the user typed anything in the bar
        :return:
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_0]:
            return True, 0
        if keys[pygame.K_1]:
            return True, 1
        if keys[pygame.K_2]:
            return True, 2
        if keys[pygame.K_3]:
            return True, 3
        if keys[pygame.K_4]:
            return True, 4
        if keys[pygame.K_5]:
            return True, 5
        if keys[pygame.K_6]:
            return True, 6
        if keys[pygame.K_7]:
            return True, 7
        if keys[pygame.K_8]:
            return True, 8
        if keys[pygame.K_9]:
            return True, 9
        if keys[pygame.K_KP0]:
            return True, 0
        if keys[pygame.K_KP1]:
            return True, 1
        if keys[pygame.K_KP2]:
            return True, 2
        if keys[pygame.K_KP3]:
            return True, 3
        if keys[pygame.K_KP4]:
            return True, 4
        if keys[pygame.K_KP5]:
            return True, 5
        if keys[pygame.K_KP6]:
            return True, 6
        if keys[pygame.K_KP7]:
            return True, 7
        if keys[pygame.K_KP8]:
            return True, 8
        if keys[pygame.K_KP9]:
            return True, 9
        else:
            return False