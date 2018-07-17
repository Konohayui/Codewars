def find_it(seq):
    L = set(seq)
    for n in L:
        c = seq.count(n)
        if c % 2 == 1:
            return n
    return None
