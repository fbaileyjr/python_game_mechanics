import pygame

pygame.init()

# create screen and size
screen = pygame.display.set_mode((800, 600), 0, 32)

# display a sprite
sprite1 = pygame.image.load('./images/football.png')

# set up the screen title
pygame.display.set_caption('Hello Sprite')

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
	screen.blit(sprite1, ((800/2)-16,(600/2)-16))

	# refresh the screen
	pygame.display.update()
pygame.quit()
