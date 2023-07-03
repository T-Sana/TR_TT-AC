import cv2
from outils.cvt import montre
from TR_vars import nf
from outils.quit import quitter
import copy

def shade(img):
    image = copy.deepcopy(cv2.cvtColor(img, cv2.COLOR_RGB2HSV))
    for i in range(30):
        image[:, :, :] = image[:, :, :] * 0.9
        image2 = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
        wk = montre(image2, nf, 5, False)
        if wk == 27: quitter()