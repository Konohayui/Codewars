def whoIsNext(names, r):
    # your code
    total_people = len(names)
    if r <= total_people:
        return names[r - 1]
    
    else:
        base = 0
        total_length = total_people
        temp = 0
        
        while total_length < r:
            base += 1
            temp = total_length
            total_length += total_people*2**(base)
        return names[(r - temp - 1)//(2**base)]
        
print(whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 1), "Sheldon")
print(whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 6), "Sheldon")
print(whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 10), "Penny")
print(whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 52), "Penny")
print(whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 7230702951), "Leonard")
