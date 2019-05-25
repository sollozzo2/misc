import random

#turns any string into the format used in the Mocking Spongebob meme.
#e.g. >>> spongebob('mitochondria are the powerhouse of the cell')
#'MitOChOndRIA arE thE poWeRhOUse of tHE ceLL'

def spongebob(text):
    res = ''
    state = 2
    #count makes sure the result doens't have more than 3 consecutive letters with the same capitalization
    count = 0
    prevchar = 'x'
    for char in text:
        if prevchar == ' ':
            res += char.lower()
            prevchar = char
            continue
        cap = random.random()
        if cap > 0.5:
            if state == 1:
                count += 1
            else:
                state = 1
                count = 0
            if count >= 2:
                res += char.lower()
            else:
                res += char.upper()
        else:
            if state == 0:
                count += 1
            else:
                state = 0
                count = 0
            if count >= 2:
                res += char.upper()
            else:
                res += char.lower()
        prevchar = char
        #print(prevchar, state, count, res)
    return res
