import itertools

def get_pins(observed):
    adjacents = {}
    adjacents["1"] = ["1","2","4"] 
    adjacents["2"] = ["1", "2", "3", "5"]
    adjacents["3"] = ["2", "3", "6"]
    adjacents["4"] = ["1", "4", "5", "7"]
    adjacents["5"] = ["2", "4", "5", "6", "8"] 
    adjacents["6"] = ["3", "5", "6", "9"] 
    adjacents["7"] = ["4", "7", "8"] 
    adjacents["8"] = ["5", "7", "8", "9","0"] 
    adjacents["9"] = ["6", "8", "9"] 
    adjacents["0"] = ["0", "8"]
    
    if len(observed) == 1:
        return adjacents[observed]
        
    else:
        observed = list(observed)
        possible_elements = [adjacents[o] for o in observed]
            
        variations = list(itertools.product(*possible_elements))
        answer = ["".join(v) for v in variations]
            
        return answer
