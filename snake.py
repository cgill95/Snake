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
LEVEL_FONT = pygame.font.SysFont('comicsans', 40)
BUTTON_FONT = pygame.font.SysFont('comicsans', 20)
TICK_RATE = 30
MULTIPLE_FOODS = False
INVISIBLE_WALLS = False

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

def text_objects(text, font, color):
	textSurface = font.render(text, True, color)
	return textSurface, textSurface.get_rect()

class Menu:
	def __init__(self,title,width, height):
		self.title = title
		self.width = width
		self.height = height

		self.game_screen = pygame.display.set_mode((width,height))
		self.game_screen.fill(BLACK_COLOR)
		pygame.display.set_caption(title)

	def showMenu(self):
		menuActive = True
		startButtonX = 150
		startButtonY = 50
		optionButtonX = 150
		optionButtonY = 150
		endButtonX = 150
		endButtonY = 250
		buttonSizeX = 100
		buttonSizeY = 50
		mouse = [0,0]

		while menuActive:
			for event in pygame.event.get():
				#print(event)
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				if event.type == pygame.MOUSEBUTTONUP:
					mouse = pygame.mouse.get_pos()
			self.game_screen.fill(BLACK_COLOR)

			pygame.draw.rect(self.game_screen, WHITE_COLOR, (startButtonX, startButtonY, buttonSizeX, buttonSizeY))
			pygame.draw.rect(self.game_screen, WHITE_COLOR, (optionButtonX, optionButtonY, buttonSizeX, buttonSizeY))
			pygame.draw.rect(self.game_screen, WHITE_COLOR, (endButtonX, endButtonY, buttonSizeX, buttonSizeY))
			
			textSurf, textRect = text_objects("Start Game", BUTTON_FONT, BLACK_COLOR)
			textRect.center = ( (startButtonX+(buttonSizeX/2)), (startButtonY+(buttonSizeY/2)) )
			self.game_screen.blit(textSurf, textRect)
			
			textSurf, textRect = text_objects("Options", BUTTON_FONT, BLACK_COLOR)
			textRect.center = ( (optionButtonX+(buttonSizeX/2)), (optionButtonY+(buttonSizeY/2)) )
			self.game_screen.blit(textSurf, textRect)

			textSurf, textRect = text_objects("Close Game", BUTTON_FONT, BLACK_COLOR)
			textRect.center = ( (endButtonX+(buttonSizeX/2)), (endButtonY+(buttonSizeY/2)) )
			self.game_screen.blit(textSurf, textRect)
			
			if startButtonX+buttonSizeX > mouse[0] > buttonSizeX and startButtonY+buttonSizeY > mouse[1] > buttonSizeY:
				new_game = Game(GAME_TITLE,SCREEN_WIDTH,SCREEN_HEIGHT).run_game_loop()
				menu = Menu(GAME_TITLE,SCREEN_WIDTH,SCREEN_HEIGHT).showMenu()
			elif optionButtonX+buttonSizeX > mouse[0] > buttonSizeX and optionButtonY+buttonSizeY > mouse[1] > buttonSizeY:
				pygame.display.quit()
				menu = Menu('Options',SCREEN_WIDTH,SCREEN_HEIGHT).optionsMenu()

			elif endButtonX+buttonSizeX > mouse[0] > buttonSizeX and endButtonY+buttonSizeY > mouse[1] > buttonSizeY:
				pygame.quit()
				quit()

			pygame.display.update()
			clock.tick(TICK_RATE)

	def optionsMenu(self):
		optionsActive = True
		option1ButtonX = 150
		option1ButtonY = 50
		option2ButtonX = 150
		option2ButtonY = 150
		backButtonX = 150
		backButtonY = 250
		buttonSizeX = 150
		buttonSizeY = 50
		mouse = [0,0]
		global INVISIBLE_WALLS
		global MULTIPLE_FOODS

		while optionsActive:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				if event.type == pygame.MOUSEBUTTONUP:
					mouse = pygame.mouse.get_pos()
			self.game_screen.fill(BLACK_COLOR)

			if INVISIBLE_WALLS:
				pygame.draw.rect(self.game_screen, GREEN_COLOR, (option1ButtonX, option1ButtonY, buttonSizeX, buttonSizeY))
			else:
				pygame.draw.rect(self.game_screen, RED_COLOR, (option1ButtonX, option1ButtonY, buttonSizeX, buttonSizeY))
			
			if MULTIPLE_FOODS:
				pygame.draw.rect(self.game_screen, GREEN_COLOR, (option2ButtonX, option2ButtonY, buttonSizeX, buttonSizeY))
			else:
				pygame.draw.rect(self.game_screen, RED_COLOR, (option2ButtonX, option2ButtonY, buttonSizeX, buttonSizeY))
			
			pygame.draw.rect(self.game_screen, WHITE_COLOR, (backButtonX, backButtonY, buttonSizeX, buttonSizeY))

			textSurf, textRect = text_objects("Invisible Walls", BUTTON_FONT, BLACK_COLOR)
			textRect.center = ( (option1ButtonX+(buttonSizeX/2)), (option1ButtonY+(buttonSizeY/2)) )
			self.game_screen.blit(textSurf, textRect)
			
			textSurf, textRect = text_objects("Multiple Food Items", BUTTON_FONT, BLACK_COLOR)
			textRect.center = ( (option2ButtonX+(buttonSizeX/2)), (option2ButtonY+(buttonSizeY/2)) )
			self.game_screen.blit(textSurf, textRect)

			textSurf, textRect = text_objects("Back To Main Menu", BUTTON_FONT, BLACK_COLOR)
			textRect.center = ( (backButtonX+(buttonSizeX/2)), (backButtonY+(buttonSizeY/2)) )
			self.game_screen.blit(textSurf, textRect)

			if option1ButtonX+buttonSizeX > mouse[0] > buttonSizeX and option1ButtonY+buttonSizeY > mouse[1] > buttonSizeY:
				if INVISIBLE_WALLS:
					INVISIBLE_WALLS = False
				else:
					INVISIBLE_WALLS = True
				

			elif option2ButtonX+buttonSizeX > mouse[0] > buttonSizeX and option2ButtonY+buttonSizeY > mouse[1] > buttonSizeY:
				if MULTIPLE_FOODS:
					MULTIPLE_FOODS = False
				else:
					MULTIPLE_FOODS = True

			elif backButtonX+buttonSizeX > mouse[0] > buttonSizeX and backButtonY+buttonSizeY > mouse[1] > buttonSizeY:
				pygame.display.quit()
				menu = Menu(GAME_TITLE,SCREEN_WIDTH,SCREEN_HEIGHT).showMenu()
			
			mouse = [0,0]
			pygame.display.update()
			clock.tick(TICK_RATE)

class Game:	
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
		foodAmount = 1
		foodList = []
		foodX = random.randint(0, SCREEN_WIDTH - snakeWidth) // 10 * 10
		foodY = random.randint(0, SCREEN_HEIGHT- snakeWidth) // 10 * 10
		foodList.append([foodX,foodY])
		snakeList.append([x,y])
		global INVISIBLE_WALLS
		global MULTIPLE_FOODS
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
			clock.tick(TICK_RATE)
			
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
				
				for fx, fy in foodList:
					pygame.draw.rect(self.game_screen, RED_COLOR, [fx, fy, snakeWidth, snakeWidth])
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

				if INVISIBLE_WALLS:
					if x <= 0:
						x = SCREEN_WIDTH
					elif y <= 0:
						y = SCREEN_HEIGHT
					elif x >= SCREEN_WIDTH:
						x = 0
					elif y >= SCREEN_HEIGHT:
						y = 0
				else:
					if x <= 0 or y <= 0 or x >= SCREEN_WIDTH or y >= SCREEN_HEIGHT:
						is_game_over = True

				snake(snakeList, snakeWidth, self.game_screen)
				
				for fx, fy in foodList:
					if (x >= fx - 10 and x <= fx + 10 ) and (y >= fy -10 and y <= fy+10):
						foodList.remove([fx,fy])
						if MULTIPLE_FOODS:
							foodAmount = random.randint(1,3)
							if len(foodList) > 2:
								foodAmount = 0
						else:
							foodAmount = 1

						for i in range(foodAmount):
							fx = random.randint(0, SCREEN_WIDTH - snakeWidth) // 10 * 10
							fy = random.randint(0, SCREEN_HEIGHT- snakeWidth) // 10 * 10
							foodList.append([fx,fy])
						snakeLength += 1
				clock.tick(TICK_RATE)		
				#pygame.display.update()

pygame.init()

menu = Menu(GAME_TITLE,SCREEN_WIDTH,SCREEN_HEIGHT).showMenu()
#new_game = Game(GAME_TITLE,SCREEN_WIDTH,SCREEN_HEIGHT).run_game_loop()

#pygame.quit()
#quit()
