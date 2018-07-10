def move_zeros(array):
    not_zero = 0
    
    for idx in range(len(array)):
        if array[idx] != 0 or array[idx] is False:
            array[not_zero] = array[idx]
            not_zero += 1
    
    while not_zero < len(array):
        array[not_zero] = 0
        not_zero += 1
        
    return array
