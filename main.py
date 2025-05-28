import pygame
import sys
from menu_main import MainMenuProgram
from mainImages import MainControlImages
from gameselect import Select_Mode
from one_vs_computer import OneVsComputer

pygame.init()
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
MainControlImages.load()

# Roda enquanto houver telas para mostrar
current_screen = "menu"

while current_screen:
    if current_screen == "menu": # Screen Menu
        main_menu = MainMenuProgram(screen)
        current_screen = main_menu.run()

    elif current_screen == "gameselect": # Screen select mode game
        selectmodegame = Select_Mode(screen)
        current_screen = selectmodegame.run()
    
    elif current_screen == "playerVScomputer": # Screen Player vs Computer
        oneVsComputer = OneVsComputer(screen)
        current_screen = oneVsComputer.run()

pygame.quit()
sys.exit()
