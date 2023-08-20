from cvt import *
from outils.souris import souris

def clicked_in(pos, boutton): ## Is pos between boutton[0] (haut gauche) and boutton[1] (bas droite) ##
    a_l_interieur = pos[0] >= boutton[0][0] and pos[0] <= boutton[1][0] and pos[1] >= boutton[0][1] and pos[1] <= boutton[1][1]
    return(a_l_interieur)
class nom:
    nom = 'Puissance4'
class puissance4:
    def __str__(self):
        return(self.nom)
    def __init__(self, nom='1', j1='j1', j2='j2'):
        tableau = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
        self.nom = str(nom)
        self.j1 = str(j1)
        self.j2 = str(j2)
        self.points_j1 = 0
        self.points_j2 = 0
        self.tableau = np.array(tableau)
        self.trait = True
        self.traite = True
        colones = []
        nb = len(tableau[0])
        x_g = 500
        lg_tb = 1920-840
        ht_tb = 1080
        for i in range(nb):
            colones.append([[x_g - (lg_tb/nb)*0.5 + (lg_tb/nb)*i, 0], [x_g - (lg_tb/nb)*0.5 + (lg_tb/nb)*(i+1), ht_tb]])
        self.colones = np.array(colones)
        files = []
        nb = len(tableau)
        for i in range(nb):
            files.append([[self.colones[0, 0, 0], (ht_tb/nb)*i], [self.colones[-1, -1, 0], (ht_tb/nb)*(i+1)]])
        self.files = np.array(files)
    def rejouer(self):
        tableau = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
        self.tableau = np.array(tableau)
        self.traite = not self.traite
        self.trait = self.traite
    def imprime(self):
        for i in self.tableau:
            out = ''
            for j in i:
                out += str(j)
            print(out)
    def image(self):
        img = image(remplissage=nouvelle_couleur('303030'))
        t = self.tableau
        for i in self.colones:
            rectangle(img, i[0], i[1], vert, 0)
            rectangle(img, i[0], i[1])
        for i in self.files:
            rectangle(img, i[0], i[1])
        for y in range(len(t)):
            for x in range(len(t[y])):
                case = [[self.colones[x][0][0], self.files[y][0][1]], [self.colones[x][1][0], self.files[y][1][1]]]
                if t[y, x] != 0:
                    cercle(img, ct_sg(case[0], case[1]), dist(case[0], case[1])/3.5, rouge if t[y, x] == 2 else bleu, 0)
        ecris(img, f'J1\n{self.points_j1}\n\n', [0, 0], p3, 5, turquoise, 15)
        ecris(img, f'J2\n{self.points_j2}\n\n', p2, [long, haut], 5, turquoise, 15)
        cercle(img, ct_sg([0, haut/2], p3), 60, bleu if self.trait else rouge, 0)
        cercle(img, ct_sg([long, haut/2], p4), 60, bleu if self.trait else rouge, 0)
        return(img)
    def move(self):
        t = self.tableau
        wk = 0
        while wk != 27:
            wk = souris_sur_image(self.image(), souris.get_souris, self.nom, 1, False)
            for i in range(len(self.colones)):
                if clicked_in(souris.pos, self.colones[i]):
                    souris.pos = [-1, -1]
                    wk = 'break'
                    break
            if wk == 'break':
                break
        if wk == 27:
            return('exit')
        for j in range(len(t)-1, -1, -1):
            case = t[j, i]
            if case == 0:
                t[j, i] = 1 if self.trait else 2
                self.trait = not self.trait
                return(True)
    def jouable(self):
        zz = False
        t = self.tableau
        for i in t:
            for j in i:
                if j == 0:
                    zz = True
                if zz: break
            if zz: break
        if not zz: return(0)
        for j in range(len(t)):
            for i in range(len(t[j])):
                arrs = []
                try:
                    if len(t[j:j+4, i]) == 4:
                        arrs.append(t[j:j+4, i])
                except Exception as e: pass
                try:
                    if len(t[j, i:i+4]) == 4:
                        arrs.append(t[j, i:i+4])
                except Exception as e: pass 
                try:
                    truc = []
                    for p in range(4):
                        truc.append(t[j+p, i+p])
                    if len(truc) == 4:
                        arrs.append(truc)
                except Exception as e: pass
                try:
                    truc = []
                    for p in range(4):
                        if j-p >= 0:
                            truc.append(t[j-p, i+p])
                    if len(truc) == 4:
                        arrs.append(truc)
                except Exception as e: pass
                for i in arrs:
                    if len(i) != 4: continue
                    if np.array_equal(i, np.array([1, 1, 1, 1])):
                        self.points_j1 += 1
                        return(1)
                    elif np.array_equal(i, np.array([2, 2, 2, 2])):
                        self.points_j2 += 1
                        return(2)
        return(True)
    def debut(self):
        moves = 0
        while True:
            jb = self.jouable()
            if type(jb) == int:
                return(jb)
            elif not jb: ## If injouable ##
                break
            else:
                q = self.move()
                moves += 1 if q else 0
                if q == 'exit':
                    return('exit')
    def jouer(self):
        while True:
            rp = self.debut()
            if rp == 'exit':
                return(self)
            elif type(rp) == bool and rp:
                break
            self.rejouer()
        return(self)
def start():
    jeu = puissance4('jeu')
    jeu.jouer()
    ferme(str(jeu))
#start()