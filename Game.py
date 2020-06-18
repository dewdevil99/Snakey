import pygame
import sys
import random
from pygame.locals import *
import Food
import Snake

class Game:
	def __init__(self):
		self.running=True
		self.width=400
		self.height=430
		self.snake_segs=[]
		self.spritesList=pygame.sprite.Group()

	def initialize(self):
		pygame.init()
		self.window=pygame.display.set_mode((self.width,self.height))
		pygame.display.set_caption("Snake Game")
		self.font_big = pygame.font.Font('freesansbold.ttf', 24)
		self.font_small=pygame.font.Font('freesansbold.ttf', 12)
		self.scoreText=self.font_big.render("SCORE : 0",True,pygame.Color(0,255,0))
		self.scoreTextRect=self.scoreText.get_rect()
		self.scoreTextRect.x=30
		self.scoreTextRect.y=405
		self.controlText1=self.font_small.render("p - Pause",True,pygame.Color(0,255,0))
		self.controlText2=self.font_small.render("c - Continue",True,pygame.Color(0,255,0))
		self.controlText1Rect=self.controlText1.get_rect()
		self.controlText2Rect=self.controlText2.get_rect()
		self.controlText1Rect.x=200
		self.controlText1Rect.y=403
		self.controlText2Rect.x=200
		self.controlText2Rect.y=417

	def setup(self):
		self.scoreText=self.font_big.render("SCORE : 0",True,pygame.Color(0,255,0))
		self.snake_head=Snake.Snake(150,150)
		self.snake_head.image.fill(pygame.Color(0,0,255))
		self.spritesList.add(self.snake_head)
		for i in range(1,3):
			segment=Snake.Snake(150,150+i*10)
			self.snake_segs.append(segment)
			self.spritesList.add(segment)
		self.food=Food.Food()
		self.score=0

	def start(self):
		self.initialize()
		self.setup()
		clock=pygame.time.Clock()

		while(self.running):
			seg=None
			keys=pygame.key.get_pressed()
			for event in pygame.event.get():
				if(event.type==QUIT):
					self.running=False
					pygame.quit()
					sys.exit()
			s=self.spritesList.sprites()
			last_seg=s[len(s)-1]
			for i in range(len(s)-1,0,-1):
				s[i].direction=s[i-1].direction

			if(keys[K_RIGHT]):
				s[0].move_right()
			if(keys[K_LEFT]):
				s[0].move_left()
			if(keys[K_UP]):
				s[0].move_up()
			if(keys[K_DOWN]):
				s[0].move_down()
			if(keys[K_p]):
				pauseText=self.font_big.render("Paused",True,pygame.Color(0,255,0))
				pauseTextRect=pauseText.get_rect()
				pauseTextRect.x=100
				pauseTextRect.y=200
				self.window.blit(pauseText,pauseTextRect)
				pygame.display.flip()
				l=0
				while True:
					for event in pygame.event.get():
						if(event.type==QUIT):
							self.running=False
							pygame.quit()
							sys.exit()
						if(event.type==KEYDOWN):
							if(event.key==K_c):
								l=1
								break
					if(l==1):
						break

			self.window.fill(pygame.Color(0,0,0))
			pygame.draw.line(self.window,pygame.Color(255,255,255),(0,self.height-30),(self.width,self.height-30),2)
			self.window.blit(self.scoreText,self.scoreTextRect)
			self.window.blit(self.controlText1,self.controlText1Rect)
			self.window.blit(self.controlText2,self.controlText2Rect)
			self.food.draw_food(self.window)

			if(self.food.food_eaten(s[0].rect)):
				seg=Snake.Snake(last_seg.rect.x,last_seg.rect.y)
				seg.direction=last_seg.direction
				self.snake_segs.append(seg)
				self.score+=1
				self.scoreText=self.font_big.render("SCORE : "+str(self.score),True,pygame.Color(0,255,0))
				self.food.new_food(s)

			if(s[0].collision(s,self.width,self.height-30)):
				self.running=False
				gameOverText=self.font_big.render("GAME OVER",True,pygame.Color(0,255,0))
				gameOverTextRect=gameOverText.get_rect()
				gameOverTextRect.x=100
				gameOverTextRect.y=200
				playAgainText=self.font_big.render("Play Again? (Y/N)",True,pygame.Color(0,255,0))
				playAgainTextRect=playAgainText.get_rect()
				playAgainTextRect.x=80
				playAgainTextRect.y=230
				self.window.blit(gameOverText,gameOverTextRect)
				self.window.blit(playAgainText,playAgainTextRect)
				pygame.display.flip()
				l=0
				while True:
					for event in pygame.event.get():
						if(event.type==KEYDOWN):
							if(event.key==pygame.K_y):
								self.running=True
								self.spritesList.empty()
								self.setup()
								l=1
								break
							if(event.key==pygame.K_n):
								pygame.quit()
								sys.exit()
					if(l==1):
						break
					
			self.spritesList.update()
			if seg is not None:
				self.spritesList.add(seg)
			self.spritesList.draw(self.window)
			clock.tick(9)
			pygame.display.flip()

game=Game()
game.start()