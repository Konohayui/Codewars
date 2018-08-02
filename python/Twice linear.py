def dbl_linear(n):
    u = [1]
    yi = zi = 0
    
    while len(u) < n + 1:
        y = 2*u[yi] + 1 
        z = 3*u[zi] + 1

        if y >= z:
            u.append(z)
            zi += 1
            if y == z:
                yi += 1
        else:
            u.append(y)
            yi += 1 
            
    return u[n]
    
    
print(dbl_linear(10))
print(dbl_linear(20))
print(dbl_linear(30))
print(dbl_linear(40))
print(dbl_linear(50))
