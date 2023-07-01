from multimethod import multimethod
@multimethod
def range2(start, stop, step: int=1):
    return(range(start, stop, step))
@multimethod
def range2(stop):
    return(range(stop))
@multimethod
def range2(start, stop, step: float):
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