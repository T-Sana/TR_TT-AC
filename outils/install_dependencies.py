try:
    from outils.pip import *
except:
    from pip import *

def install_dependencies() -> None:
    for i in ['pip']:
        update(i)
    for i in ['opencv-python', 'numpy']:
        install(i)