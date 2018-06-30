def sum_pairs(ints, s):

    if len(ints) < 2:
        return None
        
    else:
        pair = None 
        seens = set()
            
        for num in ints:
            dif = s - num
            if dif in seens:
                return [dif, num]
            seens.add(num)

    
l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]

ss = [8, -6, -7, 2, 10, 8, 0, 10]

ints_list = [l1, l2, l3, l4, l5, l6, l7, l8]

for i in range(len(ints_list)):
    print(sum_pairs(ints_list[i], ss[i]))
