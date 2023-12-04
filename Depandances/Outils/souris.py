import cv2

class move_on_map(Exception):
    def __init__(self, msg='Moved on map due of a click on it!'):
        self.msg = msg
    def __repr__(self):
        return self.msg

class souris:
    dehors = [-1, -1]
    pos = dehors
    def get_souris(event, x, y, flags, param): ## Paramettres droppés par cv2 ##
        if event == cv2.EVENT_LBUTTONDOWN: ## Si click gauche ##
            souris.pos = [x, y]
        elif event == cv2.EVENT_RBUTTONDOWN:
            souris.pos = souris.dehors
    def get_souris_(event, x, y, flags, param): ## Paramettres droppés par cv2 ##
        if event == cv2.EVENT_LBUTTONDOWN: ## Si click gauche ##
            souris.pos = [x, y]
        elif event == cv2.EVENT_RBUTTONDOWN:
            souris.pos = souris.dehors
    def clicked_in(boutton): ## Is pos between boutton[0] (haut gauche) and boutton[1] (bas droite) ##
        pos = souris.pos
        voui = pos[0] >= boutton[0][0] and pos[0] <= boutton[1][0] and pos[1] >= boutton[0][1] and pos[1] <= boutton[1][1]
        return(voui)
    def clicked_in_list_bts(lst):
        for i in range(len(lst)):
            if souris.clicked_in(lst[i]):
                return(i)
        return(-1)
    def case_clicked_in(files, colonnes):
        y = souris.clicked_in_list_bts(files)
        x = souris.clicked_in_list_bts(colonnes)
        return(x, y)