from Depandances.Outils.cvt import *
from Depandances.Outils.functs import *
from Depandances.Outils.paths__names__etc import *
from Depandances.Outils.quit import *

SUPPORTED_CHARS = '1234567890qwertyuiopasdfghjklzxcvbnm,.;:-_!"$%&/()=?*[]{}\\ '

if True:  # Pieces d'échecs ##
    def dessine_roi(img, pt1, pt2, pt3, pt4, col1, col2, ep=5, echec=False):  # Terminé ##
        ct = ct_sg(ct_sg(pt1, pt2), ct_sg(pt3, pt4))
        c1 = pt_sg(pt1, ct)
        c2 = pt_sg(pt2, ct)
        c3 = pt_sg(pt3, ct)
        c4 = pt_sg(pt4, ct)
        cg = pt_sg(c1, c3)
        cd = pt_sg(c2, c4)
        cb = pt_sg(c3, c4)
        ch = pt_sg(c1, c2)
        if echec:
            rectangle(img, pt1, pt4, rouge, 0)
        a, b = 7, 5
        rectangle(img, c1, c4, col1, 0)
        rectangle(img, c1, c4, col2, ep)
        rectangle(img, ct_sg(pt1, c1), ct_sg(c1, cg), col1, 0)
        rectangle(img, ct_sg(pt2, c2), ct_sg(c2, cd), col1, 0)
        rectangle(img, pt_sg(ct_sg(pt1, c1), ct_sg(pt2, c2), a, b),
                  pt_sg(c1, c2, b, a), col1, 0)
        rectangle(img, pt_sg(ct_sg(pt1, c1), ct_sg(pt2, c2), a, b),
                  pt_sg(c1, c2, b, a), col2, ep)
        rectangle(img, ct_sg(pt1, c1), ct_sg(c1, cg), col2, ep)
        rectangle(img, ct_sg(pt2, c2), ct_sg(c2, cd), col2, ep)
        ligne(img, ct_sg(ch, ct), ct_sg(cb, ct), col2, ep)
        ligne(img, ct_sg(cg, ct), ct_sg(cd, ct), col2, ep)
        return (img)

    def dessine_pion(img, pt1, pt2, pt3, pt4, col1, col2, ep=5):  # Terminé ##
        ct = ct_sg(ct_sg(pt1, pt2), ct_sg(pt3, pt4))
        c1 = pt_sg(pt1, ct)
        c4 = pt_sg(pt4, ct)
        rectangle(img, c1, c4, col1, 0)
        rectangle(img, c1, c4, col2, ep)
        return (img)

    def dessine_pions(img, pt1, pt2, pt3, pt4, col1, col2, ep=5):  # Terminé ##
        ct = ct_sg(ct_sg(pt1, pt2), ct_sg(pt3, pt4))
        a, b = 2, 5
        p1, p2, p3, p4 = pt_sg(ct, pt1, a, b), pt_sg(
            ct, pt2, a, b), pt_sg(ct, pt3, a, b), pt_sg(ct, pt4, a, b)
        cg, cd, ch, cb = pt_sg(p1, p3), pt_sg(
            p2, p4), pt_sg(p1, p2), pt_sg(p3, p4)
        cdb = ct_sg(cd, p4)
        cgb = ct_sg(cg, p3)
        cth = ct_cr(p1, p2, cg, cd)
        ctb = ct_sg(cgb, cdb)
        ctbg = ct_sg(ctb, cgb)
        ctbd = ct_sg(ctb, cdb)
        rectangle(img, cgb, p4, col1, 0)
        rectangle(img, cgb, p4, col2, ep)
        triangle(img, ctbd, ctbg, cth, col1, 0)
        triangle(img, ctbd, ctbg, cth, col2, ep)
        cercle(img, cth, round(dist(cth, ch)/1.5), col1, 0)
        cercle(img, cth, round(dist(cth, ch)/1.5), col2, ep)
        return (img)

    def dessine_cavalier(img, pt1, pt2, pt3, pt4, col1, col2, ep=5):  # Terminé ##
        ct = ct_sg(ct_sg(pt1, pt2), ct_sg(pt3, pt4))
        c1 = pt_sg(pt1, ct)
        c4 = pt_sg(pt4, ct)
        a, b = 1, 3
        rectangle(img, c1, c4, col1, 0)
        rectangle(img, c1, c4, col2, ep)
        rectangle(img, ct_sg(pt1, c1), pt_sg(c1, ct, a, b), col1, 0)
        rectangle(img, ct_sg(pt1, c1), pt_sg(c1, ct, a, b), col2, ep)
        return (img)

    def dessine_fou(img, pt1, pt2, pt3, pt4, col1, col2, ep=5):  # Terminé ##
        ct = ct_sg(ct_sg(pt1, pt2), ct_sg(pt3, pt4))
        c1 = pt_sg(pt1, ct)
        c2 = pt_sg(pt2, ct)
        c3 = pt_sg(pt3, ct)
        c4 = pt_sg(pt4, ct)
        cg = pt_sg(c1, c3)
        cd = pt_sg(c2, c4)
        cb = pt_sg(c3, c4)
        ch = pt_sg(c1, c2)
        a, b = 7, 5
        rectangle(img, c1, c4, col1, 0)
        rectangle(img, c1, c4, col2, ep)
        rectangle(img, pt_sg(ct_sg(pt1, c1), ct_sg(pt2, c2), a, b),
                  pt_sg(c1, c2, b, a), col1, 0)
        rectangle(img, pt_sg(ct_sg(pt1, c1), ct_sg(pt2, c2), a, b),
                  pt_sg(c1, c2, b, a), col2, ep)
        ligne(img, ct_sg(ch, ct), ct_sg(cb, ct), col2, ep)
        ligne(img, ct_sg(cg, ct), ct_sg(cd, ct), col2, ep)
        return (img)

    def dessine_tour(img, pt1, pt2, pt3, pt4, col1, col2, ep=5):  # Terminé ##
        ct = ct_sg(ct_sg(pt1, pt2), ct_sg(pt3, pt4))
        c1 = pt_sg(pt1, ct)
        c2 = pt_sg(pt2, ct)
        c3 = pt_sg(pt3, ct)
        c4 = pt_sg(pt4, ct)
        cg = pt_sg(c1, c3)
        cd = pt_sg(c2, c4)
        cb = pt_sg(c3, c4)
        ch = pt_sg(c1, c2)
        a, b = 3, 1
        rectangle(img, c1, c4, col1, 0)
        rectangle(img, c1, c4, col2, ep)
        rectangle(img, ct_sg(pt1, c1), pt_sg(c1, ct, a, b), col1, 0)
        rectangle(img, ct_sg(pt1, c1), pt_sg(c1, ct, a, b), col2, ep)
        rectangle(img, ct_sg(pt2, c2), pt_sg(c2, ct, a, b), col1, 0)
        rectangle(img, ct_sg(pt2, c2), pt_sg(c2, ct, a, b), col2, ep)
        return (img)

    def dessine_dame(img, pt1, pt2, pt3, pt4, col1, col2, ep=5):  # Terminé ##
        ct = ct_sg(ct_sg(pt1, pt2), ct_sg(pt3, pt4))
        c1 = pt_sg(pt1, ct)
        c2 = pt_sg(pt2, ct)
        c3 = pt_sg(pt3, ct)
        c4 = pt_sg(pt4, ct)
        cg = pt_sg(c1, c3)
        cd = pt_sg(c2, c4)
        a, b = 7, 5
        rectangle(img, c1, c4, col1, 0)
        rectangle(img, c1, c4, col2, ep)
        rectangle(img, ct_sg(pt1, c1), ct_sg(c1, cg), col1, 0)
        rectangle(img, ct_sg(pt2, c2), ct_sg(c2, cd), col1, 0)
        rectangle(img, pt_sg(ct_sg(pt1, c1), ct_sg(pt2, c2), a, b),
                  pt_sg(c1, c2, b, a), col1, 0)
        rectangle(img, pt_sg(ct_sg(pt1, c1), ct_sg(pt2, c2), a, b),
                  pt_sg(c1, c2, b, a), col2, ep)
        rectangle(img, ct_sg(pt1, c1), ct_sg(c1, cg), col2, ep)
        rectangle(img, ct_sg(pt2, c2), ct_sg(c2, cd), col2, ep)
        return (img)
if True:  # Noms.vars ##
    n_img_chargement = 'img_chrg.jpg'
    n_img1 = 'img1.jpg'
    n_img2 = 'img2.jpg'
    n_img3 = 'img3.jpg'
    n_img4 = 'img4.jpg'
    n_img5 = 'img5.jpg'
    imgs = 'Imgs'
if True:  # Img1 ## @@ Campagne @@
    if True:  # Vars ##
        if True:  # Ciel.vars ##
            dist_nuages = 2000
            vitesses = (0.50, 1.00, 0.75, 1.25, 0.50, 1.00)
            tailles = (1.00, 1.10, 1.20, 0.80, 0.90, 1.00)
            tailles = [i*0.8 for i in tailles]
            vta, vtb, vtc, vtd, vte, vtf = vitesses
            tla, tlb, tlc, tld, tle, tlf = tailles
            dtt = 100
        if True:  # Coos.vars ##
            pmp1 = ctg  # Position Maison Perso 1 ##
            pmp2 = cg  # Position Maison Perso 2 ##
        if True:  # Joueurs ##
            j1.place(pmp1)
            j2.place(pmp2)

    def img1(pt=0, nuages=True, persos=True, monts=True, j1=j1, j2=j2):
        img = image(remplissage=nouvelle_couleur('e08030'))
        soleil(img, [hd[0]-dtt, hd[1]+dtt])
        if nuages:  # Nuages ##
            nuage(img, [cth[0]+200, cth[1]+75], tld, [220, 220, 220])
            nuage(img, [hg[0]+150, hg[1]+150], tla)
            nuage(img, [hg[0]+300, hg[1]+200], tlb)
            nuage(img, [cth[0]+100, cth[1]-100], tlc)
            nuage(img, [hd[0]-300, hd[1]+150], tle)
            nuage(img, [hd[0]-150, hd[1]+200], tlf)
        rectangle(img, bg, pt_sg(hd, bd, 9, 4), nouvelle_couleur(
            '80e030'), 0)  # Terre (rectangle vert) ##
        if True:  # Maisons ##
            maison(img, pmp1)
            maison(img, pmp2)
        if monts:  # Montagnes ##
            montagnette(img)
            htr = pt_sg(hd, bd, 9, 4)[1]
            for i in range(0, 1920, 132):
                montagnette(img, [i, htr])
            for i in range(33, 1920, 66):
                montagnette(img, [i, htr])
            for i in range(66, 1920, 132):
                montagnette(img, [i, htr])
        return (img)
if True:  # Img2 ## @@ Ville @@
    def img2():
        if True:  # VARS ##
            if True:  # Vars - others ##
                d = [haut*2, round(long*1.5), 3]
                hg2 = [0, 0]
                bg2 = [0, haut]
                hd2 = [d[1], 0]
                bd2 = [d[1], haut]
                c_porte = []
                img = image(remplissage=nouvelle_couleur(
                    'e08030'), dimensions=d)
            if True:  # Ciel.vars ##
                dist_nuages = 2000
                vitesses = (0.50, 1.00, 0.75, 1.25, 0.50, 1.00)
                tailles = (1.00, 1.10, 1.20, 0.80, 0.90, 1.00)
                tailles = [i*0.8 for i in tailles]
                vta, vtb, vtc, vtd, vte, vtf = vitesses
                tla, tlb, tlc, tld, tle, tlf = tailles
                dtt = 100
            if True:  # Mur.vars ##
                mur = [pt_sg(hg, bg, 9, 3), pt_sg(
                    [d[1], hd[1]], [d[1], bd[1]], 9, 5), 5]
                crenaux = [pt_sg(hg, bg, 9, 2), pt_sg(
                    # Merlets [CATALÀ] ##
                    [d[1], hd[1]], [d[1], bd[1]], 9, 3), 30]
                distance = diff(crenaux[0][0], crenaux[1][0])/crenaux[2]/2
            if True:  # Porte.vars ##
                porte = 4
                d_porte = 40

        soleil(img, [hd2[0]-dtt, hd2[1]+dtt])
        if True:  # Nuages ##
            nuage(img, [cth[0]+200, cth[1]+75], tld, [220, 220, 220])
            nuage(img, [hg[0]+150, hg[1]+150], tla)
            nuage(img, [hg[0]+300, hg[1]+200], tlb)
            nuage(img, [cth[0]+100, cth[1]-100], tlc)
            nuage(img, [hd[0]-300, hd[1]+150], tle)
            nuage(img, [hd[0]-150, hd[1]+200], tlf)
        if True:  # Sol ##
            rectangle(img, [0, d[0]], pt_sg(hd2, bd2, 9, 4), nouvelle_couleur(
                '80e030'), 0)  # Terre (rectangle vert) ##
        if True:  # Muraille ##
            if True:  # Mur ##
                mult = 2
                c_dy = dy = diff(mur[0][1], mur[1][1])/mur[2]
                dx = diff(mur[0][0], mur[1][0])/crenaux[2]/mur[2]*mult
                truc = False
                t_porte = []
                for a, j in enumerate(range2(mur[0][1], mur[1][1], dy)):
                    for b, i in enumerate(range2(mur[0][0] - (dx//2 if truc else 0), mur[1][0] + (dx//2 if truc else 0), dx)):
                        t = True
                        if truc:
                            ls = [n for n in range(d_porte, d_porte+porte+1)]
                            if b == d_porte:
                                rectangle(img, [i, j], [i+dx/2, j+dy],
                                          nouvelle_couleur('404040'), 0)
                                rectangle(img, [i, j], [i+dx/2, j+dy], noir, 3)
                            elif b == d_porte+porte:
                                rectangle(
                                    img, [i+dx/2, j], [i+dx, j+dy], nouvelle_couleur('404040'), 0)
                                rectangle(img, [i+dx/2, j],
                                          [i+dx, j+dy], noir, 3)
                        else:
                            ls = [n for n in range(d_porte, d_porte+porte)]
                        if a == 2:
                            if truc:
                                dx2 = dx/2
                            else:
                                dx2 = 0
                            if b == d_porte:
                                c_porte.append([i+dx2, j])
                                t_porte.append(
                                    [[i+dx2, j], [i+dx+dx2, j], [i+dx2, j+dy]])
                            elif b == d_porte+porte-1:
                                t_porte.append(
                                    [[i+dx2, j], [i+dx+dx2, j], [i+dx+dx2, j+dy]])
                        for el in ls:
                            if b == el:
                                t = False
                        if t or a == 0 or a == 1:
                            rectangle(img, [i, j], [i+dx, j+dy],
                                      nouvelle_couleur('404040'), 0)
                            rectangle(img, [i, j], [i+dx, j+dy], noir, 3)
                        if diff(j, mur[1][1]) <= dy:
                            if b == d_porte+porte:
                                if truc:
                                    dx2 = dx/2
                                else:
                                    dx2 = 0
                                c_porte.append([i+dx2, j+dy])
                    truc = not truc
            if True:  # Porte ##
                a, b = 7, 2
                c_porte = [c_porte[0], [c_porte[1][0], c_porte[0][1]], [
                    c_porte[0][0], c_porte[1][1]], c_porte[1]]
                c_porte = [[round(i[0]), round(i[1])] for i in c_porte]
                rectangle(img, c_porte[0], c_porte[3],
                          nouvelle_couleur('80e030'), 0)
                rectangle(img, pt_sg(c_porte[0], c_porte[2], 5, 4), pt_sg(
                    c_porte[3], c_porte[1], 8, 1), bleu, 0)
                for i, j in [[c_porte[2], c_porte[0]], [c_porte[0], c_porte[1]], [c_porte[1], c_porte[3]]]:
                    ligne(img, i, j, noir, 3)
                base_pont = [pt_sg(c_porte[2], c_porte[3], a, b), pt_sg(
                    c_porte[3], c_porte[2], a, b)]
                haut_pont = [coosCercle(
                    i, dist(base_pont[0], base_pont[1])/2, -70) for i in base_pont]
                dy = 1
                for i in points_segment(base_pont[0], haut_pont[0])[::dy]:
                    rectangle(img, i, [
                              i[0]+diff(base_pont[0][0], base_pont[1][0]), i[1]+dy], nouvelle_couleur('122336'), 0)
                dy = 5
                for i in points_segment(base_pont[0], haut_pont[0])[::dy]:
                    rectangle(
                        img, i, [i[0]+diff(base_pont[0][0], base_pont[1][0]), i[1]+dy], noir, 1)
                for i in range(2):
                    arc(img, haut_pont[i], [base_pont[i]
                        [0], c_porte[0][1]], 5, noir, 2)
                dst = dist(c_porte[0], c_porte[2])/2.7
                esp = 15
                for i in points_segment(c_porte[0], c_porte[1])[::esp]:  # HERSE ##
                    p = [i[0], i[1]+dst]
                    t = 7
                    p2 = coosCercle(p, dst/t, -45)
                    p3 = coosCercle(p, dst/t, 180+45)
                    for j in [i, p2, p3]:
                        ligne(img, p, j, noir, 2)
                dst = dist(c_porte[0], c_porte[1])
                pt_h = pt_sg(c_porte[0], c_porte[2], 2.7)
                for i in points_segment(c_porte[0], pt_h)[::esp-2]:
                    p = [i[0]+dst, i[1]]
                    ligne(img, i, p, noir, 2)
                for i in t_porte:
                    triangle(img, i[0], i[1], i[2],
                             nouvelle_couleur('404040'), 0)
                    triangle(img, i[0], i[1], i[2], noir, 3)
            if True:  # Crénaux ##
                dy = c_dy
                dra = True
                chng = False
                distance *= mult
                for i in range2(crenaux[0][0]-distance, crenaux[1][0]+distance/2, dx/2):
                    if dra and not chng:
                        rectangle(img, [i, crenaux[1][1]-dy], [i+distance /
                                  8*3, crenaux[1][1]], nouvelle_couleur('404040'), 0)
                        rectangle(img, [i, crenaux[1][1]-dy],
                                  [i+distance/8*3, crenaux[1][1]], noir, 3)
                    if chng:
                        dra = not dra
                    chng = not chng
        if True:  # Chemin ##
            a, b = 7, 2
            dst = 170
            dir = 90
            c_t1 = [pt_sg(c_porte[2], c_porte[3], a, b),
                    pt_sg(c_porte[3], c_porte[2], a, b)]
            c_t1.append(coosCercle(c_t1[0], dst, dir))
            c_t1.append(coosCercle(c_t1[1], dst, dir))
            cadre(img, c_t1[0], c_t1[3], nouvelle_couleur(
                '72A4CA'), nouvelle_couleur('22648A'))
            dst = 520
            dir = 180
            c_t2 = [c_t1[2], coosCercle(
                c_t1[2], dist(c_t1[0], c_t1[1]), dir-90)]
            c_t2.append(coosCercle(c_t2[0], dst, dir))
            c_t2.append(coosCercle(c_t2[1], dst, dir))
            cadre(img, c_t2[0], c_t2[3], nouvelle_couleur(
                '72A4CA'), nouvelle_couleur('22648A'))
            triangle(img, c_t2[0], c_t2[1], c_t1[3],
                     nouvelle_couleur('72A4CA'), -3)
            cercle(img, c_t1[2], dist(c_t1[2], c_t1[3]),
                   nouvelle_couleur('72A4CA'), 0, 0, 90)
            cercle(img, c_t1[2], dist(c_t1[2], c_t1[3]),
                   nouvelle_couleur('22648A'), 3, 0, 90)
            for p in [c_t2[0], c_t2[1], c_t1[3]]:
                rectangle(img, [i-2 for i in p], [i+2 for i in p],
                          nouvelle_couleur('22648A'), 0)
            dst = 500
            dir = 90
            c_t3 = [coosCercle(c_t2[3], dist(
                c_t2[0], c_t2[1]), dir+90), c_t2[3]]
            c_t3.append(coosCercle(c_t3[0], dst, dir))
            c_t3.append(coosCercle(c_t3[1], dst, dir))
            cadre(img, c_t3[0], c_t3[3], nouvelle_couleur(
                '72A4CA'), nouvelle_couleur('22648A'))
            triangle(img, c_t2[2], c_t2[3], c_t3[0],
                     nouvelle_couleur('72A4CA'), -3)
            cercle(img, c_t2[3], dist(c_t2[2], c_t2[3]),
                   nouvelle_couleur('72A4CA'), 0, 0, 90, 180)
            cercle(img, c_t2[3], dist(c_t2[2], c_t2[3]),
                   nouvelle_couleur('22648A'), 3, 0, 90, 180)
            for p in [c_t2[2], c_t2[3], c_t3[0]]:
                rectangle(img, [i-2 for i in p], [i+2 for i in p],
                          nouvelle_couleur('22648A'), 0)
        if True:  # VARS update ##
            hg2, hd2, bg2, bd2 = [0, 0], [d[1], 0], [0, d[0]], [d[1], d[0]]
            ct = ct_cr(hg, hd, bg, bd)
        if True:  # Echiquier ##
            echq = [pt_sg(pt_sg(bg, bd, 15), pt_sg(hg, hd, 15), 4), ctg]
            dx = diff(echq[0][0], echq[1][0])/9
            dy = diff(echq[0][1], echq[1][1])/5
            for i, x in enumerate(range2(echq[0][0], echq[1][0], dx)):
                for j, y in enumerate(range2(echq[1][1], echq[0][1]-20, dy)):
                    if j == 2:
                        match i:
                            case 3:
                                coos = [x, y]
                            case _:
                                rectangle(img, [x, y], [x+dx, y+dy], nouvelle_couleur(
                                    '202020') if i % 2 == j % 2 else nouvelle_couleur('DFDFDF'), 0)

                    else:
                        rectangle(img, [x, y], [x+dx, y+dy], nouvelle_couleur('202020')
                                  if i % 2 == j % 2 else nouvelle_couleur('DFDFDF'), 0)
            x, y = coos
            rectangle(img, [x, y], [x+dx*3, y+dy],
                      nouvelle_couleur('72A4CA'), 0)
            rectangle(img, [x, y], [x+dx*3, y+dy], noir, 5)
            dessine_roi(img, [x, y], [x+dx, y], [x, y+dy], [x+dx, y+dy],
                        nouvelle_couleur('DFDFDF'), nouvelle_couleur('202020'), 3)
            dessine_roi(img, [x+dx*2, y], [x+dx*3, y], [x+dx*2, y+dy], [x+dx*3,
                        y+dy], nouvelle_couleur('202020'), nouvelle_couleur('DFDFDF'), 3)
            rectangle(img, echq[0], echq[1], noir, 3)
        return (img)


def img_cart1() -> None:
    sauve_image(n_img1, img1(), f'{dir}\\{imgs_path}')


def img_cart2() -> None:
    sauve_image(n_img2, img2(), f'{dir}\\{imgs_path}')


def demo_img2():
    img_cart2()
    d = [haut*2, long, 3]
    im2 = ouvre_image(f'{dir}\\{imgs_path}\\{n_img2}')
    for i in range(0, d[0]-haut+1, 2):
        wk = montre_part(im2, pto=[0, i], attente=1, destroy=non)
        if wk == 27:
            quitter()
    for i in range(0, d[0]-haut+1, 2)[::-1]:
        wk = montre_part(im2, pto=[0, i], attente=1, destroy=non)
        if wk == 27:
            quitter()
    montre_part(im2)


def img_chrg() -> None:  # MAIN ##
    try:
        img = ouvre_image(f'{dir}\\{imgs_path}\\{n_img1}')
    except:
        img_cart1()
        img = ouvre_image(f'{dir}\\{imgs_path}\\{n_img1}')
    try:
        if type(img) == None:
            pass
        img_cart1()
        raise Exception
    except:
        img = ouvre_image(f'{dir}\\{imgs_path}\\{n_img1}')
    marron = nouvelle_couleur('122336')
    t = 9
    t2 = 5
    a, b = 3, 2
    if t < t2:
        t = t2+1
    pg = pt_sg(hg, bg, 6)
    pg2 = pt_sg(hg, bg, 6, 4)
    pt1, pt2, pt3, pt4 = pt_sg(hg, ct, a, b), pt_sg(
        hd, ct, a, b), pt_sg(bg, ct, a, b), pt_sg(bd, ct, a, b)
    rectangle(img, pt1, pt4, bois, 0)
    for i in [[pt1, pt3], [pt1, pt2], [pt2, pt4], [pt3, pt4]]:
        ligne(img, i[0], i[1], marron)
    rien=non
    for c in nf:
        if c.lower() in SUPPORTED_CHARS: continue
        else: rien = True;break
    if rien:
        scripte(img, [pt1[0]+35, pt1[1]+80], nf, 1.2, combine=oui, couleur=noir, epaisseur=15)
        scripte(img, [pt1[0]+35, pt1[1]+80], nf, 1.2, combine=oui, couleur=turquoise, epaisseur=5)
    else:
        ecris(img, f'{nf}\n', pg, bd, t, noir, 15)
        ecris(img, f'{nf}\n', pg, bd, t, turquoise, 5)
    ecris(img, f'{aut1}', pg, bd, t-t2, noir, 15)
    ecris(img, f'{aut1}', pg, bd, t-t2, turquoise, 5)
    ecris(img, f'{aut2}', pg2, bd, t-t2, noir, 15)
    ecris(img, f'{aut2}', pg2, bd, t-t2, turquoise, 5)
    sauve_image(n_img_chargement, img, f'{dir}\\{imgs_path}')


if __name__ == '__main__':
    img_chrg()
    img = ouvre_image(f'{imgs_path}\\{n_img_chargement}')
    montre(img)