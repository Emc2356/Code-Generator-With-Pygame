from Classes.Code_Generator import Code_Generator as CG
from Classes.GUI import GUI
from Classes.User_Input import User_Input
from Classes.Window_Buttons import Window_Buttons
from Classes.Button import Button
import pygame
import pyperclip as pc


pygame.init()
pygame.font.init()


class Game:
    def __init__(self, WIN: pygame.Surface, WIDTH: int, HEIGHT: int, bar: User_Input, Gui: GUI, Win_Buttons: Window_Buttons,
                 Cg: CG, copy_button: Button, reg_button: Button, clock: pygame.time.Clock, FPS: int):
        """
        Parameters:
         ----------------------

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
        self.reg_button = reg_button
        self.clock = clock
        self.FPS = FPS
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
        self.reg_button.draw()
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
                self.click_events(event)
            # checks if the user pressed any buttons
            if event.type == pygame.KEYDOWN:
                self.keyboard_events(event)

    def click_events(self, event):
        """
        click related events
        :param event: pygame.Event
        :return: None
        """
        self.Win_Buttons.clicked(pygame.mouse.get_pos())
        if self.copy_button.is_over(pygame.mouse.get_pos()):
            self.copy("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    def keyboard_events(self, event):
        """
        click related events
        :param event: pygame.Event
        :return: None
        """
        self.bar.events(event)

    def run(self):
        while True:
            self.clock.tick(self.FPS)
            self.draw()
            self.events()
