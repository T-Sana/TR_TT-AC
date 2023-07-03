import PySimpleGUI as sg
def quitter() -> None:
    if sg.popup_yes_no('\n\nVoulez-vous VRAIMENT quitter le jeu ?\n\n', title='QUITTER') == 'Yes': raise SystemExit