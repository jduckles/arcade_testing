import arcade
import random


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'welcome to my Game'
SCALING = 1.0

class Gameenter(arcade.Window):
    def __init__(self,width, height, title):

        super().__init__(width, height, title)
        self.enemies_list = arcade.SpriteList()
        self.clouds_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()

        self.g_pressed = False

        self.setup()

    def setup(self):
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.player = arcade.Sprite('sprites/jet.png', SCALING)
        self.player.center_y = self.height / 2
        self.player.left = 10
        self.all_sprites.append(self.player)
        arcade.schedule(self.add_enemy, 0.25)

    def add_enemy(self, delta_time: float):

        enemy = arcade.Sprite('sprites/missile.png', SCALING)
        enemy.left = random.randint(self.width, self.width + 80)
        enemy.top = random.randint(10, self.height - 10)

    def on_draw(self):
        arcade.start_render()
        self.all_sprites.draw()

    def on_update(self, delta_time):
        if self.g_pressed:
            self.player.center_x = 500

    def on_key_press(self, key: int, modifiers: int):

        if arcade.key.G == key:
            self.g_pressed = True


if __name__ == "__main__":# there is a error whith this line Try now some thing with indentation nope its the class definition above
    app = Gameenter(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title = SCREEN_TITLE) # <- this is where it is instantiated
    arcade.run() # I think you need to call the run method on app? ok Checking....
