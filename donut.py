import pygame
from sprinkle import Sprinkle
from character import Character

class Donut(Character):

    def __init__(self, game):

        super().__init__(game, "Assets/donut_pic_2.jpg", (game.settings.donut_width, game.settings.donut_height))

        self.rect.x = 0
        self.rect.y = 0

        self.lives = game.settings.donut_lives

        self.sprinkles = []
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        #self.react.mid_bottom = self.screen_rect.mid_bottom

    def move(self):
        """Movement of Donut and its sprinkles"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
        if self.moving_up:
            self.rect.y -= 1
        if self.moving_down:
            self.rect.y += 1

        for sprinkle in self.sprinkles:
            sprinkle.move()

       # collsions = pygame.sprite.groupcollide(self.sprinkles, self.ai_game.breads, True, True)

    def blitme(self):
        
        self.screen.blit(self.image, self.rect)

        for sprinkle in self.sprinkles:
            pygame.draw.rect(self.screen, sprinkle.colour, sprinkle.rect)
        
        self.delete_old_sprinkles()

    def fire_sprinkle(self):
        new_sprinkle = Sprinkle(self, self.game)
        self.sprinkles.append(new_sprinkle)

        # if not self.breads:
        #     self.sprinkles.empty()
        #     self._create_breads

    def delete_old_sprinkles(self):
        #.copy()
        for sprinkle in self.sprinkles:
            if sprinkle.rect.bottom < 0:
                self.sprinkles.remove(sprinkle)
           # print(len(self.sprinkles))

    #     self.lives_text = self.LIVES_FONT.render("Lives = " + str(self.lives), 1, (0, 255, 0))
    #     self.screen.blit(self.lives_text, (self.lives_text.get_width(), 10))