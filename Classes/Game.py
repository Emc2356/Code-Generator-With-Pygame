from Classes import Code_Generator as CG
from Classes import Window_Buttons
from Classes import User_Input
from Classes import Dark_Mode
from Classes import Button
import pyperclip as pc
import pygame
import json


pygame.init()
pygame.font.init()


class Game:
    def __init__(self, WIN: pygame.Surface, WIDTH: int, HEIGHT: int, bar: User_Input, Wb: Window_Buttons,
                 Cg: CG, copy_button: Button, reg_button: Button, clock: pygame.time.Clock, FPS: int, save_button: Button,
                 save_input_field: User_Input, save_back_button: Button, save_save_button: Button):
        """
        Parameters:
         ----------------------

         WIN: pygame.Surface
         WIDTH: int
         HEIGHT: int
         bar: Bar
         Gui: GUI
         Wb: Window_Buttons
         Cg: CG
         copy_button: Button
         clock: pygame.time.Clock
         FPS: int
         save_button: Button
         save_input_field: User_Input
         save_back_button: Button
         save_save_button: Button

        """
        self.WIN = WIN
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.bar = bar
        self.Wb = Wb
        self.Cg = Cg
        self.copy_button = copy_button
        self.reg_button = reg_button
        self.save_button = save_button
        self.buttons = [copy_button, reg_button, save_button]
        self.clock = clock
        self.FPS = FPS
        self.save_input_field = save_input_field
        self.save_back_button = save_back_button
        self.save_save_button = save_save_button
        self.key_num = {
            "normal": {0: 48, 1: 49, 2: 50, 3: 51, 4: 52, 5: 53, 6: 54, 7: 55, 8: 56, 9: 57},
            "num_pad": {0: 1073741922, 1: 1073741913, 2: 1073741914, 3: 1073741915, 4: 1073741916,
                        5: 1073741917, 6: 1073741918, 7: 1073741919, 8: 1073741920, 9: 1073741921}
        }

        self.dark_mode = Dark_Mode(self.WIN, [pygame.image.load("assets/dark-32.png"), pygame.image.load("assets/bright-32.png")],
                                   [(255, 255, 255), (30, 30, 30)], self.WIDTH - (32 + 5), 5)

        self.Wb.setup_setting_buttons()

    def copy(self, copy):
        """
        copies a give thing into the clipboard
        :return: None
        """
        pc.copy(copy)

    def draw(self, save=False):
        """
        draws everything that it can
        :param save: bool
        :return: None
        """
        if not save:
            # self.Cg is just the logic for the code generator and not the actual GUI that is used
            self.dark_mode.draw()
            self.Wb.draw()
            for button in self.buttons:
                button.draw()
            self.bar.draw()
            pygame.display.update()
        else:
            self.dark_mode.draw()
            self.save_input_field.draw()
            self.save_back_button.draw()
            self.save_save_button.draw()
            pygame.display.update()

    def over(self, save=False):
        """
        checks if the mouse is over the copy or the generate button
        :param save: bool
        :return: None
        """
        if not save:
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
        else:
            # save back button
            if self.save_back_button.is_over(pygame.mouse.get_pos()):
                self.save_back_button.color = (255, 50, 39)
            else:
                self.save_back_button.color = (255, 0, 0)

            # the save save button
            if self.save_save_button.is_over(pygame.mouse.get_pos()):
                self.save_save_button.color = (80, 255, 30)
            else:
                self.save_save_button.color = (0, 255, 0)

    def event_handler(self, save=False):
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
                # check if the user clicked the screen
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.click_event_handler(event)
                # checks if the user pressed any buttons
                if event.type == pygame.KEYDOWN:
                    self.keyboard_events_handler(event)

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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.save_back_button.is_over(pygame.mouse.get_pos()):
                        self.run()
                    self.click_event_handler(event, save=True)

    def click_event_handler(self, event, save=False):
        """
        click related events
        :param event: pygame.Event
        :param save: bool
        :return: None
        """
        if not save:
            self.Wb.clicked(pygame.mouse.get_pos())
            if self.copy_button.is_over(pygame.mouse.get_pos()):
                self.copy(self.Cg.password)
            if self.reg_button.is_over(pygame.mouse.get_pos()):
                self.Cg.get_code()
            if self.save_button.is_over(pygame.mouse.get_pos()) and self.Cg.password != "":
                self.save()
        else:
            # it checks if the user pressed the save button in the save menu
            if self.save_save_button.is_over(pygame.mouse.get_pos()):
                if not self.save_input_field.text == "" or " " or self.Cg.password == "":
                    with open(f"./assets/codes.json", "r") as f:
                        data = json.loads(f.read())
                    with open(f"./assets/codes.json", "w") as f:
                        data[self.save_input_field.text] = self.Cg.password
                        f.truncate(0)
                        json.dump(data, f, indent=4)

        # universal events
        self.dark_mode.event_handler(event)

    def keyboard_events_handler(self, event, save=False):
        """
        click related events
        :param event: pygame.Event
        :param save: bool
        :return: None
        """
        if not save:
            self.bar.event_handler(event)
        else:
            pass

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

        # hooks the sel.Wb.loc<1-4>pressed to self.Cg.char_<up|down|num|spec>
        try:
            self.Cg.char_up = self.Wb.loc1_pressed
            self.Cg.char_down = self.Wb.loc2_pressed
            self.Cg.char_num = self.Wb.loc3_pressed
            self.Cg.char_spec = self.Wb.loc4_pressed
        except Exception as e:  # catch any unexpected exceptions
            print(f"""[EXCEPTION] {e} | type: {type(e)}""")

    def save(self):
        """
        saves the code that is currently generated
        :return: None
        """
        pygame.display.set_caption("Password Manager (save password)")
        while True:
            self.over(save=True)
            self.event_handler(save=True)
            self.draw(save=True)

    def run(self):
        """
        the main method to run the game
        :return:
        """
        pygame.display.set_caption("Password Manager (create password)")
        while True:
            self.clock.tick(self.FPS)
            self.hook()
            self.event_handler()
            self.over()
            self.draw()


if __name__ == '__main__':
    print("this is a class designed to be run from another file.")
    pygame.quit()
    quit()
