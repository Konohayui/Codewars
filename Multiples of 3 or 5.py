def solution(number):
    s = []
    for n in range(3, number):
        if n % 3 == 0 or n % 5 == 0:
            s.append(n)
    return sum(set(s))
