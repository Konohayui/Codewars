def decompose(n):
    result = [n]
    temp = 0 
    
    while result:
        current = result.pop()
        temp += current**2
        
        for num in range(current - 1, 0, -1):
            if temp >= num**2:
                temp -= num**2
                result.append(num)
                if temp == 0:
                    return result[::-1]

    return "Nothing"
    
print(decompose(4))
print(decompose(5))
print(decompose(50))
