# Hayden Whitney
# 5/19
# Breakout

import math
import pygame
from os import path

img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

block_width = 52
block_height = 21

high_score = 0
score = 0


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = brick_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Ball(pygame.sprite.Sprite):
    speed = 10.0
    x = 0.0
    y = 180.0
    direction = 200
    width = 10
    height = 10

    def __init__(self):
        super().__init__()
        self.image = ball_img
        self.rect = self.image.get_rect()
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()

    def bounce(self, diff):
        self.direction = (180 - self.direction) % 360
        self.direction -= diff

    def update(self):
        direction_radians = math.radians(self.direction)
        self.x += self.speed * math.sin(direction_radians)
        self.y -= self.speed * math.cos(direction_radians)
        self.rect.x = self.x
        self.rect.y = self.y

        # Where do we bounce
        if self.y <= 0:
            self.bounce(0)
            self.y = 1
        if self.x <= 0:
            self.direction = (360 - self.direction) % 360
            self.x = 1
        if self.x > self.screenwidth - self.width:
            self.direction = (360 - self.direction) % 360
            self.x = self.screenwidth - self.width - 1

        # Did we fall off the bottom edge of the screen?
        if self.y > 600:
            return True
        else:
            return False


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 75
        self.height = 15
        self.image = pad_img
        self.rect = self.image.get_rect()
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
        self.rect.x = 0
        self.rect.y = self.screenheight - self.height

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        if self.rect.x > self.screenwidth - self.width:
            self.rect.x = self.screenwidth - self.width


pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption('Breakout')

font = pygame.font.Font(None, 36)
background = pygame.Surface(screen.get_size())

# Loads images
ball_img = pygame.image.load(path.join(img_dir, 'ball.png')).convert()
pad_img = pygame.image.load(path.join(img_dir, 'pad.png')).convert()
brick_img = pygame.image.load(path.join(img_dir, 'brick.png')).convert()

# Load sound effects
blip = pygame.mixer.Sound(path.join(snd_dir, 'blip.wav'))

# Load and play music
pygame.mixer.music.load(path.join(snd_dir, 'theme.wav'))
pygame.mixer.music.set_volume(0.4)

pygame.mixer.music.play(loops=-1)

# Create sprite lists
blocks = pygame.sprite.Group()
balls = pygame.sprite.Group()
allsprites = pygame.sprite.Group()

# Creates game objects
player = Player()
allsprites.add(player)
ball = Ball()
allsprites.add(ball)
balls.add(ball)

# The top of the block (y position)
top = 80
# Number of blocks to create
blockcount = 14
# Create blocks
# Five rows of blocks
for row in range(5):
    for column in range(0, blockcount):
        # Create a block (x, y)
        block = Block(column * (block_width + 6), top)
        blocks.add(block)
        allsprites.add(block)
    # Move the top of the next row down
    top += block_height + 2
# Clock to limit speed
clock = pygame.time.Clock()
# Is the game over?
game_over = False
# Exit the program?
exit_program = False

# Main program loop
while not exit_program:
    # Limit to 30 fps
    clock.tick(30)
    # Clear the screen
    screen.fill(BLACK)
    # Process the events in the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_program = True
    # Update the ball and player position as long
    # as the game is not over.
    if not game_over:
        # Update the player and ball positions
        player.update()
        game_over = ball.update()
    # If we are done, print game over
    if game_over:
        text = pygame.font.Font(None, 40).render("Game Over", True, WHITE)
        textpos = text.get_rect(centerx=background.get_width() / 2)
        textpos.top = 300
        screen.blit(text, textpos)
    # See if the ball hits the player paddle
    if pygame.sprite.spritecollide(player, balls, False):
        # The 'diff' lets you try to bounce the ball left or right
        # depending where on the paddle you hit it
        diff = (player.rect.x + player.width / 2) - (ball.rect.x + ball.width / 2)
        # Set the ball's y position in case
        # we hit the ball on the edge of the paddle
        ball.rect.y = screen.get_height() - player.rect.height - ball.rect.height - 1
        ball.bounce(diff)

    # Check for collisions between the ball and the blocks
    deadblocks = pygame.sprite.spritecollide(ball, blocks, True)
    # If we actually hit a block, bounce the ball
    if len(deadblocks) > 0:
        ball.bounce(0)
        score += len(deadblocks) * 10
        blip.play()

        # Blocks rebuild when there are none on screen
        if len(blocks) == 0:
            top = 80
            blockcount = 14
            for row in range(5):
                for column in range(0, blockcount):
                    block = Block(column * (block_width + 6), top)
                    blocks.add(block)
                    allsprites.add(block)
                top += block_height + 2
    # Draw Everything
    width = 800
    height = 600
    score_text = pygame.font.Font(None, 28).render(str(score), True, WHITE)
    score_text_rect = score_text.get_rect()
    score_text_rect = score_text_rect.move(width - score_text_rect.right, 0)
    screen.blit(score_text, score_text_rect)
    allsprites.draw(screen)
    # Flip the screen and show what we've drawn
    pygame.display.flip()

pygame.quit()


# if score > high_score:
    # high_score = score