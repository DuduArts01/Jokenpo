import pygame

class Image_edit:
    @staticmethod
    def load_and_scale_image_dynamic(image_surface, screen_size, base_size=(1280, 720), scale=1.0):
        """
        Redimensiona a imagem dinamicamente com base no tamanho atual da tela.

        Parâmetros:
            image_surface (pygame.Surface): Imagem já carregada.
            screen_size (tuple): Tamanho atual da tela (largura, altura).
            base_size (tuple): Tamanho base de referência (largura, altura).
            scale (float): Escala adicional (1.0 = normal, 1.2 = 120%, etc).

        Retorna:
            (pygame.Surface, (int, int)): Imagem redimensionada e seu novo tamanho.
        """
        screen_width, screen_height = screen_size
        base_width, base_height = base_size

        scale_x = screen_width / base_width
        scale_y = screen_height / base_height
        scale_factor = min(scale_x, scale_y) * scale

        original_width, original_height = image_surface.get_size()
        new_width = int(original_width * scale_factor)
        new_height = int(original_height * scale_factor)

        resized_image = pygame.transform.scale(image_surface, (new_width, new_height))
        return resized_image, (new_width, new_height)

    @staticmethod
    def get_position(screen_size, image_size, x=None, y=None):
        """
        Calcula a posição (x, y) da imagem na tela.

        Se `x` ou `y` não forem informados, a imagem será centralizada naquele eixo.

        Parâmetros:
            screen_size (tuple): (largura_tela, altura_tela)
            image_size (tuple): (largura_imagem, altura_imagem)
            x (int|None): Coordenada X ou None para centralizar
            y (int|None): Coordenada Y ou None para centralizar

        Retorna:
            tuple: (x, y)
        """
        screen_width, screen_height = screen_size
        image_width, image_height = image_size

        x = (screen_width - image_width) // 2 if x is None else x
        y = (screen_height - image_height) // 2 if y is None else y

        return x, y


