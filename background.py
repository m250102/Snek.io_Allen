import pygame

class background:
    
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.b_image = pygame.image.load('photos/lights.jpg')
        self.image = self.b_image