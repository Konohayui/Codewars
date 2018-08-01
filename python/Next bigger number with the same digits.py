def next_bigger(num):
    #your code here
    num = list(str(num))
    i = [i for i in range(1, len(num)) if num[i - 1] < num[i]]
    if i != []:
        i = max(i)
    else:
        return -1
        
    j = [j for j in range(i, len(num)) if num[j] > num[i - 1]]
    if j != []:
        j = max(j)
    else:
        return -1
        
    num[j], num[i - 1] = num[i - 1], num[j]
    num[i:] = reversed(num[i:])
    return int(''.join(n for n in num))
