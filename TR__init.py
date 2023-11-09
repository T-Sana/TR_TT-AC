from Depandances.Outils.paths__names__etc import *
from Depandances.Outils.pip import *
import copy

try:
    if True: ## Packages.vars ##
            packages_to_install = ['opencv-python', 'numpy', 'python-dotenv']
            packages_installed = get_installed_packages()
    if True: ## Discard installed packages ##
        for i in copy.deepcopy(packages_to_install): ## If must be a copy. If not it exits sooner because of removing an index
            for j in packages_installed:
                if j == i:
                    packages_to_install.remove(i)
    try: update('pip')
    except: pass
    if True: ## Install required packages
        for pckg in packages_to_install:
            try: install(pckg)
            except: print(f'Couldn\'t install {pckg} package.')
except: print(f'ERROR IN {BOLD_BLUE}TR__init.py{NORMAL} !')