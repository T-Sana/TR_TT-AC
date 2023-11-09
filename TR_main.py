from TR_setup import setup; setup()
if True: ## Packages ##
    import TR_transitions as trs
    from TR_anim_debut import *
    from TR_cartes import *
    from Depandances.Outils.paths__names__etc import *
    from Depandances._init import *
if True: ## Functs ##
    def runEvent(ev, img=image(), noms=('J1', 'J2')):
        match ev:
            case i if i in list(jeux_dispos.keys()):
                trs.shade(img)
                jeu = jeux_dispos[ev]
                try: result = jeu(j1=noms[0], j2=noms[1], nm=nf, lg='fr', trn=non)
                except: result = jeu(j1=noms[0], j2=noms[1], nm=nf)
                print('Result:', result)
            case None: print('Error')
            case _: raise ValueError(f'Var <ev> of type {type(ev)} with value "{ev}" has a wrong value!\n<ev> should had one of the following values:\n{str(new_line+espace).join(i for i in list(jeux_dispos.keys()))}')
if __name__ == '__main__': ## Main ##
    vel = 4
    if True: ## Vars ##
        img = ouvre_image(f'./{imgs_path}/{n_img2}')
    trs.shade(img_part(img), v=vel)
    anim_debut(img_part(img), v=vel*5)
    trs.shade(img_part(img), v=vel)
    n_j1 = n_j2 = None
    while n_j1 == None or n_j1 == 0 or n_j1 == '' or len(str(n_j1)) > 9:
        n_j1 = visual_input(image(remplissage=turquoise), 'Nom j1: ', 'J1', '', nf)
        if n_j1 == 0 or n_j1 == '': quitter()
        else:
            if len(str(n_j1)) > 9:
                if montre(ecris(image(remplissage=turquoise), 'ERREUR !\nNom trop long,\n longeur max: 9chrs.', hg, bd, 3), nf, 10000, non) == 27: quitter()
            trs.shade(image(remplissage=turquoise))
    while n_j2 == None or n_j2 == 0 or n_j1 == '' or len(str(n_j2)) > 9 or n_j2 == n_j1:
        n_j2 = visual_input(image(remplissage=turquoise), 'Nom j2: ', 'J2', '', nf)
        if n_j2 == 0 or n_j2 == '': quitter()
        else:
            trs.shade(image(remplissage=turquoise))
            if len(str(n_j2)) > 9:
                if montre(ecris(image(remplissage=turquoise), 'ERREUR !\nNom trop long,\n longeur max: 9chrs.', hg, bd, 3), nf, 10000, non) == 27: quitter()
            if n_j2 == n_j1:
                if montre(ecris(image(remplissage=turquoise), f'ERREUR !\nVous ne pouvez vous appeller "{n_j1}",\ncar j1 ({n_j1}) s\'appelle deja ainsi.', hg, bd, 3), nf, 10000, non) == 27: quitter()
    noms = [n_j1, n_j2]
    if montre(ecris(image(remplissage=turquoise), f'Bienvenu.e.s {n_j1} & {n_j2} !\n', hg, bd, 3), nf, 10000, non) == 27: quitter()
    numb = 0; #noms = ['j1', 'j2']
    while True:
        event, img, c = carteVille(j1, j2, numb)
        runEvent(event, img, noms)