from character import Character

class Bread(Character):

    def __init__(self, game):
        
        super().__init__(game, "Assets/bread.png", (game.settings.bread_width, game.settings.bread_height))

        self.direction = game.settings.DIRECTION_RIGHT
        

    def move(self):

        self.rect.x += self.direction * self.settings.bread_speed

        if self.direction == self.settings.DIRECTION_RIGHT and self.rect.x >= self.settings.screen_width: #changing direction
            self.direction = self.settings.DIRECTION_LEFT
        elif self.direction == self.settings.DIRECTION_LEFT and self.rect.x <= self.settings.ORIGIN:
            self.direction = self.settings.DIRECTION_RIGHT         

            