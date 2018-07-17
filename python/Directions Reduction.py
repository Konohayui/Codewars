def dirReduc(arr):
    directions = {}
    directions["NORTH"] = -2
    directions["SOUTH"] = 2
    directions["EAST"] = -1
    directions["WEST"] = 1
    
    while True:
        path_length = len(arr)
        i = 0
        path = []
        while i < path_length - 1:
            if directions[arr[i]] + directions[arr[i + 1]] == 0:
                i += 2
            else:
                path.append(arr[i])
                i += 1

        if i < path_length:
            path.append(arr[i])
        if len(arr) == len(path):
            arr = path
            break
        
        arr = path
    return arr
