import pygame
import sys
from time import sleep
pygame.font.init()

from settings import Settings
from donut import Donut
from bread import Bread
from game_stats import GameStats
from play_button import PlayButton
from text_image import TextImage
from font_style import FontStyle

class Defenders:

    def __init__(self):
        pygame.init()
        self.settings = Settings((0, 0, 0))
        # self.dead_font = pygame.font.SysFont("comicsans", 50)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.paused = True
        self.game_over = False
       # self.screen = pygame.display.set_mode((900, 500))
        pygame.display.set_caption("Donut Defenders")

        self.donut = Donut(self)
        self.button = PlayButton(self)
        self.breads = []

        self.bg_colour = (0, 0, 0)

        self._create_breads()

        # self.stats = GameStats(self)

        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.button.draw()
        pygame.display.flip()
        # self.bread = pygame.sprite.Group()


    def run_game(self):
        lives_style = FontStyle((255, 0, 0), 50)
        while True:
            self.clock.tick(self.FPS)
            self._check_events()
            
            
            if self.paused == False and self.game_over == False:
                self.donut.move()

                self._update_screen()
                self._handle_bread_sprinkle_collision()
                self._handle_bread_donut_collision()
                
                lives_text = TextImage(self, f"Lives {self.donut.lives}", lives_style, (100, 50))
                lives_text.draw()


    def _check_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.paused = not self.paused

                elif self.paused == False:
                    if event.key == pygame.K_RIGHT:
                        self.donut.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.donut.moving_left = True
                    elif event.key == pygame.K_UP:
                        self.donut.moving_up = True
                    elif event.key == pygame.K_DOWN:
                        self.donut.moving_down = True
                    elif event.key == pygame.K_SPACE:
                        self.donut.fire_sprinkle()
                
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.donut.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.donut.moving_left = False
                elif event.key == pygame.K_UP:
                    self.donut.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.donut.moving_down = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_colour)
        self.donut.blitme()
        
        for bread in self.breads:
            bread.move()
            self.screen.blit(bread.image, bread.rect)

         
                #self.screen.fill(self.bg_colour)

                #pygame.display.update()
        pygame.display.flip()

    def _create_breads(self):
        # bread = Bread(self)
        # self.breads.append(bread)
        bread_width = self.settings.bread_width
        bread_height = self.settings.bread_height

        available_space_x = self.settings.screen_width - ( 2 * bread_width)
        number_breads_x = available_space_x // (2 * bread_width)
        available_space_y = self.settings.screen_height - (3 * bread_height)
        number_breads_y = available_space_y // bread_height #rows

        for bread_columns in range(number_breads_x):
    
            for bread_rows in range(number_breads_y):
                bread = Bread(self)
                bread.rect.x = bread_width + 2 * bread_width * bread_columns
                bread.rect.y = bread.rect.height + 2 * bread.rect.height * bread_rows
                
                self.breads.append(bread)
                #self.screen.blit(bread.image, bread.rect)
 
        #self.breads.empty()
        #self.sprinkles.empty() #move to donut?

    def _check_breads_bottom(self):
        screen_rect = self.screen.get_rect()
        for bread in self.breads:
            if bread.rect.bottom >= screen_rect.bottom:
                if self.donut.lives > 0:
                    self.donut.lives -= 1
                else:
                    print("OH NO UR DEAD")
                    self.game_over = True

    def check_collision(self, target, attacker):

        return target.rect.x < attacker.rect.x and attacker.rect.x < target.rect.x + target.rect.width and target.rect.y < attacker.rect.y and attacker.rect.y < target.rect.y + target.rect.height
        
        # print(return_value)
        # print(sprinkle.rect.x)
        # print(bread.rect.x)
        # print(sprinkle.rect.y)
        # print(bread.rect.y)
        # return return_value


    def _handle_bread_sprinkle_collision(self):
     
        for sprinkle in self.donut.sprinkles:
            for bread in self.breads:
                if self.check_collision(bread, sprinkle):
                    self.breads.remove(bread)

    def _handle_bread_donut_collision(self):
     
        for bread in self.breads:
            if self.check_collision(self.donut, bread):
                print("OH NO uve been hit!")
                print(self.donut.rect)
                print(bread.rect)
                if self.donut.lives > 0:
                    self.donut.lives -= 1
                else:
                    print("OH NO UR DEAD")
                    self.dead_text = "OH NO UR DEAD"
                    self.game_over = True
                    self.dead_text_pic = self.dead_font.render(self.dead_text, True, (255, 255, 255), (255, 0, 0))
                    self.screen.blit(self.dead_text_pic, (self.settings.screen_width//2,self.settings.bread_height//2))
                    pygame.display.flip()

        #self.screen.blit(self.msg_image, self.msg_image_rect)

#def main()

if __name__ == "__main__":

    defr = Defenders()
    defr.run_game()