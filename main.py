from cmath import rect
from email.mime import image
from tkinter import CENTER
from turtle import position
import pygame,sys
from random import randint

counter = 30

score1 = 0
score2 = 0

victoireR = "La voiture rouge à gagner appuyer sur R pour recommencer"
victoireB = "La voiture bleu à gagner appuyer sur R pour recommencer"
égalité = "C'est une égalité appuyer sur R pour recommencer"

class Pigeon(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.pigeon = pygame.image.load('pigeon.png')
		self.pigeon = pygame.transform.scale(self.pigeon, (50, 50))
		self.image = self.pigeon	
		self.rect = self.image.get_rect(center = (randint(1,1279),randint(1,719)))
		self.active = False


class Voiture(pygame.sprite.Sprite):
	def __init__(self):
		widthVoiture = 630
		heightVoiture = 360
		super().__init__()
		self.voiture = pygame.image.load('Voiture.png')
		self.image = self.voiture
		self.rect = self.image.get_rect(center = (widthVoiture,heightVoiture))
		self.angle = 0
		self.rotation = 3
		self.direction = 0
		self.forward = pygame.math.Vector2(0,-1)
		self.active = False

	def set_rotation(self):
		if self.direction == 1:
			self.angle -= self.rotation
		if self.direction == -1:
			self.angle += self.rotation

		self.image = pygame.transform.rotozoom(self.voiture,self.angle,0.25)
		self.rect = self.image.get_rect(center = self.rect.center)

	def get_rotation(self):
		if self.direction == 1:
			self.forward.rotate_ip(self.rotation)
		if self.direction == -1:
			self.forward.rotate_ip(-self.rotation)

	def accelerate(self):
		if self.active:
			if counter == 0 :
				self.rect.centerx = 630
				self.rect.centery = 360

			if 0 < self.rect.centerx < 1280 and 0 < self.rect.centery < 720 :
				self.rect.center += self.forward * 5
			else :
				if self.rect.centerx == self.rect.centerx and self.rect.centery >= 721 :	
					self.rect.centery = 0
				if self.rect.centerx == self.rect.centerx and self.rect.centery <= -1 :
					self.rect.centery = 720
				if self.rect.centerx >= 1281 and self.rect.centery == self.rect.centery :
					self.rect.centerx = 0
				if self.rect.centerx <= -1 and self.rect.centery == self.rect.centery :
					self.rect.centerx = 1280
				else :
					self.rect.center += self.forward * 5
			
	def update(self):
		self.set_rotation()
		self.get_rotation()
		self.accelerate()

class Voiture2(pygame.sprite.Sprite):
	def __init__(self):
		widthVoiture = 650
		heightVoiture = 360
		super().__init__()
		self.voiture = pygame.image.load('Voiture2.png')
		self.image = self.voiture
		self.rect = self.image.get_rect(center = (widthVoiture,heightVoiture))
		self.angle = 0
		self.rotation = 3
		self.direction = 0
		self.forward = pygame.math.Vector2(0,-1)
		self.active = False

	def set_rotation(self):
		if self.direction == 1:
			self.angle -= self.rotation
		if self.direction == -1:
			self.angle += self.rotation

		self.image = pygame.transform.rotozoom(self.voiture,self.angle,0.25)
		self.rect = self.image.get_rect(center = self.rect.center)

	def get_rotation(self):
		if self.direction == 1:
			self.forward.rotate_ip(self.rotation)
		if self.direction == -1:
			self.forward.rotate_ip(-self.rotation)

	def accelerate(self):
		if self.active:
			if counter == 0 :
				self.rect.centerx = 650
				self.rect.centery = 360
			if 0 < self.rect.centerx < 1280 and 0 < self.rect.centery < 720 :
				self.rect.center += self.forward * 5
			else :
				if self.rect.centerx == self.rect.centerx and self.rect.centery >= 721 :	
					self.rect.centery = 0
				if self.rect.centerx == self.rect.centerx and self.rect.centery <= -1 :
					self.rect.centery = 720
				if self.rect.centerx >= 1281 and self.rect.centery == self.rect.centery :
					self.rect.centerx = 0
				if self.rect.centerx <= -1 and self.rect.centery == self.rect.centery :
					self.rect.centerx = 1280
				else : 
					self.rect.center += self.forward * 5

	def update(self):
		self.set_rotation()
		self.get_rotation()
		self.accelerate()


		

pygame.init()
pygame.mixer.init()

file = "theme.mp3"
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)

file2 = pygame.mixer.Sound("pigeon.mp3")

width = 1280
height = 720

screen = pygame.display.set_mode((width,height))
bg_track = pygame.image.load('Circuit.png')

voiture = pygame.sprite.GroupSingle(Voiture())
voiture2 = pygame.sprite.GroupSingle(Voiture2())
pigeon = pygame.sprite.GroupSingle(Pigeon())

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 100)
font2 = pygame.font.SysFont(None, 60)
text = font.render(str(counter), True, (0, 128, 0))

textVoiture = font.render(str(score1), True, (128, 0, 0))
textVoiture2 = font.render(str(score2), True, (0, 0, 128))

timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)

run = True,
while run:
	clock.tick(60)
	screen.blit(bg_track,(0,0))
	if counter != 0 : 
		pigeon.draw(screen)
		if pygame.sprite.groupcollide(pigeon, voiture, True, False):
			file2.play()
			score1 += 1
			textVoiture = font.render(str(score1), True, (128, 0, 0))
			pigeon = pygame.sprite.GroupSingle(Pigeon())
			pigeon.draw(screen)
		if pygame.sprite.groupcollide(pigeon, voiture2, True, False):
			file2.play()
			score2 += 1
			textVoiture2 = font.render(str(score2), True, (0, 0, 128))
			pigeon = pygame.sprite.GroupSingle(Pigeon())
			pigeon.draw(screen)
	else :
		if score1 < score2 :
			textVictoire = font2.render(str(victoireB), True, (0, 0, 128))
			screen.blit(textVictoire, (0,360))
		elif score2 < score1 :
			textVictoire = font2.render(str(victoireR), True, (128, 0, 0))
			screen.blit(textVictoire, (0,360))
		else :
			textVictoire = font2.render(str(égalité), True, (0, 128, 0))
			screen.blit(textVictoire, (0,360))
		
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == timer_event:
			counter -= 1
			text = font.render(str(counter), True, (0,128,0))
			if counter == 0:
				pygame.time.set_timer(timer_event, 0)
				
		if counter != 0 :
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_d: voiture.sprite.direction += 1
				if event.key == pygame.K_q: voiture.sprite.direction -= 1
				if event.key == pygame.K_z: voiture.sprite.active = True

				if event.key == pygame.K_m: voiture2.sprite.direction += 1
				if event.key == pygame.K_k: voiture2.sprite.direction -= 1
				if event.key == pygame.K_o: voiture2.sprite.active = True

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_d: voiture.sprite.direction -= 1
				if event.key == pygame.K_q: voiture.sprite.direction += 1 
				if event.key == pygame.K_z: voiture.sprite.active = False

				if event.key == pygame.K_m: voiture2.sprite.direction -= 1
				if event.key == pygame.K_k: voiture2.sprite.direction += 1
				if event.key == pygame.K_o: voiture2.sprite.active = False

		else :
			voiture.sprite.direction += 0
			voiture2.sprite.direction += 0
			voiture2.sprite.active = False
			voiture.sprite.active = False	

			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_r: 
					pigeonPositionx = 0
					pigeonPositiony = 0
					counter = 30
					timer_event = pygame.USEREVENT+1
					pygame.time.set_timer(timer_event, 1000)
					
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_r: 
					score1 = 0
					score2 = 0
					textVoiture = font.render(str(score1), True, (128, 0, 0))
					textVoiture2 = font.render(str(score1), True, (128, 0, 0))
					counter = 30
					timer_event = pygame.USEREVENT+1
					pygame.time.set_timer(timer_event, 1000)

	voiture.draw(screen)
	voiture.update()

	voiture2.draw(screen)
	voiture2.update()
	

	screen.blit(text, (640,1))
	screen.blit(textVoiture, (320,1))
	screen.blit(textVoiture2, (960,1))

	pygame.display.update()
	