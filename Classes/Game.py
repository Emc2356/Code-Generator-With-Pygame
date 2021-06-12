from Classes.Code_Generator import Code_Generator as CG
from Classes.GUI import GUI
from Classes.Bar import Bar
from Classes.Window_Buttons import Window_Buttons
from Classes.Button import Button
import pygame
import pyperclip as pc


pygame.init()
pygame.font.init()


class Game:
    def __init__(self, WIN: pygame.Surface, WIDTH: int, HEIGHT: int, bar: Bar, Gui: GUI, Win_Buttons: Window_Buttons,
                 Cg: CG, copy_button: Button, clock: pygame.time.Clock, FPS: int):
        """
        Parameters:

         WIN: pygame.Surface
         WIDTH: int
         HEIGHT: int
         bar: Bar
         Gui: GUI
         Win_Buttons: Window_Buttons
         Cg: CG
         copy_button: Button
         clock: pygame.time.Clock
         FPS: int

        """
        self.WIN = WIN
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.bar = bar
        self.Gui = Gui
        self.Win_Buttons = Win_Buttons
        self.Cg = Cg
        self.copy_button = copy_button
        self.clock = clock
        self.FPS = FPS

        self.Gui.set_window(TITLE="Password Manager")
        self.Win_Buttons.setup_setting_buttons()

    def copy(self, copy):
        """
        copies a give thing into the clipboard
        :return: None
        """
        pc.copy(copy)

    def draw(self):
        """
        draws everything that it can
        :return: None
        """
        # self.Cg is just the logic for the code generator and not the actual GUI that is used
        self.Gui.draw()
        self.Win_Buttons.draw()
        self.copy_button.draw()
        self.bar.draw()
        pygame.display.update()

    def events(self):
        """
        checks for events
        :return: None
        """
        for event in pygame.event.get():
            # checks if the user wants to quit
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                pygame.quit()
                quit(-1)
            # check if the user presses the copy_button to copy the code
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.copy_button.is_over(pygame.mouse.get_pos()):
                    self.copy("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    def run(self):
        while True:
            self.clock.tick(self.FPS)
            self.draw()
            self.events()
