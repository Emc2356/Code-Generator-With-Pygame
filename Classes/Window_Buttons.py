import pygame


class Window_Buttons:
    def __init__(self, WIDTH: int, HEIGHT: int, WIN: pygame.surface):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.WIN = WIN
        self.rad = 25
        self.COLORS = {
            "WHITE": (255, 255, 255),
            "BLACK": (0, 0, 0),
            "RED": (255, 0, 0),
            "GREEN": (0, 255, 0),
            "BLUE": (0, 0, 255)
        }
        self.set_font = pygame.font.SysFont("comicsans", 30)
        self.labels = [
                  self.set_font.render("""press this for upper characters""", 1, self.COLORS["BLACK"]),
                  self.set_font.render("""press this for lower characters""", 1, self.COLORS["BLACK"]),
                  self.set_font.render("""press this for numbers""", 1, self.COLORS["BLACK"]),
                  self.set_font.render("""press this for special characters""", 1, self.COLORS["BLACK"])]
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
        self.WIN.blit(self.labels[0], (self.loc1[0] + 50, self.loc1[1] - (self.rad/2)))
        self.WIN.blit(self.labels[1], (self.loc2[0] + 50, self.loc2[1] - (self.rad/2)))
        self.WIN.blit(self.labels[2], (self.loc3[0] + 50, self.loc3[1] - (self.rad/2)))
        self.WIN.blit(self.labels[3], (self.loc4[0] + 50, self.loc4[1] - (self.rad/2)))

    def setup_setting_buttons(self):
        """
        sets up the buttons for the settings that are hooked up to the code generator class at Classes/Code_Generator.Code_Generator
        :return: None
        """
        self.loc1 = (self.WIDTH/5 - self.WIDTH/8, 125)
        self.loc2 = (self.WIDTH/5 - self.WIDTH/8, 200)
        self.loc3 = (self.WIDTH/5 - self.WIDTH/8, 275)
        self.loc4 = (self.WIDTH/5 - self.WIDTH/8, 350)
