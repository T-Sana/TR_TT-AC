## pakgs ##
from dotenv import load_dotenv; load_dotenv()
from outils.paths__names__etc import *
from outils.cvt import *

if True: ## Keys.vars ##
    with open('./Config/keys.txt', 'r') as file:
        keys = file.read()
        print(keys)
    configKeys = eval(keys)
    keysj1 = configKeys['keysj1']
    keysj2 = configKeys['keysj2']
j1.keys = keysj1
j2.keys = keysj2
