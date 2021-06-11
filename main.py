from Parts.Code_Generator import Code_Generator as CG
from Parts.GUI import GUI
from Parts.Bar import Bar
from Parts.Window_Buttons import Window_Buttons
from Parts.Button import Button
import pygame
import pyperclip as pc


pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

COLORS = {
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255)
}

GUI = GUI(WIDTH=HEIGHT, HEIGHT=HEIGHT, BASE_COLOR=COLORS["WHITE"], WIN=WIN)
GUI.set_window(TITLE="Password Manager")
COPY_BUTTON = Button(x=WIDTH/2 - 250/2, y=HEIGHT - 70, WIDTH=250, HEIGHT=50, WIN=WIN, text="click to copy", color=COLORS["BLUE"])
WD = Window_Buttons(WIDTH, HEIGHT, WIN)
WD.setup_setting_buttons()
bar = Bar(WIDTH, HEIGHT, WIDTH/2 - 150/2, 20, 150, 50, COLORS["BLACK"], WIN, 50)
clock = pygame.time.Clock()
FPS = 60


def draw():
    GUI.draw()
    WD.draw()
    COPY_BUTTON.draw()
    bar.draw()
    pygame.display.update()


while True:
    clock.tick(FPS)
    draw()


    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
            quit(-1)
        # check if the user presses the copy_button to copy the code
        if event.type == pygame.MOUSEBUTTONDOWN:
            if COPY_BUTTON.is_over(pygame.mouse.get_pos()):
                pc.copy("copy")

# cg = CG()
# cg.get_amount()
# cg.ask_types()
# cg.get_code()
