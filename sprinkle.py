import pygame

class Sprinkle():

    def __init__(self, donut, d_game):
        super().__init__()
        self.screen = d_game.screen
        self.settings = d_game.settings
        self.colour = self.settings.sprinkle_colour

        self.rect = pygame.Rect(0, 0, self.settings.sprinkle_size, self.settings.sprinkle_size)
        self.rect.midtop = donut.rect.midtop

        #self.y = float(self.rect.y)

    def move(self):
        self.rect.y -= 5

    def draw(self):
        pygame.draw.rect(self.screen, self.colour, self.rect)
    
    #def fire(self):
