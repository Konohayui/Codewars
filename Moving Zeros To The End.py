def move_zeros(array):
    new_array = []
    arr_length = len(array)
    
    for idx in range(arr_length):
        if array[idx] != 0 or array[idx] is False:
            new_array.append(array[idx])
            
    return new_array + [0]*(arr_length - len(new_array))
