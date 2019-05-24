# Hayden Whitney
# 5/19
# Minecraft Defenders v1.3.5

from superwires import games
import random
import math

games.init(screen_width=640, screen_height=480, fps=60)


class Fireball(games.Sprite):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    SPAWN = random.randrange(1, 4)
    images = {SMALL: games.load_image("Images/asteroid(S).png"),
              MEDIUM: games.load_image("Images/asteroid(M).png"),
              LARGE: games.load_image("Images/asteroid(L).png")}
    SPEED = 2

    def __init__(self, x, y, size):
        super(Fireball, self).__init__(image=Fireball.images[size],
                                       x=x,
                                       y=y,
                                       dx=random.choice([1, -1])*Fireball.SPEED*random.random()/size,
                                       dy=random.choice([1, -1]) * Fireball.SPEED * random.random() / size,)
        self.size = size

    def die(self):
        if self.size != Fireball.SMALL:
            for i in range(Fireball.SPAWN):
                new_fireball = Fireball(x=self.x, y=self.y, size=self.size-1)
                games.screen.add(new_fireball)
        self.destroy()

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
    sound = games.load_sound("Sounds/FX/thruster.wav")
    ROTATION_STEP = 8
    VELOCITY_STEP = .04
    SNOWBALL_DELAY = 30

    def __init__(self, x, y):
        super(Steve, self).__init__(image=Steve.image, x=x, y=y)
        self.snowball_wait = 0

    def die(self):
        self.destroy()

    def update(self):
        if self.snowball_wait > 0:
            self.snowball_wait -= 1

        if games.keyboard.is_pressed(games.K_UP) or games.keyboard.is_pressed(games.K_w):
            Steve.sound.play()
            angle = self.angle * math.pi/180
            self.dx += Steve.VELOCITY_STEP * math.sin(angle)
            self.dy += Steve.VELOCITY_STEP * -math.cos(angle)
        if games.keyboard.is_pressed(games.K_LEFT) or games.keyboard.is_pressed(games.K_a):
            self.angle -= Steve.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_RIGHT) or games.keyboard.is_pressed(games.K_d):
            self.angle += Steve.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_SPACE) and self.snowball_wait <= 0:
            new_snowball = Snowball(self.x, self.y, self.angle)
            games.screen.add(new_snowball)
            self.snowball_wait = Steve.SNOWBALL_DELAY

        if self.top > games.screen.height:
            self.bottom = 0
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width
        if self.bottom < 0:
            self.top = games.screen.height

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()


class Snowball(games.Sprite):
    image = games.load_image("Images/snowball.png")
    sound = games.load_sound("Sounds/FX/shoot.wav")
    BUFFER = 55
    VELOCITY_FACTOR = 10
    LIFETIME = 40

    def __init__(self, steve_x, steve_y, steve_angle):
        Snowball.sound.play()
        angle = steve_angle * math.pi / 180
        buffer_x = Snowball.BUFFER * math.sin(angle)
        buffer_y = Snowball.BUFFER * -math.cos(angle)
        x = steve_x + buffer_x
        y = steve_y + buffer_y
        dx = Snowball.VELOCITY_FACTOR * math.sin(angle)
        dy = Snowball.VELOCITY_FACTOR * -math.cos(angle)
        super(Snowball, self).__init__(image=Snowball.image,
                                       x=x, y=y,
                                       dx=dx, dy=dy)
        self.lifetime = Snowball.LIFETIME

    def die(self):
        self.destroy()

    def update(self):
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()

        if self.top > games.screen.height:
            self.bottom = 0
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width
        if self.bottom < 0:
            self.top = games.screen.height


class Explosion(games.Sprite):
    pass


def main():
    background_img = games.load_image("Images/stars.png", transparent=False)
    steve_img = Steve(x=games.screen.width / 2, y=games.screen.height / 2)

    for i in range(8):
        x = random.randrange(games.screen.width)
        y = random.randrange(games.screen.width)
        size = random.choice([Fireball.SMALL, Fireball.MEDIUM, Fireball.LARGE])
        new_asteroid = Fireball(x=x, y=y, size=size)
        games.screen.add(new_asteroid)

    games.screen.background = background_img
    games.screen.add(steve_img)

    games.screen.mainloop()

main()
