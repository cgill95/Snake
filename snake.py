import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
WHITE_COLOR = (255,255,255)
RED_COLOR = (255,0,0)
GREEN_COLOR = (0, 255, 0)
BLACK_COLOR = (0,0,0)
clock = pygame.time.Clock()
GAME_TITLE = "Snake Game"
pygame.font.init()
FONT = pygame.font.SysFont('comicsans', 75)
LEVEL_FONT = pygame.font.SysFont('comicsans', 30)

def snake(snake, width, background):
	for x,y in snake:
		pygame.draw.rect(background, WHITE_COLOR, [x, y, width, width])
	pygame.display.flip()

def score(points,background):
	value = LEVEL_FONT.render("Your Score: " + str(points), True, GREEN_COLOR)
	background.blit(value, [20, 20])
	pygame.display.flip()

def replayMenu(background):
	value = LEVEL_FONT.render("If you wanna replay press R, else press Q!", True, GREEN_COLOR)
	background.blit(value, [20, 60])
	pygame.display.flip()

class Game:
	
	TICK_RATE = 30
	
	def __init__(self,title,width, height):
		self.title = title
		self.width = width
		self.height = height

		self.game_screen = pygame.display.set_mode((width,height))
		self.game_screen.fill(BLACK_COLOR)
		pygame.display.set_caption(title)

	def run_game_loop(self):
		is_game_over = False
		direction = 0
		prevDirection = 0
		gameQuit = False
		x = SCREEN_HEIGHT / 2
		y = SCREEN_WIDTH / 2
		snakeList = []
		snakeWidth = 10
		snakeSpeed = 1
		snakeLength = 1
		xPos = 0
		yPos = 0
		foodX = random.randint(0, SCREEN_WIDTH - snakeWidth) // 10 * 10
		foodY = random.randint(0, SCREEN_HEIGHT- snakeWidth) // 10 * 10
		snakeList.append([x,y])
		#score(snakeLength - 1, self.game_screen)
		
		while not gameQuit:
			self.game_screen.fill(BLACK_COLOR)
			score(snakeLength -1, self.game_screen)
			replayMenu(self.game_screen)
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
					gameQuit = True
				elif event.type == pygame.KEYDOWN:
						if event.key == pygame.K_r:
							is_game_over = False
							new_game = Game(GAME_TITLE,SCREEN_WIDTH,SCREEN_HEIGHT).run_game_loop()
			clock.tick(self.TICK_RATE)
			while not is_game_over:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						gameQuit = True

					elif event.type == pygame.KEYDOWN:
						if event.key == pygame.K_UP or event.key == pygame.K_w:
							yPos = snakeWidth * -1
							xPos = 0						

						elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
							yPos = 0
							xPos = snakeWidth

						elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
							yPos = snakeWidth
							xPos = 0
							
						elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
							yPos = 0
							xPos = snakeWidth * -1

				self.game_screen.fill(BLACK_COLOR)
				
				pygame.draw.rect(self.game_screen, RED_COLOR, [foodX, foodY, snakeWidth, snakeWidth])
				score(snakeLength - 1, self.game_screen)

				x += xPos * snakeSpeed
				y += yPos * snakeSpeed

				snakeHead = []
				snakeHead.append(x)
				snakeHead.append(y)
				snakeList.insert(0, snakeHead)
				if len(snakeList) > snakeLength:
					del snakeList[-1]

				for item in snakeList[1:]:
					if snakeHead == item:
						is_game_over = True

				if x <= 0 or y <= 0 or x >= SCREEN_WIDTH or y >= SCREEN_HEIGHT:
					is_game_over = True

				snake(snakeList, snakeWidth, self.game_screen)
				

				if (x >= foodX - 10 and x <= foodX + 10 ) and (y >= foodY -10 and y <= foodY+10):
					foodX = random.randint(0, SCREEN_WIDTH - snakeWidth) // 10 * 10
					foodY = random.randint(0, SCREEN_HEIGHT- snakeWidth) // 10 * 10
					snakeLength += 1
				
				clock.tick(self.TICK_RATE)		
				#pygame.display.update()

pygame.init()

new_game = Game(GAME_TITLE,SCREEN_WIDTH,SCREEN_HEIGHT).run_game_loop()

pygame.quit()
quit()
