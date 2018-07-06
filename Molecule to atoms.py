#(incomplete)

import re 

def parse_molecule(formula):
    formula_length = len(formula)
    formula = re.sub("[\[\{]", "(", formula)
    formula = re.sub("[\]\}]", ")", formula)
    
    idx = 0
    elements = []

    while idx < formula_length:
        if formula[idx].isupper():
            if formula[idx] not in elements:
                elements.append(formula[idx])
                idx += 1 
            else:
                idx += 1
        elif formula[idx].islower():
            elements[-1] = formula[idx - 1:idx + 1]
            idx += 1
        elif formula[idx].isdigit():
            idx += 1 
        elif formula[idx] == "(" or formula[idx] == ")" :
            idx += 1 
    return elements
    
print(parse_molecule("H2O"))
print(parse_molecule("Mg(OH)2"))
print(parse_molecule("K4[ON(SO3)2]2"))
