def recoverSecret(triplets):
    all_letters = []
    for i in range(len(triplets)):
        all_letters += triplets[i]
    all_letters = list(set(all_letters))    
    
    found = False
    while not found:
        found = True
        
        for i in range(len(triplets)):
            for j in range(len(triplets[i]) - 1):
                idx_a = all_letters.index(triplets[i][j])
                idx_b = all_letters.index(triplets[i][j + 1])
                if idx_a > idx_b:
                    all_letters[idx_a], all_letters[idx_b] = all_letters[idx_b], all_letters[idx_a]
                    found = False
                    
    return "".join(all_letters)

triplets = [['t','u','p'],
            ['w','h','i'],
            ['t','s','u'],
            ['a','t','s'],
            ['h','a','p'],
            ['t','i','s'],
            ['w','h','s']]
            
            
print(recoverSecret(triplets))
