import pygame
pygame.font.init()

class TextImage:
    def __init__(self, game, msg, style, location):
        self.FONT = pygame.font.SysFont("sansserif", style.size)
        self.text_image = self.FONT.render(msg, 1, style.colour)
        self.location = location

        self.screen = game.screen

    def draw(self):
        self.screen.blit(self.text_image, self.location)
