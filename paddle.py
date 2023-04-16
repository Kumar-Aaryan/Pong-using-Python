import pygame
black = (0,0,0)

class Paddle(pygame.sprite.Sprite): #Super Class
	def __init__(self,color,width,height): #Child Class
		super().__init__()
		self.image=pygame.Surface([width,height]) #Makes an imaginary layer for the sprite to move on
		self.image.fill(black)
		self.image.set_colorkey(black)

		pygame.draw.rect(self.image,color,[0,0,width,height])
		self.rect=self.image.get_rect() #Getting the rectangle on top of the surface

	def moveup(self,pixels):
		self.rect.y-=pixels
		if self.rect.y<0:
			self.rect.y

	def movedown(self,pixels):
		self.rect.y+=pixels
		if self.rect.y>400:
			self.rect.y=400


