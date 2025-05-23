import pygame
from button import Button


class Store_Game:
    def __init__(self, screen):
        self.screen = screen
    
    def run(self):
        storeLoop = True
        next_screen = None

        while storeLoop:
            self.screen.fill([255, 255, 255])
            pygame.display.set_caption("Jogo Bilhão (Store)")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    storeLoop = False
                    next_screen = None

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        storeLoop = False
                        next_screen = "menu"  # ESC para voltar ao menu

            pygame.display.update()

        return next_screen
