import pygame
from pygame.locals import *
import random
import sys

class Node:
	def __init__(self):
		self.prev=None
		self.next=None
		self.data=None


class Snake(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image=pygame.Surface((10,10))
		self.image.fill(pygame.Color(0,255,0))
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
		# self.width=10
		# self.height=10
		# self.head_color=pygame.Color(0,255,0)
		# self.body_color=pygame.Color(0,0,255)
		# self.snake_head=Node()
		self.direction=1

	# def set_head(self,screen):
	# 	seg1=Node()
	# 	seg2=Node()
	# 	self.snake_head.next=seg1
	# 	seg1.next=seg2
	# 	seg1.prev=self.snake_head
	# 	seg2.prev=seg1
	# 	self.snake_head.data=pygame.Rect(self.x,self.y,self.width,self.height)
	# 	pygame.draw.rect(screen,self.head_color,self.snake_head.data)
	# 	seg1.data=pygame.Rect(self.x,self.y+10,self.width,self.height)
	# 	pygame.draw.rect(screen,self.body_color,seg1.data)
	# 	seg2.data=pygame.Rect(self.x,self.y+20,self.width,self.height)
	# 	pygame.draw.rect(screen,self.body_color,seg2.data)

	# def add_seg(self,screen):
	# 	seg=Node()
	# 	seg.next=self.snake_head.next
	# 	self.snake_head.next.prev=seg
	# 	self.snake_head.next=seg
	# 	seg.data=pygame.Rect(self.x,self.y,self.width,self.height)
	# 	pygame.draw.rect(screen,self.body_color,seg.data)

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
			# self.x+=10
			# print(self.x)
			# print(self.y)

	def move_left(self):
		if(self.direction!= -2 and self.direction!=2):
			self.direction=-2
			# self.x-=10

	def move_up(self):
		if(self.direction!= -1 and self.direction!=1):
			self.direction=1
			# self.y-=10

	def move_down(self):
		if(self.direction!= -1 and self.direction!=1):
			self.direction=-1
			# self.y+=10

	def update(self):
		if(self.direction==1):
			self.rect.y-=10
		if(self.direction==-1):
			self.rect.y+=10
		if(self.direction==2):
			self.rect.x+=10
		if(self.direction==-2):
			self.rect.x-=10
