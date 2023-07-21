from TR_transitions import *
from Depandances.Outils.cvt import *
from Depandances.Outils.paths__names__etc import *
from TR_imageaison import img_cart2; img_cart2()

def img(im, j1, j2):
    j1.dessine(im)
    j2.dessine(im)
    return(im)
def deplace_js(wk, j1, j2, cam=[0, 0]):
    cb = 45
    match wk:
        case j1.k_h:
            j1.deplace([0, -cb])
        case j1.k_b:
            j1.deplace([0, cb])
        case j1.k_d:
            j1.deplace([cb, 0])
        case j1.k_g:
            j1.deplace([-cb, 0])
        case j2.k_h:
            j2.deplace([0, -cb])
        case j2.k_b:
            j2.deplace([0, cb])
        case j2.k_d:
            j2.deplace([cb, 0])
        case j2.k_g:
            j2.deplace([-cb, 0])
    return(cam)

def carte1(j1=j1, j2=j2):
    while True:
        wk = montre(img(ouvre_image(f'{dir}/{imgs_path}/{n_img1}'), j1, j2), nf, 100, non)
        if wk == 27: quitter()
        elif wk != -1:
            deplace_js(wk, j1, j2)
            print(wk)
def carte2(j1=j1, j2=j2):
    dst = 400
    dst2 = 400
    cam = [0, 0]
    while True:
        if j1.pos[1] > cam[1] + haut/3*2 or j2.pos[1] > cam[1] + haut/3*2:
            if j1.pos[1] < cam[1] + haut/3+dst or j2.pos[1] < cam[1] + haut/3+dst: pass
            else: cam[1] += dst
        elif j1.pos[1] < cam[1] + haut/3 or j2.pos[1] < cam[1] + haut/3:
            if j1.pos[1] > cam[1] + haut/3*2-dst or j2.pos[1] > cam[1] + haut/3*2-dst: pass
            else: cam[1] -= dst
        if j1.pos[0] > cam[0] + long/4*3 or j2.pos[0] > cam[0] + long/4*3:
            if j1.pos[0] < cam[0] + long/4+dst2 or j2.pos[0] < cam[0] + long/4+dst2: pass
            else: cam[0] += dst2
        elif j1.pos[0] < cam[0] + long/4 or j2.pos[0] < cam[0] + long/4:
            if j1.pos[0] > cam[0] + long/4*3-dst2 or j2.pos[0] > cam[0] + long/4*3-dst2: pass
            else: cam[0] -= dst2
        if cam[1] < 0: cam[1] = 0
        elif cam[1] > haut: cam[1] = haut
        if cam[0] < 0: cam[0] = 0
        elif cam[0] > 0: cam[0] = 0
        j1.ou_peut_etre.pop()
        j2.ou_peut_etre.pop()
        hg_bd_img2 = [cam, [long, cam[1]+haut]]
        j1.ou_peut_etre.append(hg_bd_img2)
        j2.ou_peut_etre.append(hg_bd_img2)
        wk = montre(img_part(img(ouvre_image(f'{dir}/{imgs_path}/{n_img2}'), j1, j2), cam), nf, 100, non)
        if wk == 27: quitter()
        elif wk != -1:
            cam = deplace_js(wk, j1, j2, cam)
            print(j1.ou_peut_etre)
            print(j2.ou_peut_etre)
            print(cam, wk)
            print(cam[1] + haut/3, cam[1] + haut/3*2)
            print(j1.pos, j2.pos)