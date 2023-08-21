## TODO ## Import here the games to be played in the <TR_GAME> ##
try: from Outils.Jeux.echecs import start as echecs
except: from Depandances.Outils.Jeux.echecs import start as echecs
try: from Outils.Jeux.morpion import start as morpion
except: from Depandances.Outils.Jeux.morpion import start as morpion
jeux_dispos = {'echecs': echecs, 'morpion': morpion} # TODO @@ Insert the game name on key and the function (without "()") on value @@