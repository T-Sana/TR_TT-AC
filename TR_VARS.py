from outils.cvt import *
nf = 'JEU_TR'
aut1 = 'Anna Camps'
aut2 = 'Tim Tamet'
class joueur:
    def __str__(self):
        return(self.nom)
    def __init__(self, nom: str, coos=ct, clrs=[blanc, blanc], t=1, o=0) -> None:
        self.nom = nom
        self.pos = coos # [x, y]
        self.clrs = clrs
        self.t = t
        self.o = o
    def deplace(self, mouvement=[0, 0]) -> None:
        if clicked_in([self.pos[0]+mouvement[0], self.pos[1]+mouvement[1]], [hg, bd]):
            self.pos = [self.pos[0]+mouvement[0], self.pos[1]+mouvement[1]]
    def dessine(self, img=image()) -> None:
        perso(img, self.pos, self.t, self.o, self.clrs[0], self.clrs[1])
    def place(self, pos=None):
        if pos != None:
            self.pos = pos
j1 = joueur('j1', clrs=[blanc, blanc], t=1.5)
j2 = joueur('j2', clrs=[blanc, blanc], t=1.5)