import pygame
import math


class Window_Buttons:
    def __init__(self, WIDTH: int, HEIGHT: int, WIN: pygame.surface, rad: int = 25):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.WIN = WIN
        self.rad = rad
        self.COLORS = {
            "WHITE": (255, 255, 255),
            "BLACK": (0, 0, 0),
            "RED": (255, 0, 0),
            "GREEN": (0, 255, 0),
            "BLUE": (0, 0, 255)
        }
        self.set_font = pygame.font.SysFont("comicsans", 30)
        self.antialias = True
        self.labels = [  ################ press this for
                  self.set_font.render("""upper characters""", self.antialias, self.COLORS["BLACK"]),
                  self.set_font.render("""lower characters""", self.antialias, self.COLORS["BLACK"]),
                  self.set_font.render("""numbers""", self.antialias, self.COLORS["BLACK"]),
                  self.set_font.render("""special characters""", self.antialias, self.COLORS["BLACK"])
        ]
        # settings buttons
        self.loc1_pressed = False
        self.loc2_pressed = False
        self.loc3_pressed = False
        self.loc4_pressed = False
        self.loc1 = (1, 1)
        self.loc2 = (1, 1)
        self.loc3 = (1, 1)
        self.loc4 = (1, 1)

    def draw(self):
        # draw settings buttons
        if self.loc1_pressed:
            pygame.draw.circle(self.WIN, self.COLORS["GREEN"], self.loc1, self.rad)
        elif not self.loc1_pressed:
            pygame.draw.circle(self.WIN, self.COLORS["RED"], self.loc1, self.rad)
        if self.loc2_pressed:
            pygame.draw.circle(self.WIN, self.COLORS["GREEN"], self.loc2, self.rad)
        elif not self.loc2_pressed:
            pygame.draw.circle(self.WIN, self.COLORS["RED"], self.loc2, self.rad)
        if self.loc3_pressed:
            pygame.draw.circle(self.WIN, self.COLORS["GREEN"], self.loc3, self.rad)
        elif not self.loc3_pressed:
            pygame.draw.circle(self.WIN, self.COLORS["RED"], self.loc3, self.rad)
        if self.loc4_pressed:
            pygame.draw.circle(self.WIN, self.COLORS["GREEN"], self.loc4, self.rad)
        elif not self.loc4_pressed:
            pygame.draw.circle(self.WIN, self.COLORS["RED"], self.loc4, self.rad)

        # draw the labels
        self.WIN.blit(self.labels[0], (self.loc1[0] + 50, self.loc1[1] - (self.rad / 2)))
        self.WIN.blit(self.labels[1], (self.loc2[0] + 50, self.loc2[1] - (self.rad / 2)))
        self.WIN.blit(self.labels[2], (self.loc3[0] + 50, self.loc3[1] - (self.rad / 2)))
        self.WIN.blit(self.labels[3], (self.loc4[0] + 50, self.loc4[1] - (self.rad / 2)))

    def setup_setting_buttons(self):
        """
        sets up the buttons for the settings that are hooked up to the code generator class at Classes/Code_Generator.Code_Generator
        :return: None
        """
        self.loc1 = (self.WIDTH / 5 - self.WIDTH / 8, 100)
        self.loc2 = (self.WIDTH / 5 - self.WIDTH / 8, 150 + 1)
        self.loc3 = (self.WIDTH / 5 - self.WIDTH / 8, 200 + 2)
        self.loc4 = (self.WIDTH / 5 - self.WIDTH / 8, 250 + 3)

    def clicked(self, m_pos: tuple):
        """
        tells if any of the buttons have been clicked
        :param m_pos: tuple
        :return: bool
        """
        # formula used to calculate the distance from the center of the circle: dis = math.sqrt((x - m_pos[0])**2 + (y - m_pos[1])**2)

        # upper characters
        if not self.loc1_pressed:
            dis = math.sqrt((self.loc1[0] - m_pos[0]) ** 2 + (self.loc1[1] - m_pos[1]) ** 2)
            if dis < self.rad:
                self.loc1_pressed = True
        elif self.loc1_pressed:
            dis = math.sqrt((self.loc1[0] - m_pos[0]) ** 2 + (self.loc1[1] - m_pos[1]) ** 2)
            if dis < self.rad:
                self.loc1_pressed = False

        # lower characters
        if not self.loc2_pressed:
            dis = math.sqrt((self.loc2[0] - m_pos[0]) ** 2 + (self.loc2[1] - m_pos[1]) ** 2)
            if dis < self.rad:
                self.loc2_pressed = True
        elif self.loc2_pressed:
            dis = math.sqrt((self.loc2[0] - m_pos[0]) ** 2 + (self.loc2[1] - m_pos[1]) ** 2)
            if dis < self.rad:
                self.loc2_pressed = False

        # numbers
        if not self.loc3_pressed:
            dis = math.sqrt((self.loc3[0] - m_pos[0]) ** 2 + (self.loc3[1] - m_pos[1]) ** 2)
            if dis < self.rad:
                self.loc3_pressed = True
        elif self.loc3_pressed:
            dis = math.sqrt((self.loc3[0] - m_pos[0]) ** 2 + (self.loc3[1] - m_pos[1]) ** 2)
            if dis < self.rad:
                self.loc3_pressed = False

        # special characters
        if not self.loc4_pressed:
            dis = math.sqrt((self.loc4[0] - m_pos[0]) ** 2 + (self.loc4[1] - m_pos[1]) ** 2)
            if dis < self.rad:
                self.loc4_pressed = True
        elif self.loc4_pressed:
            dis = math.sqrt((self.loc4[0] - m_pos[0]) ** 2 + (self.loc4[1] - m_pos[1]) ** 2)
            if dis < self.rad:
                self.loc4_pressed = False
