from outils.cvt import *
from TR_VARS import *
from outils.functs import *


if True: ## Img1 ## @@ Campagne @@
    if True: ## Vars ##
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
    def img1(pt=0, nuages=True, persos=True, monts=True, j1=j1, j2=j2):
        img = image(remplissage=nouvelle_couleur('e08030'))
        soleil(img, [hd[0]-dtt, hd[1]+dtt])
        if nuages: ## Nuages ##
            nuage(img, [cth[0]+200, cth[1]+75], tld, [220, 220, 220])
            nuage(img, [hg[0]+150, hg[1]+150], tla)
            nuage(img, [hg[0]+300, hg[1]+200], tlb)
            nuage(img, [cth[0]+100, cth[1]-100], tlc)
            nuage(img, [hd[0]-300, hd[1]+150], tle)
            nuage(img, [hd[0]-150, hd[1]+200], tlf)
        rectangle(img, bg, pt_sg(hd, bd, 9, 4), nouvelle_couleur('80e030'), 0) ## Terre (rectangle vert) ##
        if True: ## Maisons ##
            maison(img, pmp1)
            maison(img, pmp2)
        if monts: ## Montagnes ##
            montagnette(img)
            htr = pt_sg(hd, bd, 9, 4)[1]
            for i in range(0, 1920, 132): montagnette(img, [i, htr])
            for i in range(33, 1920, 66): montagnette(img, [i, htr])
            for i in range(66, 1920, 132): montagnette(img, [i, htr])
        return(img)
if True: ## Img2 ## @@ Ville @@
    if True: ## Vars ##
        if True: ## Ciel.vars ##
            dist_nuages = 2000
            vitesses= (0.50, 1.00, 0.75, 1.25, 0.50, 1.00)
            tailles = (1.00, 1.10, 1.20, 0.80, 0.90, 1.00)
            tailles = [i*0.8 for i in tailles]
            vta, vtb, vtc, vtd, vte, vtf = vitesses
            tla, tlb, tlc, tld, tle, tlf = tailles
            dtt = 100
        if True: ## Mur.vars ##
            mur = [pt_sg(hg, bg, 9, 5), pt_sg(hd, bd, 4, 9)]
            crenaux = [pt_sg(hg, bg, 9, 4), pt_sg(hd, bd, 9, 5), 19] ## Merlets [CATALÀ] ##
        d = [haut*2, long, 3]
        hg, hd, bg, bd = [0, 0], [d[1], 0], [0, d[0]], [d[1], d[0]]
        ct = ct_cr(hg, hd, bg, bd)
    def img2():
        img = image(remplissage=nouvelle_couleur('e08030'), dimensions=d)
        soleil(img, [hd[0]-dtt, hd[1]+dtt])
        if True: ## Nuages ##
            nuage(img, [cth[0]+200, cth[1]+75], tld, [220, 220, 220])
            nuage(img, [hg[0]+150, hg[1]+150], tla)
            nuage(img, [hg[0]+300, hg[1]+200], tlb)
            nuage(img, [cth[0]+100, cth[1]-100], tlc)
            nuage(img, [hd[0]-300, hd[1]+150], tle)
            nuage(img, [hd[0]-150, hd[1]+200], tlf)
        rectangle(img, [0, d[0]], pt_sg(hd, bd, 9, 4), nouvelle_couleur('80e030'), 0) ## Terre (rectangle vert) ##
        rectangle(img, mur[0], mur[1], nouvelle_couleur('404040'), 0)
        distance = diff(crenaux[0][0], crenaux[1][0])/crenaux[2]
        dra = True
        for i in range2(crenaux[0][0], crenaux[1][0], distance):
            if dra: rectangle(img, [i, crenaux[0][1]], [i+distance, crenaux[1][1]], noir, 0)
            dra = not dra
        for i in [crenaux[0], crenaux[1]]:
            point(img, i, rouge)
        return(img)

def img_cart1() -> None:
    sauve_image(n_img1, img1(), f'{dir}/{imgs}')
def img_cart2() -> None:
    sauve_image(n_img2, img2(), f'{dir}/{imgs}')

img_cart2()
im2 = ouvre_image(f'{dir}/{imgs}/{n_img2}')
for i in range(0, d[0]-haut+1, 2):
    wk = montre_part(im2, pto=[0, i], attente=1, destroy=non)
    if wk == 27: raise SystemExit
for i in range(0, d[0]-haut+1, 2)[::-1]:
    wk = montre_part(im2, pto=[0, i], attente=1, destroy=non)
    if wk == 27: raise SystemExit
montre_part(im2)