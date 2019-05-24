# Hayden Whitney
# 5/19
# Minecraft Defenders v1.0.0

from superwires import games

games.init(screen_width=640, screen_height=480, fps=60)


class Steve(games.Sprite):
    steve_img = games.load_image("Images/steve.png", transparent=True)

    def __init__(self):
        super(Steve, self).__init__(image=Steve.steve_img, x=games.screen.width/2, y=games.screen.height/2)

    def update(self):
        if games.keyboard.is_pressed(games.K_UP) or games.keyboard.is_pressed(games.K_w):
            self.y -= 2.5
        # if games.keyboard.is_pressed(games.K_DOWN) or games.keyboard.is_pressed(games.K_s):
            # self.y += 2.5
        if games.keyboard.is_pressed(games.K_LEFT) or games.keyboard.is_pressed(games.K_a):
            self.angle -= 3
        if games.keyboard.is_pressed(games.K_RIGHT) or games.keyboard.is_pressed(games.K_d):
            self.angle += 3

        if games.keyboard.is_pressed(games.K_1):
            self.angle = 0
        if games.keyboard.is_pressed(games.K_2):
            self.angle = 90
        if games.keyboard.is_pressed(games.K_3):
            self.angle = 180
        if games.keyboard.is_pressed(games.K_4):
            self.angle = 270


def main():
    background_img = games.load_image("Images/stars.png", transparent=False)
    explosion_files = ["Images/explosion(1).png",
                       "Images/explosion(2).png",
                       "Images/explosion(3).png",
                       "Images/explosion(4).png",
                       "Images/explosion(5).png"]
    steve_img = Steve()
    explosion = games.Animation(images=explosion_files,
                                x=games.screen.width/2,
                                y=games.screen.height/2,
                                n_repeats=1,
                                repeat_interval=3)
    games.screen.add(steve_img)
    games.screen.add(explosion)
    games.screen.background = background_img
    games.screen.mainloop()


main()
