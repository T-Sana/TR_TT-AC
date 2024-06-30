import subprocess
import sys

def install(package) -> None:
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
def uninstall(package) -> None:
    if package != 'pip': subprocess.check_call([sys.executable, "-m", "pip", "uninstall", package, '-y'])
    else: print('YOU CAN\'T UNINSTALL PIP!!!\nARE YOU CRAZY???')
def update(package) -> None:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])
def get_installed_packages():
    r = str(subprocess.check_output([sys.executable, "-m", "pip", "freeze"]))
    pckgs = []; pckg = ''; t = False
    for i in r[2:len(r)-1]:
        if i == '/':
            t = True
            if pckg == 'r' or pckg == 'n': pckg = ''
            elif pckg != '':
                try: pckgs.append(pckg[:pckg.index('=')])
                except ValueError: pckgs.append(pckg)
                pckg = ''
                t = False
        elif t and i == 'r': pass
        elif t and i == 'n': t = False
        else: pckg += i
    return(pckgs)