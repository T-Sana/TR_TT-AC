if True: ## Imports ##
    try: from cvt import *
    except:
        try: from Jeux.cvt import *
        except:
            try: from Outils.Jeux.cvt import *
            except: from Depandances.Outils.Jeux.cvt import *
    try: from outils.tableau import *
    except:
        try: from Jeux.outils.tableau import *
        except:
            try: from Outils.Jeux.outils.tableau import *
            except: from Depandances.Outils.Jeux.outils.tableau import *
    try: from outils.souris import *
    except:
        try: from Jeux.outils.souris import *
        except:
            try: from Outils.Jeux.outils.souris import *
            except: from Depandances.Outils.Jeux.outils.souris import *
### TODO #########################################################################
## BUG : qd une piece bouche la case d'arv de là où une de ses propres ###########
## pièces aurait pû en capturant une pièce adverse, cela empêche le prog #########
## de voir qu'il aurait pû captirer kla pièce et ne peut être souflée par l'adv ##
##################################################################################
## BUG : qd une pièce bouge là où elle pourra capturer une pièce au mouve suiv ###
## elle peut se faire souffler ###################################################
class dames:
    def __init__(self, j1='j1', j2='j2', nom='dames') -> None:
        self.j1 = j1
        self.j2 = j2
        self.nom = nom
        self.trait = True
        self.tableau = tableau('dames', [10, 10])
        for y in range(4):
            for x in range(10):
                if y%2==x%2:
                    self.tableau.tableau[y, x] = 2
        for y in range(4):
            for x in range(10):
                if (y+1)%2==x%2:
                    self.tableau.tableau[9-y, x] = 1
        self.killed = False
    def image(self, pos=(-1, -1)) -> np.array:
        img = self.tableau.img(else_=False)
        coos = (self.tableau.colonnes[0, 0], self.tableau.colonnes[-1, -1])
        for j, x in enumerate(range2(coos[0][0], coos[1][0], diff(coos[0][0], coos[1][0])/10)):
            for i, y in enumerate(range2(coos[0][0], coos[1][0], diff(coos[0][1], coos[1][1])/10)):
                if pos[0]==j and pos[1]==i:
                    rectangle(img, (x, y), (x + diff(coos[0][0], coos[1][0])/10, y + diff(coos[0][1], coos[1][1])/10), vert, 3)
        for j, x in enumerate(range2(coos[0][0], coos[1][0], diff(coos[0][0], coos[1][0])/10)):
            for i, y in enumerate(range2(coos[0][0], coos[1][0], diff(coos[0][1], coos[1][1])/10)):
                p = self.tableau.tableau[i, j]
                if p == 11 or p == 22:
                    ct_case = ct_sg((x, y), (x + diff(coos[0][0], coos[1][0])/10, y + diff(coos[0][1], coos[1][1])/10))
                    cercle(img, ct_case, 33, bleu if p == 11  else rouge, 0)
                    for ang in range(0, 360, 90):
                        ligne(img, ct_case, coosCercle(ct_case, 15, ang), noir, 3)
        if pos != (-1, -1):
            pbg = []
            for y in range(10):
                for x in range(10):
                    if self.legal(pos, (y, x), self.trait, False):
                        pbg.append((y, x))
            for move in pbg:
                for j, x in enumerate(range2(coos[0][0], coos[1][0], diff(coos[0][0], coos[1][0])/10)):
                    for i, y in enumerate(range2(coos[0][0], coos[1][0], diff(coos[0][1], coos[1][1])/10)):
                        if move[0]==j and move[1]==i:
                            cercle(img, ct_sg((x, y), (x + diff(coos[0][0], coos[1][0])/10, y + diff(coos[0][1], coos[1][1])/10)), 3, vert, 0)
        return(img)
    def montre(self) -> None:
        montre(self.image())
    def legal(self, c1, c2, t, mod=True) -> bool:
        x1, y1 = c1
        x2, y2 = c2
        if self.tableau.tableau[y2, x2] == 0:
            if t:
                if self.tableau.tableau[y1, x1] == 1:
                    if y1-y2 == 1 and abs(x1-x2) == 1:
                        if mod and y2 == 0:
                            self.tableau.tableau[y1, x1] = 11
                        return(True)
                    elif y1-y2 == 2 and abs(x1-x2) == 2:
                        if self.tableau.tableau[(y1+y2)//2, (x1+x2)//2] == 2:
                            if mod:
                                self.tableau.tableau[(y1+y2)//2, (x1+x2)//2] = 0
                                self.killed = True
                                if y2 == 0:
                                    self.tableau.tableau[y1, x1] = 11
                            return(True)
                elif self.tableau.tableau[y1, x1] == 11:
                    if abs(y1-y2) == abs(x1-x2):
                        for y in range(min(y1, y2), max(y1, y2)):
                            for x in range(min(x1, x2), max(x1, x2)):
                                pass
            else:
                if self.tableau.tableau[y1, x1] == 2:
                    if y2-y1 == 1 and abs(x1-x2) == 1:
                        if mod and y2 == 9:
                            self.tableau.tableau[y1, x1] = 22
                        return(True)
                    elif y2-y1 == 2 and abs(x1-x2) == 2:
                        if self.tableau.tableau[(y1+y2)//2, (x1+x2)//2] == 1:
                            if mod:
                                self.tableau.tableau[(y1+y2)//2, (x1+x2)//2] = 0
                                self.killed = True
                                if y2 == 9:
                                    self.tableau.tableau[y1, x1] = 22
                            return(True)
                elif self.tableau.tableau[y1, x1] == 2: pass
        return(False)
    def peut_kill(self, coos, t) -> bool:
        for y in range(10):
            for x in range(10):
                if self.legal(coos, (y, x), t, False):
                    if abs(x-coos[1]) == 2 == abs(y-coos[0]):
                        return(True)
        return(False)
    def move(self, killed=False, coos=None) -> None:
        self.tableau.imprime()
        print(self.trait)
        if coos == None:
            while True:
                coos = self.tableau.getcase(self.nom, self.image())
                if self.trait:
                    if self.tableau.tableau[coos[1], coos[0]] == 2 and not killed:
                        if self.peut_kill(coos, not self.trait):
                            killed = True
                            self.tableau.tableau[coos[1], coos[0]] = 0
                    elif self.tableau.tableau[coos[1], coos[0]] == 1: break
                else:
                    if self.tableau.tableau[coos[1], coos[0]] == 1 and not killed:
                        if self.peut_kill(coos, not self.trait):
                            killed = True
                            self.tableau.tableau[coos[1], coos[0]] = 0
                    elif self.tableau.tableau[coos[1], coos[0]] == 2: break
        coos2 = self.tableau.getcase(self.nom, self.image(coos))
        leg = self.legal(coos, coos2, self.trait)
        if leg:
            self.tableau.tableau[coos2[1], coos2[0]] = self.tableau.tableau[coos[1], coos[0]]
            self.tableau.tableau[coos[1], coos[0]] = 0
            if not self.peut_kill(coos2, self.trait) or not self.killed:
                self.trait = not self.trait
            else:
                return(coos2)
        return(None)
    def jouable(self):
        for j in range(10):
            for i in range(10):
                p = self.tableau.tableau[j, i]
                if (p == 1 and self.trait) or (p == 2 and not self.trait):
                    for y in range(10):
                        for x in range(10):
                            if self.legal((i, j), (x, y), self.trait, False):
                                return(True)
        return(False)
    def jouer(self):
        coos = None
        while self.jouable():
            self.killed, killed = False, self.killed
            coos = self.move(killed, coos)
        if self.trait: ## Noirs ont gagné
            return([0, 1])
        else: ##
            return([1, 0])
a = dames()
print(a.jouer())