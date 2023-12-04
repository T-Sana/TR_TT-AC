import PySimpleGUI as sg
def quitter() -> None:
    if sg.popup_yes_no('\n\nVoulez-vous VRAIMENT quitter le jeu ?\n\n', title='QUITTER') == 'Yes':
        print(f'\033[1;34mGAME \033[1;32mENDED \033[1;31m!\033[00m')
        raise SystemExit