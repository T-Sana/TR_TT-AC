def range2(start, stop, step):
    if step == 0 or start == stop: return([])
    out = [start]
    index = start
    while True:
        index += step
        if index >= stop and step > 0:
            return(out)
        elif index <= stop and step < 0:
            return(out)
        out.append(index)