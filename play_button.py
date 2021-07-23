from prop import Prop
import pygame
from text_image import TextImage
from font_style import FontStyle

class PlayButton(Prop):
    def __init__(self, game):

        super().__init__(game)
 
        button_style = FontStyle((255, 255, 0), 50)
        self.play_button = TextImage(game, "PRESS P TO START", button_style, (100, 20))
        #game._create_breads()

    def draw(self):

        #self.screen.fill((255, 255, 255), self.rect)
        self.play_button.draw()
        #self.screen.blit(self.msg_image, self.msg_image_rect)


# if __name__ == "__main__":
#     button = PlayButton()
#     button.draw_button()