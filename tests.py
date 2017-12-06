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



def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(classy))
    return tests

if __name__ == '__main__':
    unittest.main()



