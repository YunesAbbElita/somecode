#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import sys, pygame
from pygame.locals import *
from level import *

# Constantes
W = 1024
H = 640
speed_down = 0
speed_up = 0
speed_x = 0
WHITE = (255,255,255)
walls = []
level = load_level(1)

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
				if x > 0: # Moving right; Hit the left side of the wall
					self.rect.right = wall.rect.left
				if x  < 0: # Moving left; Hit the right side of the wall
					self.rect.left = wall.rect.right
				if y > 0: # Moving down; Hit the top side of the wall
					self.rect.bottom = wall.rect.top
				if y < 0: # Moving up; Hit the bottom side of the wall
					self.rect.top = wall.rect.bottom

class Wall(object):
	def __init__(self, pos):
		walls.append(self)
		self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
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

# ---------------------------------------------------------------------

def main():

	screen = pygame.display.set_mode((W, H))
	pygame.display.set_caption("Pruebas Pygame")
	clock = pygame.time.Clock()
	player = Player("images/jugador.png",False,100,120)
	enemy = load_image("images/jugador1.png", False)
	
	init_level(level,Wall)
	
	while True:
		for eventos in pygame.event.get():
			if eventos.type == QUIT:
				sys.exit(0)
	
		#Mover la nave
		key = pygame.key.get_pressed()
	
		if key[K_UP]:
			player.Mover_Nave(0, -2)
		else:
			player.Mover_Nave(0, 2)
		
		if key[K_RIGHT]:
			player.Mover_Nave(2, 0)
		elif key[K_LEFT]:
			player.Mover_Nave(-2, 0)
	
		screen.fill(WHITE)
		for wall in walls:
			pygame.draw.rect(screen, (0, 0, 0), wall.rect)
		screen.blit(player.image, player.rect)
		pygame.display.flip()
		clock.tick(60)

	return
	
if __name__ == '__main__':
	pygame.init()
	main()