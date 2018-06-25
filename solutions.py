# Find the next perfect square!
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    n = sq ** (0.5)
    if n > 0 and sq % n == 0:
        return (n + 1)**2
    else:
        return -1
        
# IQ Test
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

# Remove the minimum
def remove_smallest(numbers):
    if len(numbers) > 0:
        m = min(numbers)
        print(m)
        numbers.remove(m)
        return numbers
    else:
        return numbers
    raise NotImplementedError("TODO: remove_smallest")
  
# Printer Errors
def printer_error(s):
    p = ['n', 'o', 'p', 'q', 'r', 's', 't', 
         'u', 'v', 'w', 'x', 'y', 'z']
    count = 0
    for e in list(s):
        if e in p:
            count += 1
    return str(count) + "/" + str(len(s))

# Multiples of 3 or 5
def solution(number):
    s = []
    for n in range(3, number):
        if n % 3 == 0 or n % 5 == 0:
            s.append(n)
    return sum(set(s))

# Sum of Digits / Digital Root
def digital_root(n):
    while n % 100 > 10:
        n = sum([int(i) for i in str(n)])
    return sum([int(i) for i in str(n)])
    
# Find the odd int
def find_it(seq):
    L = set(seq)
    for n in L:
        c = seq.count(n)
        if c % 2 == 1:
            return n
    return None
    
# Descending Order
def Descending_Order(num):
    n = sorted(str(num))[::-1]
    return int("".join(n))
    
# Array.diff
def array_diff(a, b):
    if a != []:
        new = []
        for e in a:
            if e not in b:
                new.append(e)
        return new
    return []
    
# Is a number prime?
def is_prime(num):
    if num != 2 and num % 2 == 0:
        return False
    elif num < 2:
        return False
    else:
        for n in range(2, int((num)**(0.5)) + 1):
            if num % n == 0:
                return False
        return True

# The Supermarket Queue
def queue_time(customers, n):
    if customers == []:
        return 0
    elif len(customers) < n:
        return max(customers)
    elif n == 1:
        return sum(customers)
    else:
        check_outs = customers[:n]
        for c in customers[n:]:
            m = check_outs.index(min(check_outs))
            check_outs[m] += c
        return max(check_outs)
        
# Which are in?
def in_array(array1, array2):
    if array1 == [] or array2 == []:
        return []
    s = []
    for a2 in array2:
        for a1 in array1:
            if a1 in a2:
                s.append(a1)
    return sorted(set(s))
    
# Human Readable Time
def make_readable(sec):
    H = sec / 3600
    M = sec /60 % 60
    S = sec % 60
    HH = str("%02d" % (H))
    MM = str("%02d" % (M))
    SS = str("%02d" % (S))
    return HH + ":" + MM + ":" + SS
    
# Pyramid Slide Down
def longest_slide_down(pyramid):
    # TODO: write some code...
    for row in range(len(pyramid) - 1, 0, -1):
        for col in range(0, row):
            pyramid[row - 1][col] += max(pyramid[row][col], pyramid[row][col + 1])
    return pyramid[0][0]

# Maximum subarray sum
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
    
# Strip Comments
def solution(string, markers):
    lines = string.split("\n")
    print(lines)
    for i, line in enumerate(lines):
        for marker in markers:
            index = line.find(marker)
            if index != -1:
                line = line[:index]
        lines[i] = line.rstrip()
    return "\n".join(lines)
    
# John and Ann sign up for Codewars
def kata_num(n):
    ann = [1]*n
    john = [0]*n
    day = 1
    while day < n:
        ann[day] = day - john[ann[day - 1]]
        john[day] = day - ann[john[day - 1]]
        day += 1
    return ann, john

def john(n):
    return kata_num(n)[1]
    
def ann(n):
    return kata_num(n)[0]
    
def sum_john(n):
    return sum(john(n))
    
def sum_ann(n):
    return sum(ann(n))
    
    
print(sum_john(75))
print(sum_ann(115))

#
