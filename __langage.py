from random import*

def sort_alphab(word_list, alphab):
    lettre_order = {alphab[i]:i for i in range(len(alphab))}

class Langage():
    def __init__(self, base="/workspaces/cryptography/langage database"):
        vowel = 'a'

        alphab = ''

        with open(base+'/noun.txt') as noun :
            self.noun_lst = noun.readlines()
            for i in range(len(self.noun_lst)) : self.noun_lst[i] = self.noun_lst[i][:-1]


        with open(base+'/name.txt') as name :
            self.name_lst = name.readlines()
            for i in range(len(self.name_lst)) : self.name_lst[i] = self.name_lst[i][:-1]
        
        self.verb_declin = {0:"", 1:"", 2:"", 3:"", 4:""}

        self.gender_declin = {0:"", 1:"", 2:""}
        self.number_declin = {0:"", 1:"", 2:""}
    
    def phrase(self, key):
        ind = 0

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

            

            return _subj
        
        subj = [subj_from_int(key[ind])]
        ind += 1
        if relativ :
            rewind = randint(1, 100)
            if rewind <= 15 : 
                subj.append(None)
            else : 
                subj.append(subj_from_int(key[ind]))
                ind += 1
        

        metadata = {'time':time, 'relat':relativ, }