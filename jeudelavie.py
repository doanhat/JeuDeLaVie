###########################################################
#                                                         #
#                    programmation                        #
#                       Python                            #
#                                                         #
#            François Marès & Nhat-Minh Doan              #
#                                                         #
###########################################################

#---------------------------------------------------------#
#                        packages                         #
#---------------------------------------------------------#
import tkinter
import random
import time

#---------------------------------------------------------#
#                  variables globales                     #
#---------------------------------------------------------#

#---------------------------------- dimensions du damier
jeuWidth=800
jeuHeight=600
jeuTaille=100
#---------------------------------- paramètres du jeu
jeuProba=50
jeuVitesse=5000
#---------------------------------- flags
flag=0 # continuer ?

#---------------------------------- Damiers
damier =        		[[0] * jeuTaille for i in range(jeuTaille)]
damierRectangles =      [[0] * jeuTaille for i in range(jeuTaille)]
damierVoisins = 		[[0] * jeuTaille for i in range(jeuTaille)]

#---------------------------------------------------------#
#                        Fonctions                        #
#---------------------------------------------------------#

#---------------------------------- modifications du damier
def nbrVoisins(i,j):
	count=0
	for a in range(i-1,i+2):
		for b in range (j-1,j+2):
			if (a<0):
				a=jeuTaille-1
			elif (a==jeuTaille):
				a=0
			if (b<0):
				b=jeuTaille-1
			elif (b==jeuTaille):
				b=0
			if (damier[a][b]==1):
				count+=1
	if (damier[i][j]==1):
		count-=1					
	return count

def Genetation():
	global damier
	global damierVoisins
	
	for i in range(jeuTaille):
			for j in range (jeuTaille):
				damierVoisins[i][j]=nbrVoisins(i,j)

	for i in range(jeuTaille):
		for j in range (jeuTaille):
			nbr_voisins=damierVoisins[i][j]
			if (damier[i][j]==1):
				if (nbr_voisins<=1 or nbr_voisins>=4):
					damier[i][j]=0
			else:
				if (nbr_voisins==3):
					damier[i][j]=1

#---------------------------------- Affichage
def Afficher():
	for i in range(jeuTaille):
		for j in range (jeuTaille):
			if (damier[i][j]==1):
				canvas.delete(damierRectangles[i][j])
				damierRectangles[i][j]=canvas.create_rectangle(jeuWidth/jeuTaille*j, jeuHeight/jeuTaille*i, jeuWidth/jeuTaille*(j+1), jeuHeight/jeuTaille*(i+1), fill='red', outline="black", width=1)
			elif(damier[i][j]==0):
				canvas.delete(damierRectangles[i][j])
				damierRectangles[i][j]=canvas.create_rectangle(jeuWidth/jeuTaille*j, jeuHeight/jeuTaille*i, jeuWidth/jeuTaille*(j+1), jeuHeight/jeuTaille*(i+1), fill='white', outline="black", width=1)

#---------------------------------- fonctions des boutons
def Propos():
	top=tkinter.Toplevel()
	top.geometry("300x100+500+350")
	top.title("Bienvenue!")
	texte="SR01-TP3\n11/01/2019\nProduit sans licence\nPython version 3.7.1/3.5.2 sur Windows 10\nPar DOAN Nhat-Minh et MARES François"
	tkinter.Label(top,text=texte).pack()

def Continuer():
	Genetation()
	Afficher()
	if flag>0:
		fenetre.after(jeuVitesse, Continuer)

def Lancer():
	global flag
	if damier == [[0] * jeuTaille for i in range(jeuTaille)]:
		flag=0
	else:	
		flag=1
		fenetre.after(jeuVitesse,Continuer)

def Initialiser():
	Arreter()
	canvas.delete(damierRectangles)
	global flag
	flag=0
	for i in range(jeuTaille):
		for j in range (jeuTaille):
			k=random.randrange(0,101)
			if k<=jeuProba:
				damier[i][j]=1
			elif k>jeuProba:
				damier[i][j]=0
	Afficher()

def Arreter():
	global flag
	global damierRectangles
	flag=0
	canvas.delete(damierRectangles)

#---------------------------------- fonctions des curseurs
def Taille(val):
	global jeuTaille
	jeuTaille=int(val)

def Proba(val):
	global jeuProba
	jeuProba=int(val)

def Vitesse(val):
	global jeuVitesse
	jeuVitesse=5010-int(val)

#---------------------------------------------------------#
#                            GUI                          #
#---------------------------------------------------------#

#--------------------------------------------------------- Fenêtre principale
fenetre = tkinter.Tk()
fenetre.title("SR01 Jeu de la vie")
fenetre.configure(width=jeuWidth+0,height=jeuHeight+200)
fenetre.resizable(width=False,height=False) 
#--------------------------------------------------------- Canevas
canvas = tkinter.Canvas(fenetre, width=jeuWidth, height=jeuHeight,bg = "white")
canvas.pack(side=tkinter.LEFT)

#--------------------------------------------------------- Boutons
tkinter.Button( fenetre,text = 'Lancer',font='helvetica',fg='DeepSkyBlue4',
                bg='light gray',height = 1,width = 15,relief='raised',
                command=Lancer).pack(side=tkinter.TOP)

tkinter.Button( fenetre,text = 'Arreter',font='helvetica',fg='DeepSkyBlue4',
                bg='light gray',height = 1,width = 15,relief='raised',
                command = Arreter).pack(side=tkinter.TOP)

tkinter.Button( fenetre,text = 'Initialiser',font='helvetica',fg='DeepSkyBlue4',
                bg='light gray',height = 1,width = 15,relief='raised',
                command = Initialiser).pack(side=tkinter.TOP)

tkinter.Button( fenetre,text = 'A propos',font='helvetica',fg='DeepSkyBlue4',
                bg='light gray',height = 1,width = 15,relief='raised',
                command = Propos).pack(side=tkinter.TOP)

tkinter.Button( fenetre,text = 'Quitter',font='helvetica',fg='DeepSkyBlue4',
                bg='light gray',height = 1,width = 15,relief='raised',
                command = fenetre.destroy).pack(side=tkinter.BOTTOM)

#--------------------------------------------------------- Curseurs
VitesseScale=tkinter.Scale(fenetre,label='Vitesse',font=('helvetica','10'),
                            fg='DeepSkyBlue4',troughcolor='gray88',
                            orient=tkinter.HORIZONTAL,width='20',from_=1,
                            to=5000, command=Vitesse)
VitesseScale.pack(side=tkinter.BOTTOM)
VitesseScale.set(2500)

VieScale=tkinter.Scale(fenetre,label='% de Vie',font=('helvetica','10'),
                        fg='DeepSkyBlue4',troughcolor='gray88',
                        orient=tkinter.HORIZONTAL,width='20',command=Proba)
VieScale.pack(side=tkinter.BOTTOM)
VieScale.set(50)

TailleScale=tkinter.Scale(fenetre,label='Taille de la grille',font=('helvetica','10'),
                            fg='DeepSkyBlue4', troughcolor='gray88',
                            from_=5, to=100,
                            orient=tkinter.HORIZONTAL,width='20',command=Taille)
TailleScale.pack(side=tkinter.BOTTOM)
TailleScale.set(100)

fenetre.mainloop()
