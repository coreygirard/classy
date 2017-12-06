import re

class Classifier(object):
    def __init__(self,i):
        '''
        >>> c = Classifier({'1':['a b',
        ...                      'a c'],
        ...                 '2':['d f',
        ...                      'e f']})
        >>> c.prior == {'1': 2, '2': 2}
        True
        >>> c.getPrior() == {'1': 0.5, '2': 0.5}
        True
        >>> c.word == {'1': {'a': 2,
        ...                  'b': 1,
        ...                  'c': 1},
        ...            '2': {'d': 1,
        ...                  'e': 1,
        ...                  'f': 2}}
        True
        >>> c.corpus == {'a': 2,
        ...              'b': 1,
        ...              'c': 1,
        ...              'd': 1,
        ...              'e': 1,
        ...              'f': 2}
        True
        '''

        self.prior = {}
        self.word = {}
        self.corpus = {}
        self.threshold = None

        self.add(i)

    def add(self,i):
        for k,v in i.items():
            for e in v:
                self.addLine(k,e)

        self.total = sum(self.prior.values())

    def addLine(self,k,e):
        '''
        >>> c = Classifier({})
        >>> c.prior == {}
        True
        >>> c.word == {}
        True
        >>> c.corpus == {}
        True
        >>> c.addLine('1','a b b')
        >>> c.prior == {'1':1}
        True
        >>> c.word == {'1':{'a': 1,
        ...                 'b': 2}}
        True
        >>> c.corpus == {'a': 1,
        ...              'b': 2}
        True
        '''

        self.prior[k] = self.prior.get(k,0)+1
        if k not in self.word.keys():
            self.word[k] = {}

        for i in self.parse(e):
            self.word[k][i] = self.word[k].get(i,0)+1
            self.corpus[i] = self.corpus.get(i,0)+1

    def parse(self,text):
        '''
        >>> Classifier({}).parse('a b c')
        ['a', 'b', 'c']
        '''

        text = text.lower()
        text = re.sub(r'[^a-z0-9 ]',r'',text)
        return [i for i in text.split(' ') if i != '']

    def getPrior(self):
        return {k:v/self.total for k,v in self.prior.items()}

    def classifyWord(self,w):
        '''
        >>> c = Classifier({'1':['a b',
        ...                      'a c'],
        ...                 '2':['d f',
        ...                      'e f']})
        >>> c.classifyWord('a') == {'1': 0.75, '2': 0.25}
        True
        >>> c.classifyWord('b') == {'1': 2/3,  '2': 1/3}
        True
        >>> c.classifyWord('f') == {'1': 0.25, '2': 0.75}
        True
        '''

        temp = {k:(v.get(w,0)+1) for k,v in self.word.items()}
        return {k:v/sum(temp.values()) for k,v in temp.items()}

    def classify(self,i):
        '''
        >>> c = Classifier({'1':['a b',
        ...                      'a c'],
        ...                 '2':['d f',
        ...                      'e f']})
        >>> c.classify('a f') == {'1': 0.5, '2': 0.5}
        True
        >>> r = c.classify('a b')
        >>> r['1'] == max(r.values())
        True
        >>> r = c.classify('a d')
        >>> r['1'] == max(r.values())
        True
        >>> r = c.classify('b f')
        >>> r['2'] == max(r.values())
        True
        >>> c.threshold = 0.8
        >>> c.classify('a a a')
        '1'
        >>> c.classify('x y z') == None
        True
        '''

        i = self.parse(i)

        p = self.getPrior()

        for word in i:
            c = self.classifyWord(word)
            for k,v in c.items():
                p[k] *= v

        total = sum(p.values())
        p = {k:v/total for k,v in p.items()}

        if self.threshold == None:
            return p
        else:
            for k,v in p.items():
                if v >= self.threshold:
                    return k
            return None


