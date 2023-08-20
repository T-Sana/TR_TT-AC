#####################
## Projet :Morpion ##
## Auteur : T-sana ##
## Date : 5/5/2023 ##
#####################

##########
## TODO ##
##########

## If var à la def de la partie :
## >>> Max 3 pièces par équipe ## (en déplacer si'il y en avait plus que 3)

##########
##/TODO/##
##########
class nom:
    nom = 'Morpion'
if True: ## Imports ##
    import cv2
    from cvt import *
    from outils.souris import souris
if oui: ## Functions ##
    def clicked_in(pos, boutton): ## Is pos between boutton[0] (haut gauche) and boutton[1] (bas droite) ##
        a_l_interieur = pos[0] >= boutton[0][0] and pos[0] <= boutton[1][0] and pos[1] >= boutton[0][1] and pos[1] <= boutton[1][1]
        return(a_l_interieur)
if oui: ## Classes ##
    class morpion:
        def __str__(self):
            return(self.nom)
        def __init__(self, nom='partie 1'):
            self.points_j1 = self.points_j2 = 0 ## 
            self.nom = nom
            table = [
                ['_', '_', '_'],
                ['_', '_', '_'],
                ['_', '_', '_']
            ]
            cases = [
                [
                    [p1, pt_sg(p1, p2, 2), pt_sg(p1, p3, 2), pt_sg(p1, p4, 2)], ## 00
                    [pt_sg(p1, p2, 2), pt_sg(p2, p1, 2), pt_sg(p1, p4, 2), pt_sg(p2, p3, 2)], ## 01
                    [pt_sg(p2, p1, 2), p2, pt_sg(p2, p3, 2), pt_sg(p2, p4, 2)]  ## 02
                ],
                [
                    [pt_sg(p1, p3, 2), pt_sg(p1, p4, 2), pt_sg(p3, p1, 2), pt_sg(p3, p2, 2)], ## 10
                    [pt_sg(p1, p4, 2), pt_sg(p2, p3, 2), pt_sg(p3, p2, 2), pt_sg(p4, p1, 2)], ## 11
                    [pt_sg(p2, p3, 2), pt_sg(p2, p4, 2), pt_sg(p4, p1, 2), pt_sg(p4, p2, 2)]  ## 12
                ],
                [
                    [pt_sg(p3, p1, 2), pt_sg(p3, p2, 2), p3, pt_sg(p3, p4, 2)], ## 20
                    [pt_sg(p3, p2, 2), pt_sg(p4, p1, 2), pt_sg(p3, p4, 2), pt_sg(p4, p3, 2)], ## 21
                    [pt_sg(p4, p1, 2), pt_sg(p4, p2, 2), pt_sg(p4, p3, 2), p4]  ## 22
                ]
            ]
            self.table = np.array(table)
            self.cases = np.array(cases)
            self.trait = True
            self.image()
        def image(self):
            if oui: ## Couleurs ##
                bois = nouvelle_couleur('355080')
                gris = nouvelle_couleur('353535')
            img = image(remplissage=nouvelle_couleur('303030'))
            if oui: ## Dessin ##
                rectangle(img, p1, p4, gris, 0)
                rectangle(img, p1, p4, bois, 10)
                rectangle(img, pt_sg(p1, p4, 2), p4, bois, 10)
                rectangle(img, p1, pt_sg(p1, p4, 1, 2), bois, 10)
                rectangle(img, pt_sg(p2, p3, 2), p3, bois, 10)
                rectangle(img, p2, pt_sg(p2, p3, 1, 2), bois, 10)
                t = '/' if self.trait else '0'
                ecris(img, f'J1\n{self.points_j1}\n\n{t}', [0, 0], p3, 5, turquoise, 15)
                ecris(img, f'J2\n{self.points_j2}\n\n{t}', p2, [long, haut], 5, turquoise, 15)
                for j in range(len(self.table)):
                    for i in range(len(self.table[j])):
                        c = self.table[j, i]
                        case = self.cases[j, i]
                        if not c == '_':
                            ecris(img, c, case[0], case[3], 15, vert, 20, police=cv2.FONT_HERSHEY_SIMPLEX)
            self.img = img
        def jouable(self):
            t = self.table
            for j in range(len(t)): ## Get poses de victoire ##
                c = []
                c.append(t[0, 0:3])
                c.append(t[1, 0:3])
                c.append(t[2, 0:3])
                c.append(t[0:3, 0])
                c.append(t[0:3, 1])
                c.append(t[0:3, 2])
                c.append([t[0, 0], t[1, 1], t[2, 2]])
                c.append([t[0, 2], t[1, 1], t[2, 0]])
            for i in c: ## Y'a-t-il un·e gagnant·e ? ##
                x = o = 0
                for a in i:
                    if a.lower() == 'x': ## Compte les 'x' en ligne ##
                        x += 1
                    elif a.lower() == 'o': ## Compte les 'o' en ligne ##
                        o += 1
                if x == 3: return('x') ## Victoire des x ##
                elif o == 3: return('o') ## Victoire des o ##
            plein = True ## Vérification qu'il y a encore de l'espace où jouer ##
            for i in self.table:
                for j in i:
                    if j == '_' or j == ' ': ## Si la case est vide ##
                        plein = False
            if plein: ## Égalité ##
                return('_')
        def get_case(self):
            for j in range(len(self.cases)): ## Séléction des bords de la case ##
                for i in range(len(self.cases[j])): ## Séléction des bords de la case ##
                    if clicked_in(souris.pos, [self.cases[j, i][0], self.cases[j, i][-1]]): ## Si cliqué sur la case ##
                        if self.table[j, i] == '_' or self.table[j, i]== ' ': ## Si la case est vide ##
                            self.table[j, i] = 'x' if self.trait else 'o' ## Met la pièce ##
                            self.trait = not self.trait ## Joue le suivant ##
            souris.pos = [-1, -1] ## Hors l'écran ##
        def move(self):
            img_plein_ecran(self.nom)
            wk = souris_sur_image(self.img, souris.get_souris, self.nom, 1, False)
            self.get_case()
            self.image()
            if wk == 27:
                return(True)
        def rejouer(self, winner):
            table = [
                ['_', '_', '_'],
                ['_', '_', '_'],
                ['_', '_', '_']
            ]
            if winner == 'x':
                self.points_j1 += 1
            elif winner == 'o':
                self.points_j2 += 1
            self.table = np.array(table)
            self.trait = True if winner == 'o' else False if winner == 'x' else self.trait
            self.image()
        def jouer(self):
            while True:
                stop = self.move()
                if stop:
                    break
                r = self.jouable()
                if r == 'x' or r == 'o' or r == '_':
                    self.rejouer(r)
def start():
    jeu = morpion()
    jeu.jouer()
    ferme(str(jeu))

#start()