def samples():
    max_long_h = 25
    max_haut_h = 9

    max_long_b = 14
    max_haut_b = 17

    max_chrs_h = 17
    max_chrs_v = 18

    samples = []

    out = []
    alphabet1 = ' abcdefghijklmnopqrstuvwxyz'
    alphabet2 = 'abcdefghijklmnopqrstuvwxyz'
    cmb = len(alphabet1) * len(alphabet2)
    lettres = []
    for a in alphabet1:
        for b in alphabet2:
            char = a+b
            char = char.replace(' ', '')
            if char != '':
                lettres.append(char)
    a = 1
    while True:
        if cmb / a <= max_chrs_h:
            div = a
            break
        a += 1
    a = 1
    cnt = 0
    cnt2 = 0
    outy = f'\'\\b\\\\'
    out = ''
    for feuille in range(div):
        y = max_chrs_h*feuille
        lets = lettres[y:y+max_chrs_h]
        for i in range(max_chrs_v):
            for j in lets:
                outy += f'{j}{str(i+1)}\\\\'
                cnt += 1
                if cnt%max_long_h == 0:
                    out += outy
                    outy = 'n\\\\'
                    cnt2 += 1
                    if cnt2%max_haut_h == 0:
                        outy += '\',\n\'\\b\\\\'
    out += outy
    samples.append(out)
    a = 1
    cnt = 0
    cnt2 = 0
    outy = '\'\\b\\\\'
    out = ''
    for feuille in range(div):
        y = max_chrs_h*feuille
        lets = lettres[y:y+max_chrs_h]
        for i in range(max_chrs_v):
            for j in lets:
                outy += f'{j}{str(i+1)}\\\\'
                cnt += 1
                if cnt%max_long_b == 0:
                    out += outy
                    outy = 'n\\\\'
                    cnt2 += 1
                    if cnt2%max_haut_b == 0:
                        outy += '\',\n\'\\b\\\\'
    out += outy
    samples.append(out)
    return(samples)