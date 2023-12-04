try: from cvt import *
except:
    try: from Jeux.cvt import *
    except:
        try: from Outils.Jeux.cvt import *
        except: from Depandances.Outils.Jeux.cvt import *
        
if oui: ## Fonctions ##
    def liste_pts_sg(p1, p2, n_pts): ## Returne une liste ayant n_pts équidistants sur le ségment donné ##
            pts = []
            for i in range(n_pts):
                pts.append(pt_sg(p1, p2, i, n_pts))
            return(pts)
    def liste_nbs_sg(a, b, n_sgs): ## Returne une liste avec len() = n_sgs ## La liste contient les numéros de (a->b)/i for i in n_sgs ##
        diff = abs(a-b)
        dist = diff/n_sgs
        c = min(a, b)
        nbs = []
        for i in range(n_sgs+1):
            nbs.append(c+dist*i)
        return(nbs)
    def liste_numbs(start, end, step=1): ## Comme celle de ci dessus ## ## WHY??? ##
        num = np.linspace(start, end,(end-start)*int(1/step)+1).tolist()
        return [round(i, 2) for i in num]
    def rectangle_dist(img, p1=ct, dists=[50, 50], couleur=vert, epaisseur=epaisseur): ## Dessine un réctangles à partir d'un point & deux longeurs ##
        rectangle(img, p1, (int(p1[0] + dists[0]), int(p1[1] + dists[1])), couleur, epaisseur)
        return(img)
    def clicked_in(pos, boutton): ## Is pos between boutton[0] (haut gauche) and boutton[1] (bas droite) ##
        a_l_interieur = pos[0] >= boutton[0][0] and pos[0] <= boutton[1][0] and pos[1] >= boutton[0][1] and pos[1] <= boutton[1][1]
        return(a_l_interieur)