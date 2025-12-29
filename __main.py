def pop_item(lst, item):
    for i in range(len(lst)):
        if lst[i]==item : 
            lst.pop(i)
            break

class Canvas():
    def __init__(self, lst_unpack_rep=[]):
        self.lst_unpack_rep = lst_unpack_rep

        length = 0
        while length < len(lst_unpack_rep) and isinstance(lst_unpack_rep[length], list): 
            length +=1
        
        self.len = length

    @classmethod
    def from_text(cls, key_text:str):
        max_jump = 10

        canvas = []
        key = [len(w) for w in key_text.split(' ')]

        rank = 0
        for n in key :
            for ind in range(rank, rank+n):
                if ind >= len(canvas) : ind.append([i0+1 for i0 in range(max_jump)])
            
            possible_values = canvas[rank]
            value = possible_values[key[n]%len(possible_values)]
            canvas[rank] = value

            for ind in range(1, value):
                pop_item(canvas[ind], value-ind)
            
            rank += 1

        return Canvas(canvas)

    def pack(self):
        L = self.len
        return self.lst_unpack_rep[:L]
    
    def __repr__(self):
        lst_pack = self.pack()
        str_list = [str(n) for n in lst_pack]
        return '[ '+ ', '.join(str_list) +']'