from outils.cvt import *
from outils.quit import *
from TR_anim_debut import img
from TR_vars import *

im = copy.deepcopy(img)

def titre(t=9):
    t2 = 5
    marron = nouvelle_couleur('122336')
    a, b = 3, 2
    if t < t2: t = t2+1
    pg = pt_sg(hg, bg, 6)
    pg2 = pt_sg(hg, bg, 6, 4)
    pt1, pt2, pt3, pt4 = pt_sg(hg, ct, a, b), pt_sg(hd, ct, a, b), pt_sg(bg, ct, a, b), pt_sg(bd, ct, a, b)
    rectangle(im, pt1, pt4, bois, 0)
    for i in [[pt1, pt3], [pt1, pt2], [pt2, pt4], [pt3, pt4]]:
        ligne(im, i[0], i[1], marron)
    ecris(im, f'{nf}\n', pg, bd, t, noir, 15)
    ecris(im, f'{nf}\n', pg, bd, t, turquoise, 5)
    ecris(im, f'{aut1}', pg, bd, t-t2, noir, 15)
    ecris(im, f'{aut1}', pg, bd, t-t2, turquoise, 5)
    ecris(im, f'{aut2}', pg2, bd, t-t2, noir, 15)
    ecris(im, f'{aut2}', pg2, bd, t-t2, turquoise, 5)
    while True:
        wk = montre(im, nf, destroy=False)
        if wk == 27: quitter()
        else: return(None)