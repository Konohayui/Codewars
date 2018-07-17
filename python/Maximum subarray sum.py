def maxSequence(array):
    if array == []:
        return 0
    m = array[0]
    M = m
    for i in range(1, len(array)):
        m = max(array[i], m + array[i])
        M = max(M, m)
    if M < 0:
        return 0
    return M
