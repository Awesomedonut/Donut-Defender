import pygame
pygame.font.init()

class Prop:

    def __init__(self, game):
        
        self.screen = game.screen
        self.settings = game.settings

    def draw(self):
        pygame.draw.rect(self.screen, self.colour, self.rect)