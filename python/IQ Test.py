def iq_test(numbers):
    #your code here
    even = []
    odd = []
    for i, n in enumerate(numbers.split(" ")):
        print(n)
        if int(n) % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    if len(even) == 1:
        return even[0] + 1
    return odd[0] + 1
