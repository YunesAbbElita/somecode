#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import sys, pygame
from pygame.locals import *
from level import init_level, load_level

# Constantes
W = 1024
H = 640
speed_down = 0
speed_up = 0
speed_x = 0
WHITE = (255,255,255)
GREEN = (64,239,20)
walls = []
enemies = []
level = load_level(1)
xE = 1

# Clases
# ---------------------------------------------------------------------
class Player(object):
	def __init__(self,imagen,transp,posX,posY):
		self.image = load_image(imagen, transp)
		self.rect = self.image.get_rect()
		self.rect.centerx = posX
		self.rect.centery = posY
	
	def Mover_Nave(self,x,y):
		
		self.rect.centerx += x
		self.rect.centery += y
		
		for wall in walls:
			if self.rect.colliderect(wall.rect):
				if x > 0:
					self.rect.right = wall.rect.left
				if x  < 0:
					self.rect.left = wall.rect.right
				if y > 0: 
					self.rect.bottom = wall.rect.top
				if y < 0: 
					self.rect.top = wall.rect.bottom
		for enemy in enemies:
			if self.rect.colliderect(enemy.rect):
				if x > 0: 
					self.rect.right = enemy.rect.left
				if x  < 0: 
					self.rect.left = enemy.rect.right
				if y > 0: 
					self.rect.bottom = enemy.rect.top
				if y < 0: 
					self.rect.top = enemy.rect.bottom

class Wall(object):
	def __init__(self, pos):
		walls.append(self)
		self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
		
class Enemy(object):
	def __init__(self,pos):
		enemies.append(self)
		self.rect = pygame.Rect(pos[0], pos[1], 48, 48)
# ---------------------------------------------------------------------
# Funciones
# ---------------------------------------------------------------------
def load_image(filename, transparent=False):
	try: image = pygame.image.load(filename)
	except pygame.error, message:
		raise SystemExit, message
	if image.get_alpha() is None:
		image = image.convert()
	else:
		image = image.convert_alpha()
	if transparent:
		color = image.get_at((0,0))
		image.set_colorkey(color, RLEACCEL)
	return image

def Move_Enemy(player):
	global xE
	for enemy in enemies:
		enemy.rect.x += xE
		if enemy.rect.colliderect(player.rect):
				if xE > 0:
					enemy.rect.right = player.rect.left
				elif xE  < 0:
					enemy.rect.left = player.rect.right
		for wall in walls:
			if enemy.rect.colliderect(wall.rect):
				if xE > 0: 
					enemy.rect.right = wall.rect.left
					xE = -1
				elif xE < 0: 
					enemy.rect.left = wall.rect.right
					xE = 1
# ---------------------------------------------------------------------

def main():

	screen = pygame.display.set_mode((W, H))
	pygame.display.set_caption("Pruebas Pygame")
	clock = pygame.time.Clock()
	player = Player("images/jugador.png",False,100,120)
	enemy = load_image("images/enemy.png", False)
	
	end_rect = init_level(level,Wall,Enemy)
	
	while True:
		for eventos in pygame.event.get():
			if eventos.type == QUIT:
				sys.exit(0)
	
		Move_Enemy(player)
		key = pygame.key.get_pressed()
	
		if key[K_UP]:
			player.Mover_Nave(0, -2)
		else:
			player.Mover_Nave(0, 2)
		
		if key[K_RIGHT]:
			player.Mover_Nave(2, 0)
		elif key[K_LEFT]:
			player.Mover_Nave(-2, 0)
	
		"""if player.rect.colliderect(end_rect):
			raise SystemExit, "You win!"""
	
		screen.fill(WHITE)
		for wall in walls:
			pygame.draw.rect(screen, (0, 0, 0), wall.rect)
		for i in enemies:
			screen.blit(enemy, i.rect)
		pygame.draw.rect(screen, GREEN, end_rect)
		screen.blit(player.image, player.rect)
		pygame.display.flip()
		clock.tick(60)

	return
	
if __name__ == '__main__':
	pygame.init()
	main()