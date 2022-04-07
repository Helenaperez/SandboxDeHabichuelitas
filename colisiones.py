import arcade

SCREEN_WIDTH = 1537.5
SCREEN_HEIGHT = 863.5
MOVEMENT_SPEED = 5


class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Instancio las propiedades de la clase
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Dibujo la pelota con las propiedades """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        # Muevo la pelota
        self.position_y += self.change_y
        self.position_x += self.change_x

        # Compruebo si llega al final de la pantalla
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Llamada a la funcion inicial de la clase padre
        super().__init__(width, height, title, True)

        # Hago desaparecer el raton
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BRONZE_YELLOW)

        # Creo la pelota
        self.ball = Ball(50, 50, 0, 0, 25, arcade.color.GREEN)

    def on_draw(self):
        """ Llamada cuando necesito dibujar la ventana """
        arcade.start_render()
        self.ball.draw()

        # Obtenemos las dimensiones
        left, screen_width, bottom, screen_height = self.get_viewport()

        text_size = 18
        # Escribo el texto en la pantalla
        arcade.draw_text("Presiona F para minimizar la ventana",
                         screen_width // 2, screen_height // 2 - 20,
                         arcade.color.WHITE, text_size, anchor_x="center")
        arcade.draw_text("Presiona G para minimizar la ventana (estirada/stretched)",
                         screen_width // 2, screen_height // 2 + 20,
                         arcade.color.WHITE, text_size, anchor_x="center")

    def update(self, delta_time):
        self.ball.update()

    def on_key_press(self, key, modifiers):
        """ Llamada cuando se pulsa una tecla """
        if key == arcade.key.A:
            self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.ball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.W:
            self.ball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.ball.change_y = -MOVEMENT_SPEED
        if key == arcade.key.F:    # Cuando se pulsa F se cambia entre pantalla completa y minimizada
            self.set_fullscreen(not self.fullscreen)

            # Obtengo las coordenadas de la ventana.
            width, height = self.get_size()
            self.set_viewport(0, width, 0, height)

        if key == arcade.key.G:   # Cuando se pulsa G se cambia entre pantalla completa y minimizada (stretched)
            self.set_fullscreen(not self.fullscreen)

            self.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)

    def on_key_release(self, key, modifiers):
        """ Llamada cuando se deja de pulsar una tecla """
        if key == arcade.key.A or key == arcade.key.D:
            self.ball.change_x = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.ball.change_y = 0


def main():
    ventana = MyGame(640, 480, "Ejemplo")
    arcade.run()


main()
