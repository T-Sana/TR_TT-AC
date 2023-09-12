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
##################################################################################
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
        self.tableaux = []
    def image(self, pos=(-1, -1), sec=False) -> np.array:
        img = self.tableau.img(else_=False)
        cercle(img, ctd, 33, bleu if self.trait else rouge, 0)
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
                    if self.legal(pos, (y, x), self.trait, False, sec):
                        pbg.append((y, x))
            for move in pbg:
                for j, x in enumerate(range2(coos[0][0], coos[1][0], diff(coos[0][0], coos[1][0])/10)):
                    for i, y in enumerate(range2(coos[0][0], coos[1][0], diff(coos[0][1], coos[1][1])/10)):
                        if move[0]==j and move[1]==i:
                            cercle(img, ct_sg((x, y), (x + diff(coos[0][0], coos[1][0])/10, y + diff(coos[0][1], coos[1][1])/10)), 3, vert, 0)
        return(img)
    def montre(self) -> None:
        montre(self.image())
    def legal(self, c1, c2, t, mod=True, sec=False) -> bool:
        x1, y1 = c1
        x2, y2 = c2
        p = self.tableau.tableau[y1, x1]
        if self.tableau.tableau[y2, x2] == 0:
            if t:
                if p == 1:
                    if y1-y2 == 1 and abs(x1-x2) == 1:
                        if sec: return(False)
                        if mod and y2 == 0:
                            self.tableau.tableau[y2, x2] = 11
                            self.tableau.tableau[y1, x1] = 0
                            self.trait = not self.trait
                            return(False)
                        return(True)
                    elif y1-y2 == 2 and abs(x1-x2) == 2:
                        p2 = self.tableau.tableau[(y1+y2)//2, (x1+x2)//2]
                        if p2 == 2 or p2 == 22:
                            self.killed = True
                            if mod:
                                self.tableau.tableau[(y1+y2)//2, (x1+x2)//2] = 0
                                if y2 == 0:
                                    self.tableau.tableau[y2, x2] = 11
                                    self.tableau.tableau[y1, x1] = 0
                                    self.trait = not self.trait
                                    return(False)
                            return(True)
                elif p == 11:
                    if diff(y1, y2) == diff(x1, x2):
                        a, b = [], []
                        for y in range(y1+(1 if y2>y1 else -1), y2, 1 if y2>y1 else -1):
                            a.append(y)
                        for x in range(x1+(1 if x2>x1 else -1), x2, 1 if x2>x1 else -1): 
                            b.append(x)
                        pts = [[a[n], b[n]] for n in range(len(a))]
                        for n, pt in enumerate(pts):
                            y, x = pt
                            p = self.tableau.tableau[y, x]
                            if p != 0 and n < len(pts)-1:
                                return(False)
                            elif p != 0:
                                if p == (1 if self.trait else 2) or p == (11 if self.trait else 22):
                                    return(False)
                                elif mod:
                                    self.tableau.tableau[y, x] = 0
                                self.killed = True
                            elif p == 0 and n == len(pts)-1:
                                if not sec: return(True)
                                else: return(False)
                        return(True)
            else:
                if p == 2:
                    if y2-y1 == 1 and abs(x1-x2) == 1:
                        if sec: return(False)
                        if mod and y2 == 9:
                            self.tableau.tableau[y2, x2] = 22
                            self.tableau.tableau[y1, x1] = 0
                            self.trait = not self.trait
                            return(False)
                        return(True)
                    elif y2-y1 == 2 and abs(x1-x2) == 2:
                        p2 = self.tableau.tableau[(y1+y2)//2, (x1+x2)//2]
                        if p2 == 1 or p2 == 11:
                            self.killed = True
                            if mod:
                                self.tableau.tableau[(y1+y2)//2, (x1+x2)//2] = 0
                                if y2 == 9:
                                    self.tableau.tableau[y2, x2] = 22
                                    self.tableau.tableau[y1, x1] = 0
                                    self.trait = not self.trait
                                    return(False)
                            return(True)
                elif p == 22:
                    if diff(y1, y2) == diff(x1, x2):
                        a, b = [], []
                        for y in range(y1+(1 if y2>y1 else -1), y2, 1 if y2>y1 else -1):
                            a.append(y)
                        for x in range(x1+(1 if x2>x1 else -1), x2, 1 if x2>x1 else -1): 
                            b.append(x)
                        pts = [[a[n], b[n]] for n in range(len(a))]
                        for n, pt in enumerate(pts):
                            y, x = pt
                            p = self.tableau.tableau[y, x]
                            if p != 0 and n < len(pts)-1:
                                return(False)
                            elif p != 0:
                                if p == (1 if not self.trait else 2) or p == (11 if not self.trait else 22):
                                    return(False)
                                elif mod:
                                    self.tableau.tableau[y, x] = 0
                                self.killed = True
                            elif p == 0:
                                if not sec: return(True)
                                else: return(False)
                        return(True)
        return(False)
    def peut_kill(self, coos, t, tableau=None) -> bool:
        if tableau == None: tableau = self.tableau.tableau
        self.save_killed, self.killed = self.killed, False
        for y in range(10):
            for x in range(10):
                if self.legal(coos, (y, x), t, False):
                    if self.killed:
                        self.killed = self.save_killed
                        return(True)
        self.killed = self.save_killed
        return(False)
    def move(self, killed=False, coos=None) -> None:
        self.tableau.imprime()
        if coos == None:
            sec = False
            while True:
                coos = self.tableau.getcase(self.nom, self.image())
                p = self.tableau.tableau[coos[1], coos[0]]
                if self.trait:
                    if (p == 2 or p == 22) and not killed:
                        if self.peut_kill(coos, not self.trait):
                            killed = True
                            self.tableau.tableau[coos[1], coos[0]] = 0
                    elif p == 1 or p == 11: break
                else:
                    if (p == 1 or p == 11) and not killed:
                        if self.peut_kill(coos, not self.trait):
                            killed = True
                            self.tableau.tableau[coos[1], coos[0]] = 0
                    elif p == 2 or p == 22: break
        else:
            if not self.peut_kill(coos, self.trait): return(None)
            sec = True
        coos2 = self.tableau.getcase(self.nom, self.image(coos, sec))
        leg = self.legal(coos, coos2, self.trait, True, sec)
        if leg:
            self.tableau.tableau[coos2[1], coos2[0]] = self.tableau.tableau[coos[1], coos[0]]
            self.tableau.tableau[coos[1], coos[0]] = 0
            if not self.peut_kill(coos2, self.trait) or not self.killed:
                self.trait = not self.trait
            else:
                return(coos2)
        elif sec: self.trait = not self.trait
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
            self.tableaux.append(self.tableau.tableau)
            self.killed, killed = False, self.killed
            coos = self.move(killed, coos)
        if self.trait: ## Noirs ont gagné
            return([0, 1])
        else: ##
            return([1, 0])
if __name__ == '__main__':
    a = dames()
    print(a.jouer())