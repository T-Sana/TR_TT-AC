from outils.cvt import *
from outils.souris import TRsouris as souris
from outils.quit import quitter
from TR_VARS import *

if True: ## Functs ##
    pass
if True: ## Classes ##
    pass
if True: ## Vars ##
    if True: ## Anim.vars ##
        p_dep = [1700, 100]
        p_arr = [200, 300]
        arng = 500
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
        j1 = joueur('j1', pmp1, [blanc, blanc], 1.5)
        j2 = joueur('j2', pmp2, [blanc, blanc], 1.5)
if True: ## Imageaison ##
    def img(pt=0, nuages=True, persos=True, monts=True):
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
        if persos: ## Persos ##
            if True: ## Joueurs ##
                j1.dessine(img)
                j2.dessine(img)
            if True: ## PNJ ##
                pass
        if monts: ## Montagnes ##
            montagnette(img)
        return(img)
def anim_debut(anim=True, v=5):
    cc = 0
    if anim: #True: ## Animation début ##
        for i in points_segment(p_dep, p_arr)[::v]:
            montre_img(zoom_at(img(cc-arng), 2, coord=i), nf)
            wk = attend_touche(1)
            if wk == 27: quitter()
            cc += 1
        pts = points_segment(p_arr, ct)
        zp = 1/len(pts)
        cnt = 0
        for j in pts[::v]:
            montre_img(zoom_at(img(cc-arng), 2-zp*cnt, coord=j), nf)
            wk = attend_touche(1)
            if wk == 27: quitter()
            cnt+=1
            cc += 1
    return(j1, j2, zoom_at(img(cc-arng), 2-zp*cnt, coord=j))
    while True:
        wk = souris_sur_image(img(cc-arng), souris.get_souris_, nf, 1, False)
        j1.deplace([cc%21-10, 0])
        j1.deplace([0, cc%51-25])
        j2.deplace([0, cc%51-25])
        if wk == 27: quitter()
        elif wk != -1: print(wk)
        cc += 1
        j1.place(souris.pos if souris.pos != souris.dehors else None)
