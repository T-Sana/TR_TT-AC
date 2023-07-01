from outils.souris import souris as s
from TR_transitions import *
from outils.cvt import *
from TR_VARS import *

def img(im=ouvre_image(f'{dir}/{imgs}/{n_img1}'), j1=j1, j2=j2):
    j1.dessine(im)
    j2.dessine(im)
    return(im)

def carte1(j1=j1, j2=j2):
    while True:
        wk = souris_sur_image(img(ouvre_image(f'{dir}/{imgs}/{n_img1}'), j1, j2), s.get_souris, nf, 100, non)
        if wk == 27: quitter()
        elif wk != -1: print(wk)
        if wk == key_arr_u: ## Flèche du haut ##
            j2.deplace([0, -50])
        elif wk == key_arr_d: ## Flèche du Bas ##
            j2.deplace([0, 50])
        elif wk == key_arr_r: ## Flèche droite ##
            j2.deplace([50, 0])
        elif wk == key_arr_l: ## Flèche gauche ##
            j2.deplace([-50, 0])
        elif wk == key_w: ## W ##
            j1.deplace([0, -50])
        elif wk == key_s: ## S ##
            j1.deplace([0, 50])
        elif wk == key_d: ## D ##
            j1.deplace([50, 0])
        elif wk == key_a: ## A ##
            j1.deplace([-50, 0])
        '''if s.pos != s.dehors:
            a = angleEntrePoints(j1.pos, s.pos)
            j1.deplace(coosCercle([0, 0], 0.5*dist(j1.pos, s.pos), a))
            s.pos = s.dehors'''