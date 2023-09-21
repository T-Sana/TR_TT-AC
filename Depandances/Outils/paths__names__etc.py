from dotenv import load_dotenv; load_dotenv()
try: from Depandances.Outils.cvt import *
except:
    try: from Outils.cvt import *
    except: from cvt import *
import os

def get_dir() -> str:
    return(os.getcwd())
def create_dir_if_unexisting(name, path='./') -> None:
    '''
    :name: name of the file/folder to check existance of\n
    :path: where the file is supposed to be and would be created the file
    '''
    v_dir = os.listdir(path)
    try: v_dir.index(name)
    except: os.mkdir(f"{path}\{name}")

if True: ## Format.vars ##
    new_line = '\n'
    espace = ' '
    BLACK        = "\033[30m"
    RED          = "\033[31m"
    GREEN        = "\033[32m"
    BROWN        = "\033[33m"
    BLUE         = "\033[34m"
    PURPLE       = "\033[35m"
    CYAN         = "\033[36m"
    LIGHT_GRAY   = "\033[37m"
    DARK_GRAY    = "\033[30m"
    LIGHT_RED    = "\033[31m"
    LIGHT_GREEN  = "\033[32m"
    YELLOW       = "\033[33m"
    LIGHT_BLUE   = "\033[34m"
    LIGHT_PURPLE = "\033[35m"
    LIGHT_CYAN   = "\033[36m"
    LIGHT_WHITE  = "\033[37m"
    BOLD         = '\033[1m'
    UNDERLINED   = '\033[4m'
    NORMAL       = '\033[00m' # @@ Always append to the end, else: terminal = BUG @@
    BOLD_RED     = f'{RED}{BOLD}'
    BOLD_GREEN   = f'{GREEN}{BOLD}'
    BOLD_BLUE    = f'{BLUE}{BOLD}'
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
    n_img_chargement = 'img_chrg.jpg'
    n_img1 = 'img1.jpg'
    n_img2 = 'img2.jpg'
    n_img3 = 'img3.jpg'
    n_img4 = 'img4.jpg'
    n_img5 = 'img5.jpg'
    trash = 'Trash'
    imgs = 'Imgs'
    config = 'Config'
    depts_path = 'Depandances' ## Do NOT change ! (unless you know what you are doing) ##
    imgs_path = f'{depts_path}\{imgs}'
    trash_path = f'{depts_path}\{trash}'
    config_path = f'{depts_path}\{config}'
if True: ## Exceptions ##
    class invalidPlace(Exception):
        def __init__(self, file, line):
            path = f'{BOLD_BLUE}{os.getcwd()}\{imgs_path}{NORMAL}'
            path_here = f'{BOLD_BLUE}{os.getcwd()}\TR_setup.py, line {line}{NORMAL}'
            filename = f'{UNDERLINED+BOLD_GREEN}{file}{NORMAL}'
            file = f'{BOLD_RED}FILE{NORMAL}'
            error = f'{BOLD_RED}ERROR WHILE SCANING DIRECTORY{NORMAL}'
            expla = f'{BOLD_RED}SHOULD {UNDERLINED}NOT{NORMAL+BOLD_RED} BE HERE{NORMAL} ({path})'
            issue1 = f'{PURPLE}If{NORMAL} {filename} {BOLD_RED}SHOULD{NORMAL} be in {path}:\n   {NORMAL+LIGHT_CYAN}Add{NORMAL} {filename} into "imgs_to_create" -> {path_here}'
            issue2 = f'File {filename} has been moved from {UNDERLINED+BOLD_GREEN}{imgs_path}{NORMAL} to {UNDERLINED+BOLD_GREEN}{trash_path}{NORMAL}'
            print(f"{error}: {path}\n{file} {filename} {expla}\n{issue1}\n{issue2}\n")
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
            self.ou_ne_peut_etre = copy.deepcopy(ou_ne_peut_etre)
            self.keys = keys
            self.k_h, self.k_b, self.k_d, self.k_g = self.keys
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
    keys = {'keysj1': [2490368, 2621440, 2555904, 2424832], 'keysj2': [119, 115, 100, 97]}
    try:
        with open(f'./{config_path}/keys.txt', 'r') as file: keys = file.read()
    except:
        create_dir_if_unexisting(f'./{config_path}/')
        with open(f'./{config_path}/keys.txt', 'w') as file: file.write(keys)
    configKeys = eval(keys)
j1 = joueur('j1', clrs=[rouge, bleu], t=1.5, keys=configKeys['keysj1'])
j2 = joueur('j2', clrs=[blanc, blanc], t=1.5, keys=configKeys['keysj2'])
joueurs = [j1, j2]