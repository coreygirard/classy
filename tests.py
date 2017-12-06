import unittest
import doctest
import classy



class TestClassy(unittest.TestCase):
    def test_basic_classify(self):
        data = {'Class A':['a b c',
                           'a c e',
                           'b a c',
                           'e d f'],
                'Class B':['e f g',
                           'e y v',
                           'f e w',
                           'f e v',
                           'v f d']}

        c = classy.Classifier(data)

        result = c.classify('a')
        self.assertEqual(result['Class A'],max(result.values()))

    def test_custom_parse(self):
        data = {'1':['a,b,c',
                     'd,e f'],
                '2':['i,j,k',
                     'x y,z']}

        c = classy.Classifier(data)

        self.assertEqual(c.prior,{'1': 2, '2': 2})
        self.assertEqual(c.getPrior(),{'1': 0.5, '2': 0.5})
        self.assertEqual(c.word,{'1': {'abc': 1,
                                       'de': 1,
                                       'f': 1},
                                 '2': {'ijk': 1,
                                       'x': 1,
                                       'yz': 1}})
        self.assertEqual(c.corpus,{'abc': 1,
                                   'de': 1,
                                   'f': 1,
                                   'ijk': 1,
                                   'x': 1,
                                   'yz': 1})

        def newParse(t):
            return [i for i in t.split(',') if i != '']

        c2 = classy.Classifier(data,f=newParse)

        self.assertEqual(c2.prior,{'1': 2, '2': 2})
        self.assertEqual(c2.getPrior(),{'1': 0.5, '2': 0.5})
        self.assertEqual(c2.word,{'1': {'a': 1,
                                        'b': 1,
                                        'c': 1,
                                        'd': 1,
                                        'e f': 1},
                                  '2': {'i': 1,
                                        'j': 1,
                                        'k': 1,
                                        'x y': 1,
                                        'z': 1}})
        self.assertEqual(c2.corpus,{'a': 1,
                                    'b': 1,
                                    'c': 1,
                                    'd': 1,
                                    'e f': 1,
                                    'i': 1,
                                    'j': 1,
                                    'k': 1,
                                    'x y': 1,
                                    'z': 1})



def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(classy))
    return tests

if __name__ == '__main__':
    unittest.main()



