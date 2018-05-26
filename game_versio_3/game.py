#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import sys
import pygame
import time
from pygame.locals import *
from level import init_level, load_level

# Constantes 

W = 1024
H = 640
speed_down = 0
speed_up = 0
speed = 0
WHITE = (255,255,255)
GREEN = (64,239,20)
BLUE = (22,27,173)
walls = []
enemies = []
lvl = 1
level = load_level(1)
xE = 2
damage = 192
fuel = 192
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Flying Square")
clock = pygame.time.Clock()

# Clases
# ---------------------------------------------------------------------
class Player(object):
	def __init__(self,imagen,transp,posX,posY):
		self.image = load_image(imagen, transp)
		self.rect = self.image.get_rect()
		self.rect.centerx = posX
		self.rect.centery = posY
	
	def Mover_Nave(self,x,y):
		
		global damage
		
		self.rect.centerx += x
		self.rect.centery += y
		
		for wall in walls:
			if self.rect.colliderect(wall.rect):
				damage -= 0.5
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

def text_objects(text, font,):
	
	textSurface = font.render(text, True, (0,0,0))
	
	return textSurface, textSurface.get_rect()

def message(text):
	largeText = pygame.font.Font("freesansbold.ttf",115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((W/2),(H/2))
	screen.fill(WHITE)
	screen.blit(TextSurf, TextRect)
	pygame.display.update()
	time.sleep(5)
	Init(lvl)
	

def Init(lvl):
	global W,H,speed_down,speed_up,speed_x,walls,enemies,level,xE,damage,fuel
	speed_down = 0
	speed_up = 0
	speed_x = 0
	walls = []
	enemies = []
	level = load_level(lvl)
	damage = 192
	fuel = 192
	main()

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
					xE = -2
				elif xE < 0: 
					enemy.rect.left = wall.rect.right
					xE = 2

def Contador():
	
	global damage, fuel
	
	vida = pygame.Rect(32, 32, damage, 16)
	energia = pygame.Rect(32, 48, fuel, 16)
	pygame.draw.rect(screen, (255,0,0), vida)
	pygame.draw.rect(screen, (249,218,4), energia)

def Draw_Update(enemy, end_rect, player, key, fire_bottom, fire_left, fire_right, fuel):
	screen.fill(WHITE)
	for wall in walls:
		pygame.draw.rect(screen, (0, 0, 0), wall.rect)
	pygame.draw.rect(screen, GREEN, end_rect)
	for i in enemies:
		screen.blit(enemy, i.rect)
	screen.blit(player.image, player.rect)
	if key[K_UP] and fuel != 0:
		screen.blit(fire_bottom, (player.rect.x + 5.5, player.rect.y + 48))
	if key[K_LEFT] and fuel != 0:
		screen.blit(fire_right, (player.rect.x + 47, player.rect.y + 9))
	if key[K_RIGHT] and fuel != 0:
		screen.blit(fire_left, (player.rect.x - 56, player.rect.y + 10))

def boton(xB,yB): # Funcion encargada de los botones Start Stop
	
	empezar = pygame.image.load("images/start.png")
	empezar1 = pygame.image.load("images/start1.png")
	quitar = pygame.image.load("images/stop.png")
	quitar1 = pygame.image.load("images/stop1.png")

	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	
	if 250 + 152 > mouse[0] > 250 and 400 + 45 > mouse [1] > 400:
		screen.blit(empezar,(250, 400))
		if click[0] == 1:
			main()
	else:
		screen.blit(empezar1,(250, 400))
	
	if 550 + 152 > mouse[0] > 550 and 400 + 45 > mouse [1] > 400:
		screen.blit(quitar1,(550, 400))
		if click[0] == 1:
			pygame.quit()
			quit()
	else:
		screen.blit(quitar,(550, 400))

def Intro_Juego(): # Funcion introduccion
	
	xB = 0
	yB = 0
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		

		screen.fill(WHITE)
		largeText = pygame.font.Font("freesansbold.ttf",115)
		TextSurf, TextRect = text_objects("SQUARE IT UP", largeText)
		TextRect.center = ((W/2),(H/3))
		screen.blit(TextSurf, TextRect)
		
		boton(xB,yB)
		
		pygame.display.update()
		clock.tick(15)

# ---------------------------------------------------------------------

def main():

	player = Player("images/jugador.png",False,100,120)
	fire_bottom = load_image("images/fire_b.png", False)
	fire_left = load_image("images/fire_l.png", False)
	fire_right = load_image("images/fire_r.png", False)
	enemy = load_image("images/enemy.png", False)
	end_rect = init_level(level,Wall,Enemy)
	
	global fuel, speed_down, speed_up, lvl

	while True:
		for eventos in pygame.event.get():
			if eventos.type == QUIT:
				sys.exit(0)
	
		Move_Enemy(player)
		key = pygame.key.get_pressed()
	
		if key[K_UP] and fuel!=0:
			player.Mover_Nave(0, -speed_up)
			fuel -= 0.05
			if speed_up <= 4:
				speed_up += 0.1
				speed_down -= 0.1
		else:
			player.Mover_Nave(0, speed_down)
			if speed_down <= 3:
				speed_down += 0.1
				speed_up -= 0.1
		
		if key[K_RIGHT] and fuel!=0:
			player.Mover_Nave(1, 0)
			fuel -= 0.05
		if key[K_LEFT] and fuel!=0:
			player.Mover_Nave(-1, 0)
			fuel -= 0.05
		
		if damage==1:
			message("GAME OVER")
		if fuel <= 0:
			fuel = 0
		
		if player.rect.colliderect(end_rect):
			if lvl == 2:
				lvl = 1
			else:
				lvl += 1
			Init(lvl)
		
		Draw_Update(enemy, end_rect, player, key, fire_bottom, fire_left, fire_right, fuel)
		
		Contador()
		
		pygame.display.flip()
		clock.tick(60)

	return
	
if __name__ == '__main__':
	pygame.init()
	Intro_Juego()