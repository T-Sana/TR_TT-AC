from TR_setup import setup; setup()
if True: ## Packages ##
    from outils.souris import souris as s
    import TR_transitions as trs
    from TR_anim_debut import *
    from TR_cartes import *
    from TR_vars import *
if True: ## Main ##
    trs.shade(ouvre_image(f'./{imgs}/{n_img1}'))
    anim_debut()
    trs.shade(ouvre_image(f'./{imgs}/{n_img1}'))
    #carte1(j1, j2)
    carte2(j1, j2)