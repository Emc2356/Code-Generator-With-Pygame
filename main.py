from Parts.Code_Generator import Code_Generator
from Parts.GUI import GUI
import pygame

pygame.init()

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


while True:
    GUI.draw()
    if GUI.escape():
        pygame.quit()
        quit(-1)
    


# cg = Code_Generator()
# cg.get_amount()
# cg.ask_types()
# cg.get_code()
