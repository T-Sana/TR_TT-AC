from dotenv import load_dotenv; load_dotenv()
try: from outils.cvt import *
except: from cvt import *
import os

def get_dir() -> str:
    return(os.getcwd())
def create_dir_if_unexisting(name, path='./', where='./') -> None:
    v_dir = os.listdir(where)
    try: v_dir.index(name)
    except: os.mkdir(f"{path}{name}")

if True: ## KeyConfig ##
    keyConfig = {'keysj1': [2490368, 2621440, 2555904, 2424832], 'keysj2': [119, 115, 100, 97]}
if True: ## Checking Config ##
    create_dir_if_unexisting('Config')
    if True: ## Creating Config/keys.txt ##
        v_dir = os.listdir('./Config')
        try: v_dir.index('keys.txt')
        except:
            with open("./Config/keys.txt", "w") as file:
                file.write(str(keyConfig))
if True: ## keys ##
    key_a = 97
    key_d = 100
    key_w = 119
    key_s = 115

    key_arr_l = 2424832
    key_arr_r = 2555904
    key_arr_u = 2490368
    key_arr_d = 2621440
if True: ## Paths ##
    dir = get_dir()
    n_img_chargement='img_chrg.jpg'
    n_img1='img1.jpg'
    n_img2='img2.jpg'
    n_img3='img3.jpg'
    n_img4='img4.jpg'
    n_img5='img5.jpg'
    imgs='Imgs'
if True: ## Noms ##
    nf = os.getenv('nomJeu') # nf = NomFenêtre
    aut1 = os.getenv('aut1')
    aut2 = os.getenv('aut2')
    if aut1 == None: aut1 = 'Author1'
    if aut2 == None: aut2 = 'Author2'
if True: ## persos ##
    class joueur:
        def __str__(self):
            return(self.nom)
        def __init__(self, nom: str, coos=ct, clrs=[blanc, blanc], t=1, o=0, keys=[key_arr_u, key_arr_d, key_arr_r, key_arr_l], ou_peut_etre=[hg, bd], ou_ne_peut_etre=[]) -> None:
            self.ou_peut_etre = [ou_peut_etre if type(ou_peut_etre[0][0]) == int or type(ou_peut_etre[0][0]) == float else i for i in ou_peut_etre]
            self.ou_ne_peut_etre = ou_ne_peut_etre
            self.keys = keys
            self.k_h, self.k_b, self.k_d, self.k_g = self.keys
            print([self.k_h, self.k_b, self.k_d, self.k_g])
            self.nom = nom
            self.pos = coos # [x, y]
            self.clrs = clrs
            self.t = t
            self.o = o
        def deplace(self, mouvement=[0, 0]) -> None:
            for i in self.ou_peut_etre:
                if clicked_in([self.pos[0]+mouvement[0], self.pos[1]+mouvement[1]], i):
                    for i in self.ou_ne_peut_etre:
                        if clicked_in([self.pos[0]+mouvement[0], self.pos[1]+mouvement[1]], i):
                            return(None)
                    self.pos = list([self.pos[0]+mouvement[0], self.pos[1]+mouvement[1]])
                    return(None)
        def dessine(self, img=image()) -> None:
            perso(img, self.pos, self.t, self.o, self.clrs[0], self.clrs[1])
            return(img)
        def place(self, pos=None):
            if pos != None:
                self.pos = list(pos)
if True: ## Keys.vars ##
    with open('./Config/keys.txt', 'r') as file:
        keys = file.read()
        print(keys)
    configKeys = eval(keys)
j1 = joueur('j1', clrs=[rouge, bleu], t=1.5, keys=configKeys['keysj1'])
j2 = joueur('j2', clrs=[blanc, blanc], t=1.5, keys=configKeys['keysj2'])