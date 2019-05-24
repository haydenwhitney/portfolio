# Hayden Whitney
# 5/19
# Minecraft Defenders v1.2.5

from superwires import games
import random
import math

games.init(screen_width=640, screen_height=480, fps=60)


class Asteroids(games.Sprite):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {SMALL: games.load_image("Images/asteroid(S).png"),
              MEDIUM: games.load_image("Images/asteroid(M).png"),
              LARGE: games.load_image("Images/asteroid(L).png")}
    SPEED = 2

    def __init__(self, x, y, size):
        super(Asteroids, self).__init__(image=Asteroids.images[size],
                                        x=x,
                                        y=y,
                                        dx=random.choice([1, -1])*Asteroids.SPEED*random.random()/size,
                                        dy=random.choice([1, -1]) * Asteroids.SPEED * random.random() / size,)
        self.size = size

    def update(self):
        if self.top > games.screen.height:
            self.bottom = 0
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width
        if self.bottom < 0:
            self.top = games.screen.height


class Steve(games.Sprite):
    image = games.load_image("Images/steve.png")
    sound = games.load_sound("Sounds/FX/thruster2.wav")
    ROTATION_STEP = 8
    VELOCITY_STEP = .05

    def update(self):
        if games.keyboard.is_pressed(games.K_UP) or games.keyboard.is_pressed(games.K_w):
            Steve.sound.play()
            angle = self.angle * math.pi/180
            self.dx += Steve.VELOCITY_STEP * math.sin(angle)
            self.dy += Steve.VELOCITY_STEP * -math.cos(angle)
        if games.keyboard.is_pressed(games.K_LEFT) or games.keyboard.is_pressed(games.K_a):
            self.angle -= Steve.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_RIGHT) or games.keyboard.is_pressed(games.K_d):
            self.angle += Steve.ROTATION_STEP

        if self.top > games.screen.height:
            self.bottom = 0
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width
        if self.bottom < 0:
            self.bottom = games.screen.height


class Arrow(games.Sprite):
    pass


class Explosion(games.Sprite):
    pass


def main():
    background_img = games.load_image("Images/stars.png", transparent=False)
    steve_img = Steve(image=Steve.image, x=games.screen.width / 2, y=games.screen.height / 2)

    for i in range(8):
        x = random.randrange(games.screen.width)
        y = random.randrange(games.screen.width)
        size = random.choice([Asteroids.SMALL, Asteroids.MEDIUM, Asteroids.LARGE])
        new_asteroid = Asteroids(x=x, y=y, size=size)
        games.screen.add(new_asteroid)

    games.screen.background = background_img
    games.screen.add(steve_img)

    games.screen.mainloop()

main()
