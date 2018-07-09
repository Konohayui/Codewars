import re
from collections import Counter

def expand_str(pidx, formula):
    while pidx != []:                
            if formula[pidx[1] + 1].isdigit():
                factor = int(formula[pidx[1] + 1])
            else:
                factor = 1
                
            for idx, elements in enumerate(formula[pidx[0]:pidx[1]]):
                if elements.isdigit():
                    formula[pidx[0] + idx] = formula[pidx[0] + idx - 1]*(int(elements) - 1)
                elif elements not in ["(", "[", "{", ")", "]", "}"]:
                    formula[pidx[0] + idx] = formula[pidx[0] + idx]*factor
            pidx.pop(0)
            pidx.pop(0)
    return formula
            
def parse_molecule (formula):
    formula = re.findall(r'[A-Z][a-z]?|[()\[\]{}]|\d+', formula)
    p = []
    b = []
    c = []
    length = len(formula)
    idx = 0
    
    while idx < length:
        if formula[idx]  == "(" or formula[idx] == ")":
            p.append(idx)
            idx += 1
        elif formula[idx] == "[" or formula[idx] == "]":
            b.append(idx)
            idx += 1
            
        elif formula[idx] == "{" or formula[idx] == "}":
            c.append(idx)
            idx += 1
        else:
            idx += 1
    
    if p != []:
        formula = expand_str(p, formula)
    if b != []:
        formula = expand_str(b, formula)
    if c != []:
        formula = expand_str(c, formula)
        
    for idx, elements in enumerate(formula):
        if elements.isdigit():
            formula[idx] = formula[idx - 1]*(int(elements) - 1)
            
    formula = "".join(s for s in formula if s.isalpha())
    formula = re.findall(r'[A-Z][a-z]?', formula)
    return Counter(formula)
    
    
print(parse_molecule("H2O"))
print(parse_molecule("Mg(OH)2"))
print(parse_molecule("K4[ON(SO3)2]2"))
print(parse_molecule("As2{Be4C5[BCo3(CO2)3]2}4Cu5"))




'''
good solutions
'''
from collections import Counter
import re

COMPONENT_RE = (
    r'('
        r'[A-Z][a-z]?'
        r'|'
        r'\([^(]+\)'
        r'|'
        r'\[[^[]+\]'
        r'|'
        r'\{[^}]+\}'
    r')'
    r'(\d*)'
)


def parse_molecule(formula):
    counts = Counter()
    for element, count in re.findall(COMPONENT_RE, formula):
        count = int(count) if count else 1
        if element[0] in '([{':
            for k, v in parse_molecule(element[1:-1]).items():
                counts[k] += count * v
        else:
            counts[element] += count
    return counts

########################################################################################
import re
from collections import Counter

def expand_str(m):
    return m.group(1) * int(m.group(2))

def parse_molecule (formula):
    formula = re.sub(r'\(([^\)]+)\)(\d+)',expand_str,formula)
    formula = re.sub(r'\[([^\]]+)\](\d+)',expand_str,formula)
    formula = re.sub(r'\{([^\}]+)\}(\d+)',expand_str,formula)
    formula = re.sub(r'([A-Z][a-z]?)(\d+)',expand_str,formula)
    m = re.findall(r'[A-Z][a-z]?',formula)
    return Counter(m)
    
