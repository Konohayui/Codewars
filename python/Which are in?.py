def in_array(array1, array2):
    if array1 == [] or array2 == []:
        return []
    s = []
    for a2 in array2:
        for a1 in array1:
            if a1 in a2:
                s.append(a1)
    return sorted(set(s))
