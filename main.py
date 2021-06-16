from Classes import Code_Generator as CG
from Classes import Window_Buttons
from Classes import User_Input
from Classes import Dark_Mode
from Classes import Button
from Classes import Game
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
    "BLUE": (0, 0, 255),
    "GRAY-BLACK": (30, 30, 30)
}

# setup the classes instances
Cg = CG()
COPY_BUTTON = Button(x=round(WIDTH/2 - 250/2), y=HEIGHT - 70, width=250, height=50, WIN=WIN,
                     text="click to copy", text_color=COLORS["BLACK"], color=COLORS["BLUE"])
REG_BUTTON = Button(x=round(WIDTH/2 - 340/2), y=HEIGHT - 115, width=340, height=40, WIN=WIN,
                    text="click to regenerate the password", text_color=COLORS["BLACK"], color=COLORS["RED"], font_size=30)
save_button = Button(x=12, y=HEIGHT - 70, width=100, height=50,
                     WIN=WIN, text="save", text_color=COLORS["BLACK"], color=COLORS["GREEN"], font_size=60)
save_save_button = Button(x=10, y=385, width=100, height=50, WIN=WIN,
                          text_color=COLORS["BLACK"], color=COLORS["GREEN"], text="save", font_size=60)
WD = Window_Buttons(WIDTH, HEIGHT, WIN)
bar = User_Input(WIDTH, HEIGHT, round(WIDTH/2 - 150/2), 20, 150, 50, COLORS["BLACK"], WIN, COLORS["WHITE"], 50)
save_input_field = User_Input(WIDTH, HEIGHT, 10, 50, WIDTH - 20, 50, (0, 0, 0), WIN, (255, 255, 255), 60)
save_back_button = Button(COLORS["RED"], 10, 440, 100, 50, WIN, COLORS["BLACK"], "Go back", font_size=35)
dark_mode = Dark_Mode(WIN, [pygame.image.load("assets/mode-assets/dark-32.png"), pygame.image.load(
    "assets/mode-assets/bright-32.png")],
                      [(255, 255, 255), (30, 30, 30)], WIDTH - (32 + 5), 5)
clock = pygame.time.Clock()
FPS = 60


game = Game(WIN=WIN, WIDTH=WIDTH, HEIGHT=HEIGHT, bar=bar, Wb=WD, Cg=Cg, copy_button=COPY_BUTTON, reg_button=REG_BUTTON,
            clock=clock, FPS=FPS, save_button=save_button, save_input_field=save_input_field,
            save_back_button=save_back_button, save_save_button=save_save_button, dark_mode=dark_mode)
game.run()
