from prop import Prop
import pygame

class Character(Prop):

    def __init__(self, game, image_path, size):
        
        super().__init__(game)
        
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()