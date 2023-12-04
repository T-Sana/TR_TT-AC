from outils.tableau import *

class nom:
    nom = 'Bombardement'
    
if True: ## result "errors" ##
    class J1_gagne(Exception):
        def __init__(self, msg) -> None:
            self.msg = msg
        def __repr__(self) -> str:
            return(self.msg)
    class J2_gagne(Exception):
        def __init__(self, msg) -> None:
            self.msg = msg
        def __repr__(self) -> str:
            return(self.msg)
    class Egalite(Exception):
        def __init__(self, msg) -> None:
            self.msg = msg
        def __repr__(self) -> str:
            return(self.msg)

class bombardement:
    def __init__(self, nom=nom.nom, j1='j1', j2='j2'):
        self.expl = 'explose'
        self.nom = nom
        t = tableau(d=[8, 8])
        for j in [0, 1]:
            for i in range(len(t.tableau[j])):
                t.tableau[j, i] = 2
        for j in [-1, -2]:
            for i in range(len(t.tableau[j])):
                t.tableau[j, i] = 1
        self.tableau = t
        self.trait = True
    def legal(self, x1, y1, x2, y2):
        if x1 == x2 and y1 == y2:
            return(self.expl)
        if self.tableau.tableau[y2, x2] == 0:
            if self.tableau.tableau[y1, x1] == 1:
                if y2 - y1 == -1:
                    if abs(x1 - x2) <= 1:
                        return(True)
            elif self.tableau.tableau[y1, x1] == 2: 
                if y2 - y1 == 1:
                    if abs(x1 - x2) <= 1:
                        return(True)
        return(False)
    def move(self):
        x1, y1 = self.tableau.getcase()
        img = self.tableau.img()
        for j in range(len(self.tableau.files)):
            for i in range(len(self.tableau.colonnes)):
                hg, bd = [self.tableau.colonnes[i, 0, 0], self.tableau.files[j, 0, 1]], [self.tableau.colonnes[i, 1, 0], self.tableau.files[j, 1, 1]]
                try:
                    if self.legal(x1, y1, i, j) and self.tableau.tableau[y1, x1] == (1 if self.trait else 2):
                        cercle(img, ct_sg(hg, bd), dist(hg, bd)//10, nouvelle_couleur('800080'), 0)
                except: pass
        x2, y2 = self.tableau.getcase(img=img)
        if self.tableau.tableau[y1, x1] == (1 if self.trait else 2):
            if x1 >= 0 and y1 >= 0 and x2 >= 0 and y2 >= 0:
                mov = self.legal(x1, y1, x2, y2)
                if mov == self.expl:
                    l = [
                        [-1, -1], [ 0, -1], [ 1, -1],
                        [-1,  0], [ 0,  0], [ 1,  0],
                        [-1,  1], [ 0,  1], [ 1,  1]
                    ]
                    for i in l:
                        try:
                            if y1 + i[1] >= 0 and x1 + i[0] >= 0:
                                self.tableau.tableau[y1 + i[1], x1 + i[0]] = 0
                        except: continue
                    self.trait = not self.trait
                elif mov:
                    self.tableau.tableau[y2, x2] = self.tableau.tableau[y1, x1]
                    self.tableau.tableau[y1, x1] = 0
                    self.trait = not self.trait
    def jouer(self):
        while True:
            try:
                a = b = False
                t = self.tableau.tableau
                for j in range(len(t)):
                    for i in range(len(t[j])):
                        if t[j, i] == 1: a = True
                        elif t[j, i] == 2: b = True
                if not a and not b:
                    raise Egalite('Egalite')
                elif not a:
                    raise J1_gagne('Victoire')
                elif not b:
                    raise J2_gagne('Victoire')
                else:
                    self.move()
            except J1_gagne:
                a.tableau.result('Les bleus\ngagnent')
            except J2_gagne:
                a.tableau.result('Les Rouges\ngagnent')
            except Egalite:
                a.tableau.result('Égalité')
def start(nom=nom.nom, j1='j1', j2='j2'):
    a = bombardement(nom, j1, j2)
    a.jouer()

if __name__ == '__main__':
    start()