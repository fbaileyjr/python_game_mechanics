import pygame
from pygame.locals import *


def get_pic_size(pic_file: str):
    with Image.open(f'./images/{pic_file}') as test_image:
        return test_image.size

screen_width = 700
screen_height = 700
image = 'butterfly.png'
'''
center = ((screen_width/2), (screen_height/2))

image_width, image_height = get_pic_size(image)
'''
pygame.init()

# create screen and size
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

# scale and display a sprite
sprite1 = pygame.image.load(f'./images/{image}')
sprite1 = pygame.transform.scale(sprite1, (32,32))
spriteWidth = sprite1.get_width()
spriteHeight = sprite1.get_height()

# set up the screen title
pygame.display.set_caption('Hello Resize')

# fill the screen with color - RGB
screen.fill((0, 0, 0))

# game over flag
game_over = False

# declaring keyboard stuff
x, y = (0, 0)

# setting the clock
clock = pygame.time.Clock()


# main loop
while not game_over:
    # setting the frame rate
    dt = clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEMOTION:
            x,y = event.pos
            x = x - (spriteWidth/2)
            y = y - (spriteHeight/2)
        pressed = pygame.key.get_pressed()
    # multiplying the frame rate times the movement variable
    if pressed[K_UP]:
        y -= 0.5 * dt
    if pressed[K_DOWN]:
        y += 0.5 * dt
    if pressed[K_RIGHT]:
        x += 0.5 * dt
    if pressed[K_LEFT]:
        x -= 0.5 * dt

    if pressed[K_SPACE]:
        x, y = (0, 0)

    if x > (screen.get_width() - spriteWidth):
        x = screen.get_width() - spriteWidth

    if x < 0:
        x = 0

    if y > (screen.get_height() - spriteHeight):
        y = screen.get_height() - spriteHeight

    if y < 0:
        y = 0
    # clear the screen
    # fill the screen with color - RGB
    screen.fill((0, 0, 0))

   
    # draw the sprite object
    screen.blit(sprite1, (x, y))

    # refresh the screen
    pygame.display.update()
pygame.quit()
