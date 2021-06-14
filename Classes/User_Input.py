import pygame


class User_Input:
    def __init__(self, WIDTH: int, HEIGHT: int, x: int, y: int, width: int, height: int,
                 base_color: tuple[int, int, int], WIN: pygame.Surface, text_color: tuple[int, int, int], font_size: int):
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
        self.key_num = {
            "normal": {
                       0: 48,
                       1: 49,
                       2: 50,
                       3: 51,
                       4: 52,
                       5: 53,
                       6: 54,
                       7: 55,
                       8: 56,
                       9: 57
                       },
            "num_pad": {
                        0: 1073741922,
                        1: 1073741913,
                        2: 1073741914,
                        3: 1073741915,
                        4: 1073741916,
                        5: 1073741917,
                        6: 1073741918,
                        7: 1073741919,
                        8: 1073741920,
                        9: 1073741921
                        }
        }

    def draw(self):
        """
        draws the bar in the window
        :return: None
        """
        # pygame.draw.rect(pygame.Surface, color: tuple, (x, y, width, height))
        pygame.draw.rect(self.WIN, self.base_clr, (self.x, self.y, self.width, self.height))
        text = self.font.render(str(self.text), True, self.text_clr)
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

    def insert_letter(self, ltr):
        """
        inserts the letter at the end of the text
        :param ltr: str
        :return: None
        """
        self.text += ltr

    def write(self, character, MAX: int=4):
        """
        writes a character to the field
        :param character: any
        :param MAX: int
        :return: None
        """
        if len(self.text) >= MAX:
            return
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

    def event_handler(self, event):
        """
        :param event: pygame.Event
        :return: None
        """
        # number input
        if event.key in self.key_num["normal"].values() or event.key in self.key_num["num_pad"].values():
            # check for normal 0-9 values
            if event.key in self.key_num["normal"].values():
                for char_value in list(self.key_num["normal"].values()):
                    if char_value == event.key:
                        self.write(str(list(self.key_num["normal"].values()).index(char_value)))
            # check for numpad input 0-9
            elif event.key in self.key_num["num_pad"].values():
                for char_value in list(self.key_num["num_pad"].values()):
                    if char_value == event.key:
                        self.write(str(list(self.key_num["num_pad"].values()).index(char_value)))
        # delete last character from the text
        if event.key == pygame.K_BACKSPACE:
            """check if the user wants to delete the last item from a list"""
            self.delete_last()
