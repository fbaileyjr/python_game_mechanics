import pygame
from PIL import Image


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

# main loop
while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True
    
    # draw the sprite object
	screen.blit(sprite1, (((screen.get_width()/2)-(spriteWidth/2)),((screen.get_height())/2)-(spriteHeight/2)))

	# refresh the screen
	pygame.display.update()
pygame.quit()
