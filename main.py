import pygame,sys

class Voiture(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.voiture = pygame.image.load('Voiture.png')
		self.image = self.voiture
		self.rect = self.image.get_rect(center = (640,360))
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
			self.rect.center += self.forward * 5

	def update(self):
		self.set_rotation()
		self.get_rotation()
		self.accelerate()


pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
bg_track = pygame.image.load('Circuit.png')

Voiture = pygame.sprite.GroupSingle(Voiture())

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_d: Voiture.sprite.direction += 1
			if event.key == pygame.K_q: Voiture.sprite.direction -= 1
			if event.key == pygame.K_z: Voiture.sprite.active = True

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_d: Voiture.sprite.direction -= 1
			if event.key == pygame.K_q: Voiture.sprite.direction += 1 
			if event.key == pygame.K_z: Voiture.sprite.active = False

	screen.blit(bg_track,(0,0))
	Voiture.draw(screen)
	Voiture.update()
	pygame.display.update()
	clock.tick(300000)