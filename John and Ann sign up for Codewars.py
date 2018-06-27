def kata_num(n):
    ann = [1]*n
    john = [0]*n
    day = 1
    while day < n:
        ann[day] = day - john[ann[day - 1]]
        john[day] = day - ann[john[day - 1]]
        day += 1
    return ann, john

def john(n):
    return kata_num(n)[1]
    
def ann(n):
    return kata_num(n)[0]
    
def sum_john(n):
    return sum(john(n))
    
def sum_ann(n):
    return sum(ann(n))
