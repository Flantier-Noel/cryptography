import warnings

def pop_item(lst:list, item:object):
    """ given a list lst and an object item, return a list lst containing elements of lst except item.
        The object item may not belongs to lst, in this case nothing is done """
    

    lst_new = []

    for i in range(len(lst)) :
        if lst[i]==item : lst_new.append(lst[i])

    return lst_new        

class Canvas():
    """ class of canvas used for the cypher as described in the wiki"""

    def __init__(self, lst_unpack_rep=[]):
        """ lst_unpack_rep:[int] represents represents the whole canvas representation in machine 
            len:int is the index before which lst_unpack_rep correspond to the canvas usable and after which lst_unpack_rep is purely machine data """
        
        self.lst_unpack_rep = lst_unpack_rep

        length = 0
        while length < len(lst_unpack_rep) and not(isinstance(lst_unpack_rep[length], list)): 
            length +=1
        
        self.len = length

    def __getitem__(self, ind:int):
        """ return the item of self.lst_unpack_rep at the position ind """

        assert ind >= 0, "canvas indices must be positive"
        assert isinstance(ind, int), "canvas indices must be integer"
        assert ind < len(self.lst_unpack_rep), "canvas index out of range"

        if ind > self.len : warnings.warn("index given is above user range")

        return self.lst_unpack_rep[ind]

    @classmethod
    def from_text(cls, key_text:str):
        """ create a canvas from a key text using the method explained in the wiki """

        max_jump = 9 ## could be set differently

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
                canvas[rank+ind] = pop_item(canvas[rank+ind], value-ind)
            
            rank += 1

        return Canvas(canvas)

    def pack(self):
        """ user friendly method in order to easly get the list representation of the usable part of the canvas """
        
        L = self.len
        return self.lst_unpack_rep[:L]
    
    def __repr__(self):
        """ usual special method to represent conveniently the canvas ie with the truncated list built by the pack method"""
        
        lst_pack = self.pack()
        str_list = [str(n) for n in lst_pack]
        return '['+ ', '.join(str_list) +']'
    
## without modular variation :
from random import randint

def encode_int(cnv:Canvas, msg_int:list[int], mod=10):
    """without modular variation -- cypher part which encypher a list of integers msg_int using the canvas cnv as described in the wiki"""

    code = []

    for ind in range(len(msg_int)) :
        pos = ind+cnv[ind]

        for _ in range(len(code), pos+1): code.append(None) ## None items are used to filled gaps before they get their values

        if code[ind] == None : code[ind] = randint(0, 9)
        code[pos] = (msg_int[ind]-code[ind])%mod

    for ind in range(len(code)):
        if code[ind] == None : code[ind] = randint(0, 9) ## gaps may stay at the end of the process

    return code