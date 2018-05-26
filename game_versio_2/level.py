import pygame

def init_level(level,Wall,Enemy):
	x = y = 0
	for row in level:
		for col in row:
			if col == "W":
				Wall((x, y))
			if col == "E":
				Enemy((x, y-32))
			if col == "O":
				end_rect = pygame.Rect(x, y, 16, 16)
			x += 16
		y += 16
		x = 0
	return end_rect

def load_level(op):
	if op==1:
		level = [
		"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
		"W              WWW                                             W",
		"W              WWW                                             W",
		"W              WWW                                             W",
		"W              WWW                                             W",
		"W              WWW                                             W",
		"W              WWW                                             W",
		"W              WWW      WWWWWWWWWWWWWWWWWWWWWWWWWWW            W",
		"W              WWW      WWW                     WWW            W",
		"W              WWW      WWW                     WWW            W",
		"W              WWW      WWW                     WWW            W",
		"W              WWW                              WWW           OW",
		"W              WWW                              WWWWWWWWWWWWWWWW",
		"W              WWW                                             W",
		"WWWWWWWWW      WWW                                             W",
		"W              WWW                                             W",
		"W              WWW                                             W",
		"W              WWW                     W                       W",
		"W              WWW                     W                       W",
		"W              WWW         E           W                       W", 
		"W              WWWWWWWWWWWWWWWWWWWWWWWWW                       W",
		"W                                    WWW                       W",
		"W                                    WWW                       W",
		"W                                    WWW                       W",
		"W                                    WWW                       W",
		"W                                    WWW                       W",
		"W                                    WWW                       W",
		"W                                    WWW                       W",
		"W                                    WWW                       W",
		"WWWWWWWWWWWWWWWWWWWWWWWWWWW          WWW                       W",
		"W                                    WWW                       W",
		"W                                    WWW                       W",
		"W                                    WWW                       W",
		"W                                    WWW                       W",
		"W                                                              W",
		"W                                                              W",
		"W                                                              W",
		"W                                                              W",
		"W                                    E                         W",
		"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
		]
		
		return level