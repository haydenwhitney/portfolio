# Hayden Whitney
# 4/19
# The Nowhere Dimension

from superwires import games, color
import pygame
import random


pygame.init()
games.init(screen_width=640, screen_height=480, fps=50)


class Square(games.Sprite):
    image = games.load_image("images/square.png")
    speed = 3

    def __init__(self, x, y=50):
        super(Square, self).__init__(image=Square.image, x=x, y=y, dy=Square.speed)
        self.score = games.Text(value=0, size=25, color=color.black, top=5,
                                right=games.screen.width - 10, is_collideable=False)
        games.screen.add(self.score)

    def update(self):
        if self.top > games.screen.height:
            self.destroy()
            self.score.value = self.score.value + 10
            self.score.right = games.screen.width - 10


class Squid(games.Sprite):
    image = games.load_image("images/squid.png", transparent=True)

    def __init__(self):
        super(Squid, self).__init__(image=Squid.image, x=games.mouse.x, y=435)

    def update(self):
        self.x = games.mouse.x
        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games. screen.width
        self.check_collision()

    def check_collision(self):
        for square in self.overlapping_sprites:
            self.destroy()
            self.end_game()

    def end_game(self):
        end_message = games.Message(value="GAME OVER",
                                    size=120,
                                    color=color.dark_red,
                                    x=games.screen.width / 2,
                                    y=games.screen.height / 2,
                                    lifetime=10*games.screen.fps,
                                    after_death=games.screen.quit)
        games.screen.add(end_message)


class Nothing(games.Sprite):
    image = games.load_image("images/alone.png", transparent=True)

    def __init__(self, y=10, speed=3, odds=100):
        super(Nothing, self).__init__(image=Nothing.image, x=games.screen.width/2, y=y, dx=speed)
        self.odds = odds
        self.time = 1

    def update(self):
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds) == 0:
            self.dx = -self.dx
        self.check_drop()

    def check_drop(self):
        if self.time > 0:
            self.time -= 1
        else:
            new_square = Square(x=self.x)
            games.screen.add(new_square)
            self.time = random.randrange(5, 200)


def main():
    background_image = games.load_image("images/nowhere.png", transparent=False)
    icon_image = games.load_image("images/icon.png", transparent=False)
    squid_image = Squid()
    nothing_image = Nothing()
    square_image = Square(100)
    games.screen.background = background_image
    add = games.screen.add
    add(squid_image)
    add(nothing_image)
    add(square_image)
    pygame.display.set_caption("The Nowhere Dimension")
    pygame.display.set_icon(icon_image)
    games.screen.mainloop()


main()
