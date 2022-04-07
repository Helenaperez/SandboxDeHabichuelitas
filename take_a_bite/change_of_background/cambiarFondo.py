import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class Ball:
    def __init__(self, position_x, position_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)




class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)


        # Make the mouse disappear when it is over the window.

        # So we just see our object, not the pointer.

        self.set_mouse_visible(True)


        arcade.set_background_color(arcade.color.ASH_GREY)
        arcade.draw_lrtb_rectangle_filled(0, 10, 250, 230, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(SCREEN_WIDTH - 10, SCREEN_WIDTH, 250, 230, arcade.color.BLACK)

        # Create our ball
        self.ball = Ball(50, 50, 1, arcade.color.WHITE)



    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()
        arcade.draw_lrtb_rectangle_filled(0, 10, 250, 230, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_filled(SCREEN_WIDTH - 10, SCREEN_WIDTH, 250, 230, arcade.color.BLACK)


    def on_mouse_motion(self, x, y, dx, dy):

        """ Called to update our objects.

        Happens approximately 60 times per second."""

        self.ball.position_x = x

        self.ball.position_y = y

        if self.ball.position_x <= 10 and 230 < self.ball.position_y < 250:
            arcade.set_background_color(arcade.color.GREEN)

        if self.ball.position_x >= SCREEN_WIDTH - 10 and 230 < self.ball.position_y < 250:
            arcade.set_background_color(arcade.color.BROWN)


def main():
    window = MyGame(640, 480, "Drawing Example")

    arcade.run()


main()