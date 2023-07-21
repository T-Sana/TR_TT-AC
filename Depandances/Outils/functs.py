def range2(start, stop, step):
    if step == 0 or start == stop: return([])
    out = [start]
    a = start
    while True:
        a += step
        if a >= stop and step > 0:
            return(out)
        elif a <= stop and step < 0:
            return(out)
        out.append(a)