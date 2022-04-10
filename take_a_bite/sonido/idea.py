import arcade


class BeanAHero(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height, "Sound")


        self.door_open = arcade.load_sound("qubodup-DoorOpen07.flac")
        self.door_closed = arcade.load_sound("qubodup-DoorClose07.flac")
        self.eats_habichuela = arcade.load_sound("habichuelas.mp3")
        self.start_playing = arcade.load_sound("heroic-story-drums-ampamp-bass-9827.mp3")
        self.battle = arcade.load_sound("misc129.mp3")


    def on_key_press(self, key, modifiers):

        if key == arcade.key.D:
            arcade.play_sound(self.door_open)
        if key == arcade.key.A:
            arcade.play_sound(self.door_closed)
        if key == arcade.key.R:
            arcade.play_sound(self.eats_habichuela)
        if key == arcade.key.ENTER:
            arcade.play_sound(self.start_playing)
        if key == arcade.key.E:
            arcade.play_sound(self.battle)



def main():
    window = BeanAHero(500, 500)
    arcade.run()


main()
