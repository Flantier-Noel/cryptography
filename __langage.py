from random import*

def sort_alphab(word_list, alphab):
    lettre_order = {alphab[i]:i for i in range(len(alphab))}
    key_fun = lambda word : [lettre_order for lettre in word]
    return sorted(word_list, key=key_fun)

class Langage():
    def __init__(self, base="/workspaces/cryptography/langage database"):
        self.vowel = ['a', 'æ', 'i', 'o']
        self.consH = ['ch', 'j', 'f']
        self.consL = ['r' , 'l', 'n']

        self.alphab = self.vowel + self.consH + self.consL
        #self.lettre_order = {self.alphab[i]:i for i in range(len(self.alphab))}

        with open(base+'/noun.txt') as noun :
            self.noun_lst = noun.readlines()
            for i in range(len(self.noun_lst)) : self.noun_lst[i] = self.noun_lst[i][:-1]
            self.noun_lst = sort_alphab(self.noun_lst, self.alphab)
            self.noun_reg = {lettre:-1 for lettre in self.alphab}
            ind = 0
            while self.noun_reg[self.alphab[-1]] == -1 :
                lettre = self.noun_lst[ind][0]
                if self.noun_reg[lettre] == -1 : self.noun_reg[lettre] = ind
                ind += 1

        with open(base+'/name.txt') as name :
            self.name_lst = name.readlines()
            for i in range(len(self.name_lst)) : self.name_lst[i] = self.name_lst[i][:-1]
            self.name_lst = sort_alphab(self.name_lst, self.alphab)
            self.name_reg = {lettre:[-1,-1] for lettre in self.alphab}
            ind = 0
            while self.name_reg[self.alphab[-1]][0] == -1 :
                lettre = self.name_lst[ind][0]
                if self.name_reg[lettre] == -1 : 
                    self.name_reg[lettre][0] = ind
                    self.name_reg[self.name_lst[ind-1][0]][1] = ind-1
                ind += 1

        self.verb_declin = {0:"a", 1:"à", 2:"àf", 3:"á", 4:"áf"}

        self.gender_declin = {0:"", 1:"o", 2:"i"}
        self.number_declin = {0:".", 1:":", 2:"|"}
    
    def phrase(self, key, ind0=0):
        ind = ind0

        time_int = int(key[ind])
        relativ = (time_int>=5)
        if relativ : time = [time_int]
        else : time = [time_int, time_int-5]
        ind += 1

        def subj_from_int(val0, val1):
            _subj = {}
            if val0 == 9 : 
                _subj['tp'] = 0
                _subj['gend'] = 0
                _subj['num'] = randint(0, 2)
            else : 
                _subj['tp'] = 1
                _subj['gend'] = val0%3
                _subj['num']  = val0//3

            l0 = self.alphab[val1]
            name = randint(1, 100)
            if name <= 15 :
                [i0, i1] = self.name_reg[l0]
                i = randint(i0, i1)
                _subj['base'] = self.name_lst[i]
            else :
                [i0, i1] = self.noun_reg[l0]
                i = randint(i0, i1)
                _subj['base'] = self.noun_lst[i]

            _subj['value'] = self.number_declin[_subj['num']] + _subj['base'] + self.gender_declin[_subj['gend']]
            return _subj
        
        subj = [subj_from_int(key[ind], key[ind+1])]
        ind += 2
        if relativ :
            rewind = randint(1, 100)
            if rewind <= 15 : 
                subj.append(None)
            else : 
                subj.append(subj_from_int(key[ind], key[ind+1]))
                ind += 2
        
        def verb_from_int(val0, valT):
            _verb = {}
            l0 = self.alphab[val0]
            [i0, i1] = self.noun_reg[l0]
            i = randint(i0, i1)
            _verb['base'] = self.noun_lst[i]
            _verb['value'] = _verb['base'] + self.verb_declin[valT]
        
            return _verb

        verb = [verb_from_int(key[ind], time[0])]
        ind += 1
        if relativ : 
            verb.append(verb_from_int(key[ind], time[1]))
            ind += 1

        metadata = {'time':time, 'relat':relativ, 'subj':subj, 'verb':verb}