from outils.cvt import *
from outils.functs import *
from outils.paths__names__etc import *
from outils.quit import *

if True: ## Noms.vars ##
    n_img_chargement='img_chrg.jpg';n_img1='img1.jpg';n_img2='img2.jpg';n_img3='img3.jpg';n_img4='img4.jpg';n_img5='img5.jpg';imgs='Imgs'
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
            pmp1 = ctg  ## Position Maison Perso 1 ##
            pmp2 = cg ## Position Maison Perso 2 ##
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
    def img2():
        if True: ## VARS ##
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
                distance = diff(crenaux[0][0], crenaux[1][0])/crenaux[2]/2
            if True: ## Porte.vars ##
                porte = 4
                d_porte = 12
            d = [haut*2, long, 3]
            hg2 = [0, 0]
            bg2 = [0, haut]
            hd2 = [long, 0]
            bd2 = [long, haut]
            c_porte = []
            img = image(remplissage=nouvelle_couleur('e08030'), dimensions=d)
        soleil(img, [hd2[0]-dtt, hd2[1]+dtt])
        if True: ## Nuages ##
            nuage(img, [cth[0]+200, cth[1]+75], tld, [220, 220, 220])
            nuage(img, [hg[0]+150, hg[1]+150], tla)
            nuage(img, [hg[0]+300, hg[1]+200], tlb)
            nuage(img, [cth[0]+100, cth[1]-100], tlc)
            nuage(img, [hd[0]-300, hd[1]+150], tle)
            nuage(img, [hd[0]-150, hd[1]+200], tlf)
        if True: ## Sol ##
            rectangle(img, [0, d[0]], pt_sg(hd2, bd2, 9, 4), nouvelle_couleur('80e030'), 0) ## Terre (rectangle vert) ##
        if True: ## Mur ##
            mult = 2
            dy = diff(mur[0][1], mur[1][1])/mur[2]
            dx = diff(mur[0][0], mur[1][0])/crenaux[2]/mur[2]*mult
            truc = False
            t_porte = []
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
                            t_porte.append([[i+dx2, j], [i+dx+dx2, j], [i+dx2, j+dy]])
                        elif b == d_porte+porte-1:
                            t_porte.append([[i+dx2, j], [i+dx+dx2, j], [i+dx+dx2, j+dy]])
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
                ## TODO ## Dessin du pont levis, de la herse ... ##
                t = 1.25; ecris(img, 'Dessin', c_porte[0], c_porte[3], t, noir, 10/4*t)
                for i in t_porte:
                    triangle(img, i[0], i[1], i[2], nouvelle_couleur('404040'), 0)
                    triangle(img, i[0], i[1], i[2], noir, 3)
            if True: ## Crénaux ##
                dra = True
                chng = False
                distance *= mult
                for i in range2(crenaux[0][0]-distance, crenaux[1][0]+distance/2, dx/2):
                    if dra and not chng:
                        rectangle(img, [i, crenaux[1][1]-dy], [i+distance/8*3, crenaux[1][1]], nouvelle_couleur('404040'), 0)
                        rectangle(img, [i, crenaux[1][1]-dy], [i+distance/8*3, crenaux[1][1]], noir, 3)
                    if chng:
                        dra = not dra
                    chng = not chng
        if True: ## VARS update ##
            hg2, hd2, bg2, bd2 = [0, 0], [d[1], 0], [0, d[0]], [d[1], d[0]]
            ct = ct_cr(hg, hd, bg, bd)
        return(img)

def img_cart1() -> None:
    sauve_image(n_img1, img1(), f'{dir}/{imgs}')
def img_cart2() -> None:
    sauve_image(n_img2, img2(), f'{dir}/{imgs}')

def demo_img2():
    img_cart2()
    d = [haut*2, long, 3]
    im2 = ouvre_image(f'{dir}/{imgs}/{n_img2}')
    for i in range(0, d[0]-haut+1, 2):
        wk = montre_part(im2, pto=[0, i], attente=1, destroy=non)
        if wk == 27: quitter()
    for i in range(0, d[0]-haut+1, 2)[::-1]:
        wk = montre_part(im2, pto=[0, i], attente=1, destroy=non)
        if wk == 27: quitter()
    montre_part(im2)


def img_chrg() -> None: ## MAIN ##
    '''if True: ## ImgChargement ##
        img = img1(); a, b = 8, 9
        pt1, pt2 = pt_sg(hg, ct, a, b), pt_sg(pt_sg(ct_sg(hd, bd), bd, a, b), ct, a, b)
        rectangle(img, pt1, pt2, nouvelle_couleur('72A4CA'), 0)
        rectangle(img, pt1, pt2, nouvelle_couleur('225070'), 10)
        ecris(img, nf, pt1, pt2, 4, nouvelle_couleur('152030'))
        sauve_image(n_img_chargement, img, f'{dir}/{imgs}')'''
    img = ouvre_image(f'{dir}/{imgs}/{n_img1}')
    marron = nouvelle_couleur('122336')
    t=9
    t2 = 5
    a, b = 3, 2
    if t < t2: t = t2+1
    pg = pt_sg(hg, bg, 6)
    pg2 = pt_sg(hg, bg, 6, 4)
    pt1, pt2, pt3, pt4 = pt_sg(hg, ct, a, b), pt_sg(hd, ct, a, b), pt_sg(bg, ct, a, b), pt_sg(bd, ct, a, b)
    rectangle(img, pt1, pt4, bois, 0)
    for i in [[pt1, pt3], [pt1, pt2], [pt2, pt4], [pt3, pt4]]:
        ligne(img, i[0], i[1], marron)
    ecris(img, f'{nf}\n', pg, bd, t, noir, 15)
    ecris(img, f'{nf}\n', pg, bd, t, turquoise, 5)
    ecris(img, f'{aut1}', pg, bd, t-t2, noir, 15)
    ecris(img, f'{aut1}', pg, bd, t-t2, turquoise, 5)
    ecris(img, f'{aut2}', pg2, bd, t-t2, noir, 15)
    ecris(img, f'{aut2}', pg2, bd, t-t2, turquoise, 5)
    sauve_image(n_img_chargement, img, f'{dir}/{imgs}')