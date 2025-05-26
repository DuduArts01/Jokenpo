import pygame
from mainImages import MainControlImages
from button import Button
from title import Title

class OneVsComputer:
    def __init__(self, screen):
        self.screen = screen
        self.fullscreen = False
        self.image_hand_rock_data = MainControlImages.sprite_player_rock_image_data
        self.image_paper_data = MainControlImages.sprite_player_paper_image_data
        self.image_scissor_data = MainControlImages.sprite_player_scissor_image_data
        self.resizedElements()

    def resizedElements(self):
        width, height = self.screen.get_size()
        base_width = 1280
        base_height = 720
        scale_x = width / base_width
        scale_y = height / base_height
        scale_factor = min(scale_x, scale_y) * 1

        self.hand_rock = Button(
            self.image_hand_rock_data["image"],
            x=width / 4,
            y=height - (height / 3),
            scale_factor=scale_factor * 8.5
        ) # Button hand rock

        self.hand_paper = Button(
            self.image_paper_data["image"],
            x=width / 2,
            y=height - (height / 3),
            scale_factor=scale_factor * 8
        ) # Button hand paper

        self.hand_scissor = Button(
            self.image_scissor_data["image"],
            x=width / 1.33,
            y=height - (height / 3),
            scale_factor=scale_factor * 8.5
        ) # Button hand scissor


        self.title = Title("Player Vs Computer", "Arial", 60, (0,0,0)) #Title Game

    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        if self.fullscreen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
        self.resizedElements()

    def run(self):
        running = True
        next_screen = None

        while running:
            self.screen.fill((255, 255, 255))
            pygame.display.set_caption("Jokenpô (Player Vs Computer)")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    next_screen = None  # Encerra o jogo

                elif event.type == pygame.VIDEORESIZE and not self.fullscreen:
                    width, height = event.size
                    self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                    self.resizedElements()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        self.toggle_fullscreen()

            # Verifica se o botão foi clicado
            if self.hand_rock.action:
                self.hand_rock.draw(self.screen)         # Mostra imagem clicada
                pygame.display.update()                    # Atualiza tela
                pygame.time.delay(150)                     # Delay de 150ms
                running = False
                next_screen = "gameselect"                      # Troca para tela 1vComputer

            # Draw Title (show on screen)
            self.title.draw(self.screen, y=100)  # Draw center title

            # Draw buttons (show on screen)
            self.hand_rock.draw(self.screen) # Button one vs computer
            self.hand_paper.draw(self.screen) # Button one vs one
            self.hand_scissor.draw(self.screen) # Button one vs one
            
            pygame.display.update()

        return next_screen
