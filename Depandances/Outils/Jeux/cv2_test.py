import cv2
import cvt
import time

class souris:
    def type(event, x, y, flags, param):
        print(event)
nf = 'img'

while True:
    cv2.namedWindow(nf, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(nf, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.setMouseCallback(nf, souris.type)
    cv2.imshow(nf, cvt.image())
    wk = cv2.waitKey(1000)
    if wk == 27 : break