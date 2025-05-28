import pygame
from PIL import Image

class HandAnimator:
    def __init__(self, sprite_path, screen_size, base_size=(1280, 720), scale=1.0):
        """
        sprite_path: caminho da sprite (imagem horizontal com todos os frames lado a lado)
        screen_size: tupla (largura_tela, altura_tela)
        base_size: tamanho base para cálculo de escala (default 1280x720)
        scale: escala adicional (float), default 1.0
        """
        self.screen_width, self.screen_height = screen_size
        self.base_width, self.base_height = base_size
        self.scale = scale

        # Detecta tamanho do frame e total de frames automaticamente
        self.frame_width, self.frame_height, self.total_frames = self.detect_frame_size(sprite_path)

        # Carrega a sprite sheet completa com pygame
        self.sprite_sheet = pygame.image.load(sprite_path).convert_alpha()

        # Extrai cada frame da sprite sheet para uma lista
        self.frames = []
        for i in range(self.total_frames):
            frame = self.sprite_sheet.subsurface(
                pygame.Rect(i * self.frame_width, 0, self.frame_width, self.frame_height)
            )
            self.frames.append(frame)

        # Estado inicial da animação
        self.state = "rock"  # padrão inicial
        self.frame_index = 0
        self.animation_cycles = 3  # quantas vezes sobe e desce a mão
        self.current_cycle = 0
        self.animating = False

        # Divide a sprite em 3 partes iguais para rock, paper e scissor
        third = self.total_frames // 3
        self.state_map = {
            "rock": (0, third),
            "paper": (third, 2 * third),
            "scissor": (2 * third, self.total_frames),
        }
        self.current_range = self.state_map[self.state]

        # Calcula o fator de escala com base no tamanho da tela e escala extra
        self.scale_factor = min(self.screen_width / self.base_width, self.screen_height / self.base_height) * self.scale

        # Redimensiona todos os frames já na escala correta
        self.scaled_frames = [pygame.transform.scale(frame, (int(self.frame_width * self.scale_factor), int(self.frame_height * self.scale_factor))) for frame in self.frames]

        # Posição padrão: centralizado na tela
        self.x = (self.screen_width - self.frame_width * self.scale_factor) // 2
        self.y = (self.screen_height - self.frame_height * self.scale_factor) // 2

    def detect_frame_size(self, sprite_path):
        """
        Detecta automaticamente o tamanho do frame e o número total de frames da sprite horizontal.
        Tenta dividir a largura da imagem por 3 (rock, paper, scissor).
        Se não for divisível por 3, tenta dividir por altura assumindo frames quadrados.
        """
        img = Image.open(sprite_path).convert("RGBA")
        width, height = img.size

        # Se a largura for divisível por 3, assume divisão em 3 estados
        if width % 3 == 0:
            frame_width = width // 3
            frame_height = height
            total_frames = 3

            # Se a sprite tiver mais frames, tenta detectar máximo divisor (frames quadrados)
            max_frames = width // height
            if max_frames > 3:
                total_frames = max_frames
                frame_width = height
            return frame_width, frame_height, total_frames
        else:
            # Caso contrário, divide pela altura assumindo frames quadrados
            max_frames = width // height
            frame_width = width // max_frames
            frame_height = height
            total_frames = max_frames
            return frame_width, frame_height, total_frames

    def play(self, state):
        """
        Inicia a animação para o estado passado: "rock", "paper" ou "scissor".
        """
        if state not in self.state_map:
            raise ValueError(f"Estado inválido: {state}")
        self.state = state
        self.current_range = self.state_map[state]
        self.frame_index = self.current_range[0]
        self.current_cycle = 0
        self.animation_cycles = 3
        self.animating = True

    def update(self):
        """
        Atualiza o frame da animação. Deve ser chamado no loop principal.
        """
        if not self.animating:
            return

        animation_speed = 5  # controla a velocidade da animação

        # Só atualiza frame a cada "animation_speed" ticks
        self.current_cycle += 1
        if self.current_cycle % animation_speed == 0:
            self.frame_index += 1

            # Se passou do último frame do estado, volta para o primeiro frame e conta o ciclo
            if self.frame_index >= self.current_range[1]:
                self.frame_index = self.current_range[0]
                self.animation_cycles -= 1

                # Se terminou os ciclos, para a animação no último frame
                if self.animation_cycles <= 0:
                    self.animating = False
                    self.frame_index = self.current_range[1] - 1

    def draw(self, surface, x=None, y=None):
        """
        Desenha o frame atual na tela.
        Pode passar x, y para mudar a posição, senão usa posição padrão.
        """
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

        frame = self.scaled_frames[self.frame_index]
        surface.blit(frame, (self.x, self.y))
