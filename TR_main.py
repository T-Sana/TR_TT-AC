from TR_setup import setup; #setup()
if True: ## Packages ##
    import TR_transitions as trs
    from TR_anim_debut import *
    from TR_cartes import *
    from Depandances.Outils.paths__names__etc import *
    from Depandances._init import *
if True: ## Functs ##
    def runEvent(ev, img=image()):
        match ev:
            case i if i in list(jeux_dispos.keys()):
                trs.shade(img)
                jeu = jeux_dispos[ev]
                jeu()
            case None: print('Error')
            case _: raise ValueError(f'Var <ev> of type {type(ev)} with value "{ev}" has a wrong value!\n<ev> should had one of the following values:\n{str(new_line+espace).join(i for i in list(jeux_dispos.keys()))}')
if True: ## Vars ##
    img = ouvre_image(f'./{imgs_path}/{n_img2}')
if True: ## Main ##
    '''trs.shade(img)
    anim_debut(img)
    trs.shade(img)'''
    while True:
        event, img = carteVille(j1, j2)
        runEvent(event, img)