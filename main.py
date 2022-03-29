from cmath import rect
from email.mime import image
from tkinter import CENTER
from turtle import position
import pygame,sys
from random import randint

counter = 3

score1 = 0
score2 = 0

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
			if self.rect.center == pigeonPosition :
				score1 += 1
				self.rect.center -= self.forward * 5

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

width = 1280
height = 720

screen = pygame.display.set_mode((width,height))
bg_track = pygame.image.load('Circuit.png')

Voiture = pygame.sprite.GroupSingle(Voiture())
Voiture2 = pygame.sprite.GroupSingle(Voiture2())

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 100)
text = font.render(str(counter), True, (0, 128, 0))

timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)

textVoiture = font.render(str(score1), True, (128, 0, 0))
textVoiture2 = font.render(str(score2), True, (0, 0, 128))

pigeon = pygame.image.load('pigeon.png')
pigeon = pygame.transform.scale(pigeon, (50, 50))

pigeonPositionx = randint(1,1279)
pigeonPositiony = randint(1,719)

pigeonPosition = (pigeon.get_rect().centerx, pigeon.get_rect().centery)


run = True,
while run:
	clock.tick(60)
	screen.blit(bg_track,(0,0))
	if counter != 0 : 
		if pigeonPositionx != 0 and pigeonPositiony != 0 :
			screen.blit(pigeon, (pigeonPositionx,pigeonPositiony))
		else :
			pigeonPositionx = randint(1,1279)
			pigeonPositiony = randint(1,719)
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
				if event.key == pygame.K_d: Voiture.sprite.direction += 1
				if event.key == pygame.K_q: Voiture.sprite.direction -= 1
				if event.key == pygame.K_z: Voiture.sprite.active = True

				if event.key == pygame.K_m: Voiture2.sprite.direction += 1
				if event.key == pygame.K_k: Voiture2.sprite.direction -= 1
				if event.key == pygame.K_o: Voiture2.sprite.active = True

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_d: Voiture.sprite.direction -= 1
				if event.key == pygame.K_q: Voiture.sprite.direction += 1 
				if event.key == pygame.K_z: Voiture.sprite.active = False

				if event.key == pygame.K_m: Voiture2.sprite.direction -= 1
				if event.key == pygame.K_k: Voiture2.sprite.direction += 1
				if event.key == pygame.K_o: Voiture2.sprite.active = False

		else :
			Voiture.sprite.direction += 0
			Voiture2.sprite.direction += 0
			Voiture2.sprite.active = False
			Voiture.sprite.active = False

			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_r: 
					pigeonPositionx = 0
					pigeonPositiony = 0
					counter = 30
					timer_event = pygame.USEREVENT+1
					pygame.time.set_timer(timer_event, 1000)
					
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_r: 
					counter = 30
					timer_event = pygame.USEREVENT+1
					pygame.time.set_timer(timer_event, 1000)

	Voiture.draw(screen)
	Voiture.update()

	Voiture2.draw(screen)
	Voiture2.update()
	

	screen.blit(text, (640,1))
	screen.blit(textVoiture, (320,1))
	screen.blit(textVoiture2, (960,1))

	pygame.display.update()
	