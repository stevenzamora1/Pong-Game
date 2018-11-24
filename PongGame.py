import pygame #import all the resources and utilities from pygame

pygame.init() #initialize  pygame resources 

# set mode will set the information regarding our game window and initializes it
gamewindow = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()

# Initialize a font (font name, font size)
game_font = pygame.font.SysFont(None, 45)
title_font = pygame.font.SysFont(None, 36)

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

gameRunning = True
paused = False

player_width = 10
player_height = 50

player_one_y = 275
player_two_y = 275

player_update_y = 0
player_two_update_y = 0

first_player_score = 0
second_player_score = 0

ball_x = 390
ball_y = 290
ball_width = 10
ball_height = 10

ball_speed = 5

ball_x_move = -ball_speed
ball_y_move = ball_speed

pong_title  = title_font.render(" Pong ", True, white)


# Define new function (a set of instructions) and have one parameter (score)
def render_score(score, second_player):
	# Render the font (text, antialias flag, color)
	text = game_font.render(str(score), True, white)
	if not second_player:
		gamewindow.blit(text, (345, 75))
	else:
		gamewindow.blit(text, (401, 75))

while gameRunning:
	#while our game is running, this is all going to happen
	for event in pygame.event.get():
		#handles all sort of user input
		print event 
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				player_update_y = -10
			if event.key == pygame.K_s:
				player_update_y = 10
			if event.key == pygame.K_UP:
				player_two_update_y = -10
			if event.key == pygame.K_DOWN:
				player_two_update_y = 10
			if event.key == pygame.K_ESCAPE:
				paused = not paused
		
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w or event.key == pygame.K_s:
				player_update_y = 0
				
			if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				player_two_update_y = 0
		
		#a condition that checks whether the event type is a quit event
		if event.type == pygame.QUIT:
			gameRunning = False
	
	if not paused:
		player_one_y += player_update_y
		player_two_y += player_two_update_y
		
		if player_one_y <= 0:
			player_one_y = 0
			
		if player_one_y >= 550:
			player_one_y = 550
			
		if player_two_y <= 0:
			player_two_y = 0
			
		if player_two_y >= 550:
			player_two_y = 550
		
		ball_x += ball_x_move
		ball_y += ball_y_move
		
		
		if ball_y >= 600 - ball_width:
			ball_y_move = -ball_speed
		
		if ball_y <= 0:
			ball_y_move = ball_speed
			
		if ball_x >= 800:
			ball_x = 390
			ball_y = 290
			first_player_score += 1
			ball_x_move = -ball_x_move
			ball_y_move = -ball_y_move
		if ball_x <= 0 - ball_width:
			ball_x = 390
			ball_y = 290
			second_player_score += 1
			ball_x_move = -ball_x_move
			ball_y_move = -ball_y_move
		
		if  ball_x == 50 + player_width and ball_y >= player_one_y and ball_y + ball_width <= player_one_y + player_height:
			ball_x_move = ball_speed
			
		if  ball_x == 750 - ball_width and ball_y >= player_two_y and ball_y + ball_height <= player_two_y + player_height:
			ball_x_move = -ball_speed
	
	gamewindow.fill(black)
		
	render_score(first_player_score, False)
	render_score(second_player_score, True)
	pygame.draw.rect(gamewindow, white, (50, player_one_y, player_width, player_height))
	pygame.draw.rect(gamewindow, white, (750, player_two_y, player_width, player_height))
	pygame.draw.rect(gamewindow, white, (ball_x, ball_y, ball_width, ball_height))
	
	if not paused:
		gamewindow.blit(pong_title, (220, 25))


	
	
	clock.tick(60)
	pygame.display.update() #updates all the graphic components in the game window
	
pygame.quit() #shuts down all the pygame resources and closes the game window
quit() #quits the python process