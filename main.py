from Classes.Code_Generator import Code_Generator as CG
from Classes.Window_Buttons import Window_Buttons
from Classes.Button import Button
from Classes.Game import Game
from Classes.GUI import GUI
from Classes.User_Input import User_Input
import pyperclip as pc
import pygame


# initialize pygame info
pygame.init()
pygame.font.init()

# setup the main window
WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# setup a small color palette
COLORS = {
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255)
}

# setup the classes instances
GUI = GUI(WIDTH=HEIGHT, HEIGHT=HEIGHT, BASE_COLOR=COLORS["WHITE"], WIN=WIN)
Cg = CG()
COPY_BUTTON = Button(x=WIDTH/2 - 250/2, y=HEIGHT - 70, WIDTH=250, HEIGHT=50, WIN=WIN, text="click to copy", text_color=COLORS["BLACK"], color=COLORS["BLUE"])
REG_BUTTON = Button(x=WIDTH/2 - 340/2, y=HEIGHT - 115, WIDTH=340, HEIGHT=40, WIN=WIN, text="click to regenerate the password",
                    text_color=COLORS["GREEN"], color=COLORS["RED"], font_size=30)
WD = Window_Buttons(WIDTH, HEIGHT, WIN)
bar = User_Input(WIDTH, HEIGHT, round(WIDTH/2 - 150/2), 20, 150, 50, COLORS["BLACK"], WIN, COLORS["WHITE"], 50)
clock = pygame.time.Clock()
FPS = 60


game = Game(WIN=WIN, WIDTH=WIDTH, HEIGHT=HEIGHT, bar=bar, Gui=GUI, Win_Buttons=WD, Cg=Cg,
            copy_button=COPY_BUTTON, reg_button=REG_BUTTON, clock=clock, FPS=FPS)
game.run()


# Cg.get_amount()
# Cg.ask_types()
# Cg.get_code()
