
def init_level(level,Wall):
	x = y = 0
	for row in level:
		for col in row:
			if col == "W":
				Wall((x, y))
			x += 16
		y += 16
		x = 0
			
def load_level(op):
	if op==1:
		level = [
		"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
		"W                                                              W",
		"W                                                              W",
		"W                       W                                      W",
		"W                       W                                      W",
		"W                       W                                      W",
		"W                       W                                      W",
		"W                                                              W",
		"W                                                              W",
		"W                                                              W",
		"W                                                              W",
		"W                                                       WWWWWWWW",
		"W                                                       WWWWWWWW",
		"W                                                              W",
		"WWWWWWWWW      WWW                                             W",
		"WWWWWWWWW      WWW                                             W",
		"W              WWW                                             W",
		"W              WWW                                             W",
		"W              WWW                                             W",
		"W              WWW                                             W", 
		"W              WWWWWWWWWWWWWWWWWWWWWWWW                        W",
		"W              WWWWWWWWWWWWWWWWWWWWWWWW                        W",
		"W                                                              W",
		"W                                                              W",
		"W                                                              W",
		"W                                                              W",
		"W                                                              W",
		"W                                                              W",
		"W                                                              W",
		"W                                                              W",
		"W                                                              W",
		"W                                                              W",
		"W                                                              W",
		"W                                                              W",
		"W                                                              W",
		"W                                                              W",
		"W              WWW                                             W",
		"W              WWW                                             W",
		"W              WWW                                             W",
		"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
		]
		
		return level