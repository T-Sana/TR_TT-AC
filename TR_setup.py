from TR__init import * ## Doit être le premier import à faire ##
import shutil
from Depandances.Outils.cvt import *
from TR_imageaison import img_cart1, img_cart2, img_chrg
from inspect import currentframe
from Depandances.Outils.pip import *
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image ## Même si pas esthétique l'importer après @tkinter@ au risque de faire péter le programme ##
from Depandances.Outils.paths__names__etc import * ## L'importer après @tkinter@ au risque de faire péter le programme ##
import os
print(f'\033[1;32mRunning \033[1;35mfrom \033[1;4;36m{os.path.dirname(__file__)}\033[00m')

if True:  # Format + def montre_img_charg() ##
    def montre_img_charg(action='', steps=0, taille=1.2) -> None:
        t_steps = 20
        if steps > t_steps:
            steps = t_steps
        img_chrg = ouvre_image(f'{dir}\\{imgs_path}\\{n_img_chargement}')
        print(f'\033[1;32mOpening \033[1;36m{n_img_chargement}{NORMAL} \033[1;35mfrom {CYAN+BOLD+UNDERLINED}{dir}\\{imgs_path}\\{NORMAL}')
        a, b = 3, 7
        dst = 75
        b_c_c = [pt_sg(cg, ct_sg(bg, bd), a, b),
                 pt_sg(cd, ct_sg(bg, bd), a, b)]
        b1, b2 = [[b_c_c[0][0], b_c_c[0][1]-25], [b_c_c[1][0], b_c_c[1][1]+25]]
        b3, b4 = [[b_c_c[0][0], b_c_c[0][1]-25], [b_c_c[0][0] + (b_c_c[1][0]-b_c_c[0][0])/t_steps*steps, b_c_c[1][1]+25]]
        rectangle(img_chrg, b3, b4, rouge, 0)
        rectangle(img_chrg, b1, b2, noir)
        ecris(img_chrg, f'{round(steps/t_steps*100)}%',
              [b1[0], b1[1]+dst], [b2[0], b2[1]+dst], 2.7/2, noir, 10/2/4*2.7)
        b1, b2 = [[b1[0], b1[1]+dst], [b2[0], b2[1]+dst]]
        dst = 50
        ecris(img_chrg, action, [b1[0], b1[1]+dst],
              [b2[0], b2[1]+dst], taille, noir, 10/5*taille)
        montre(img_chrg, nf, 1, non)
        time.sleep(rd.random()*0.1)
##########
## MAIN ##
##########


class rt:
    def destroy(self) -> None: pass


def setup_(root=rt()):
    steps = 0
    if True:  # Trash dir ##
        create_dir_if_unexisting(trash, f'.\\{depts_path}')
    if True:  # Imgs.vars ##
        line = currentframe().f_lineno+1
        imgs_to_create = {n_img1: img_cart1, n_img_chargement: img_chrg, n_img2: img_cart2}
    if True:  # Checking Imgs/ ##
        create_dir_if_unexisting(imgs, f'.\\{depts_path}')
    if True:  # Checking imgs to create in Imgs/ ##
        for i in os.listdir(f".\\{imgs_path}"):
            try:
                imgs_to_create.pop(i)
                steps += 1
            except:
                try:
                    raise invalidPlace(i, line)
                except:
                    shutil.move(f'./{imgs_path}/{i}', f'./{trash_path}')
        for i in imgs_to_create:
            print(f'\033[1;32mCreated \033[1;35mimage \033[1;4;36m{i}\033[00m')
            imgs_to_create[i]()
    if True:  # KeyConfig ##
        keyConfig = {'keysj1': [2490368, 2621440, 2555904, 2424832],
                     'keysj2': [119, 115, 100, 97]}
    if True:  # Checking Config ##
        create_dir_if_unexisting(config, f'.\\{depts_path}')
        if True:  # Creating Config/keys.txt ##
            v_dir = os.listdir(f'.\\{config_path}')
            try:
                v_dir.index('keys.txt')
            except:
                with open(f"./{config_path}/keys.txt", "w") as file:
                    file.write(str(keyConfig))
    time.sleep(rd.random()*1.3)
    montre_img_charg('Finishing', 18)
    root.destroy()
    time.sleep(rd.random()*0.5)
    montre_img_charg('Finished!', 20)
    while True:
        wk = attend_touche(1)
        if wk != -1:
            break


def setup():
    root = Tk()

    class imag:
        def __init__(self, t_steps=100, steps=5, action='Installing pip', image_path=f'{dir}\\Depandances\\Imgs\\img_chrg.jpg'):
            try:
                bgr_img_chrg = ouvre_image(image_path)
            except:
                img_chrg()
                bgr_img_chrg = ouvre_image(image_path)
            a, b = 3, 7
            dst = 75
            b_c_c = [pt_sg(cg, ct_sg(bg, bd), a, b),
                     pt_sg(cd, ct_sg(bg, bd), a, b)]
            b1, b2 = [[b_c_c[0][0], b_c_c[0][1]-25],
                      [b_c_c[1][0], b_c_c[1][1]+25]]
            b3, b4 = [[b_c_c[0][0], b_c_c[0][1]-25], [b_c_c[0][0] +
                                                      (b_c_c[1][0]-b_c_c[0][0])/t_steps*steps, b_c_c[1][1]+25]]
            rectangle(bgr_img_chrg, b3, b4, rouge, 0)
            rectangle(bgr_img_chrg, b1, b2, noir)
            ecris(bgr_img_chrg, f'{round(steps/t_steps*100)}%',
                  [b1[0], b1[1]+dst], [b2[0], b2[1]+dst], 2.7/2, noir, 10/2/4*2.7)
            b1, b2 = [[b1[0], b1[1]+dst], [b2[0], b2[1]+dst]]
            dst = 50
            ecris(bgr_img_chrg, action, [b1[0], b1[1]+dst],
                  [b2[0], b2[1]+dst], taille, noir, 10/5*taille)
            rgb_img_chrg = bgr_img_chrg[::, ::, ::-1]
            self.img = ImageTk.PhotoImage(Image.fromarray(rgb_img_chrg))
    root.title('JEU_TR')
    p1 = PhotoImage(file='./Infos/Favicon.ico')
    root.iconphoto(True, p1)
    root.attributes('-fullscreen', True)
    image = imag()
    panel = Label(root, image=image.img)
    panel.pack(side="top", fill="both", expand=True)
    root.update_idletasks()
    root.update()
    setup_(root)
