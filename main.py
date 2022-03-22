import pygame,sys

class Voiture(pygame.sprite.Sprite):
	def __init__(self):
		widthVoiture = 640
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
			if self.rect.centerx < 1280 and self.rect.centery < 720 :
				self.rect.center += self.forward * 5
			else :
				self.rect.center -= self.forward * 5
			

	def update(self):
		self.set_rotation()
		self.get_rotation()
		self.accelerate()

class Voiture2(pygame.sprite.Sprite):
	def __init__(self):
		widthVoiture = 640
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
			if -1280 < self.rect.centerx < 1280 and -720 < self.rect.centery < 720 :
				self.rect.center += self.forward * 5
			else :
				self.rect.center -= self.forward * 5

	def update(self):
		self.set_rotation()
		self.get_rotation()
		self.accelerate()

pygame.init()

width = 1280
height = 720

screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
bg_track = pygame.image.load('Circuit.png')

Voiture = pygame.sprite.GroupSingle(Voiture())
Voiture2 = pygame.sprite.GroupSingle(Voiture2())

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
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

	screen.blit(bg_track,(0,0))

	Voiture.draw(screen)
	Voiture.update()

	Voiture2.draw(screen)
	Voiture2.update()

	pygame.display.update()
	clock.tick(300000)