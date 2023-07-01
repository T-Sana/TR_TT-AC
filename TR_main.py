from outils.install_dependencies import install_dependencies as i_dep; #i_dep()
from outils.souris import souris as s
import TR_transitions as trs
from TR_anim_debut import *
from TR_cartes import *
from TR_titre import *
from TR_VARS import *

titre()
trs.shade(img)
j1, j2 = anim_debut()
trs.shade(img)
carte1(j1, j2)