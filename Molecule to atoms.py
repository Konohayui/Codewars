#(incomplete)

import re 

def parse_molecule(formula):
    formula_length = len(formula)
    formula = re.sub("[\[\{]", "(", formula)
    formula = re.sub("[\]\}]", ")", formula)
    
    idx = 0
    elements = {}
    left_parenthese = []
    
    while idx < formula_length:
        if formula[idx].isupper():
            if formula[idx] not in elements:
                if idx + 1 < formula_length and formula[idx + 1].isdigit():
                    elements[formula[idx]] = int(formula[idx + 1])
                    idx += 2
                else:
                    elements[formula[idx]] = 1
                    idx += 1
            else:
                if idx + 1 < formula_length and formula[idx + 1].isdigit():
                    elements[formula[idx]] += int(formula[idx + 1])
                    idx += 2
                else:
                    elements[formula[idx]] += 1
                    idx += 1
        elif formula[idx].islower():
            elements[formula[idx - 1:idx + 1]] = elements[formula[idx - 1]]
            del elements[formula[idx - 1]]
            idx += 1
        elif formula[idx].isdigit():
            idx += 1 
        elif formula[idx] == "(":
            left_parenthese.append(idx)
            idx += 1 
        elif formula[idx] == ")":
            if idx + 1 < formula_length and formula[idx + 1].isdigit():
                for e in elements:
                    if e in formula[left_parenthese[-1] + 1:idx]:
                        elements[e] *= int(formula[idx + 1])
                left_parenthese.remove(left_parenthese[-1])
                # print(formula[left_parenthese[-1] + 1:idx])
            idx += 1    
    return elements
    
print(parse_molecule("H2OO"))
print(parse_molecule("Mg(OH)2"))
print(parse_molecule("K4[ON(SO3)2]2"))
