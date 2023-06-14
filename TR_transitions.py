import cv2
from outils.cvt import montre
from TR_VARS import nf
from outils.quit import quitter
import copy

def shade(img):
    image = copy.deepcopy(cv2.cvtColor(img, cv2.COLOR_RGB2HSV))
    for i in range(30):
        # Adjust the hue, saturation, and value of the image
        image[:, :, :] = image[:, :, :] * 0.9
        # Convert the image back to BGR color space
        image2 = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
        wk = montre(image2, nf, 5, False)
        if wk == 27: quitter()