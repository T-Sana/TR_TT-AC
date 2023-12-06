def tours(X, A, B, C):
    A.reverse()
    B.reverse()
    C.reverse()
    X = X + 1
    Y = X
    print('/----------------------\ ')
    OUT = []
    while X > 0:
        Z = Y - X
        truc = '    '
        out = '¦' + truc
        try:
            if len(str(A[Z])) == 1:
                out += ' ' + str(A[Z])
            else:
                out += str(A[Z])
        except:
            out += ' |'
        out += truc
        try:
            if len(str(B[Z])) == 1:
                out += ' ' + str(B[Z])
            else:
                out += str(B[Z])
        except:
            out += ' |'
        out += truc
        try:
            if len(str(C[Z])) == 1:
                out += ' ' + str(C[Z])
            else:
                out += str(C[Z])
        except:
            out += ' |'
        out += truc + '¦'
        X -= 1
        OUT.insert(0, out)
    for chose in OUT:
        print(chose)
    A.reverse()
    B.reverse()
    C.reverse()
    print('\----------------------/')
def verify(o, d):
    if o == 1:
        if d == 2:
            if A[0] < B[0]:
                return(True)
        else:
            if A[0] < C[0]:
                return(True)
    elif o == 2:
        if d == 1:
            if B[0] < A[0]:
                return(True)
        else:
            if B[0] < C[0]:
                return(True)
    else:
        if d == 1:
            if C[0] < A[0]:
                return(True)
        else:
            if C[0] < B[0]:
                return(True)
def bouge2(o, d):
    if o == 1:
        if d == 2:
            B.append(A[0])
            A.pop(0)
        else:
            C.append(A[0])
            A.pop(0)
    elif o == 2:
        if d == 1:
            A.append(B[0])
            B.pop(0)
        else:
            C.append(B[0])
            B.pop(0)
    else:
        if d == 1:
            A.append(C[0])
            C.pop(0)
        else:
            B.append(C[0])
            C.pop(0)
def bouge1(o, d):
    if o == 1:
        if d == 2:
            B.insert(0, A[0])
            A.pop(0)
        else:
            C.insert(0, A[0])
            A.pop(0)
    elif o == 2:
        if d == 1:
            A.insert(0, B[0])
            B.pop(0)
        else:
            C.insert(0, B[0])
            B.pop(0)
    else:
        if d == 1:
            A.insert(0, C[0])
            C.pop(0)
        else:
            B.insert(0, C[0])
            C.pop(0)
def move(origine, destination, moves, max_moves):
    print(' ')
    if origine == destination:
        origin = False
        destin = False
    else:
        if origine == 1:
            if len(A) != 0: origin = True
            else: origin = False
        elif origine == 2:
            if len(B) != 0: origin = True
            else: origin = False
        else:
            if len(C) != 0: origin = True
            else: origin = False
        if destination == 1:
            if len(A) != 0: destin = True
            else: destin = False
        elif destination == 2:
            if len(B) != 0: destin = True
            else: destin = False
        else:
            if len(C) != 0: destin = True
            else: destin = False
    if origin == False:
        pass
    else:
        if destin == True:
            if verify(origine, destination) == True:
                bouge1(origine, destination)
                moves += 1
            else:
                print()
        else:
            bouge2(origine, destination)
            moves += 1
    print(moves, of_, max_moves, min_moves)
    return(moves)
langue = input('Français [fr], Català [ca], Español [es] or English [en]: ')
Q = True
if langue == 'fr':
    input_origin = "D'la tour: "
    input_destin = 'À la tour: '
    of_ = 'sur'
    min_moves = 'mouvements minimums。'
    disques = 'Nº de disques: '
    error_ = 'Tu ne peux pas y faire !'
elif langue == 'ca':
    input_origin = 'Des la torre: '
    input_destin = 'Cap la torre: '
    of_ = 'de'
    min_moves = 'moviments mínims。'
    disques = 'Nº de discs: '
    error = 'No ho pots pas fer això!'
elif langue == 'es':
    input_origin = 'Desde la torre: '
    input_destin = 'Hacia la torre: '
    of_ = 'de'
    min_moves = 'movimientos mínimos。'
    disques = 'Nº de discos: '
    error = 'No puedes hacer esto!'
if langue.lower() == 'auto':
    Q = False
else:
    input_origin = 'From the tower nº: '
    input_destin = 'To the tower nº: '
    of_ = 'of'
    min_moves = 'minim moves。'
    disques = 'Nº of disks: '
    error = 'Invalid move!'
while Q == True:
    A = []
    B = []
    C = []
    try:
        x = int(input(disques))
        if x < 1:
            x = 1
        elif x > 64:
            x = 64
    except:
        x = 1
    X = x
    moves = 0
    max_moves = (2**X-1)
    while x >= 1:
        A.insert(0, x)
        x -= 1
    tours(X, A, B, C)
    while True:
        if len(A) == 0:
            if len(B) == 0:
                break
            elif len(C) == 0:
                break
        print('')
        try:
            orig = int(input(input_origin))
            dest = int(input(input_destin))
        except:
            orig = 1
            dest = 1
        moves = move(orig, dest, moves, max_moves)
        tours(X, A, B, C)
    print('Félicitations ! Tu as résolu ce niveau !\n\n')
