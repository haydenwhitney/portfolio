# Hayden Whitney
# 5/19
# Minecraft Defenders v1.1.0

from superwires import games
import random

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
                self.bottom = games.screen.height



class Ship(games.Sprite):
    pass


class Arrow(games.Sprite):
    pass


class Explosion(games.Sprite):
    pass


def main():
    background_img = games.load_image("Images/stars.png", transparent=False)

    for i in range(8):
        x = random.randrange(games.screen.width)
        y = random.randrange(games.screen.width)
        size = random.choice([Asteroids.SMALL, Asteroids.MEDIUM, Asteroids.LARGE])
        new_asteroid = Asteroids(x=x, y=y, size=size)
        games.screen.add(new_asteroid)

    games.screen.background = background_img

    games.screen.mainloop()

main()
