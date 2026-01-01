'''from lorem_text import lorem

alphab = 'èé'

import random
random.text = lorem.words

from __cypher import*

N = 7
canvas_key = random.text(N)
canvas = Canvas.from_text(canvas_key)

print(canvas)


msg_int = [2, 7, 1, 8, 2, 8, 1]
cnv = Canvas(lst_unpack_rep=[3,4,2,4,2,4,2])
code = encode_int(cnv, msg_int)

print(code)'''

from __langage import __Tree

alphab = ['a', 'b', 'c']
def rules(past):
    if len(past) == 0 : return {c:True for c in alphab}
    possible = {c:True for c in alphab}
    for l in alphab :
        if l == past[-1]: possible[l] = False
    return possible

t0 = __Tree.generate0(alphab, rules, 3)