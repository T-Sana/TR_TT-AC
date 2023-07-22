from TR_setup import setup; setup() ## Don't comment this line, it could break if the files are not fine.
if True: ## Packages ##
    import TR_transitions as trs
    from TR_anim_debut import *
    from TR_cartes import *
    from Depandances.Outils.paths__names__etc import *
    from Depandances._init import *
if True: ## Functs ##
    def runEvent(ev):
        match ev:
            case i if i in jeux_dispos: print(ev)
            case None: print('Error')
            case _: raise ValueError(f'Var <ev> of type {type(ev)} with value {ev} has a wrong value!')
if True: ## Main ##
    '''trs.shade(ouvre_image(f'./{imgs_path}/{n_img1}'))
    anim_debut()
    trs.shade(ouvre_image(f'./{imgs_path}/{n_img1}'))'''
    while True:
        event = carteVille(j1, j2)
        runEvent(event)