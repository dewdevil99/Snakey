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
		self.font = pygame.font.Font('freesansbold.ttf', 24)
		self.text=self.font.render("SCORE : 0",True,pygame.Color(0,255,0))
		self.textRect=self.text.get_rect()
		self.textRect.x=100
		self.textRect.y=405
		self.score=0

	def start(self):
		self.initialize()
		self.snake_head=Snake.Snake(150,150)
		self.snake_head.image.fill(pygame.Color(0,0,255))
		self.spritesList.add(self.snake_head)
		for i in range(1,3):
			segment=Snake.Snake(150,150+i*10)
			self.snake_segs.append(segment)
			self.spritesList.add(segment)
		#self.snake.set_head(self.window)
		self.food=Food.Food()
		# self.food.draw_food(self.window)
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

			self.window.fill(pygame.Color(0,0,0))
			self.window.blit(self.text,self.textRect)
			self.food.draw_food(self.window)

			if(self.food.food_eaten(s[0].rect)):
				seg=Snake.Snake(last_seg.rect.x,last_seg.rect.y)
				seg.direction=last_seg.direction
				#s[0].rect.x=s[0].rect.x+10
				#snake_head.rect.y=snake_head.rect.y
				self.snake_segs.append(seg)
				self.score+=1
				self.text=self.font.render("SCORE : "+str(self.score),True,pygame.Color(0,255,0))
				self.food.new_food(s)
				#self.spritesList.add(seg)
				#self.snake.add_seg(self.window)
			if(s[0].collision(s,self.width,self.height-30)):
				self.running=False
				pygame.quit()
				sys.exit()

			
			self.spritesList.update()
			if seg is not None:
				self.spritesList.add(seg)
			self.spritesList.draw(self.window)
			clock.tick(10)
			pygame.display.flip()

game=Game()
game.start()