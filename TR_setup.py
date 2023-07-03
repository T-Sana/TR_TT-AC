from dotenv import load_dotenv; load_dotenv()
from outils.paths__names__etc import *
from TR_imageaison import img_cart1, img_cart2, Maine
from outils.cvt import *
from outils.pip import *
from inspect import currentframe

nf = os.getenv('nomJeu') # nf = NomFenêtre
if True: ## KeyConfig ##
    keyConfig = {'keysj1': [2490368, 2621440, 2555904, 2424832], 'keysj2': [119, 115, 100, 97]}
if True: ## Format + def montre_img_charg() ##
    print('\n', end='')
    def montre_img_charg(action='', steps=0, taille=2.7) -> None:
        t_steps = 20
        if steps > t_steps: steps = t_steps
        img_chrg = ouvre_image(f'{dir}/{imgs}/{n_img_chargement}')
        ecris(img_chrg, action, cg, p4, taille, noir, 10/4*taille)
        a, b = 3, 7; dst = 75
        b_c_c = [pt_sg(cg, ct_sg(bg, bd), a, b), pt_sg(cd, ct_sg(bg, bd), a, b)]
        b1, b2 = [[b_c_c[0][0], b_c_c[0][1]-25], [b_c_c[1][0], b_c_c[1][1]+25]]
        b3, b4 = [[b_c_c[0][0], b_c_c[0][1]-25], [b_c_c[0][0]+(b_c_c[1][0]-b_c_c[0][0])/t_steps*steps, b_c_c[1][1]+25]]
        rectangle(img_chrg, b3, b4, rouge, 0)
        rectangle(img_chrg, b1, b2, noir)
        ecris(img_chrg, f'{round(steps/t_steps*100)}%', [b1[0], b1[1]+dst], [b2[0], b2[1]+dst], taille/2, noir, 10/2/4*taille)
        montre(img_chrg, nf, 1, non)
        time.sleep(0.05)
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
    def install_dependencies(packages_to_install=[], packages_to_update=[], steps=0) -> None:
        for i in ['pip']:
            update(i)
            montre_img_charg(f'Updating {i}', steps)
            steps += 1
        for i in packages_to_install:
            install(i)
            montre_img_charg(f'Installing {i}', steps)
            steps += 1
        for i in packages_to_update:
            update(i)
            montre_img_charg(f'Updating {i}', steps)
            steps += 1
        return(steps)
    def create_dir_if_unexisting(name, path='./', where='./') -> None:
        v_dir = os.listdir(where)
        try: v_dir.index(name)
        except: os.mkdir(f"{path}{name}")
##########
## MAIN ##
##########
def setup():
    steps = 0
    if True: ## Packages.vars ##
        montre_img_charg(f'Creating Packages.vars', steps)
        steps += 1
        packages_to_install = ['opencv-python', 'numpy', 'python-dotenv']
        packages_installed = get_installed_packages()
        c_packages_to_install = copy.deepcopy(packages_to_install)
    if True: ## Imgs.vars ##
        montre_img_charg(f'Creating Imgs.vars', steps)
        steps += 1
        line = currentframe().f_lineno+1
        imgs_to_create = {n_img1: img_cart1, n_img2: img_cart2}
    if True: ## Checking Imgs/ ##
        create_dir_if_unexisting('Imgs')
    Maine() ################## Creates the chrg_img (À y changer d'endroit et de nom)
    montre_img_charg(f'Checking ./Imgs/', steps)
    steps += 1
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
            montre_img_charg(f'Checking {i}', steps)
            steps += 1
        for i in imgs_to_create:
            imgs_to_create[i]()
            montre_img_charg(f'Creating {i}', steps)
            steps += 1
    if True: ## Discard installed packages ##
        for i in c_packages_to_install:
            for j in packages_installed:
                if j == i:
                    packages_to_install.remove(i)
                    montre_img_charg(f'Checking {j} == {i}', steps)
                    steps += 1
    if True: ## Install required packages
        steps = install_dependencies(packages_to_install, [], steps)
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
setup()
time.sleep(2)
montre_img_charg('Finishing', 18)
time.sleep(0.5)
montre_img_charg('Finished!', 20)
while True:
    wk = attend_touche(1)
    if wk == 27: break