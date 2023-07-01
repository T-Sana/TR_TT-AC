from outils.cvt import *
from TR_VARS import *
from outils.functs import *
from outils.quit import *


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
            mur = [pt_sg(hg, bg, 9, 3), pt_sg(hd, bd, 9, 5), 5]
            crenaux = [pt_sg(hg, bg, 9, 2), pt_sg(hd, bd, 9, 3), 19] ## Merlets [CATALÀ] ##
            distance = diff(crenaux[0][0], crenaux[1][0])/crenaux[2]
        if True: ## Porte.vars ##
            porte = 4
            d_porte = 12
        if True: ## VARS ##
            d = [haut*2, long, 3]
    def img2():
        if True: ## VARS ##
            hg = [0, 0]
            bg = [0, haut]
            hd = [long, 0]
            bd = [long, haut]
            c_porte = []
            img = image(remplissage=nouvelle_couleur('e08030'), dimensions=d)
        soleil(img, [hd[0]-dtt, hd[1]+dtt])
        if True: ## Nuages ##
            nuage(img, [cth[0]+200, cth[1]+75], tld, [220, 220, 220])
            nuage(img, [hg[0]+150, hg[1]+150], tla)
            nuage(img, [hg[0]+300, hg[1]+200], tlb)
            nuage(img, [cth[0]+100, cth[1]-100], tlc)
            nuage(img, [hd[0]-300, hd[1]+150], tle)
            nuage(img, [hd[0]-150, hd[1]+200], tlf)
        if True: ## Sol ##
            rectangle(img, [0, d[0]], pt_sg(hd, bd, 9, 4), nouvelle_couleur('80e030'), 0) ## Terre (rectangle vert) ##
        if True: ## Mur ##
            dy = diff(mur[0][1], mur[1][1])/mur[2]
            dx = diff(mur[0][0], mur[1][0])/crenaux[2]/mur[2]
            truc = False
            for a, j in enumerate(range2(mur[0][1], mur[1][1], dy)):
                for b, i in enumerate(range2(mur[0][0] - (dx//2 if truc else 0), mur[1][0] + (dx//2 if truc else 0), dx)):
                    t = True
                    if truc:
                        ls = [n for n in range(d_porte, d_porte+porte+1)]
                        if b == d_porte:
                            rectangle(img, [i, j], [i+dx/2, j+dy], nouvelle_couleur('404040'), 0)
                            rectangle(img, [i, j], [i+dx/2, j+dy], noir, 3)
                        elif b == d_porte+porte:
                            rectangle(img, [i+dx/2, j], [i+dx, j+dy], nouvelle_couleur('404040'), 0)
                            rectangle(img, [i+dx/2, j], [i+dx, j+dy], noir, 3)
                    else:
                        ls = [n for n in range(d_porte, d_porte+porte)]
                    if a == 2:
                        if truc: dx2 = dx/2
                        else: dx2 = 0
                        if b == d_porte:
                            c_porte.append([i+dx2, j])
                            triangle(img, [i+dx2, j], [i+dx+dx2, j], [i+dx2, j+dy], nouvelle_couleur('404040'), 0)
                            triangle(img, [i+dx2, j], [i+dx+dx2, j], [i+dx2, j+dy], noir, 3)
                        elif b == d_porte+porte-1:
                            triangle(img, [i+dx2, j], [i+dx+dx2, j], [i+dx+dx2, j+dy], nouvelle_couleur('404040'), 0)
                            triangle(img, [i+dx2, j], [i+dx+dx2, j], [i+dx+dx2, j+dy], noir, 3)
                    for el in ls:
                        if b == el:
                            t = False
                    if t or a == 0 or a == 1:
                        rectangle(img, [i, j], [i+dx, j+dy], nouvelle_couleur('404040'), 0)
                        rectangle(img, [i, j], [i+dx, j+dy], noir, 3)
                    if diff(j, mur[1][1]) <= dy:
                        if b == d_porte+porte:
                            if truc: dx2 = dx/2
                            else: dx2 = 0
                            c_porte.append([i+dx2, j+dy])
                truc = not truc
        if True: ## Porte ##
            c_porte = [c_porte[0], [c_porte[1][0], c_porte[0][1]], [c_porte[0][0], c_porte[1][1]], c_porte[1]]
            for i in c_porte:
                point(img, i)
        if True: ## Crénaux ##
            dra = True
            chng = False
            for i in range2(crenaux[0][0]-distance/2, crenaux[1][0]+distance/2, dx):
                if dra and not chng:
                    rectangle(img, [i, crenaux[1][1]-dy], [i+distance/8*3, crenaux[1][1]], nouvelle_couleur('404040'), 0)
                    rectangle(img, [i, crenaux[1][1]-dy], [i+distance/8*3, crenaux[1][1]], noir, 3)
                if chng:
                    dra = not dra
                chng = not chng
        if True: ## VARS update ##
            hg, hd, bg, bd = [0, 0], [d[1], 0], [0, d[0]], [d[1], d[0]]
            ct = ct_cr(hg, hd, bg, bd)
        return(img)

def img_cart1() -> None:
    sauve_image(n_img1, img1(), f'{dir}/{imgs}')
def img_cart2() -> None:
    sauve_image(n_img2, img2(), f'{dir}/{imgs}')

def demo_img2():
    img_cart2()
    im2 = ouvre_image(f'{dir}/{imgs}/{n_img2}')
    for i in range(0, d[0]-haut+1, 2):
        wk = montre_part(im2, pto=[0, i], attente=1, destroy=non)
        if wk == 27: quitter()
    for i in range(0, d[0]-haut+1, 2)[::-1]:
        wk = montre_part(im2, pto=[0, i], attente=1, destroy=non)
        if wk == 27: quitter()
    montre_part(im2)
demo_img2()