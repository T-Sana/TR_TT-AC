from outils.cvt import *
from outils.souris import souris
from TR_anim_debut import img as imag
img = imag()
t = 1
while True:
    wk = souris_sur_image(img, souris.get_souris, attente=1, destroy=False)
    if wk == 27: raise SystemExit
    if wk != -1: print(wk)
    if wk == 2490368: t += 1
    elif wk == 2621440 and t > 1: t -= 1
    if souris.pos != souris.dehors:
        pos = souris.pos
        souris.pos = souris.dehors
        montagnette(img, pos, t)