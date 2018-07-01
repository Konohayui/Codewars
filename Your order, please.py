def order(sentence):
    new_sent = {}
    ints = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i, word in enumerate(sentence.split()):
        for w in word:
            if w in ints:
                new_sent[w] = word
    return " ".join(new_sent[w] for w in sorted(new_sent))
    
print(order("is2 Thi1s T4est 3a"))
