#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import pygame, time, sys
from pygame.locals import *
from level import init_level, load_level
from time import sleep

# Constantes 
W = 1024
H = 640
speed_y = 0
speed_x = 0
gravity = 0.055
WHITE = (255,255,255)
GREEN = (64,239,20)
GREY = (72,72,72)
BLUE = (22,27,173)
PURPLE = (126,5,123)
walls = []
enemies = []
direction = True
lvl = 1
level = load_level(1)
xE = 2
damage = 192
fuel = 192
pause = False
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Flying Square")
clock = pygame.time.Clock()

############################## CLASES #################################
# ---------------------------------------------------------------------

# Clase del jugador
class Player(object):
  def __init__(self,imagen,transp,posX,posY):
    self.image = load_image(imagen, transp)
    self.rect = self.image.get_rect()
    self.rect.centerx = posX
    self.rect.centery = posY
  
  # Funcion que mueve al jugador
  def Mover_Nave(self,x,y):
    global damage, speed_y, speed_x
    
    self.rect.centerx += x
    self.rect.centery += y
    
    # Bucle que itera sobre la lista muros comprobando las colisiones del jugador con cada muro del mapa
    for wall in walls:
      if self.rect.colliderect(wall.rect):
        # dependiendo de la velocidad se quita una vida o otra
        if speed_x > 5 or speed_y > 5:
          damage -= 20
        elif speed_x > 3 or speed_y > 3:
          damage -= 10
        else:
          damage -= 1
  
        if x > 0: # viene por la izquierda
          self.rect.right = wall.rect.left
          speed_x = 0
        if x < 0: # viene por la derecha
          self.rect.left = wall.rect.right
          speed_x = 0
        if y > 0: # viene por arriba
          self.rect.bottom = wall.rect.top
          speed_y = 0
        if y < 0: # viene por abajo
          self.rect.top = wall.rect.bottom
          speed_y = 0
    
    # Bucle que itera sobre la lista enemigos comprobando las colisiones del jugador con cada enemigo del mapa
    for enemy in enemies:
      if self.rect.colliderect(enemy.rect):
        damage -= 150
        if x > 0: # viene por la izquierda
          self.rect.right = enemy.rect.left
          speed_x = 0
        if x  < 0: # viene por la derecha
          self.rect.left = enemy.rect.right
          speed_x = 0
        if y > 0: # viene por arriba
          self.rect.bottom = enemy.rect.top
          speed_y = 0
        if y < 0: # viene por abajo
          self.rect.top = enemy.rect.bottom
          speed_y = 0

# Clase muro
class Wall(object):
  def __init__(self, pos):
    walls.append(self) # guarda en la lista un muro 
    self.rect = pygame.Rect(pos[0], pos[1], 16, 16) # guarda las cordenadas x,y recibidas por parametro del muero anterior 

# Clase enemigo
class Enemy(object):
  def __init__(self,pos):
    enemies.append(self)
    self.rect = pygame.Rect(pos[0], pos[1], 48, 48)
    
# ---------------------------------------------------------------------
# Funciones
# ---------------------------------------------------------------------
def load_image(filename, transparent=False): # Funcion que carga y convierte imagenes
  try: image = pygame.image.load(filename)
  except pygame.error, message:
    raise SystemExit, message
  if image.get_alpha() is None: # esto soluciona un error de conversion que habia en la funcion original
    image = image.convert()
  else:
    image = image.convert_alpha()
  if transparent:
    color = image.get_at((0,0))
    image.set_colorkey(color, RLEACCEL)
    
  return image

def text_objects(text, font): # funcion que renderiza el texto pasado por parametro con la fuente correspondiente
  textSurface = font.render(text, True, (0,0,0))
  
  return textSurface, textSurface.get_rect()

def message(text): # Funcion mensage, duerme y manda un mensage durante 5 segundos, sirve para el game over en este caso
  largeText = pygame.font.Font("freesansbold.ttf",115)
  TextSurf, TextRect = text_objects(text, largeText)
  TextRect.center = ((W/2),(H/2))
  screen.fill(WHITE)
  screen.blit(TextSurf, TextRect)
  pygame.display.update()
  time.sleep(5)
  Init()

def Init(): # funcion que reinicia las constantes importantes a cada cambio de mapa
  global W,H,speed_y,walls,enemies,level,xE,damage,fuel, speed_x, lvl
  
  speed_y = 0
  walls = []
  enemies = []
  level = load_level(lvl)
  damage = 192
  fuel = 192
  speed_x = 0
  speed_y = 0
  main()

def Move_Enemy(player): # Funcion que mueve al enemigo
  global xE
  
  # este bucle itera sobre la lista enemigos seleccionando todos los enemigos
  for enemy in enemies: 
    enemy.rect.x += xE
    # comprueba colision con los jugadores
    if enemy.rect.colliderect(player.rect):
      if xE > 0: # viene por la derecha
        enemy.rect.right = player.rect.left
      elif xE < 0: # viene por la izquierda
        enemy.rect.left = player.rect.right
    # bucle que itera sobre los muros comprobando colision con los enemigos    
    for wall in walls:
      if enemy.rect.colliderect(wall.rect):
        if xE > 0: # viene por la derecha
          enemy.rect.right = wall.rect.left
          xE = -2
        elif xE < 0: # viene por la izquierda
          enemy.rect.left = wall.rect.right
          xE = 2

def Contador(): # Funcion que imprime los contadores de vida y energia
  global damage, fuel

  vida = pygame.Rect(32, 32, damage, 16)
  energia = pygame.Rect(32, 48, fuel, 16)
  pygame.draw.rect(screen, (255,0,0), vida)
  pygame.draw.rect(screen, (249,218,4), energia)

def unpausa(): # Funcion que detiene la pausa
  global pause

  keys = pygame.key.get_pressed()

  if keys[K_c]:
    pause = False

def pausa(): # Funcion que pausa el juego
  
  # imprime una imagen medio translucida y el mensage "paused"
  pause_img = load_image("images/pausa.png", False)
  screen.blit(pause_img,(0,0))
  font = pygame.font.Font("freesansbold.ttf",115)
  TextSurf = font.render("Paused", True, WHITE)
  TextRect = TextSurf.get_rect()
  TextRect.center = ((W/2),(H/2))
  screen.blit(TextSurf, TextRect)

  while pause: # itera y duerme 1 milisegundo comprobando la funcion unpausa
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
    
    unpausa()
    pygame.display.update()
    time.sleep(0.001)
    clock.tick(15)

def Draw_Update(enemy, end_rect, teleport_rect, player, key, fire_bottom, fire_left, fire_right, fuel, fondo): # Funcion que actualiza la pantalla, dibuja todo
  bloque = load_image("images/bloque.png", False)
  screen.blit(fondo,(0,0)) # imprime el fondo
  
  for wall in walls: # itera dibujando cada bloque
    #pygame.draw.rect(screen, (0, 0, 0), wall.rect)
    screen.blit(bloque,wall.rect)
  
  # imprime los cuadrados de teleport y salida
  pygame.draw.rect(screen, GREEN, end_rect)
  pygame.draw.rect(screen, PURPLE, teleport_rect)
  
  for i in enemies: # itera dibujando los enemigos
    screen.blit(enemy, i.rect)
    
  screen.blit(player.image, player.rect) # imprime al jugador
  
  # imprime la ignicion del jugador
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

  if 250 + 152 > mouse[0] > 250 and 540 + 45 > mouse [1] > 540:
    screen.blit(empezar,(250, 540))
    if click[0] == 1:
      Init()
  else:
    screen.blit(empezar1,(250, 540))

  if 550 + 152 > mouse[0] > 550 and 540 + 45 > mouse [1] > 540:
    screen.blit(quitar1,(560, 535))
    if click[0] == 1:
      pygame.quit()
      quit()
  else:
    screen.blit(quitar,(550, 540))

def Intro_Juego(): # Funcion introduccion al juego
  global gravity, fondo
  
  # cargado de imagenes
  jupiter = load_image("images/jupiter_map.png", False)
  jupiter1 = load_image("images/jupiter_map1.png", False)
  luna = load_image("images/moon_map.png", False)
  luna1 = load_image("images/moon_map1.png", False)
  sol = load_image("images/sun_map.png", False)
  sol1 = load_image("images/sun_map1.png", False)
  tierra = load_image("images/tierra_map.png", False)
  tierra1 = load_image("images/tierra_map1.png", False)
  hole = load_image("images/backhole_map.png", False)
  hole1 = load_image("images/blackhole_map1.png", False)
  back = load_image("images/background.jpg", False)
  keys = load_image("images/keys.png", False)
  pygame.mixer.music.load("sounds/Stay_Inside_Me.wav")
  pygame.mixer.music.play(-1)
  fondo = load_image("images/moon.png", False)
  
  xB = 0
  yB = 0

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
    
    screen.blit(back,(0,0))
    
    mouse = pygame.mouse.get_pos() # proporciona la posicion del raton
    click = pygame.mouse.get_pressed() # devuelve los clicks del raton

    if 30 + 300 > mouse[0] > 30 and 100 + 188 > mouse [1] > 100:
      screen.blit(luna1,(30,100))
      if click[0] == 1:
        gravity = 0.045
    else:
      screen.blit(luna,(30,100))
    
    if 30 + 300 > mouse[0] > 30 and 320 + 188 > mouse [1] > 320:
      screen.blit(tierra1,(30,320))
      if click[0] == 1:
        fondo = load_image("images/tierra.png", False)
        gravity = 0.065
    else:
      screen.blit(tierra,(30,320))
  
    if (W-330) + 300 > mouse[0] > (W-330) and 320 + 188 > mouse [1] > 320:
      screen.blit(hole1,(W-330,320))
      if click[0] == 1:
        fondo = load_image("images/blackhole.png", False)
        gravity = 0.165
    else:
      screen.blit(hole,(W-330,320))
    
    if 362 + 300 > mouse[0] > 362 and 100 + 188 > mouse [1] > 100:
      screen.blit(jupiter1,(362,100))
      if click[0] == 1:
        fondo = load_image("images/jupiter.png", False)
        gravity = 0.095
    else:
      screen.blit(jupiter,(362,100))
    
    if (W-330) + 300 > mouse[0] > (W-330) and 100 + 188 > mouse [1] > 100:
      screen.blit(sol1,(W-330,100))
      if click[0] == 1:
        fondo = load_image("images/sun.png", False)
        gravity = 0.105
    else:
      screen.blit(sol,(W-330,100))
    
    screen.blit(keys,(362,318))
    
    largeText = pygame.font.Font("freesansbold.ttf",50)
    TextSurf, TextRect = text_objects("SQUARE IT UP", largeText)
    TextRect.center = ((W/2),(50))
    screen.blit(TextSurf, TextRect)
    
    boton(xB,yB)
    
    pygame.display.update()
    clock.tick(15)

# ---------------------------------------------------------------------
def main(): # Funcion main del juego

  player = Player("images/jugador.png",False,100,120)
  fire_bottom = load_image("images/fire_b.png", False)
  fire_left = load_image("images/fire_l.png", False)
  fire_right = load_image("images/fire_r.png", False)
  enemy = load_image("images/enemy.png", False)
  end_rect, teleport_rect, tele = init_level(level,Wall,Enemy)
  
  ignicion = pygame.mixer.Sound("sounds/load.wav")
  ignicion.set_volume(0.1)
  
  global fuel, speed_y, speed_x, lvl, gravity, direction, fondo, pause

  while True:
    for eventos in pygame.event.get():
      if eventos.type == QUIT:
        pygame.quit()
        sys.exit(0)

    key = pygame.key.get_pressed() # proporciona las teclas seleccionadas
    
    # comprueba si se pausa el juego
    if key[K_p]:
      pause = True
      ignicion.stop()
      pausa()
    
    # lee las acciones del jugador
    if key[K_UP] and fuel!=0:
      ignicion.play()
      player.Mover_Nave(0, speed_y)
      fuel -= 0.1
      speed_y -= 0.15
    else:
      ignicion.stop()
      player.Mover_Nave(0, speed_y)
      speed_y += gravity
    
    if key[K_RIGHT] and fuel>0:
      ignicion.play()
      fuel -= 0.1
      direction = True
      speed_x += 0.1
      
    if key[K_LEFT] and fuel>0:
      ignicion.play()
      fuel -= 0.1
      direction = False
      speed_x -= 0.1
    
    # mueve al jugador en las direcciones seleccionadas
    if direction == True:
      player.Mover_Nave(speed_x, 0)
    else:
      player.Mover_Nave(speed_x, 0)
    
    # llama a game over en caso de que te quedes sin vida
    if damage<1:
      ignicion.stop()
      message("GAME OVER")
    if fuel <= 0:
      fuel = 0
    
    # comprueba que el jugador lleque a la salida
    if player.rect.colliderect(end_rect):
      if lvl == 9:
        lvl = 1
        Intro_Juego()
      else:
        lvl += 1
      Init()
    
    # comprueba que el jugador toque la entrada de teleport
    if player.rect.colliderect(teleport_rect):
      player.rect.left = tele[0]
      player.rect.bottom = tele[1]
    
    Move_Enemy(player)
    Draw_Update(enemy, end_rect, teleport_rect, player, key, fire_bottom, fire_left, fire_right, fuel, fondo)
    Contador()
    
    pygame.display.flip()
    clock.tick(60)

if __name__ == '__main__':
  pygame.init()
  Intro_Juego()
  main()