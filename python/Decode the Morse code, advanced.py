'''
"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
'''

from re import compile

Tokenizer = compile("(0+)")

def decodeBits(bits):
    tokens = Tokenizer.split(bits.strip("0"))
    dot_len = min([len(token) for token in tokens])
    dash_len = 3*dot_len
    
    code = []
    for token in tokens:
        if token[0] == '1':
            if len(token) < dash_len:
                code.append(".")
            else:
                code.append("-")
        elif token[0] == '0':
            if len(token) == dot_len:
                code.append("")
            elif dot_len < len(token) <= dash_len:
                code.append(" ")
            else:
                code.append("  ")
                
    return "".join(code)

def decodeMorse(morseCode):
    return " ".join("".join(MORSE_CODE[c] for c in word.split(" ")) for word in morseCode.strip().split("  "))
