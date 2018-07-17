def printer_error(s):
    p = ['n', 'o', 'p', 'q', 'r', 's', 't', 
         'u', 'v', 'w', 'x', 'y', 'z']
    count = 0
    for e in list(s):
        if e in p:
            count += 1
    return str(count) + "/" + str(len(s))
