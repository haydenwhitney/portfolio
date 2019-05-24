# Hayden Whitney
# 5/19
# Blockworld Defenders v1.3.5

from superwires import games, color
import random
import math

games.init(screen_width=640, screen_height=480, fps=60)


class Wrapper(games.Sprite):
    def update(self):
        if self.top > games.screen.height:
            self.bottom = 0
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width
        if self.bottom < 0:
            self.top = games.screen.height

    def die(self):
        self.destroy()


class Collider(Wrapper):
    def update(self):
        super(Collider, self).update()
        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()

    def die(self):
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()


class Fireball(Wrapper):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    SPAWN = random.randrange(1, 4)
    POINTS = 10
    images = {SMALL: games.load_image("Images/asteroid(S).png"),
              MEDIUM: games.load_image("Images/asteroid(M).png"),
              LARGE: games.load_image("Images/asteroid(L).png")}
    SPEED = 2

    total = 0

    def __init__(self, game, x, y, size):
        Fireball.total += 1
        super(Fireball, self).__init__(image=Fireball.images[size],
                                       x=x,
                                       y=y,
                                       dx=random.choice([1, -1])*Fireball.SPEED*random.random()/size,
                                       dy=random.choice([1, -1]) * Fireball.SPEED * random.random() / size,)
        self.size = size
        self.game = game

    def die(self):
        Fireball.total -= 1
        self.game.score.value += int(Fireball.POINTS*self.size)
        self.game.score.right = games.screen.width - 10
        if self.size != Fireball.SMALL:
            for i in range(Fireball.SPAWN):
                new_fireball = Fireball(game=self.game, x=self.x, y=self.y, size=self.size-1)
                games.screen.add(new_fireball)
        if Fireball.total == 0:
            self.game.advance()
        super(Fireball, self).die()


class Steve(Collider):
    image = games.load_image("Images/steve.png")
    sound = games.load_sound("Sounds/FX/thruster.wav")
    ROTATION_STEP = 5
    VELOCITY_STEP = .05
    SNOWBALL_DELAY = 30
    VELOCITY_MAX = 3

    def __init__(self, game, x, y):
        super(Steve, self).__init__(image=Steve.image, x=x, y=y)
        self.snowball_wait = 0
        self.game = game

    def update(self):
        super(Steve, self).update()
        if self.snowball_wait > 0:
            self.snowball_wait -= 1

        if games.keyboard.is_pressed(games.K_UP) or games.keyboard.is_pressed(games.K_w):
            Steve.sound.play()
            angle = self.angle * math.pi/180
            self.dx += Steve.VELOCITY_STEP * math.sin(angle)
            self.dy += Steve.VELOCITY_STEP * -math.cos(angle)
            self.dx = min(max(self.dx, -Steve.VELOCITY_MAX), Steve.VELOCITY_MAX)
            self.dy = min(max(self.dy, -Steve.VELOCITY_MAX), Steve.VELOCITY_MAX)
        if games.keyboard.is_pressed(games.K_LEFT) or games.keyboard.is_pressed(games.K_a):
            self.angle -= Steve.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_RIGHT) or games.keyboard.is_pressed(games.K_d):
            self.angle += Steve.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_SPACE) and self.snowball_wait <= 0:
            new_snowball = Snowball(self.x, self.y, self.angle)
            games.screen.add(new_snowball)
            self.snowball_wait = Steve.SNOWBALL_DELAY

    def die(self):
        self.game.end()
        super(Steve, self).die()


class Snowball(Collider):
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

    def update(self):
        super(Snowball, self).update()
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()


class Explosion(games.Animation):
    sound = games.load_sound("Sounds/FX/explosion.wav")
    explosion_files = ["Images/explosion(1).png",
                       "Images/explosion(2).png",
                       "Images/explosion(3).png",
                       "Images/explosion(4).png",
                       "Images/explosion(5).png",
                       "Images/explosion(6).png",
                       "Images/explosion(7).png"]

    def __init__(self, x, y):
        super(Explosion, self).__init__(images=Explosion.explosion_files,
                                        x=x, y=y, n_repeats=1,
                                        repeat_interval=3,
                                        is_collideable=False)
        Explosion.sound.play()


class Game(object):
    def __init__(self):
        self.score = games.Text(value=0,
                                size=30,
                                top=5,
                                color=color.white,
                                right=games.screen.width-10,
                                is_collideable=False)
        games.screen.add(self.score)
        self.startup = games.load_sound("Sounds/FX/startup.wav")
        self.startup.play()
        self.sound = games.load_sound("Sounds/FX/level.wav")
        self.theme = games.music.load("Sounds/Theme/far.wav")
        self.level = 0
        self.birth_steve()

    def birth_steve(self):
        self.player = Steve(game=self,
                            x=games.screen.width / 2,
                            y=games.screen.height / 2)
        games.screen.add(self.player)

    def play(self):
        games.music.play(-1)
        background_img = games.load_image("Images/stars.png", transparent=False)
        games.screen.background = background_img
        self.advance()
        games.screen.mainloop()

    def advance(self):
        self.level += 1
        BUFFER = 150
        for i in range(self.level):
            x_min = random.randrange(BUFFER)
            y_min = BUFFER - x_min
            x_distance = random.randrange(x_min, games.screen.width-x_min)
            y_distance = random.randrange(y_min, games.screen.width - y_min)
            x = self.player.x + x_distance
            y = self.player.y + y_distance
            x %= games.screen.width
            y %= games.screen.height
            new_fireball = Fireball(game=self, x=x, y=y, size=Fireball.LARGE)
            games.screen.add(new_fireball)
        level_message = games.Message(value="Level " + str(self.level),
                                      size=40,
                                      color=color.white,
                                      x= games.screen.width/2,
                                      y=games.screen.width/10,
                                      lifetime=3*games.screen.fps,
                                      is_collideable=False)
        games.screen.add(level_message)
        if self.level > 1:
            self.sound.play()

    def end(self):
        end_message = games.Message(value="Game Over ",
                                    size=90,
                                    color=color.dark_red,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2,
                                    lifetime=-1 * games.screen.fps,
                                    is_collideable=False)
        games.screen.add(end_message)


def main():
    blockworld_defenders = Game()
    blockworld_defenders.play()


main()
