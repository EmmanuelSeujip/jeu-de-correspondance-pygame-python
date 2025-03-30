import pygame,sys,time,random
from pygame.locals import *

# definition de constante
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE
DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'
SQUAREBOX='squarebox'
BOXSIZE=40
ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
PRCPT=0
#selection des formes
def seclectionneur(shape,color,left,top):
	quarter = int(40*0.25) 
	half =int(40*0.5)
	if shape == DONUT:
	    pygame.draw.circle(DISPLAYSURF, color, (left + half, top + half), half - 5)
	    pygame.draw.circle(DISPLAYSURF, BGCOLOR, (left + half, top + half), quarter - 5)
	elif shape == SQUARE:
	    pygame.draw.rect(DISPLAYSURF, color, (left + quarter, top + quarter, BOXSIZE - half, BOXSIZE - half))
	elif shape == DIAMOND:
	    pygame.draw.polygon(DISPLAYSURF, color, ((left + half, top), (left + BOXSIZE - 1, top + half), (left + half, top + BOXSIZE - 1), (left, top + half)))
	elif shape == LINES:
	    for i in range(0, BOXSIZE, 4):
	        pygame.draw.line(DISPLAYSURF, color, (left, top + i), (left + i, top))
	        pygame.draw.line(DISPLAYSURF, color, (left + i, top + BOXSIZE - 1), (left + BOXSIZE - 1, top + i))
	elif shape == OVAL:
	    pygame.draw.ellipse(DISPLAYSURF, color, (left, top + quarter, BOXSIZE, half))
	elif shape== SQUAREBOX:
		pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, 40, BOXSIZE))

def pivot(sens,a,b):
	if sens=='haut':
		b=b-50
	if sens=='bas':
		b=b+50
	if sens=='droite':
		a=a+50
	if sens=='gauche':
		a=a-50
	if sens== 'oblique':
		a=a+50
		b=b+50
	return a,b

#permet de ranger de manier aleatoire les couleurs dans tuples
def placetuple(b,z):
	icone= []
	while len(icone)<= 100:
		for color in z:
			for shape in b :
				icone.append((shape,color))
				icone.append((shape,color))
	icone=icone[0:100]
	random.shuffle(icone)
	return icone


def placeobjet(a):
	change=0
	direction=['haut','gauche','bas','droite']
	x=325
	y=325
	i=j=1
	e=0
	while 1:
		if len(a) >0  :
			while change<4:
				while e<i:
					if len (a)==0:
						break
					seclectionneur(a[0][0],a[0][1],x,y)
					del(a[0])
					e=e+1
					x,y=pivot(direction[change],x,y)
					pygame.display.update()
					pygame.time.wait(20)
				change=change+1
				e=0
		i=i+2
		x,y=pivot('oblique',x,y)
		if change>3:
			change=0
		if len(a)==0:
			break
#creation du systeme de corrresponce d'une systeme classique au case
def correspondance(a,b):
	x=a-75
	y=b-75
	if x<0 or y<0 or a>565 or b>565:
		return (-1,-1)
	elif x>=0 and y>=0 :
		x=x//50
		y=y//50
		return (x,y) 
		
def survol(x,y,fcolor):
	ab=x*50 +70
	ordo=y*50 +70
	if x>=0 and y>=0:
		pygame.draw.rect(DISPLAYSURF,fcolor, (ab,ordo, BOXSIZE + 10, BOXSIZE + 10), 4)
	pygame.display.update()
#fonction permettant de faire le classement classique
def leftTopCoordsOfBox(boxx, boxy):
    # Convert board coordinates to pixel coordinates
    left = boxx * (BOXSIZE + 10) + 75
    top = boxy * (BOXSIZE + 10) + 75
    return (top, left)

def clasementicone(liste):
	cpt1=0
	for x in range(10):
		for y in range(10):
			cardx=leftTopCoordsOfBox(x,y)[0]
			cardy=leftTopCoordsOfBox(x,y)[1]
			seclectionneur(liste[cpt1][0],liste[cpt1][1],cardx,cardy)
			cardx=cardx+50
			cpt1=cpt1+1
		cardy=cardy+50
		cardx=75
		fps.tick(30)
	pygame.display.update()
	
def classementbox(liste,coverage,liste2):
	cpt=0
	for x in range(10):
		for y in range(10):
			cardx=leftTopCoordsOfBox(x,y)[0]
			cardy=leftTopCoordsOfBox(x,y)[1]
			pygame.draw.rect(DISPLAYSURF, BGCOLOR, (cardx, cardy, 50, 50))
			seclectionneur(liste[cpt][0],liste[cpt][1],cardx,cardy)
			# (liste2[cpt]==True or liste2[cpt]==False) and 
			if  liste2[cpt]==False and coverage>=0:
					pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (cardx, cardy, coverage, BOXSIZE))
					pygame.display.update()
			elif liste2[cpt]!= True and liste2[cpt]!=False:
				pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (cardx, cardy, BOXSIZE, BOXSIZE))
			cpt=cpt+1
	pygame.display.update()
	
def revealbox(etat):
	if etat==True:
		for revealx in [50,40,30,20,10,0]:
			classementbox(ic,revealx,ica)
			pygame.display.update()
			pygame.time.wait(40)
	if etat==False:
		classementbox(ic,-1,ica)
def coverbox():
	for revealx in [0,10,20,30,40]:
		classementbox(ic,revealx,ica)
		pygame.display.update()
		pygame.time.wait(10)
def verif(gc,dr):
	if ic[gc]==ic[dr]:
		ica[gc]=ica[dr]=True

	else :
		ica[gc]= ('squarebox', (255, 255, 255))
		ica[dr]= ('squarebox', (255, 255, 255))
def victoire():
	pygame.time.wait(1000)
	DISPLAYSURF.fill(BGCOLOR)
	pygame.display.update()
	font =pygame.font.Font('freesansbold.ttf',80)
	text=font.render("YOU ARE WIN",True,WHITE,BGCOLOR)
	textrect=text.get_rect()
	textrect.center=(340,340)
	DISPLAYSURF.blit(text,textrect)
	pygame.display.update()
	pygame.time.wait(5000)
	main()
	
#debut de l'initiation de la page
def main():
	arg=0
	mouseClicked = False
	global DISPLAYSURF,ica,ic,fps
	fps=pygame.time.Clock()
	pygame.init()
	pygame.display.set_caption('JEU DE CORRESPONDANCE')
	DISPLAYSURF= pygame.display.set_mode((640,640))
	DISPLAYSURF.fill((60,60, 100))
	ic=placetuple(ALLSHAPES,ALLCOLORS)
	clasementicone(ic)
	pygame.time.wait(2000)
	ica=placetuple([SQUAREBOX],[WHITE])
	placeobjet(ica)
	ica=placetuple([SQUAREBOX],[WHITE])
	supx=supy=-1
	cptreveal=gc=dr=0
	DISPLAYSURF.fill((60,60, 100))
	classementbox(ic,-1,ica)
	# bouble de jeu
	while 1:
		for event in pygame.event.get():
			if event.type== QUIT:
				sys.exit()
				pygame.quit()
			if event.type== MOUSEMOTION :				
				mousex,mousey=event.pos
				cordx,cordy=correspondance(mousex,mousey)
				if cordx!=supx or cordy!=supy:
					survol(supx,supy,BGCOLOR)
				survol(cordx,cordy,BLUE)
				supx=cordx
				supy=cordy 
			if event.type==MOUSEBUTTONUP:
				DISPLAYSURF.fill((60,60, 100))
				mousex,mousey=event.pos
				cordx,cordy=correspondance(mousex,mousey)
				if cordx >=0:
					arg=cordx+(cordy*10)
					if ica[arg]!=True:
						ica[arg]=False
						mouseClicked=True
						revealbox(mouseClicked)
						if cptreveal<2:
							gpos=cordx+(cordy*10)
							ica[gpos]=True
							if gc==0:
								gc=gpos
								cptreveal=cptreveal+1
							elif dr==0 and gc!=0 and gc!=gpos:
								dr=gpos
								cptreveal=cptreveal+1
				else :
						classementbox(ic,-1,ica)
			if cptreveal==2:
				verif(gc,dr)
				cptreveal=gc=dr=0
				pygame.time.wait(1000)
				mouseClicked=False
				coverbox()
		if ica.count(True)==len(ica):
			victoire()

		pygame.display.update()
		fps.tick(30)

#lancement du programmme
if __name__ == '__main__':
	main()
print