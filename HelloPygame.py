import pygame

pygame.init()

# create screen and size
screen = pygame.display.set_mode((640, 480), 0, 32)

# set up the screen title
pygame.display.set_caption('Hello Pygame')

# fill the screen with color - RGB
screen.fill((0, 0, 0))

# game over flag
game_over = False

# main loop
while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True

pygame.quit()
