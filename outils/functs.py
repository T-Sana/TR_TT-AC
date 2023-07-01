from multimethod import multimethod
@multimethod
def range2(start: int, stop: int, step: int=1):
    start = round(start)
    stop = round(stop)
    step = round(step)
    return(range(start, stop, step))
@multimethod
def range2(stop: int):
    return(range(stop))
@multimethod
def range2(start, stop, step):
    if step == 0: return([])
    out = [start]
    a = start
    while True:
        a += step
        if a >= stop and step > 0:
            return(out)
        elif a <= stop and step < 0:
            return(out)
        out.append(a)