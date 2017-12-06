
def splitInput(i):
    '''
    >>> splitInput('a b c')
    ['a', 'b', 'c']
    '''

    return i.split(' ')

class Classifier(object):
    def __init__(self,i):
        self.raw = i
        self.n = {}
        for k,v in i.items():
            self.n[k] = len(v)

        self.numItems = sum(self.n.values())

        self.allWords = {}

        self.d = {}
        for k,v in i.items():
            self.d[k] = {}
            for v2 in v:
                for e in splitInput(v2):
                    self.d[k][e] = self.d[k].get(e,0)+1
                    self.allWords[e] = self.allWords.get(e,0)+1

    def classifyWord(self,w):
        temp = {k:(v.get(w,0)+1) for k,v in self.d.items()}
        return {k:v/sum(temp.values()) for k,v in temp.items()}

    def classify(self,i):
        i = splitInput(i)

        p = {k:v/self.numItems for k,v in self.n.items()}

        for word in i:
            for k,v in self.classifyWord(word).items():
                p[k] *= v
            p = {k:v/sum(p.values()) for k,v in p.items()}

        return p
