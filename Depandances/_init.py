## TODO ## Import here the games to be played in the <TR_GAME> ##
try: from Outils.Jeux.echecs import start as echecs
except: from Depandances.Outils.Jeux.echecs import start as echecs
jeux_dispos = {'echecs': echecs} # TODO @@ Insert the game name on key and the function (without "()") on value @@