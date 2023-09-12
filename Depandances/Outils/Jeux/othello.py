from cvt import *
from outils.souris import souris
class nom:
    nom = 'Othello'
##################################
## Règles ########################
##################################
## Il faut capturer pour jouer ###
## Si on ne le peut, on passe ####
## Si aucun des deux joueurs ne ##
## peut jouer, la partie finit ###
## La couleur + présente gagne ###
##################################

##################################
## TODO ##########################
## Afficher comptage des points ##
## Caisses des joueurs ###########
## Indicateur de trait amélioré ##
##################################

end = 'End'

class othello:
    def __str__(self):
        return(self.nom)
    def __init__(self, nom=nom.nom, j1='j1', j2='j2'):
        self.nb_pts = 0
        self.nom = str(nom)
        self.j1 = str(j1)
        self.j2 = str(j2)
        self.ptsj1 = 0
        self.ptsj2 = 0
        self.pts_blanc = 0
        self.pts_noir = 0
        tableau = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 1, 0, 0, 0],
            [0, 0, 0, 1, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.tableau = np.array(tableau)
        self.trait = True
        self.restant = 64
        colones = []
        nb = len(tableau[0])
        lg_tb = 1920-840
        ht_tb = 1080
        x_g = 0 + (lg_tb/nb)*0.5
        for i in range(nb):
            colones.append([[x_g - (lg_tb/nb)*0.5 + (lg_tb/nb)*i, 0], [x_g - (lg_tb/nb)*0.5 + (lg_tb/nb)*(i+1), ht_tb]])
        self.colones = np.array(colones)
        files = []
        nb = len(tableau)
        for i in range(nb):
            files.append([[self.colones[0, 0, 0], (ht_tb/nb)*i], [self.colones[-1, -1, 0], (ht_tb/nb)*(i+1)]])
        self.files = np.array(files)
        self.image()
    def rejouer(self):
        tableau = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 1, 0, 0, 0],
            [0, 0, 0, 1, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.pts_blanc = 0
        self.pts_noir = 0
        self.tableau = np.array(tableau)
        self.trait = True
        self.restant = 64
        self.j1, self.j2 = self.j2, self.j1
    def image(self):
        t = self.tableau
        img = image(remplissage=nouvelle_couleur('303030'))
        rectangle(img, self.colones[0, 0], self.colones[-1, -1], vert, 0)
        for i in range(len(self.colones)):
            rectangle(img, self.colones[i, 0], self.colones[i, -1])
        for i in range(len(self.files)):
            rectangle(img, self.files[i, 0], self.files[i, -1])
        nb = len(self.tableau[0])
        lg_tb = 1920-840
        ht_tb = 1080
        x_g = 0 + (lg_tb/nb)*0.5
        p1, p2, p3, p4 = [0, 0], [x_g - (lg_tb/nb)*0.5 + (lg_tb/nb)*nb, 0], [0, haut], [x_g - (lg_tb/nb)*0.5 + (lg_tb/nb)*nb, haut]
        ct = ct_cr(p1, p2, p3, p4)
        for i in [p1, p2, p3, p4]:
            cercle(img, ct_sg(i, ct), epaisseur*1.5, noir, 0)
        p1, p2, p3, p4 = [self.colones[-1, -1, 0], 0], [long, 0], self.colones[-1, -1], [long, haut]
        ch, cg, cd, cb = ct_sg(p1, p2), ct_sg(p1, p3), ct_sg(p2, p4), ct_sg(p3, p4)
        ct = ct_cr(p1, p2, p3, p4)
        case = [[self.colones[0][0][0], self.files[0][0][1]], [self.colones[0][1][0], self.files[0][1][1]]]
        cercle(img, ct, dist(case[0], case[1])/3.5, noir if self.trait else blanc, 0)
        for i in [p1, p2, p3, p4]: point(img, i, nouvelle_couleur('ff50ff'))
        for i in [ch, cg, cd, cb]: point(img, i, cyan)
        for i in [ct]: point(img, i, jaune)
        for y in range(len(t)):
            for x in range(len(t[y])):
                case = [[self.colones[x][0][0], self.files[y][0][1]], [self.colones[x][1][0], self.files[y][1][1]]]
                if t[y, x] != 0:
                    cercle(img, ct_sg(case[0], case[1]), dist(case[0], case[1])/3.5, noir if t[y, x] == 1 else blanc, 0)
        return(img)
    def legal(self, x, y, lkng=False):
        t = self.tableau
        leg = False
        dirs = [
            (-1, -1), ( 0, -1), ( 1, -1),
            (-1,  0),           ( 1,  0),
            (-1,  1), ( 0,  1), ( 1,  1)
        ]
        for i, j in dirs:
            l = False
            try:
                for d in range(1, 8):
                    r1 = y+j*d
                    r2 = x+i*d
                    if r1 < 0 or r2 < 0 or r1 > 7 or r2 > 7: break
                    try:
                        c = t[y+j*d, x+i*d]
                    except: d -= 1 ; c = t[y+j*d, x+i*d]
                    if c == (2 if self.trait else 1):
                        l = True
                    elif c == (1 if self.trait else 2) and l:
                        if not lkng:
                            for r in range(1, d):
                                t[y+j*r, x+i*r] = 1 if self.trait else 2
                        leg = True
                        break
                    else: break
            except Exception as ERREUR: print(ERREUR)
        return(leg)
    def jouable(self):
        moves = False
        for i in range(len(self.tableau)):
            for j in range(len(self.tableau[i])):
                if self.tableau[i, j] == 0 and self.legal(i, j, True):
                    moves = True
                if moves: break
            if moves: break
        if not moves:
            self.trait = not self.trait
            for i in range(len(self.tableau)):
                for j in range(len(self.tableau[i])):
                    if self.tableau[i, j] == 0 and self.legal(i, j, True):
                        moves = True
                    if moves: break
                if moves: break
            if not moves:
                return(end)
        return('Continue')
    def move(self):
        wk = 0
        while True:
            ver = self.jouable()
            if ver == end:
                return(end)
            img = self.image()
            wk = souris_sur_image(img, souris.get_souris, self.nom, 1, non)
            for i in range(len(self.tableau)):
                for j in range(len(self.tableau[i])):
                    if souris.clicked_in(self.colones[j]) and souris.clicked_in(self.files[i]):
                        if self.tableau[i, j] == 0:
                            if self.legal(j, i):
                                self.tableau[i, j] = 1 if self.trait else 2
                                self.trait = not self.trait
                                self.restant -= 1
                                break
            souris.pos = souris.dehors
            '''ver = self.jouable()
            if ver == end:
                return(end)'''
            if wk == 27:
                return('exit')
    def end(self):
        img = self.image()
        montre_img(img, self.nom)
        b = n = 0
        for i in range(8):
            for j in range(8):
                if self.tableau[i, j] == 1: n += 1
                elif self.tableau[i, j] == 2: b += 1
        self.pts_blanc += b
        self.pts_noir += n
        self.nb_pts += 1
        taille = 3
        txt = ''
        if b == n:
            txt += 'Égalité !'
        else:
            gagnant = 'noirs' if n > b else 'blancs'
            txt += f'Les {gagnant} gagnent\n({max(b, n)}-{min(b, n)})'
        b = self.pts_blanc
        n = self.pts_noir
        if b == n:
            txt += '\n\nÉgalité !'
        else:
            gagnant = 'noirs' if n > b else 'blancs'
            txt = f'\n\nLes {gagnant} gagnent\n({max(b, n)}-{min(b, n)})'
        txt += f'\nNb_pts{self.nb_pts}'
        rectangle(img, ct_sg(p1, c1), ct_sg(p4, c4), nouvelle_couleur('50A0C0'), 0)
        rectangle(img, ct_sg(p1, c1), ct_sg(p4, c4), nouvelle_couleur('206070'))
        ecris(img, txt, ct_sg(p1, c1), ct_sg(p4, c4), 2)
        montre(img)
    def jouer(self):
        while True:
            r = self.move()
            if r == 'exit':
                return(None)
            elif r == end:
                self.end()
                self.rejouer()
def start(nom=nom.nom, j1='j1', j2='j2'):
    jeu = othello(nom, j1, j2)
    jeu.jouer()
    ferme(jeu.nom)