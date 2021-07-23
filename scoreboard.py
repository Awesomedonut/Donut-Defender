import pygame.font
class Scoreboard:

    def __init__(self, d_game):
        self.screen = d_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = d_game.settings
        self.stats = d_game.stats

        self.prep_score()

    #def prep_score(self):
    
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        