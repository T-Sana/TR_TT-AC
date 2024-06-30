from Depandances.Outils.pip import *
import copy

try:
    if True: ## Packages.vars ##
        with open('./Depandances/requirements.txt', 'r', encoding='utf8') as file:
            packages_to_install = [package[:package.find('='):] for package in file.readlines()]
        packages_installed = get_installed_packages()
    if True: ## Discard installed packages ##
        if 'pillow' in packages_installed: packages_to_install.remove('Pillow')
        for pckg in copy.deepcopy(packages_to_install): ## It must be a copy. If not it exits sooner because of removing indexes ##
            if pckg in packages_installed:
                packages_to_install.remove(pckg)
                print(f'{f"\033[34m\033[1m{pckg}\033[00m \033[35m":{"-"}<35}\033[00m \033[21;33mIs\033[00m \033[36malready\033[00m \033[32minstalled\033[00m \033[31m!\033[00m')
    if True: ## Install required packages
        for pckg in packages_to_install:
            try:
                print(f'Installing \033[34m\033[1m{pckg}\033[00m')
                install(pckg)
                print(f'Installed \033[34m\033[1m{pckg}\033[00m!')
            except:
                print(f'Couldn\'t install {pckg} package.')
except Exception as e: print(f'ERROR IN \033[34m\033[1mTR__init.py\033[00m !', e, sep='\n')