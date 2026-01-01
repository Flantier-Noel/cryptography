'''from lorem_text import lorem

import random
random.text = lorem.words

from __cypher import*

N = 100
canvas_key = random.text(N)
canvas = Canvas.from_text(canvas_key)

print(canvas)


msg_int = [2, 7, 1, 8, 2, 8, 1]
cnv = Canvas(lst_unpack_rep=[3,4,2,4,2,4,2])
code = encode_int(cnv, msg_int)

print(code)'''

'''
from __langage import __Tree

alphab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
def rules(past):
    if len(past) == 0 : return {c:True for c in alphab}
    possible = {c:True for c in alphab}
    for l in alphab :
        if l == past[-1]: possible[l] = False
    return possible

t0 = __Tree.generate0(alphab, rules, 3)

d = t0['a']
d['b'] = 1

print(t0['a'])'''

from __langage import*

lang = Langage()
sent = lang.sentence([1, 5, 3, 7, 3, 6, 7, 8, 9, 1, 3, 2, 3, 6, 1, 2, 2, 3, 1, 2, 2, 5])
print(sent['repr']['str'])