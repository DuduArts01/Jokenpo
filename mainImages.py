import os
import pygame

class MainControlImages:
    @classmethod
    def load(cls):
        # main directory
        main = os.path.dirname(__file__)
        
        #sprites
            #directory button
        button = os.path.join(main, "data/sprite/button")

            #directory hand
        hands = os.path.join(main, "data/sprite/player")
        
        #images
            #directory images
        images = os.path.join(main, "data/images")


        #Sprite in directory button
        sprite_start = os.path.join(button, "start/start.png")
        sprite_1vComputer = os.path.join(button, "1vComputer/1vComputer.png")
        sprite_1v1 = os.path.join(button, "1v1/1v1.png")

        #Player Button
        sprite_player_rock = os.path.join(button, "hands/rock.png")
        sprite_player_paper = os.path.join(button, "hands/paper.png")
        sprite_player_scissor = os.path.join(button, "hands/scissors.png")

        #Players Hands
        sprite_hand_player1 = os.path.join(hands, "player.png")

        #load sprites
        cls.start_image = pygame.image.load(sprite_start).convert_alpha()
        cls.sprite_1vComputer_image = pygame.image.load(sprite_1vComputer).convert_alpha()
        cls.sprite_1v1_image = pygame.image.load(sprite_1v1).convert_alpha()

            #Player Button
        cls.sprite_player_rock_image = pygame.image.load(sprite_player_rock).convert_alpha()
        cls.sprite_player_paper_image = pygame.image.load(sprite_player_paper).convert_alpha()
        cls.sprite_player_scissor_image = pygame.image.load(sprite_player_scissor).convert_alpha()
        
        # hands load
        cls.sprite_player_hand_image = pygame.image.load(sprite_hand_player1).convert_alpha()
        cls.sprite_player_hand_path = sprite_hand_player1

        #Images 
        score_board = os.path.join(images, "scoreboard/scoreboard.png")

        #load images
        cls.score_board_image = pygame.image.load(score_board).convert_alpha()
        
        width, height = cls.start_image.get_size()
        cls.start_image_data = {
            "image": cls.start_image,
            "x": 0, #position x
            "y": 0, #position y
            "width": width, #width
            "height": height, #height
            "resize_x": width * 2, #resize x
            "resize_y": height * 2, #resize y
        } #sprite button start

        cls.sprite_1vComputer_image_data = {
            "image": cls.sprite_1vComputer_image,
            "x": 0,
            "y": 0,
            "width": width,
            "height": height,
            "resize_x": width * 2,
            "resize_y": height * 2,
        } #sprite 1vC

        cls.sprite_1v1_image_data = {
            "image": cls.sprite_1v1_image,
            "x": 0,
            "y": 0,
            "width": width,
            "height": height,
            "resize_x": width * 2,
            "resize_y": height * 2,
        } #sprite 1v1

        cls.sprite_player_rock_image_data = {
            "image": cls.sprite_player_rock_image,
            "x": 0,
            "y": 0,
            "width": width,
            "height": height,
            "resize_x": width * 2,
            "resize_y": height * 2,
        } #sprite hand rock

        cls.sprite_player_paper_image_data = {
            "image": cls.sprite_player_paper_image,
            "x": 0,
            "y": 0,
            "width": width,
            "height": height,
            "resize_x": width * 2,
            "resize_y": height * 2,
        } #sprite hand paper

        cls.sprite_player_scissor_image_data = {
            "image": cls.sprite_player_scissor_image,
            "x": 0,
            "y": 0,
            "width": width,
            "height": height,
            "resize_x": width * 2,
            "resize_y": height * 2,
        } #sprite hand scissor

        #images
        cls.scoreboard_image_data = {
            "image": cls.score_board_image,
            "x": 0,
            "y": 0,
            "width": width,
            "height": height,
            "resize_x": width * 2,
            "resize_y": height * 2,
        } #image scoreboard

        cls.sprite_player_hand_image_data = {
            "image": cls.sprite_player_hand_image,
            "x": 0,
            "y": 0,
            "width": width,
            "height": height,
            "resize_x": width * 2,
            "resize_y": height * 2,
        } #sprite hand player