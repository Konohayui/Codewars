'''
1^3 + 2^3 + 3^3 + ... + (n-1)^3 + n^3 = (n(n+1)/2)^2
num = (n(n+1)/2)^2
n(n+1) = 2*sqrt(num)
'''

import math

def find_nb(num):
    n = int(math.sqrt(2 * math.sqrt(num)))
    if n >> 1 and ((n * (n + 1)) >> 1) ** 2 == num:
        return n
    return -1
