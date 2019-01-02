# https://arcade-book.readthedocs.io/en/latest/labs/lab_02_drawing/drawing.html?highlight=draw_lines
# http://arcade.academy/arcade.html#arcade.draw_commands.draw_line

import arcade
  
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

BLOCK_WIDTH = 50
BLOCK_HEIGHT = 50

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        # Set up your game here
        pass

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()

        y = 0
        # Your drawing code goes here
        for x in range(0, 1): # int(SCREEN_WIDTH/BLOCK_WIDTH)):
            arcade.draw_rectangle_outline(
                x*BLOCK_WIDTH,
                y*BLOCK_HEIGHT,
                BLOCK_WIDTH,
                BLOCK_HEIGHT,
                arcade.color.BONE,
                5
            )

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        pass


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
