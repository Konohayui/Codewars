def digital_root(n):
    while n % 100 > 10:
        n = sum([int(i) for i in str(n)])
    return sum([int(i) for i in str(n)])
    
