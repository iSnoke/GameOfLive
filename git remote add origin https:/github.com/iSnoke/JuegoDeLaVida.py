#!/usr/bin/python3
import pygame
import time
import os
pygame.init()
pygame.display.set_caption("Juego de la vida")


modo = True
end = False
width, height = 700,700
bg = (0,0,0)
value = 10
cantidad_celdas = int(width/value)
celdas = []
for i in range(0, cantidad_celdas):
	celdas.append([0 for i in range(0,cantidad_celdas+1)])


screen = pygame.display.set_mode((height, width))

def draw_celdas(celdas,color=1):
	if color == 1:
		for x in range(0,cantidad_celdas):
			cx = x*value
			pygame.draw.line(screen,(120,120,120),(cx,0),(cx,700))
			for y in range(0,cantidad_celdas):
				cy = y*value
				pygame.draw.line(screen,(120,120,120),(0,cy),(700,cy))
				if celdas[x][y] == 1:
			                pygame.draw.rect(screen,(120,120,120),(cx,cy,value,value))
	else:
                for x in range(0,cantidad_celdas):
                        cx = x*value
                        pygame.draw.line(screen,(255,255,255),(cx,0),(cx,700))
                        for y in range(0,cantidad_celdas):
                                cy = y*value
                                pygame.draw.line(screen,(255,255,255),(0,cy),(700,cy))
                                if celdas[x][y] == 1:
                                        pygame.draw.rect(screen,(255,255,255),(cx,cy,value,value))



def vecinas(x,y,celdas):
	vecinas = 0
	if celdas[(x-1) % cantidad_celdas ][(y-1) % cantidad_celdas] == 1:
		vecinas += 1
	if celdas[x % cantidad_celdas ][(y-1) % cantidad_celdas] == 1:
		vecinas += 1
	if celdas[(x+1) % cantidad_celdas][(y-1) % cantidad_celdas]:
		vecinas += 1
	if celdas[(x-1) % cantidad_celdas][y % cantidad_celdas]:
		vecinas += 1
	if celdas[(x+1) % cantidad_celdas][y % cantidad_celdas]:
		vecinas += 1
	if celdas[(x-1) % cantidad_celdas][(y+1) % cantidad_celdas]:
		vecinas += 1
	if celdas[x % cantidad_celdas][(y+1) % cantidad_celdas]:
		vecinas += 1
	if celdas[(x+1) % cantidad_celdas ][(y+1) % cantidad_celdas]:
		vecinas +=1


	return vecinas

while not end:

	screen.fill(bg)
	for event in pygame.event.get():
		if event == pygame.QUIT:
			pygame.quit()

		if event.type == pygame.KEYUP: #tecla[pygame.K_SPACE]:
			if modo == False:
				modo = True
			else:
				modo = False
		if modo == True:
			mouse = pygame.mouse.get_pos()
			mx,my = mouse
			mx = int(mx/value)
			my = int(my/value)
			if event.type == pygame.MOUSEBUTTONUP: #or event.button == 3: #or pygame.mouse.get_pressed()[0]:
				if event.button == 3:
					time.sleep(0.1)
				if celdas[mx][my] == 1:
					celdas[mx][my] = 0
				else:
					celdas[mx][my] = 1



	if modo == False:
		time.sleep(0.08)
		generacion = []
		for i in range(0, cantidad_celdas):
			generacion.append([0 for i in range(0,cantidad_celdas+1)])

		cx = 0
		cy = 0
		for x in celdas:
			for y in celdas:
				vecina = vecinas(cx,cy,celdas)
				if vecina >= 3:
					generacion[cx][cy] = 1
				if vecina > 3 or vecina < 2:
					generacion[cx][cy] = 0
				elif celdas[cx][cy] == 1:
					generacion[cx][cy] = 1
				cy += 1
			cx += 1
			cy = 0
		celdas = generacion[:]


	if modo == True:
		draw_celdas(celdas)
	else:
		draw_celdas(celdas,color=0)
		#time.sleep(1)

	pygame.display.update()
