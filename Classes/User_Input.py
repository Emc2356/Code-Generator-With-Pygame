import pygame


class User_Input:
    def __init__(self, WIDTH: int, HEIGHT: int, x: int, y: int, width: int, height: int,
                 base_color: tuple, WIN: pygame.Surface, text_color: tuple, font_size: int):
        """
        Parameters
        ----------

         WIDTH: int
         HEIGHT: int
         x: int
         y: int
         width: int
         height: int
         base_color: tuple
         WIN: pygame.Surface
         text_color: tuple
         font_size: int
        """
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.base_clr = base_color
        self.WIN = WIN
        self.text_clr = text_color
        self.font_size = font_size
        self.font = pygame.font.SysFont("comicsans", self.font_size)
        self.text = ""
        self.antialias = True

    def draw(self):
        """
        draws the bar in the window
        :return: None
        """
        # pygame.draw.rect(pygame.Surface, color: tuple, (x, y, width, height))
        pygame.draw.rect(self.WIN, self.base_clr, (self.x, self.y, self.width, self.height))
        text = self.font.render(str(self.text), 1, self.text_clr)
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
        elif keys[pygame.K_1]:
            return 1
        elif keys[pygame.K_2]:
            return 2
        elif keys[pygame.K_3]:
            return 3
        elif keys[pygame.K_4]:
            return 4
        elif keys[pygame.K_5]:
            return 5
        elif keys[pygame.K_6]:
            return 6
        elif keys[pygame.K_7]:
            return 7
        elif keys[pygame.K_8]:
            return 8
        elif keys[pygame.K_9]:
            return 9
        elif keys[pygame.K_KP0]:
            return 0
        elif keys[pygame.K_KP1]:
            return 1
        elif keys[pygame.K_KP2]:
            return 2
        elif keys[pygame.K_KP3]:
            return 3
        elif keys[pygame.K_KP4]:
            return 4
        elif keys[pygame.K_KP5]:
            return 5
        elif keys[pygame.K_KP6]:
            return 6
        elif keys[pygame.K_KP7]:
            return 7
        elif keys[pygame.K_KP8]:
            return 8
        elif keys[pygame.K_KP9]:
            return 9
        else:
            return False

    def insert_letter(self, ltr):
        """
        inserts the letter at the end of the text
        :param ltr: str
        :return: None
        """
        self.text += ltr

    def write(self, character):
        """
        writes a character to the field
        :param character: any
        :return: None
        """
        self.text += character

    def clear(self):
        """
        clears the tect that is writen
        :return: None
        """
        self.text = ""

    def delete_last(self):
        """
        deletes the last character of the text
        :return: None
        """
        self.text = self.text[:-1]

    def get_text(self):
        """
        it gives the current text of the field
        :return: self.text: str
        """
        return self.text

    def is_empty(self):
        """
        tells if the field is empty
        :return: bool
        """
        return self.text == ""

    def text_color(self, color: tuple):
        """
        sets the color for the text
        :param color: tuple
        :return: None
        """
        self.text_clr = color

    def base_color(self, color: tuple):
        """
        sets the color of the base field color
        :param color:
        :return: None
        """
        self.base_clr = color

    def events(self, event):
        """
        pygame events that are used by this class
        :param event: pygame.Event
        :return: None
        """
        if event.type == pygame.K_BACKSPACE:
            self.delete_last()
