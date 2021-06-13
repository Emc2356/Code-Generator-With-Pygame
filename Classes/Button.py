import pygame


class Button:
    def __init__(self, color, x: int, y: int, width: int, height: int, WIN: pygame.Surface,
                 text_color: tuple, text='', font_size: int=60):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text_color = text_color
        self.text = text
        self.WIN = WIN
        self.font_size = font_size

    def draw(self, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(self.WIN, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(self.WIN, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', self.font_size)
            text = font.render(self.text, 1, self.text_color)
            self.WIN.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def is_over(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_pos(self):
        """
        it returns the poss of the button
        :return: tuple(x, y)
        """
        return self.x, self.y
