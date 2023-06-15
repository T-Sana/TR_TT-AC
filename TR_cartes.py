from outils.souris import souris as s
from TR_anim_debut import img as imag
from TR_transitions import *
from outils.cvt import *
from TR_VARS import *

def carte1(j1=j1, j2=j2, cc=0):
    while True:
        wk = souris_sur_image(imag(j1=j1, j2=j2, pt=cc), s.get_souris, nf, 100, non)
        #print(j1.pos)
        if wk == 27: quitter()
        elif wk != -1: print(wk)
        if wk == 2490368: ## Flèche du haut ##
            j2.deplace([0, -50])
        elif wk == 2621440: ## Flèche du Bas ##
            j2.deplace([0, 50])
        elif wk == 2555904: ## Flèche droite ##
            j2.deplace([50, 0])
        elif wk == 2424832: ## Flèche gauche ##
            j2.deplace([-50, 0])
        if s.pos != s.dehors:
            a = angleEntrePoints(j1.pos, s.pos)
            j1.deplace(coosCercle([0, 0], 0.5*dist(j1.pos, s.pos), a))
            s.pos = s.dehors