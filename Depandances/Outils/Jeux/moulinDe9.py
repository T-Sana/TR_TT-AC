from cvt import *
from outils.souris import souris as s

class moulin9:
    def __str__(self):
        return(self.nom)
    def __init__(self, nom='moulin9', j1='j1', j2='j2'):
        self.nom = nom
        self.j1 = j1
        self.j2 = j2
        self.f = 2*2
        self.tableau = {
            'a':{
                '1':0, 'h':0, '2':0,
                'g':0,        'd':0,
                '3':0, 'b':0, '4':0
            },
            'b':{
                '1':0, 'h':0, '2':0,
                'g':0,        'd':0,
                '3':0, 'b':0, '4':0
            },
            'c':{
                '1':0, 'h':0, '2':0,
                'g':0,        'd':0,
                '3':0, 'b':0, '4':0
            }
        }
        self.fase = 0
        print('Phase de Pose')
        self.trait = True
        while True:
            self.imprimme()
            
            self.move()
    def legal0(self, p):
        if self.tableau[p[0]][p[1]] == 0:
            return(True)
        else: return(False)
    def legal1(self, p1, p2):
        if self.tableau[p2[0]][p2[1]] != 0: return(False)
        c1, c2 = p1[0], p2[0]
        w1, w2 = p1[1], p2[1]
        p = self.tableau[p1[0]][p1[1]]
        if p == (2 if self.trait else 1): return(False)
        leg = False
        if c1 == c2:
            if w1 == w2:
                return(False) ## Le mouvement vise de là où la pièce part ##
            if w1 == 'h':
                if w2 == '1' or w2 == '2':
                    leg = True
            elif w1 == 'g':
                if w2 == '1' or w2 == '3':
                    leg = True
            elif w1 == 'd':
                if w2 == '2' or w2 == '4':
                    leg = True
            elif w1 == 'b':
                if w2 == '3' or w2 == '4':
                    leg = True
            elif w1 == '1':
                if w2 == 'h' or w2 == 'g':
                    leg = True
            elif w1 == '2':
                if w2 == 'h' or w2 == 'd':
                    leg = True
            elif w1 == '3':
                if w2 == 'g' or w2 == 'b':
                    leg = True
            elif w1 == '4':
                if w2 == 'd' or w2 == 'b':
                    leg = True
        if w1.isalpha() and w2.isalpha() and w1 == w2:
            if c1 == 'b' and c2 != 'b':
                leg = True
            elif c1 == 'a' and c2 == 'b':
                leg = True
            elif c1 == 'c' and c2 == 'b':
                leg = True
        return(leg)
    def imprimme(self):
        t = self.tableau
        a = 'a'
        b = 'b'
        c = 'c'
        h = 'h'
        d = 'd'
        g = 'g'
        _1 = '1'
        _2 = '2'
        _3 = '3'
        _4 = '4'
        s = f'''
{t[a][_1]}------------{t[a][h]}------------{t[a][_2]}
|            |            |
|   {t[b][_1]}--------{t[b][h]}--------{t[b][_2]}   |
|   |        |        |   |
|   |   {t[c][_1]}----{t[c][h]}----{t[c][_2]}   |   |
|   |   |         |   |   |
{t[a][g]}---{t[b][g]}---{t[c][g]}         {t[c][d]}---{t[b][d]}---{t[a][d]}
|   |   |         |   |   |
|   |   {t[c][_3]}----{t[c][b]}----{t[c][_4]}   |   |
|   |        |        |   |
|   {t[b][_3]}--------{t[b][b]}--------{t[b][_4]}   |
|            |            |
{t[a][_3]}------------{t[a][b]}------------{t[a][_4]}
'''
        print(s)
    def move(self):
        if self.fase == 0:
            while True:
                try:
                    p1 = input()[0:2]
                    for i in p1[0]:
                        if i == 'a' or i == 'b' or i == 'c':
                            a1 = True
                            break
                    for i in p1[1]:
                        if i == '1' or i == '2' or i == '3' or i == '4' or i == 'h' or i == 'g' or i == 'b' or i == 'd':
                            a2 = True
                            break
                    if a1 and a2 :
                        pass
                except:
                    print('Invalid entry')
                else:
                    break
            if self.legal0(p1):
                self.tableau[p1[0]][p1[1]] = 1 if self.trait else 2
                self.trait = not self.trait
                self.f -= 1
                if self.f == 0:
                    self.fase = 1
                print('Phase de Mouvement')
        else:
            while True:
                try:
                    p1, p2 = input()[0:2], input()[0:2]
                    for i in p1[0]:
                        if i == 'a' or i == 'b' or i == 'c':
                            a1 = True
                            break
                    for i in p1[1]:
                        if i == '1' or i == '2' or i == '3' or i == '4' or i == 'h' or i == 'g' or i == 'b' or i == 'd':
                            a2 = True
                            break
                    for i in p2[0]:
                        if i == 'a' or i == 'b' or i == 'c':
                            b1 = True
                            break
                    for i in p2[1]:
                        if i == '1' or i == '2' or i == '3' or i == '4' or i == 'h' or i == 'g' or i == 'b' or i == 'd':
                            b2 = True
                            break
                    if a1 and a2 and b1 and b2:
                        pass
                except:
                    print('Invalid entry')
                else:
                    break
            if self.legal1(p1, p2):
                self.tableau[p2[0]][p2[1]] = self.tableau[p1[0]][p1[1]]
                self.tableau[p1[0]][p1[1]] = 0
                self.trait = not self.trait
a = moulin9()