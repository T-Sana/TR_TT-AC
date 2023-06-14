from outils.cvt import *
nf = 'JEU_TR'
aut1 = 'Anna Camps'
aut2 = 'Tim Tamet'
class joueur:
    def __str__(self):
        return(self.nom)
    def __init__(self, nom: str, coos=[960, 512], clrs=[[0, 0, 0], [0, 0, 0]], t=1, o=0) -> None:
        self.nom = nom
        self.pos = coos # [x, y]
        self.clrs = clrs
        self.t = t
        self.o = o
    def deplace(self, mouvement=[0, 0]) -> None:
        m = mouvement
        self.pos = [self.pos[0]+m[0], self.pos[1]+m[1]]
    def dessine(self, img=image()) -> None:
        perso(img, self.pos, self.t, self.o, self.clrs[0], self.clrs[1])
    def place(self, pos=None):
        if pos != None:
            self.pos = pos