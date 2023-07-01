from outils.cvt import *
from outils.quit import quitter
from TR_VARS import *

if True: ## Vars ##
    if True: ## Anim.vars ##
        p_dep = [1700, 100]
        p_arr = [200, 300]
    if True: ## Ciel.vars ##
        dist_nuages = 2000
        vitesses= (0.50, 1.00, 0.75, 1.25, 0.50, 1.00)
        tailles = (1.00, 1.10, 1.20, 0.80, 0.90, 1.00)
        tailles = [i*0.8 for i in tailles]
        vta, vtb, vtc, vtd, vte, vtf = vitesses
        tla, tlb, tlc, tld, tle, tlf = tailles
        dtt = 100
    if True: ## Coos.vars ##
        pmp1 = cg  ## Position Maison Perso 1 ##
        pmp2 = ctg ## Position Maison Perso 2 ##
    if True: ## Joueurs ##
        j1.place(pmp1)
        j2.place(pmp2)
if True: ## Imageaison ##
    def imag(pt=0, nuages=True, persos=True, monts=True, j1=j1, j2=j2):
        pd = pt_sg(hd, bd, 9, 4)
        img = image(remplissage=nouvelle_couleur('e08030'))
        soleil(img, [hd[0]-dtt, hd[1]+dtt], rot=pt/4)
        if nuages: ## Nuages ##
            nuage(img, [cth[0]+200+((pt*vtd)%dist_nuages), cth[1]+75], tld, [220, 220, 220])
            nuage(img, [hg[0]+150+((pt*vta)%dist_nuages), hg[1]+150], tla)
            nuage(img, [hg[0]+300+((pt*vtb)%dist_nuages), hg[1]+200], tlb)
            nuage(img, [cth[0]+100+((pt*vtc)%dist_nuages), cth[1]-100], tlc)
            nuage(img, [hd[0]-300+((pt*vte)%dist_nuages), hd[1]+150], tle)
            nuage(img, [hd[0]-150+((pt*vtf)%dist_nuages), hd[1]+200], tlf)
            nuage(img, [cth[0]+200+((pt*vtd)%dist_nuages)-dist_nuages, cth[1]+75], tld, [220, 220, 220])
            nuage(img, [hg[0]+150+((pt*vta)%dist_nuages)-dist_nuages, hg[1]+150], tla)
            nuage(img, [hg[0]+300+((pt*vtb)%dist_nuages)-dist_nuages, hg[1]+200], tlb)
            nuage(img, [cth[0]+100+((pt*vtc)%dist_nuages)-dist_nuages, cth[1]-100], tlc)
            nuage(img, [hd[0]-300+((pt*vte)%dist_nuages)-dist_nuages, hd[1]+150], tle)
            nuage(img, [hd[0]-150+((pt*vtf)%dist_nuages)-dist_nuages, hd[1]+200], tlf)
            nuage(img, [cth[0]+200+((pt*vtd)%dist_nuages)-2*dist_nuages, cth[1]+75], tld, [220, 220, 220])
            nuage(img, [hg[0]+150+((pt*vta)%dist_nuages)-2*dist_nuages, hg[1]+150], tla)
            nuage(img, [hg[0]+300+((pt*vtb)%dist_nuages)-2*dist_nuages, hg[1]+200], tlb)
            nuage(img, [cth[0]+100+((pt*vtc)%dist_nuages)-2*dist_nuages, cth[1]-100], tlc)
            nuage(img, [hd[0]-300+((pt*vte)%dist_nuages)-2*dist_nuages, hd[1]+150], tle)
            nuage(img, [hd[0]-150+((pt*vtf)%dist_nuages)-2*dist_nuages, hd[1]+200], tlf)
        rectangle(img, bg, pd, nouvelle_couleur('80e030'), 0) ## Terre (rectangle vert) ##
        if True: ## Maisons ##
            maison(img, pmp1)
            maison(img, pmp2)
        if monts: ## Montagnes ##
            montagnette(img)
            htr = pd[1]
            for i in range(0, 1920, 132): montagnette(img, [i, htr])
            for i in range(33, 1920, 66): montagnette(img, [i, htr])
            for i in range(66, 1920, 132): montagnette(img, [i, htr])
        return(img)
sauve_image(n_img1, imag(), f'{dir}/{imgs}')
img = ouvre_image(f'{dir}/{imgs}/{n_img1}')
def anim_debut(anim=True, v=5):
    if anim: ## Animation début ##
        for i in points_segment(p_dep, p_arr)[::v]:
            montre_img(zoom_at(img, 2, coord=i), nf)
            wk = attend_touche(1)
            if wk == 27: quitter()
        pts = points_segment(p_arr, ct)
        zp = 1/len(pts)
        cnt = 0
        v2 = round(v/2)
        for j in pts[::v2]:
            montre_img(zoom_at(img, 2-zp*cnt, coord=j), nf)
            wk = attend_touche(1)
            if wk == 27: quitter()
            cnt += v2
    return(j1, j2)