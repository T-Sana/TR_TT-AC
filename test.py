from outils.cvt import *
from outils.souris import souris as s
from TR_anim_debut import img as imag
from TR_VARS import *

img = imag()
t = 1
a = []
while True:
    wk = souris_sur_image(img, s.get_souris, nf, 1, False)
    if wk == 27: ferme(nf); break
    if wk != -1: print(wk)
    if wk == 2490368: t += 1
    elif wk == 2621440 and t > 1: t -= 1
    if s.pos != s.dehors:
        pos = s.pos
        s.pos = s.dehors
        montagnette(img, pos, t)
        a.append([pos, t])
print(a)