import pygame
from mainImages import MainControlImages
from button import Button
from title import Title

class MainMenuProgram:
    def __init__(self, screen):
        self.screen = screen
        self.fullscreen = False
        self.image_data = MainControlImages.start_button_data
        self.create_buttons()

    def create_buttons(self):
        width, height = self.screen.get_size()
        base_width = 1280
        base_height = 720
        scale_x = width / base_width
        scale_y = height / base_height
        scale_factor = min(scale_x, scale_y) * 8

        self.start_button = Button(
            self.image_data["image"],
            x=width / 2,
            y=height - (height / 5),
            full_width=self.image_data["width"],
            height=self.image_data["height"],
            scale_factor=scale_factor
        )

    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        if self.fullscreen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
        self.create_buttons()

    def run(self):
        running = True
        next_screen = None

        title = Title("Title Base", "Arial", 60, (0,0,0)) #Title Game

        while running:
            self.screen.fill((255, 255, 255))
            pygame.display.set_caption("Title Base (MAIN MENU)")

            title.draw(self.screen, y=100)  # Draw center title

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    next_screen = None  # Encerra o jogo

                elif event.type == pygame.VIDEORESIZE and not self.fullscreen:
                    width, height = event.size
                    self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                    self.create_buttons()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        self.toggle_fullscreen()

            # Verifica se o botão foi clicado
            if self.start_button.action:
                self.start_button.draw(self.screen)         # Mostra imagem clicada
                pygame.display.update()                    # Atualiza tela
                pygame.time.delay(150)                     # Delay de 150ms
                running = False
                next_screen = "store"                      # Troca para tela da loja

            self.start_button.draw(self.screen)
            pygame.display.flip()

        return next_screen
