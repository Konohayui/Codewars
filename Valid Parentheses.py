import re

def valid_parentheses(string):
    string = re.findall("[()]", string)
    string = "".join(s for s in string)
    
    while "()" in string:
        string = string.replace("()", "")
    
    return string == ""
