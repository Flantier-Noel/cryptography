def pop_item(lst, item):
    for i in range(len(lst)):
        if lst[i]==item : 
            lst.pop(i)
            break

class Canvas():
    def __init__(self, lst_unpack_rep=[]):
        self.lst_unpack_rep = lst_unpack_rep

        length = 0
        while length < len(lst_unpack_rep) and not(isinstance(lst_unpack_rep[length], list)): 
            length +=1
        
        self.len = length

    @classmethod
    def from_text(cls, key_text:str):
        max_jump = 9

        canvas = []
        key = [len(w) for w in key_text.split(' ')]

        rank = 0
        for n in key :
            for ind in range(max_jump+1):
                if rank+ind >= len(canvas) : canvas.append([i0+1 for i0 in range(max_jump)])

            possible_values = canvas[rank]
            value = possible_values[n%len(possible_values)]
            canvas[rank] = value

            for ind in range(1, value):
                pop_item(canvas[rank+ind], value-ind)
            
            rank += 1

        return Canvas(canvas)

    def pack(self):
        L = self.len
        return self.lst_unpack_rep[:L]
    
    def __repr__(self):
        lst_pack = self.pack()
        str_list = [str(n) for n in lst_pack]
        return '['+ ', '.join(str_list) +']'
    
## without modular variation :
from random import randint

def encode_int(cnv, msg_int):
    code = []

    for ind in range(len(msg_int)) :
        pos = cnv[ind]

        for _ in range(len(code), pos): code.append(-1)

        if code[ind] == -1 : code[ind] = randint(0, 9)
        code[pos] = msg_int(pos)-code[ind]

    return code