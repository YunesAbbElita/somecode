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
				end_rect = pygame.Rect(x, y, 48, 16)
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
		"W              WWW                                             W",
		"W              WWW                                             W",
		"W              WWW      WWWWWWWWWWWWWWWWWWWWWWWWWWW            W",
		"W              WWW      WWW                     WWW            W",
		"W              WWW                              WWW         O  W",
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
		"W                                                              W",
		"W                                                              W",
		"W                                                              W",
		"W                                                              W",
		"W                                                              W",
		"W                                                              W",
		"W                                                              W",
		"W                                                              W",
		"W                                    E                         W",
		"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
		]
	elif op==2:
		level = [
		"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
		"W              WWW                                             W",
		"W              WWW                                             W",
		"W              WWW                                             W",
		"W              WWW                                             W",
		"W              WWW                                             W",
		"W              WWW                                             W",
		"W              WWW                                             W",
		"W              WWW                                             W",
		"W              WWWO               E       WWWWWWWWWw           W",
		"W              WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW                  W",
		"W              WWW                        WWW                  W",
		"W              WWW                        WWW                  W",
		"W              WWW                        WWW                  W",
		"WWWWWWWWW      WWW                        WWW                  W",
		"W              WWW                        WWW                  W",
		"W              WWW                        WWW                  W",
		"W              WWW                        WWW                  W",
		"W              WWW                        WWW       WWWWWWWWWWWW",
		"W              WWW           WWW          WWW                  W", 
		"W              WWW           WWW          WWW                  W",
		"W              WWW           WWW          WWW                  W",
		"W              WWW           WWW          WWW                  W",
		"W              WWW           WWW          WWW                  W",
		"W              WWW           WWW          WWW                  W",
		"W              WWW           WWW          WWW                  W",
		"W              WWW           WWW          WWW                  W",
		"W              WWW           WWW          WWW                  W",
		"W              WWW           WWW          WWW                  W",
		"W              WWW           WWW          WWWWWWWWWWWWW        W",
		"W                            WWW                               W",
		"W                            WWW                               W",
		"W                            WWW                               W",
		"W                            WWW                               W",
		"W                            WWW                               W",
		"W                            WWW                               W",
		"W                            WWW                               W",
		"W                            WWW                               W",
		"W                            WWW                               W",
		"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
		]
	return level