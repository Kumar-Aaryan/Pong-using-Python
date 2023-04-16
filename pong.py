import pygame,sys
from pygame.locals import*
from paddle import Paddle #Importing the class name actually
from Ball import Ball


pygame.init()


font1 = introfont = pygame.font.SysFont(None,45)
black=(0,0,0)
white=(255,255,255)
size = (700,500)
hot_ponk=(139,58,98)

screen = pygame.display.set_mode(size)# Making the app run at a specific size
pygame.display.set_caption("Pong")

paddleA=Paddle(white,10,100)
paddleA.rect.x=20
paddleA.rect.y=200
paddleB=Paddle(white,10,100)
paddleB.rect.x=670
paddleB.rect.y=200

ball=Ball(white,10,10)
ball.rect.x=345
ball.rect.y=195




all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

scoreA=0
scoreB=0

def show_score_A(x,y):
	
	score=font1.render("SCORE A:"+str(scoreA),True,(white))
	screen.blit(score,(x,y))

def show_score_B(x,y):
	score=font1.render("SCORE B:"+str(scoreB),True,(white))
	screen.blit(score,(x,y))


carryon = True

clock = pygame.time.Clock() #Sets the animation Speed fps basically

while carryon:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			carryon = False

		elif event.type==pygame.KEYDOWN:
			if event.key==pygame.K_x:
				carryon=False




	keys=pygame.key.get_pressed()
	if keys[pygame.K_w]:
		paddleA.moveup(5*2)
	if keys[pygame.K_s]:
		paddleA.movedown(5*2)
	if keys[pygame.K_UP]:
		paddleB.moveup(5*2)
	if keys[pygame.K_DOWN]:
		paddleB.movedown(5*2)

	if ball.rect.x>=690:
		scoreA+=1
		ball.velocity[0]=-ball.velocity[0]

	if ball.rect.x<=0:
		scoreB+=1
		ball.velocity[0]=-ball.velocity[0]
		
	if ball.rect.y>=490:
		ball.velocity[1]=-ball.velocity[1]

	if ball.rect.y<=0:
		ball.velocity[1]=-ball.velocity[1]


	if pygame.sprite.collide_mask(ball,paddleA) or pygame.sprite.collide_mask(ball,paddleB):
		ball.bounce()

	

	print(scoreA)
	print(scoreB)
	all_sprites_list.update()
	screen.fill(black) 
	show_score_A(100,100)
	show_score_B(100,200)             #Beginning  and the end
	pygame.draw.line(screen,hot_ponk,(349,0),(349,500),5) #Drawing a line
	all_sprites_list.draw(screen)
	pygame.display.flip() #Update the screen with what you've drawn
	clock.tick(60)

	


pygame.quit()
