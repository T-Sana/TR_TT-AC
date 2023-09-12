from TR_imageaison import *
from TR_transitions import *
from Depandances.Outils.cvt import *
from Depandances.Outils.paths__names__etc import *

def img(im, j1, j2):
    if j1.pos[1] <= j2.pos[1]:
        j1.dessine(im)
        j2.dessine(im)
    else:
        j2.dessine(im)
        j1.dessine(im)
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
def carteVille(j1=j1, j2=j2, numb=0): ## Carte de Img2 ##
    for i in [[[0, 0], [1905, 315]], [[0, 2003], [2000, 2160]]]:
        j1.ou_ne_peut_etre.append(i)
        j2.ou_ne_peut_etre.append(i)
    dst = 400; dst2 = 400; cam = [0, 0]
    echiquier = [[120, 540], [690, 865]]
    ech = [echiquier[0][0]-echiquier[1][0], echiquier[0][1]-echiquier[1][1]] #####
    x_, y_ = abs(ech[0])/9, abs(ech[1])/5
    ous = [[0, 0], [4, 0], [8, 0], [8, 4], [4, 4], [0, 4]]
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
        ### Blocage caméra ###
        if cam[1] < 0: cam[1] = 0
        elif cam[1] > haut: cam[1] = haut
        if cam[0] < 0: cam[0] = 0
        elif cam[0] > long: cam[0] = long
        hg_bd_img2 = [cam, [long, cam[1]+haut]]
        j1.ou_peut_etre[-1] = hg_bd_img2
        j2.ou_peut_etre[-1] = hg_bd_img2
        im = ouvre_image(f'{dir}/{imgs_path}/{n_img2}')
        img_xy_len = [len(im[0]), len(im)]
        for j in joueurs:
            try: j.ou_peut_etre.index([[0, 0], img_xy_len])
            except: j.ou_peut_etre.append([[0, 0], img_xy_len])
        cl1, cl2 = blanc, noir
        for ou in ous:
            dessine_pion(im, (echiquier[0][0]+x_*ou[0], echiquier[0][1]+y_*ou[1]), (echiquier[0][0]+x_*(ou[0]+1), echiquier[0][1]+y_*ou[1]), (echiquier[0][0]+x_*(ou[0]), echiquier[0][1]+y_*(ou[1]+1)), (echiquier[0][0]+x_*(ou[0]+1), echiquier[0][1]+y_*(ou[1]+1)), cl1, cl2, 3)
            cl1, cl2 = cl2, cl1
        ecris(im, 'vs', (echiquier[0][0]+x_*4.5, echiquier[0][1]+y_*2.5), (echiquier[0][0]+x_*4.5, echiquier[0][1]+y_*2.5), 2, rouge, 5)
        imag = img_part(img(im, j1, j2), cam)
        if numb%3 == 0:
            for n in range(len(ous)):
                if ous[n][1] == 0:
                    if ous[n][0] < 8: ous[n] = ous[n][0]+1, ous[n][1]
                    else: ous[n] = ous[n][0], ous[n][1]+1
                elif ous[n][0] == 8:
                    if ous[n][1] < 4: ous[n] = ous[n][0], ous[n][1]+1
                    else: ous[n] = ous[n][0]-1, ous[n][1]
                elif ous[n][1] == 4:
                    if ous[n][0] > 0: ous[n] = ous[n][0]-1, ous[n][1]
                    else: ous[n] = ous[n][0], ous[n][1]-1
                elif ous[n][0] == 0:
                    if ous[n][1] > 0: ous[n] = ous[n][0], ous[n][1]-1
                    else: ous[n] = ous[n][0]+1, ous[n][1]
        wk = souris_sur_image(imag, f, nf, 100, non) ### C'est pour avoir des coos ###
        if wk == 27: quitter()
        elif wk == 32:
            echq = [list(c-50 for c in echiquier[0]), list(c+50 for c in echiquier[1])]
            if clicked_in(j1.pos, echq) and clicked_in(j2.pos, echq): return('echecs', imag, numb)
            return('morpion', imag, numb)
        elif wk != -1:
            cam = deplace_js(wk, j1, j2, cam)
        numb += 1
if __name__ == '__main__': carteVille()