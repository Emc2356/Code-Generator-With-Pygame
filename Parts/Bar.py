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
        self.text = ""

    def draw(self):
        """
        draws the bar in the window
        :return: None
        """
        # pygame.draw.rect(pygame.Surface, color: tuple, (x, y, width, height))
        pygame.draw.rect(self.WIN, self.color, (self.x, self.y, self.width, self.height))
        text = self.font.render(str(self.text), 1, (255, 255, 255))
        self.WIN.blit(text, (
                            self.WIDTH/2 - text.get_width()/2,
                            self.y/2 + text.get_height()/2
                            )
                      )

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
            return 0
        if keys[pygame.K_1]:
            return 1
        if keys[pygame.K_2]:
            return 2
        if keys[pygame.K_3]:
            return 3
        if keys[pygame.K_4]:
            return 4
        if keys[pygame.K_5]:
            return 5
        if keys[pygame.K_6]:
            return 6
        if keys[pygame.K_7]:
            return 7
        if keys[pygame.K_8]:
            return 8
        if keys[pygame.K_9]:
            return 9
        if keys[pygame.K_KP0]:
            return 0
        if keys[pygame.K_KP1]:
            return 1
        if keys[pygame.K_KP2]:
            return 2
        if keys[pygame.K_KP3]:
            return 3
        if keys[pygame.K_KP4]:
            return 4
        if keys[pygame.K_KP5]:
            return 5
        if keys[pygame.K_KP6]:
            return 6
        if keys[pygame.K_KP7]:
            return 7
        if keys[pygame.K_KP8]:
            return 8
        if keys[pygame.K_KP9]:
            return 9
        else:
            return False
