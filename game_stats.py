class GameStats:
    def __init__(self, d_game):
        self.settings = d_game.settings
        self.reset_stats()

        self.game_active = True

    def reset_stats(self):
        self.donuts_left = self.settings.donut_lives