import cv2
from Depandances.Outils.cvt import montre
from Depandances.Outils.paths__names__etc import *
from Depandances.Outils.quit import quitter
import copy

def shade(img, v=1):
    image = copy.deepcopy(cv2.cvtColor(img, cv2.COLOR_RGB2HSV))
    for _ in range(0, 30, v):
        image[:,:,:] = image[:,:,:] * 0.9
        image2 = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
        wk = montre(image2, nf, 5, False)
        if wk == 27:
            quitter()