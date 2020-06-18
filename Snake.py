import pygame
from pygame.locals import *
import random
import sys


class Snake(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image=pygame.Surface((10,10))
		self.image.fill(pygame.Color(0,255,0))
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
		self.direction=1

	def collision(self,snake_segments_sprites,width,height):
		if(self.rect.x<0 or self.rect.y<0 or self.rect.x>=width or self.rect.y>=height):
			return True
		l=len(snake_segments_sprites)
		for segment in snake_segments_sprites[1:l]:
			if(self.rect.colliderect(segment.rect)):
				return True
		return False

	def move_right(self):
		if(self.direction!= -2 and self.direction!=2):
			self.direction=2

	def move_left(self):
		if(self.direction!= -2 and self.direction!=2):
			self.direction=-2

	def move_up(self):
		if(self.direction!= -1 and self.direction!=1):
			self.direction=1

	def move_down(self):
		if(self.direction!= -1 and self.direction!=1):
			self.direction=-1

	def update(self):
		if(self.direction==1):
			self.rect.y-=10
		if(self.direction==-1):
			self.rect.y+=10
		if(self.direction==2):
			self.rect.x+=10
		if(self.direction==-2):
			self.rect.x-=10
