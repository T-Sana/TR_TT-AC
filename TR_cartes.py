from outils.souris import souris as s
from TR_transitions import *
from outils.cvt import *
from TR_vars import *
from TR_imageaison import img_cart2; img_cart2()

def img(im, j1, j2):
    j1.dessine(im)
    j2.dessine(im)
    return(im)
def deplace_js(wk, j1, j2, cam=[0, 0]):
    match wk:
        case j1.k_h:
            j1.deplace([0, -50])
        case j1.k_b:
            j1.deplace([0, 50])
        case j1.k_d:
            j1.deplace([50, 0])
        case j1.k_g:
            j1.deplace([-50, 0])
        case j2.k_h:
            j2.deplace([0, -50])
        case j2.k_b:
            j2.deplace([0, 50])
        case j2.k_d:
            j2.deplace([50, 0])
        case j2.k_g:
            j2.deplace([-50, 0])
    
    return(cam)

def carte1(j1=j1, j2=j2):
    while True:
        wk = souris_sur_image(img(ouvre_image(f'{dir}/{imgs}/{n_img1}'), j1, j2), s.get_souris, nf, 100, non)
        if wk == 27: quitter()
        elif wk != -1:
            deplace_js(wk, j1, j2)
            print(wk)
def carte2(j1=j1, j2=j2):
    dst = 400
    while True:
        cam = [0, 0]
        if j1.pos[1] > cam[1] + haut/3*2:
            cam[1] += dst
        elif j2.pos[1] > cam[1] + haut/3*2:
            cam[1] += dst
        elif j1.pos[1] < cam[1] + haut/3:
            cam[1] -= dst
        elif j2.pos[1] < cam[1] + haut/3:
            cam[1] -= dst
        if cam[1] < 0: cam[1] = 0
        elif cam[1] > haut: cam[1] = haut
        j1.ou_peut_etre.pop()
        j2.ou_peut_etre.pop()
        hg_bd_img2 = [cam, [long, cam[1]+haut]]
        j1.ou_peut_etre.append(hg_bd_img2)
        j2.ou_peut_etre.append(hg_bd_img2)
        wk = souris_sur_image(img_part(img(ouvre_image(f'{dir}/{imgs}/{n_img2}'), j1, j2), cam), s.get_souris, nf, 100, non)
        if wk == 27: quitter()
        elif wk != -1:
            cam = deplace_js(wk, j1, j2, cam)
            print(wk)
#carte2(j1, j2)