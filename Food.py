import pygame
import random
import sys
from pygame.locals import *


class Food:
	def __init__(self):
		self.x=50
		self.y=50
		self.color=pygame.Color(255,0,0)
		self.width=10
		self.height=10

	def draw_food(self,surface):
		self.food=pygame.Rect(self.x,self.y,self.width,self.height)
		pygame.draw.rect(surface,self.color,self.food)

	def food_eaten(self,head):
		return self.food.colliderect(head)

	def new_food(self,segments):
		segment_coord=[]
		for i in range(len(segments)):
			segment_coord.append([segments[i].rect.x,segments[i].rect.y])
		rand_x=random.randrange(0,400,10)
		rand_y=random.randrange(0,400,10)
		while([rand_x,rand_y] in segment_coord):
			rand_x=random.randrange(0,400,10)
			rand_y=random.randrange(0,400,10)
		self.x=rand_x
		self.y=rand_y

# pygame.init()
# screen=pygame.display.set_mode((600,620))
# pygame.display.set_caption("Food Screen")

# while True:
# 	for event in pygame.event.get():
# 		if event.type==QUIT:
# 			pygame.quit()
# 			sys.exit()
# 	f=Food()
# 	f.draw_food(screen)
# 	pygame.display.update()
