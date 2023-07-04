from outils.cvt import *
from outils.quit import quitter
from outils.paths__names__etc import *

if True: ## Vars ##
    if True: ## Anim.vars ##
        p_dep = [1700, 100]
        p_arr = [200, 300]
    img = ouvre_image(f'{dir}/{imgs}/{n_img1}')
def anim_debut(anim=True, v=5) -> None:
    if anim: ## Animation début ##
        for i in points_segment(p_dep, p_arr)[::v]:
            montre_img(zoom_at(img, 2, coord=i), nf)
            wk = attend_touche(1)
            if wk == 27: quitter()
        if True: ## Vars ##
            pts = points_segment(p_arr, ct)
            zp = 1/len(pts)
            cnt = 0
            v2 = round(v/2)
        for j in pts[::v2]:
            montre_img(zoom_at(img, 2-zp*cnt, coord=j), nf)
            wk = attend_touche(1)
            if wk == 27: quitter()
            cnt += v2