import pygame
import sys
from menu_main import MainMenuProgram
from mainImages import MainControlImages
from store import Store_Game

pygame.init()
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
MainControlImages.load()

# Roda enquanto houver telas para mostrar
current_screen = "menu"

while current_screen:
    if current_screen == "menu":
        main_menu = MainMenuProgram(screen)
        current_screen = main_menu.run()

    elif current_screen == "store":
        store = Store_Game(screen)
        current_screen = store.run()

pygame.quit()
sys.exit()
