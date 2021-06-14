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
                 Cg: CG, copy_button: Button, reg_button: Button, clock: pygame.time.Clock, FPS: int, save_button: Button):
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
         save_button: Button

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
        self.save_button = save_button
        self.buttons = [copy_button, reg_button, save_button]
        self.clock = clock
        self.FPS = FPS
        self.save_input_field = User_Input(self.WIDTH, self.HEIGHT, 0, 50, self.WIDTH, 50,
                                           (0, 0, 0), self.WIN, (255, 255, 255), 60)
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
        for button in self.buttons:
            button.draw()
        self.bar.draw()
        pygame.display.update()

    def over(self):
        """
        checks if the mouse is over the copy or the generate button
        :return: None
        """

        # the copy button
        if self.copy_button.is_over(pygame.mouse.get_pos()):
            self.copy_button.color = (50, 0, 255)
        else:
            self.copy_button.color = (0, 0, 255)

        # the regen button
        if self.reg_button.is_over(pygame.mouse.get_pos()):
            self.reg_button.color = (255, 50, 30)
        else:
            self.reg_button.color = (255, 0, 0)

        # the save button
        if self.save_button.is_over(pygame.mouse.get_pos()):
            self.save_button.color = (80, 255, 30)
        else:
            self.save_button.color = (0, 255, 0)

    def events(self, save=False):
        """
        checks for events
        :return: None
        """
        if not save:
            for event in pygame.event.get():
                # checks if the user wants to quit
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    pygame.quit()
                    quit(-1)
                # check if the user presses the copy_button to copy the code
                if event.type == pygame.MOUSEBUTTONDOWN and not event.type == pygame.MOUSEWHEEL:
                    self.click_events(event)
                # checks if the user pressed any buttons
                if event.type == pygame.KEYDOWN:
                    self.keyboard_events(event)
        elif save:
            for event in pygame.event.get():
                # checks if the user wants to quit
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    pygame.quit()
                    quit(-1)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.save_input_field.delete_last()
                    else:
                        self.save_input_field.write(event.unicode, MAX=100)

    def click_events(self, event):
        """
        click related events
        :param event: pygame.Event
        :return: None
        """
        self.Win_Buttons.clicked(pygame.mouse.get_pos())
        if self.copy_button.is_over(pygame.mouse.get_pos()):
            self.copy(self.Cg.password)
        if self.reg_button.is_over(pygame.mouse.get_pos()):
            self.Cg.get_code()
        if self.save_button.is_over(pygame.mouse.get_pos()):
            self.save()

    def keyboard_events(self, event):
        """
        click related events
        :param event: pygame.Event
        :return: None
        """
        self.bar.events(event)

    def hook(self):
        """
        hooks the GUI with the algorithm for the code generation
        :return: None
        """

        # hooks the self.bar.text with the self.Cg.amount
        try:
            self.Cg.amount = int(self.bar.text)
        except ValueError:  # it cant convert a empty string to a int so it throws a error and we need to catch it so the program doesnt crash
            pass
        except Exception as e:  # catch any unexpected exceptions
            print(f"""[EXCEPTION] {e} | type: {type(e)}""")

        # hooks the sel.Win_Buttons.loc<1-4>pressed to self.Cg.char_<up|down|num|spec>
        try:
            self.Cg.char_up = self.Win_Buttons.loc1_pressed
            self.Cg.char_down = self.Win_Buttons.loc2_pressed
            self.Cg.char_num = self.Win_Buttons.loc3_pressed
            self.Cg.char_spec = self.Win_Buttons.loc4_pressed
        except Exception as e:  # catch any unexpected exceptions
            print(f"""[EXCEPTION] {e} | type: {type(e)}""")

    def save(self):
        """
        saves the code that is currently generated
        :return: None
        """
        while True:
            self.events(save=True)
            self.WIN.fill((255, 255, 255))
            self.save_input_field.draw()
            pygame.display.update()



    def run(self):
        while True:
            self.clock.tick(self.FPS)
            self.hook()
            self.events()
            self.over()
            self.draw()

