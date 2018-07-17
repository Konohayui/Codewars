def order_weight(string):
    order = {}
    for ind, weight in enumerate(string.split()):
        w = sum(map(int, weight))
        try:
            order[w].append(weight)
        except:
            order[w] = [weight]
    
    weights = []
    for k in sorted(order):
        weights += sorted(order[k])
    return " ".join(w for w in weights)
