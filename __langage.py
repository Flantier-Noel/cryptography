from random import*

def sort_alphab(word_list, alphab):
    lettre_order = {alphab[i]:i for i in range(len(alphab))}
    key_fun = lambda word : [lettre_order for lettre in word]
    return sorted(word_list, key=key_fun)

def random_dic(probas):
    x = random()
    i0, i1 = 0, 0
    for key in probas.keys():
        i0, i1 = i1, i1+probas[key]
        if i0 <= x < i1: return key

class Langage():
    def __init__(self, base="/workspaces/cryptography/langage database"):
        self.vowel = ['a', 'æ', 'i', 'o']
        self.consH = ['ś', 'j', 'f']
        self.consL = ['r' , 'l', 'n']

        self.alphab = self.vowel + self.consH + self.consL

        with open(base+'/noun.txt', 'r') as noun :
            self.noun_lst = noun.readlines()
            for i in range(len(self.noun_lst)) : self.noun_lst[i] = self.noun_lst[i][:-1]
            self.noun_lst = sort_alphab(self.noun_lst, self.alphab)
            self.noun_reg = {lettre:-1 for lettre in self.alphab}
            ind = 0
            while self.noun_reg[self.alphab[-1]] == -1 :
                lettre = self.noun_lst[ind][0]
                if self.noun_reg[lettre] == -1 : self.noun_reg[lettre] = ind
                ind += 1

        with open(base+'/name.txt', 'r') as name :
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

        with open(base+'/link.txt', 'r') as link :
            self.link_lst = link.readlines()
            for i in range(len(self.link_lst)) : self.link_lst[i] = self.link_lst[i][:-1]

        self.verb_declin = {0:"a", 1:"à", 2:"àf", 3:"á", 4:"áf"}

        self.gender_declin = {0:"", 1:"o", 2:"i"}
        self.number_declin = {0:".", 1:":", 2:"|"}

    def sentence(self, key:list[int], ind0=0):
        ind = ind0

        time_int = key[ind]
        relativ = (time_int<5)
        if relativ : 
            time = [time_int]
            link = None
        else :
            t0 = randint(5, time_int) 
            time = [t0-5, time_int-t0]
            i0 = randint(0, len(self.link_lst)-1)
            link = self.link_lst[i0]
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

        objt = []
        alone = randint(1, 100)
        if alone <= 10 : objt.append(None)
        else :
            objt.append(subj_from_int(key[ind], key[ind+1]))
            ind += 2
        if relativ :
            alone = randint(1, 100)
            if alone <= 10 : objt.append(None)
            else :
                objt.append(subj_from_int(key[ind], key[ind+1]))
                ind += 2

        str_lst_repr = []
        str_lst_repr.append(subj[0]['value'])
        str_lst_repr.append(verb[0]['value'])
        if objt[0] != None : str_lst_repr.append(objt[0]['value'])
        if len(time) >= 2 :
            str_lst_repr.append(link)
            if subj[1] != None : str_lst_repr.append(subj[1]['value'])
            str_lst_repr.append(verb[1]['value'])
            if objt[1] != None : str_lst_repr.append(subj[1]['value'])

        str_repr = ' '.join(str_lst_repr)
        char_lst_rerpr = list(str_repr)
        repr = {'word':str_lst_repr, 'char':char_lst_rerpr, 'str':str_repr}

        metadata = {'time':time, 'subj':subj, 'verb':verb, 'objt':objt, 'link':link, 'repr':repr, 'last':ind}

        return metadata

    def paragraph(self, key):
        ind = 0
        key1 = key.copy()
        metadata = {'metas':[]}
        repr_str_lst = []

        while ind <= len(key):
            if len(key1)-ind <= 12 :
                for _ in range(12): key1.append(randint(0, 9))
            
            metadata0 = self.sentence(key1, ind0=ind)
            ind = metadata0['last']
            metadata['metas'].append(metadata0)
            for word in metadata0['repr']['word'] : repr_str_lst.append(word)
            repr_str_lst.append('.')

        repr_str = ' '.join(repr_str_lst)
        repr_char = list(repr_str)
        metadata['repr'] = {'word':repr_str_lst, 'char':repr_char, 'str':repr_str}

        return metadata

class __Tree():
    def __init__(self, value, sons, probas):
        self.value = value
        self.sons = sons ## dict str:three ?
        self.probas = probas ## dict str:float ?

    def __getitem__(self, key:list[str]):
        def search_with_ind(tree, __ind):
            if len(key)==__ind : return tree.probas
            assert key[__ind] in tree.sons.keys(), "KeyError : '" + ''.join(key) +"'"
            return search_with_ind(tree.sons[key[__ind]], __ind+1)
        return search_with_ind(self, 0)

    @classmethod
    def generate0(cls, alphab, rules, max_deepth):
        def generate_with_memory(val, past):
            if len(past) == max_deepth : return cls(None, [], [])
            usable = rules(past)
            sons = {}
            for l in alphab :
                if usable[l] :
                    past_ = past.copy() ; past_.append(l)
                    sons[l] = generate_with_memory(l, past_)
            sons[None] = cls(None, [], [])
            probas = {l:1/len(sons) for l in sons.keys()}
            return cls(val, sons, probas)
        
        return generate_with_memory('', [])

class __generator():
    def __init__(self, language:Langage, tp:str):
        self.data = {'noun':language.noun_lst, 'name':language.name_lst}[tp]
        self.__normal_size = 100
        self.max_size = 5

        def rules(past):
            possibles = {l:True for l in language.alphab}
            for l in language.alphab :
                # no consecutive high consone
                if len(past) >= 1 and past[-1] in language.consH and l in language.consH :
                    possibles[l] = False
                # no consecutive same letter
                if len(past) >= 1 and past[-1] == l :
                    possibles[l] = False
                # no consecutive 3 consonnes
                if len(past) >= 2 and (past[-1] in language.consH or past[-1] in language.consL) and (past[-2] in language.consH or past[-2] in language.consL) and (l in language.consH or l in language.consL) :
                    possibles[l] = False
                # no consecutive 4 vowels
                if len(past) >= 3 and past[-1] in language.vowel and past[-2] in language.vowel and past[-3] in language.vowel and l in language.vowel :
                    possibles[l] = False
            return possibles
        self.tree = __Tree.generate0(language.alphab, rules, self.max_size)

        for word_str in self.data :
            word_lst = list(word_str)
            for i in range(len(word_lst)):
                key = word_lst[:i]
                probas0 = self.tree[key]
                for l in probas0.keys():
                    if l == key[i] : probas0[l] = (self.__normal_size * probas0[l] + 1)/(self.__normal_size + 1)
                    else : probas0[l] = self.__normal_size * probas0[l]/(self.__normal_size + 1)

    def add(self, word):
        word_lst = list(word)
        for i in range(len(word_lst)):
            key = word_lst[:i]
            probas0 = self.tree[key]
            for l in probas0.keys():
                if l == key[i] : probas0[l] = (self.__normal_size * probas0[l] + 1)/(self.__normal_size + 1)
                else : probas0[l] = self.__normal_size * probas0[l]/(self.__normal_size + 1)

    def new(self, root=''):
        new_lettre = ''
        word = list(root)
        while new_lettre != None :
            probas = self[word]
            new_lettre = random_dic(probas)
            word.append(new_lettre)
        return ''.join(word)