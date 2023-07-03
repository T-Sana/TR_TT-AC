from TR__init import *
from outils.pip import *
from inspect import currentframe
from outils.paths__names__etc import *
from TR_imageaison import img_cart1, img_cart2, img_chrg
from outils.cvt import *

nf = os.getenv('nomJeu') # nf = NomFenêtre
if True: ## KeyConfig ##
    keyConfig = {'keysj1': [2490368, 2621440, 2555904, 2424832], 'keysj2': [119, 115, 100, 97]}
if True: ## Format + def montre_img_charg() ##
    print('\n', end='')
    def montre_img_charg(action='', steps=0, taille=1.2) -> None:
        t_steps = 20
        if steps > t_steps: steps = t_steps
        img_chrg = ouvre_image(f'{dir}/{imgs}/{n_img_chargement}')
        a, b = 3, 7; dst = 75
        b_c_c = [pt_sg(cg, ct_sg(bg, bd), a, b), pt_sg(cd, ct_sg(bg, bd), a, b)]
        b1, b2 = [[b_c_c[0][0], b_c_c[0][1]-25], [b_c_c[1][0], b_c_c[1][1]+25]]
        b3, b4 = [[b_c_c[0][0], b_c_c[0][1]-25], [b_c_c[0][0]+(b_c_c[1][0]-b_c_c[0][0])/t_steps*steps, b_c_c[1][1]+25]]
        rectangle(img_chrg, b3, b4, rouge, 0)
        rectangle(img_chrg, b1, b2, noir)
        ecris(img_chrg, f'{round(steps/t_steps*100)}%', [b1[0], b1[1]+dst], [b2[0], b2[1]+dst], 2.7/2, noir, 10/2/4*2.7)
        b1, b2 = [[b1[0], b1[1]+dst], [b2[0], b2[1]+dst]]; dst = 50
        ecris(img_chrg, action, [b1[0], b1[1]+dst], [b2[0], b2[1]+dst], taille, noir, 10/5*taille)
        montre(img_chrg, nf, 1, non)
        time.sleep(rd.random()*0.1)
if True: ## Format.vars ##
    red = '\033[91m'
    green = '\033[92m'
    blue = '\033[96m'
    bold = '\033[1m'
    underlined = '\033[4m'
    bold_red = f'{red}{bold}'
    bold_blue = f'{blue}{bold}'
    bold_green = f'{green}{bold}'
    normal = '\033[00m'
if True: ## Functs ##
    def create_dir_if_unexisting(name, path='./', where='./') -> None:
        v_dir = os.listdir(where)
        try: v_dir.index(name)
        except: os.mkdir(f"{path}{name}")
##########
## MAIN ##
##########
def setup():
    steps = 0
    if True: ## Imgs.vars ##
        line = currentframe().f_lineno+1
        imgs_to_create = {n_img_chargement: img_chrg, n_img1: img_cart1, n_img2: img_cart2}
    if True: ## Checking Imgs/ ##
        create_dir_if_unexisting('Imgs')
    if True: ## Checking imgs to create in Imgs/ ##
        for i in os.listdir(".\Imgs"):
            try: imgs_to_create.pop(i); steps += 1
            except:
                path = f'{bold_blue}{os.getcwd()}\IMGS{normal}'
                path_here = f'{bold_blue}{os.getcwd()}\TR_setup.py, line {line}{normal}'
                filename = f'{underlined}{bold_green}{i}{normal}'
                file = f'{bold_red}FILE{normal}'
                error = f'{bold_red}ERROR WHILE SCANING DIRECTORY{normal}'
                expla = f'{bold_red}SHOULD {underlined}NOT{normal+bold_red} BE HERE{normal} ({path})'
                issue = f'If {filename} {bold_red}SHOULD{normal} be in {path}:\nAdd {filename} into "imgs_to_create" -> {path_here}'
                print(f"{error}: {path}\n{file} {filename} {expla}\n{issue}\n")
        for i in imgs_to_create:
            imgs_to_create[i]()
            montre_img_charg(f'Creating {i}', steps)
            steps += 1
    if True: ## Checking Config ##
        montre_img_charg(f'Checking ./Config/', steps)
        steps += 1
        create_dir_if_unexisting('Config')
    if True: ## Creating Config/keys.txt ##
        v_dir = os.listdir('./Config')
        try: v_dir.index('keys.txt')
        except:
            with open("./Config/keys.txt", "w") as file:
                file.write(str(keyConfig))
    time.sleep(rd.random()*1.3)
    montre_img_charg('Finishing', 18)
    time.sleep(rd.random()*0.5)
    montre_img_charg('Finished!', 20)
    while True:
        wk = attend_touche(1)
        if wk != -1: break
#setup()