if True: ## Prerequisites ##
    from outils.install_dependencies import install_dependencies as i_dep
    #i_dep() ## Only on new machines @@ Installs the game's dependencies @@
if True: ## Packages ##
    from TR_IMAGEAISON import img_cart1 as img1, demo_img2; img1()
    from outils.souris import souris as s
    import TR_transitions as trs
    from TR_anim_debut import *
    from TR_cartes import *
    from TR_titre import *
    from TR_VARS import *
if True: ## Building | Etc ##
    pass
if True: ## Main ##
    titre()
    trs.shade(img)
    j1, j2 = anim_debut()
    trs.shade(img)
    carte1(j1, j2)
    demo_img2()
    