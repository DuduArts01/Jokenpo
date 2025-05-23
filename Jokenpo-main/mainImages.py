import os
import pygame

class MainControlImages:
    @classmethod
    def load(cls):
        base = os.path.dirname(__file__)
        path = os.path.join(base, "data/sprite/button/start/start.png")
        cls.start_image = pygame.image.load(path).convert_alpha()
        width, height = cls.start_image.get_size()
        cls.start_button_data = {
            "image": cls.start_image,
            "x": 0,
            "y": 0,
            "width": width,
            "height": height,
            "resize_x": width * 2,
            "resize_y": height * 2,
        }
