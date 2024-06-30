try:
    points_p_g = 10  # Points pour gagner 10 par défaut #

    class ENDGAME(Exception):
        def __init__(self, *args: object) -> None:
            super().__init__(*args)

    class points:
        def __init__(self) -> None:
            self.j1 = 0
            self.j2 = 0

        def update(self, points):
            self.j1 += points[0]
            self.j2 += points[1]
    compteur = points()
    from TR_setup import setup
    setup()
    if True:  # Packages ##
        import TR_transitions as trs
        from TR_anim_debut import *
        from TR_cartes import *
        from Depandances.Outils.paths__names__etc import *
        from Depandances._init import *
    if True:  # Functs ##
        def runEvent(ev, img=image(), noms=('J1', 'J2')):
            match ev:
                case i if i in list(jeux_dispos.keys()):
                    trs.shade(img)
                    jeu = jeux_dispos[ev]
                    try:
                        result = jeu(j1=noms[0], j2=noms[1], nm=nf, lg='fr', trn=non)
                    except:
                        result = jeu(j1=noms[0], j2=noms[1], nm=nf)
                    compteur.update(result)
                case None: print('Error')
                case _: raise ValueError(f'Var <ev> of type {type(ev)} with value "{ev}" has a wrong value!\n<ev> should had one of the following values:\n{str(new_line+espace).join(i for i in list(jeux_dispos.keys()))}')
    if __name__ == '__main__':  # Main ##
        vel = 4
        if True:  # Vars ##
            img = ouvre_image(f'./{imgs_path}/{n_img2}')
        trs.shade(img_part(img), v=vel)
        anim_debut(img_part(img), v=vel*5)
        trs.shade(img_part(img), v=vel)
        n_j1 = n_j2 = None
        while n_j1 == None or n_j1 == 0 or n_j1 == '' or len(str(n_j1)) > 9:
            n_j1 = visual_input(image(remplissage=turquoise), 'Nom j1: ', 'J1', '', nf)
            if n_j1 == 0 or n_j1 == '':
                quitter()
            else:
                if len(str(n_j1)) > 9:
                    if montre(ecris(image(remplissage=turquoise), 'ERREUR !\nNom trop long,\n longeur max: 9chrs.', hg, bd, 3), nf, 10000, non) == 27:
                        quitter()
                trs.shade(image(remplissage=turquoise))
        while n_j2 == None or n_j2 == 0 or n_j1 == '' or len(str(n_j2)) > 9 or n_j2 == n_j1:
            n_j2 = visual_input(image(remplissage=turquoise), 'Nom j2: ', 'J2', '', nf)
            if n_j2 == 0 or n_j2 == '':
                quitter()
            else:
                trs.shade(image(remplissage=turquoise))
                if len(str(n_j2)) > 9:
                    if montre(ecris(image(remplissage=turquoise), 'ERREUR !\nNom trop long,\n longeur max: 9chrs.', hg, bd, 3), nf, 10000, non) == 27:
                        quitter()
                if n_j2 == n_j1:
                    if montre(ecris(image(remplissage=turquoise), f'ERREUR !\nVous ne pouvez vous appeller "{n_j1}",\ncar j1 ({n_j1}) s\'appelle deja ainsi.', hg, bd, 3), nf, 10000, non) == 27:
                        quitter()
        noms = [n_j1, n_j2]
        if montre(ecris(image(remplissage=turquoise), f'Bienvenu.e.s {n_j1} & {n_j2} !\n', hg, bd, 3), nf, 10000, non) == 27:
            quitter()
        j1.nom = n_j1
        j2.nom = n_j2
        numb = 0
        while True:
            event, img, c = carteVille(
                j1, j2, numb, [compteur.j1, compteur.j2])
            runEvent(event, img, noms)
            if points_p_g in [compteur.j1, compteur.j2]:
                break
        text = f'Le.a gagnant.e est\n{j1.nom if compteur.j1 > compteur.j2 else j2.nom} !!!\nFelicitations'
        montre(ecris(ouvre_image(f'{imgs_path}/{n_img1}'), text, taille=3))
        raise ENDGAME
except KeyboardInterrupt: pass
except ENDGAME:
    if points_p_g in [compteur.j1, compteur.j2]:
        print(f'\033[1;34m{str(j1.nom if compteur.j1 > compteur.j2 else j2.nom).upper()} \033[1;32mWON \033[1;31m!\033[00m')
except Exception as e:
    import traceback as tb
    import os
    err = '\n'.join(er for er in tb.format_exception(e))
    with open(f'{os.path.dirname(__file__)}/Infos/Logs.log', 'a', encoding='utf8') as file:
        file.write('\n'+'-'*50+'\n'+err)
    print(f'AN EXCEPTION OCCURRED\n\tRefer to \033[1;4;36m{os.path.dirname(__file__)}/Infos/Logs.log\033[00m')
finally:
    print(f'\033[1;34mGAME \033[1;32mENDED \033[1;31m!\033[00m')