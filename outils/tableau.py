try: from functs import *
except: from outils.functs import *
import numpy as np
from outils.cvt import *
try:
    import outils.souris as s
except:
    import souris as s

marron_clair = [77, 113, 181]
marron_clair2 = [30, 60, 120]
marron_fonce = [37, 53, 101]

class tableau:
    def __array__(self):
        return(self.tableau)
    def __init__(self, nom='tableau', d=[8, 8], pts=[[0, 0], [1080, 0], [0, 1080], [1080, 1080]], ab=[10, 3], r=0):
        for i in d:
            if type(i) != int:
                raise TypeError(f'Received the object {i} of {type(i)} and not of the required {int}.')
        self.a, self.b = ab
        self.r = r
        self.mxl = 1
        self.nom = nom
        t = []
        for i in range(d[0]):
            t.append([])
            for j in range(d[1]):
                t[i].append(r)
        self.tableau = np.array(t, dtype=object)
        if pts != None:
            self.p1, self.p2, self.p3, self.p4 = pts
        if d != None:
            h, l = d
            self.files(h)
            self.colonnes(l)
    def __str__(self):
        for i in self.tableau:
            for j in i:
                if len(str(j)) > self.mxl:
                    self.mxl = len(str(j))
        lg = len(str(len(self.tableau)))
        m = '-'*lg + '-'
        esp = ' '
        out = f'*{esp*(lg-1)} |'
        for j in range(len(self.tableau[0])):
            l = len(chr(j+65))
            out += f'{chr(j+65)}{esp*(self.mxl-l)} '
        out = out[:len(out)-1]
        out += f'| {esp*(lg-1)}*'
        out += f'\n{m}+' + '-'*(self.mxl+1)*(len(self.tableau[0])-1) + '-'*(self.mxl) + f'+{m}\n{len(self.tableau)} |'
        for j in range(len(self.tableau)):
            for i in range(len(self.tableau[j])):
                l = len(str(self.tableau[j, i]))
                out += f'{str(self.tableau[j, i])}{esp*(self.mxl-l)} '
            out = out[:len(out)-1]
            out += f'| {esp*(lg-len(str(len(self.tableau)-(j))))}{len(self.tableau)-(j)}\n{esp*(lg-len(str(len(self.tableau)-(j+1))))}{len(self.tableau)-(j+1)} |'
        out = out[:len(out)-(3+lg)]
        out += f'\n{m}+' + '-'*(self.mxl+1)*(len(self.tableau[0])-1) + '-'*(self.mxl) + f'+{m}\n*{esp*(lg-1)} |'
        for j in range(len(self.tableau[0])):
            l = len(chr(j+65))
            out += f'{chr(j+65)}{esp*(self.mxl-l)} '
        out = out[:len(out)-1]
        out += f'| {esp*(lg-1)}*'
        return(out)
    def imprime(self):
        print(self.__str__())
    def files(self, n):
        ct = ct_cr(self.p1, self.p2, self.p3, self.p4)
        c1, c2 = pt_sg(self.p1, ct, self.a, self.b), pt_sg(self.p2, ct, self.a, self.b)
        long = abs(c1[0]-c2[0])
        d = long/n
        f = []
        for i in range2(0, long, d):
            f.append([[c1[0], c1[1]+round(i)], [c1[0]+long, c1[1]+round(i+d)]])
        self.files = np.array(f)
    def colonnes(self, n):
        ct = ct_cr(self.p1, self.p2, self.p3, self.p4)
        c1, c3 = pt_sg(self.p1, ct, self.a, self.b), pt_sg(self.p3, ct, self.a, self.b)
        haut = abs(c1[1]-c3[1])
        d = haut/n
        c = []
        for i in range2(0, haut, d):
            c.append([[c1[0]+round(i), c1[1]], [c1[0]+round(i+d), c1[1]+haut]])
        self.colonnes = np.array(c)
    def img_(self, c1=noir, c2=blanc, cf=bois, cg=nouvelle_couleur('804000', 'rgb'), ep_g=2):
        img = image()
        rectangle(img, self.p1, self.p4, cf, 0)
        rectangle(img, self.p1, self.p4, cg)
        for j in range(len(self.files)):
            for i in range(len(self.colonnes)):
                hg, bd = [self.colonnes[i, 0, 0], self.files[j, 0, 1]], [self.colonnes[i, 1, 0], self.files[j, 1, 1]]
                cl = c1 if i%2 == j%2 else c2
                rectangle(img, hg, bd, cl, 0)
        for hg, bd in self.colonnes: rectangle(img, hg, bd, cg, ep_g)
        for hg, bd in self.files: rectangle(img, hg, bd, cg, ep_g)
        return(img)
    def img(self, c1=noir, c2=blanc, cf=bois, cg=nouvelle_couleur('804000', 'rgb'), ep_g=2):
        img = image()
        rectangle(img, self.p1, self.p4, cf, 0)
        rectangle(img, self.p1, self.p4, cg)
        for j in range(len(self.files)):
            for i in range(len(self.colonnes)):
                hg, bd = [self.colonnes[i, 0, 0], self.files[j, 0, 1]], [self.colonnes[i, 1, 0], self.files[j, 1, 1]]
                cl = c1 if i%2 == j%2 else c2
                rectangle(img, hg, bd, cl, 0)
                try:
                    t = self.tableau[j, i]
                    tl, tlm = 10, 3
                    if t == 1:
                        cercle(img, ct_sg(hg, bd), dist(hg, bd)//tl*tlm, bleu, 0)
                    elif t == 2:
                        cercle(img, ct_sg(hg, bd), dist(hg, bd)//tl*tlm, rouge, 0)
                    elif t == 0:
                        pass
                    else:
                        ecris(img, self.tableau[j, i], hg, bd, 2, turquoise)
                except: pass
        for hg, bd in self.colonnes: rectangle(img, hg, bd, cg, ep_g)
        for hg, bd in self.files: rectangle(img, hg, bd, cg, ep_g)
        return(img)
    def getcase(self, nom=None, img=None):
        if nom == None: nom = self.nom
        try:
            if img == None: img = self.img()
        except: pass
        while True:
            cv2.namedWindow(nom, cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty(nom, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.setMouseCallback(nom, s.souris.get_souris)
            cv2.imshow(nom, img)
            wk = cv2.waitKey(10)
            if wk == 27: cv2.destroyAllWindows(); raise SystemExit
            x, y = s.souris.case_clicked_in(self.files, self.colonnes)
            if x != -1 and y != -1:
                break
        s.souris.pos = s.souris.dehors
        return(x, y)
    def getcol(self, nom=None, img=None):
        if nom == None: nom = self.nom
        if img == None: img = self.img()
        while True:
            cv2.namedWindow(nom, cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty(nom, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.setMouseCallback(nom, s.souris.get_souris)
            cv2.imshow(nom, img)
            wk = cv2.waitKey(10)
            if wk == 27: cv2.destroyAllWindows(); raise SystemExit
            x = s.souris.clicked_in_list_bts(self.colonnes)
            if x != -1:
                break
        s.souris.pos = s.souris.dehors
        return(x)
    def getfil(self, nom=None, img=None):
        if nom == None: nom = self.nom
        if img == None: img = self.img()
        while True:
            cv2.namedWindow(nom, cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty(nom, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.setMouseCallback(nom, s.souris.get_souris)
            cv2.imshow(nom, img)
            wk = cv2.waitKey(10)
            if wk == 27: cv2.destroyAllWindows(); raise SystemExit
            y = s.souris.clicked_in_list_bts(self.file)
            if y != -1:
                break
        s.souris.pos = s.souris.dehors
        return(y)
    def montre(self):
        wk = montre(self.img(), self.nom)
        if wk == 27: cv2.destroyAllWindows(); raise SystemExit
    def place(self, x=0, y=0, place=None, cond=None):
        if place == None: return(False)
        if cond != None:
            if self.tableau[y, x] == cond:
                self.tableau[y, x] = place
            else: return(False)
        else: self.tableau[y, x] = place
        return(True)
    def result(self, text):
        img = self.img()
        hg, bd = self.files[0][0], self.files[-1][1]
        ct = ct_sg(hg, bd)
        a, b = 5, 3
        c1, c2 = pt_sg(hg, ct, a, b), pt_sg(bd, ct, a, b)
        rectangle(img, c1, c2, marron_clair, 0)
        rectangle(img, c1, c2, marron_fonce)
        ecris(img, text, c1, c2, 3, noir)
        montre(img)

t = tableau(d=[10, 10])
for i in range(len(t.tableau)):
    for j in range(len(t.tableau[i])):
        if i%2 == j%2:
            if i <= 3:
                t.tableau[i, j] = 2
            elif i >= 10-4:
                t.tableau[i, j] = 1
t.imprime()
t.getcase()