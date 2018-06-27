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
