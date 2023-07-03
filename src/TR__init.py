from outils.pip import *
import copy

if True: ## Packages.vars ##
        packages_to_install = ['opencv-python', 'numpy', 'python-dotenv']
        packages_installed = get_installed_packages()
if True: ## Discard installed packages ##
    for i in copy.deepcopy(packages_to_install): ## If must be a copy. If not it exits sooner because of removing an index
        for j in packages_installed:
            if j == i:
                packages_to_install.remove(i)
update('pip')
if True: ## Install required packages
    for i in packages_to_install:
        install(i)