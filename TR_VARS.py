## pakgs ##
from outils.directoires import *
from outils.cvt import *
## dir ##
dir = get_dir()
imgs = 'Imgs'
n_img1 = 'img1.jpg'
## noms ##
nf = 'JEU_TR'
aut1 = 'Anna Camps'
aut2 = 'Tim Tamet'
## persos ##
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
        return(img)
    def place(self, pos=None):
        if pos != None:
            self.pos = pos
j1 = joueur('j1', clrs=[blanc, blanc], t=1.5)
j2 = joueur('j2', clrs=[blanc, blanc], t=1.5)
## keys ##
key_a = 97
key_d = 100
key_w = 119
key_s = 115

key_arr_l = 2424832
key_arr_r = 2555904
key_arr_u = 2490368
key_arr_d = 2621440