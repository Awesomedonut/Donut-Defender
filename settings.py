class Settings:

    def __init__(self, bg_colour):

        self.ORIGIN = 0
        self.DIRECTION_RIGHT = 1
        self.DIRECTION_LEFT = -1

        self.screen_width = 900
        self.screen_height = 500
        self.bg_colour = bg_colour
        self.sprinkle_speed = 1
        self.sprinkle_size = 5
        self.sprinkle_colour = (255, 0, 0)
        self.bread_width = 50
        self.bread_height = 60

        self.donut_width = 55
        self.donut_height = 40

        self.donut_lives = 5

        self.bread_speed = 7
        self.breads_drop_speed = 10

        self.button_width = 100
        self.button_height = 50
        self.button_colour = (255, 255, 0)
        self.button_text_colour = (0, 0, 0)
        
        