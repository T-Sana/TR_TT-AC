from Depandances.Outils.pip import *

with open('./Depandances/Requirements.txt', 'r', encoding='utf8') as file:
    packages_to_uninstall = [
        package[:package.find('='):] for package in file.readlines()]
packages_installed = get_installed_packages()
for pckg in packages_to_uninstall:
    if pckg in packages_installed:
        try:
            print(f'Uninstalling \033[34m\033[1m{pckg}\033[00m')
            uninstall(pckg)
            print(f'Uninstalled \033[34m\033[1m{pckg}\033[00m!')
        except:
            print(f'Couldn\'t uninstall {pckg}.')
    else:
        print(f'{f"\033[3;4;34m\033[1m{pckg}\033[00m \033[35m":{"-"}<40}\033[00m \033[21;33mIsn\'t\033[00m \033[32minstalled\033[00m \033[31m!\033[00m')
