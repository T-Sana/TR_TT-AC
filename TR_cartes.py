from outils.souris import souris as s
from TR_transitions import *
from outils.cvt import *
from TR_vars import *

def img(im=image(), j1=j1, j2=j2):
    j1.dessine(im)
    j2.dessine(im)
    return(im)

def deplace_js(wk, j1=j1, j2=j2):
    match wk:
        case j2.k_h: ## Flèche du haut ##
            j2.deplace([0, -50])
        case j2.k_b: ## Flèche du Bas ##
            j2.deplace([0, 50])
        case j2.k_d: ## Flèche droite ##
            j2.deplace([50, 0])
        case j2.k_g: ## Flèche gauche ##
            j2.deplace([-50, 0])
        case j1.k_h: ## W ##
            j1.deplace([0, -50])
        case j1.k_b: ## S ##
            j1.deplace([0, 50])
        case j1.k_d: ## D ##
            j1.deplace([50, 0])
        case j1.k_g: ## A ##
            j1.deplace([-50, 0])

def carte1(j1=j1, j2=j2):
    while True:
        wk = souris_sur_image(img(ouvre_image(f'{dir}/{imgs}/{n_img1}'), j1, j2), s.get_souris, nf, 100, non)
        if wk == 27: quitter()
        elif wk != -1:
            deplace_js(wk, j1, j2)
            print(wk)
carte1()