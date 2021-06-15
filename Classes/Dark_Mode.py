from itertools import cycle
import pygame


class Dark_Mode:
    def __init__(self, WIN: pygame.Surface, imgs: list[pygame.Surface, pygame.Surface],
                 colors: list[tuple[int, int, int], tuple[int, int, int]], x: float, y: float):
        """
        it creates a white mode button that you can press to switch modes
        this is on the top of the draw function/method because it fills the screen

        Parameters
         ----------

         WIN: pygame.Surface
          the surface that the button is going to be drawn in
         imgs: list[pygame.Surface, pygame.Surface]
          the images that are going to be drawn to the surface
         colors: list[tuple[int, int, int], tuple[int, int, int]]
          the colors that are used to for bright and dark mod
         x: float
          the x location of the button
         y: float
          the y location of the button
        """
        self.WIN = WIN
        self.imgs = cycle(imgs)
        self.cur_img = next(self.imgs)
        self.colors = cycle(colors)
        self.cur_color = next(self.colors)
        self.x = x
        self.y = y
        self.mode_rect = pygame.Rect((self.x, self.y, 32, 32))

    def event_handler(self, event):
        """
        checks for the events that this class can process
        :param event: pygame.Event
        :return: None
        """
        if self.mode_rect.collidepoint(event.pos):
            self.cur_img = next(self.imgs)
            self.cur_color = next(self.colors)

    def draw(self):
        """
        it fills the base screen the current color either bright or dark mode and then it draws the button
        :return: None
        """
        self.WIN.fill(self.cur_color)
        self.WIN.blit(self.cur_img, (self.x, self.y))


